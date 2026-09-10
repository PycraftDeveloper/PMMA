#pragma once

#include <cpr/cpr.h>
#include <iostream>

namespace PMMA::Internal {
class NetworkingManager {
public:
    void QueryLatest_PMMA_Version() {
        // We must pass a User-Agent header, or the GitHub API will reject the request.
        cpr::Response r = cpr::Get(
            cpr::Url{"https://api.github.com/repos/PycraftDeveloper/PMMA/tags"},
            cpr::Header{{"User-Agent", "MyCppApp/1.0"}});

        if (r.status_code == 200) {
            std::cout << "Success! JSON Response:\n"
                      << r.text << std::endl;
        } else {
            std::cerr << "Error " << r.status_code << ": " << r.error.message << std::endl;
        }
    }
};
} // namespace PMMA::Internal