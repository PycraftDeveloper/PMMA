#include "RenderPipelineCore.hpp"
#include "RenderPipelineManager.hpp"

#include <iostream>

using namespace std;

CPP_RenderPipelineCore::CPP_RenderPipelineCore() {

}

void CPP_RenderPipelineCore::Render() {
    for (auto& item : RenderData) {
        std::visit([](auto* ptr) {
            ptr->InternalRender();
        }, item);
    }
}

void CPP_RenderPipelineCore::Clear() {
    RenderData.clear();
}

void CPP_RenderPipelineCore::AddObject(RenderPipelineDataObject* RenderObject, bool RenderPipelineCompatable) {
    if (RenderData.empty()) {
        if (RenderPipelineCompatable) {
            RenderData.emplace_back(new CPP_RenderPipelineManager());
        } else {
            std::visit([&](auto* actualPtr) {
                RenderData.emplace_back(actualPtr);
            }, *RenderObject);
            return;
        }
    }

    auto& lastVariant = RenderData.back();

    if (RenderPipelineCompatable) {
        // Try to extract the CPP_RenderPipelineManager*
        if (CPP_RenderPipelineManager** managerPtr = std::get_if<CPP_RenderPipelineManager*>(&lastVariant)) {
            if ((*managerPtr)->shape_colors.size() < (*managerPtr)->MaxSize) {
                (*managerPtr)->AddRenderTarget(RenderObject);
            } else {
                // Manager full — add new one and push to it
                RenderData.emplace_back(new CPP_RenderPipelineManager());
                auto& newVariant = RenderData.back();
                if (CPP_RenderPipelineManager** newManagerPtr = std::get_if<CPP_RenderPipelineManager*>(&newVariant)) {
                    (*newManagerPtr)->AddRenderTarget(RenderObject);
                }
            }
        } else {
            // Last item is NOT a CPP_RenderPipelineManager — add a new one
            RenderData.emplace_back(new CPP_RenderPipelineManager());
            auto& newVariant = RenderData.back();
            if (CPP_RenderPipelineManager** newManagerPtr = std::get_if<CPP_RenderPipelineManager*>(&newVariant)) {
                (*newManagerPtr)->AddRenderTarget(RenderObject);
            }
        }
    } else {
        // If not compatible, just add it
        std::visit([&](auto* actualPtr) {
            RenderData.emplace_back(actualPtr);
        }, *RenderObject);
    }
}