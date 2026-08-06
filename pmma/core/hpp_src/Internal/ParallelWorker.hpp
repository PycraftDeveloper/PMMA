#pragma once

#include <condition_variable>
#include <functional>
#include <future>
#include <mutex>
#include <queue>
#include <thread>
#include <vector>

namespace PMMA::Internal {
class ParallelWorker {
private:
    void Worker() {
        while (true) {
            std::function<void()> job;

            {
                std::unique_lock lock(mutex);

                cv.wait(lock, [this] {
                    return stopping || !jobs.empty();
                });

                if (stopping && jobs.empty())
                    return;

                job = std::move(jobs.front());
                jobs.pop();
            }

            job();
        }
    }

    std::vector<std::thread> workers;

    std::queue<std::function<void()>> jobs;

    std::mutex mutex;
    std::condition_variable cv;

    bool stopping = false;

public:
    ParallelWorker(unsigned int threadCount) {
        for (size_t i = 0; i < threadCount; ++i) {
            workers.emplace_back(&ParallelWorker::Worker, this);
        }
    }

    ~ParallelWorker() {
        {
            std::lock_guard lock(mutex);
            stopping = true;
        }

        cv.notify_all();

        for (auto &thread : workers)
            thread.join();
    }

    template <typename Func, typename... Args>
    inline auto Enqueue(Func &&func, Args &&...args)
        -> std::future<std::invoke_result_t<Func, Args...>> {
        using ReturnType = std::invoke_result_t<Func, Args...>;

        auto task = std::make_shared<std::packaged_task<ReturnType()>>(
            std::bind(std::forward<Func>(func), std::forward<Args>(args)...));

        std::future<ReturnType> future = task->get_future();

        {
            std::lock_guard lock(mutex);

            jobs.emplace([task]() {
                (*task)();
            });
        }

        cv.notify_one();

        return future;
    }
};
} // namespace PMMA::Internal