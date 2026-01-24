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

    ID = PMMA_Registry::ClassObject_ID_System++;

    Position = new CPP_DisplayCoordinate();
    ForegroundColor = new CPP_Color();
    BackgroundColor = new CPP_Color();

    uint8_t Color[4] = {0, 0, 0, 0};
    BackgroundColor->Set_RGBA(Color);

    Font = PMMA_Registry::PMMA_Location + PMMA_Registry::PathSeparator +
        "fonts" + PMMA_Registry::PathSeparator + "Noto_Sans" +
        PMMA_Registry::PathSeparator + "static" +
        PMMA_Registry::PathSeparator + "NotoSans-Regular.ttf";
}

void CPP_TextRenderer::Render() {
    if (Text.empty()) {
        if (Logger == nullptr) {
            Logger = new CPP_Logger();
        }

        Logger->InternalLogWarn(
            50,
            "This text has no text to render! Please use \
`TextRenderer.set_text` to set it.", false);
    }

    if (!SizeSet) {
        if (Logger == nullptr) {
            Logger = new CPP_Logger();
        }

        Logger->InternalLogError(
            54,
            "This text has no size set! \
Please use `TextRenderer.set_size` to set it.");
        throw runtime_error("Size not set!");
    }

    if (!ForegroundColor->GetSet()) {
        if (Logger == nullptr) {
            Logger = new CPP_Logger();
        }
        Logger->InternalLogError(
            52,
            "This text has no color set, please use the \
`TextRenderer.ForegroundColor` API to set it.");
        throw runtime_error("Text has no color set");
    }

    if (!Position->GetSet()) {
        if (Logger == nullptr) {
            Logger = new CPP_Logger();
        }
        Logger->InternalLogError(
            53,
            "This text has no position set, please use the \
`TextRenderer.Position` API to set it.");
        throw runtime_error("Text has no position set");
    }

    PMMA_Core::RenderPipelineCore->Add_Text_Object(this);
}