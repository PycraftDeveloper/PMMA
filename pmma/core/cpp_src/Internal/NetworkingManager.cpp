#include <JSON/json.hpp>

#include "Internal/Core/PMMA_Core.hpp"
#include "Internal/Core/PMMA_Registry.hpp"

#include "Internal/LoggingManager.hpp"
#include "Internal/NetworkingManager.hpp"

void PMMA::Internal::NetworkingManager::QueryLatest_PMMA_Version() {
    PMMA::Core::LoggingManagerInstance->InternalLogInfo(
        74,
        "Querying GitHub for the latest PMMA version...");

    PMMA::Core::LoggingManagerInstance->InternalLogDebug(
        75, "PMMA is connecting to the internet to check for new versions of PMMA. \
PMMA is not using this to phone home, collect any usage data or send any information \
about you or your computer to any third party. You are welcome to check the source \
code of PMMA to verify this if you wish. Note however, the server PMMA is connecting \
to is a third party server (GitHub) and PMMA has no control over what data GitHub collects.");

    cpr::Response r = cpr::Get(
        cpr::Url{"https://api.github.com/repos/PycraftDeveloper/PMMA/tags"},
        cpr::Header{
            {"User-Agent", "PMMA/" + PMMA::Core::Registry::Current_PMMA_Version},
            {"Accept", "application/vnd.github+json"}});

    if (r.status_code != 200) {
        std::cerr << "GitHub request failed: "
                  << r.status_code << '\n';
        return;
    }

    try {
        nlohmann::json tags = nlohmann::json::parse(r.text);

        if (tags.empty()) {
            return;
        }

        PMMA::Core::Registry::Latest_PMMA_Version = tags[0]["name"].get<std::string>();
        return;
    } catch (const nlohmann::json::exception &e) {
        std::cerr << "Failed to parse GitHub response: "
                  << e.what() << '\n';
        return;
    }
}