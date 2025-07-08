#include "PMMA_Core.hpp"

using namespace std;

CPP_TextRenderer::CPP_TextRenderer() {
    if (PMMA::DisplayInstance == nullptr) {
        throw runtime_error("Display not initialized!");
    }
}

void CPP_TextRenderer::Render() {
    PMMA::RenderPipelineCore->AddObject(this);
}