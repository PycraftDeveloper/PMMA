#include "PMMA_Core.hpp"

CPP_RadialPolygonShape::CPP_RadialPolygonShape() {
    ShapeCenter = new CPP_DisplayCoordinate();
    Color = new CPP_Color();

    ID = PMMA_Registry::ClassObject_ID_System++;
}

unsigned int CPP_RadialPolygonShape::GetPointCount() {
    if (!RadiusSet) {
        if (Logger == nullptr) {
            Logger = new CPP_Logger();
        }
        Logger->InternalLogError(
            30,
            "This shape has no radius set, please use `RadialPolygon.set_radius` to set it.");
        throw std::runtime_error("Shape has no radius set");
    }

    if (PointCount == 0) {
        float minAngle = asin(1.0f / Radius);
        return std::max(3, static_cast<int>(1 + (CPP_Constants::TAU / minAngle) * PMMA_Registry::CurrentShapeQuality));
    }
    return PointCount;
}

unsigned int CPP_RadialPolygonShape::GetVertexCount() {
    if (!RadiusSet) {
        if (Logger == nullptr) {
            Logger = new CPP_Logger();
        }
        Logger->InternalLogError(
            30,
            "This shape has no radius set, please use `RadialPolygon.set_radius` to set it.");
        throw std::runtime_error("Shape has no radius set");
    }

    // Compute the maximum allowed point count based on radius and quality
    float minAngle = asin(1.0f / Radius);
    unsigned int MaxPoints = std::max(
        3,
        static_cast<int>(1 + (CPP_Constants::TAU / minAngle) * PMMA_Registry::CurrentShapeQuality));

    // Determine InternalPointCount exactly as the generator does
    unsigned int InternalPointCount = PointCount;

    if (InternalPointCount > MaxPoints || InternalPointCount < 3) {
        InternalPointCount = MaxPoints;
    }

    // The generator produces:
    //   InternalPointCount * 2 vertices (outer + inner/center)
    // + 2 closing vertices
    return InternalPointCount * 2 + 2;
}

void CPP_RadialPolygonShape::UpdateColorIndex() {
    uint8_t ColorData[4];
    Color->Get_RGBA(ColorData);

    ColorIndexChanged = false;
    float newColorIndex = Shape2D_RenderPipelineManager->GetColorIndex(ColorData, ID);

    if (newColorIndex != ColorIndex) {
        ColorIndexChanged = true;
        VertexDataChanged = true;
        ColorIndex = newColorIndex;
    }
}

void CPP_RadialPolygonShape::Render() {
    PMMA_Core::RenderPipelineCore->Add_2D_Shape_Object(this);
}

void CPP_RadialPolygonShape::InternalRender() {
    int DisplaySize[2];
    PMMA_Core::DisplayInstance->GetSize(DisplaySize);

    if (!ShapeCenter->GetSet()) {
        if (Logger == nullptr) {
            Logger = new CPP_Logger();
        }
        Logger->InternalLogError(
            30,
            "This shape has no center set, please use the `RadialPolygon.shape_center` \
API to set it.");
        throw std::runtime_error("Shape has no center set");
    }

    if (!Color->GetSet()) {
        if (Logger == nullptr) {
            Logger = new CPP_Logger();
        }
        Logger->InternalLogError(
            30,
            "This shape has no color set, please use the `RadialPolygon.shape_color` \
API to set it.");
        throw std::runtime_error("Shape has no color set");
    }

    if (!RadiusSet) {
        if (Logger == nullptr) {
            Logger = new CPP_Logger();
        }
        Logger->InternalLogError(
            30,
            "This shape has no radius set, please use `RadialPolygon.set_radius` to set it.");
        throw std::runtime_error("Shape has no radius set");
    }

    float ShapeCenterPosition[2];
    ShapeCenter->Get(ShapeCenterPosition);

    VertexDataChanged = VertexDataChanged ||
                        ShapeCenter->GetChangedToggle() ||
                        PMMA_Core::DisplayInstance->DisplaySizeChanged;

    if (ShapeCenterPosition[0] + Radius < 0 ||
        ShapeCenterPosition[0] - Radius > DisplaySize[0] ||
        ShapeCenterPosition[1] + Radius < 0 ||
        ShapeCenterPosition[1] - Radius > DisplaySize[1]) {
        return;
    }

    uint8_t ColorData[4];
    Color->Get_RGBA(ColorData);

    ColorDataChanged = ColorDataChanged || Color->GetInternalChangedToggle();

    if (ColorData[3] == 0) { // Return if shape not visible
        return;
    }

    if (VertexDataChanged) {
        unsigned int InternalPointCount = PointCount;
        float minAngle = asin(1.0f / Radius);
        unsigned int MaxPoints = std::max(3, static_cast<int>(1 + (CPP_Constants::TAU / minAngle) * PMMA_Registry::CurrentShapeQuality));
        if (InternalPointCount > MaxPoints || InternalPointCount < 3) {
            InternalPointCount = MaxPoints;
        }
        float angleStep = CPP_Constants::TAU / InternalPointCount;

        unsigned int outer_radius = Radius;

        unsigned int inner_radius = std::max(0, static_cast<int>(Radius) - static_cast<int>(Width) * 2);
        if (Width == 0) {
            inner_radius = 0;
        }

        // Reserve the exact number of vertices upfront
        size_t vertexCount = InternalPointCount * 2 + 2;
        Shape2D_RenderPipelineVertices.resize(vertexCount);

        float angle = Rotation;
        float cx = ShapeCenterPosition[0];
        float cy = ShapeCenterPosition[1];
        float cosStep = std::cos(angleStep);
        float sinStep = std::sin(angleStep);
        float cosA = std::cos(angle);
        float sinA = std::sin(angle);

        Vertex *v = Shape2D_RenderPipelineVertices.data();
        if (inner_radius == 0) {
            auto &v1 = Shape2D_RenderPipelineVertices[1];
            v1.x = cx;
            v1.y = cy;
            v1.s = ColorIndex;

            const Vertex Center = Shape2D_RenderPipelineVertices[1];
            for (unsigned int i = 0; i < InternalPointCount; ++i) {
                v[0].x = outer_radius * cosA + cx;
                v[0].y = outer_radius * sinA + cy;
                v[0].s = ColorIndex;

                v[1] = Center; // center vertex
                v += 2;

                float new_cosA = cosA * cosStep - sinA * sinStep;
                float new_sinA = sinA * cosStep + cosA * sinStep;
                cosA = new_cosA;
                sinA = new_sinA;
            }
        } else {
            for (unsigned int i = 0; i < InternalPointCount; ++i) {
                v[0].x = outer_radius * cosA + cx;
                v[0].y = outer_radius * sinA + cy;
                v[0].s = ColorIndex;

                v[1].x = inner_radius * cosA + cx;
                v[1].y = inner_radius * sinA + cy;
                v[1].s = ColorIndex;

                v += 2;

                float new_cosA = cosA * cosStep - sinA * sinStep;
                float new_sinA = sinA * cosStep + cosA * sinStep;
                cosA = new_cosA;
                sinA = new_sinA;
            }
        }

        // Close the shape by repeating the first pair
        Shape2D_RenderPipelineVertices[vertexCount - 2] = Shape2D_RenderPipelineVertices[0];
        Shape2D_RenderPipelineVertices[vertexCount - 1] = Shape2D_RenderPipelineVertices[1];
    }

    // Cache references (avoids repeated pointer chasing)
    auto *manager = Shape2D_RenderPipelineManager;
    auto &prevContent = manager->PreviousRenderContent[manager->LivePreviousRenderContent];

    // Check if we can skip writing
    if (ShapeIndex < prevContent.size()) {
        const auto &[existingID, existingOffset] = prevContent[ShapeIndex];
        if (ID == existingID && !VertexDataChanged) {
            VertexDataChanged = false;
            ColorDataChanged = false;
            PreviousLocation = Location;

            return;
        }
    }

    VertexDataChanged = false;
    ColorDataChanged = false;
    PreviousLocation = Location;

    manager->VertexDataChanged = true;

    // Cache buffer + pointers
    auto &buffer = manager->combined_vertexes[manager->LiveBufferCount];
    Vertex *__restrict base = buffer.data();
    Vertex *__restrict writePtr = base + Location;

    // Cache vertex data
    const Vertex *__restrict src = Shape2D_RenderPipelineVertices.data();
    const size_t count = Shape2D_RenderPipelineVertices.size();

    // Precompute conditions (branch-friendly)
    const bool notFirst = (Location != 0);
    const bool notLast = (Location + count != buffer.size());

    // Cache first/last EARLY (keeps in registers)
    const Vertex first = src[0];
    const Vertex last = src[count - 1];

    // ---- Prefix (degenerate) ----
    // Move pointer once, branch once
    if (notFirst) {
        writePtr -= 2;

        // Write 2 vertices directly (faster than memcpy for tiny count)
        writePtr[0] = first;
        writePtr[1] = first;
        writePtr += 2;
    }

    // ---- Main body (dominant cost path) ----
    // Bulk copy (compiler emits optimal intrinsic)
    std::memcpy(writePtr, src, count * sizeof(Vertex));
    writePtr += count;

    // ---- Suffix (degenerate) ----
    if (notLast) {
        *writePtr = last;
    }
}
