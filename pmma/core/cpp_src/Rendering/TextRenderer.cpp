#include "PMMA_Core.hpp"

using namespace std;

CPP_TextRenderer::CPP_TextRenderer() {
    if (PMMA_Core::DisplayInstance == nullptr) {
        PMMA_Core::LoggingManagerInstance->InternalLogError(
            18,
            "You need to create a display before using this function. \
You can do this using `Display.create`."
        );
        throw runtime_error("Display not created yet!");
    }
}

void CPP_TextRenderer::Render() {
    PMMA_Core::RenderPipelineCore->AddObject(this);
}