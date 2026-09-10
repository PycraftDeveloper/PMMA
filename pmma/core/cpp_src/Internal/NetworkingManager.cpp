#include <JSON/json.hpp>

#include "Internal/Core/PMMA_Registry.hpp"

#include "Internal/NetworkingManager.hpp"

std::string PMMA::Internal::NetworkingManager::QueryLatest_PMMA_Version() {
    cpr::Response r = cpr::Get(
        cpr::Url{"https://api.github.com/repos/PycraftDeveloper/PMMA/tags"},
        cpr::Header{
            {"User-Agent", "PMMA/1.0"},
            {"Accept", "application/vnd.github+json"}});

    if (r.status_code != 200) {
        std::cerr << "GitHub request failed: "
                  << r.status_code << '\n';
        return "";
    }

    try {
        nlohmann::json tags = nlohmann::json::parse(r.text);

        if (tags.empty()) {
            return "";
        }

        return tags[0]["name"].get<std::string>();
    } catch (const nlohmann::json::exception &e) {
        std::cerr << "Failed to parse GitHub response: "
                  << e.what() << '\n';
        return "";
    }
}