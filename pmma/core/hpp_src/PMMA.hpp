#pragma once

#include "Animation/LinearAnimation.hpp"
#include "Animation/RadialAnimation.hpp"

#include "Events/ControllerEvents.hpp"
#include "Events/KeyEvents.hpp"
#include "Events/KeyPadEvents.hpp"
#include "Events/MouseEvents.hpp"
#include "Events/WindowEvents.hpp"

#include "Graphics/Shader.hpp"

#include "Rendering/Shapes2D/AdditionalShapes.hpp"
#include "Rendering/Shapes2D/ArcShape.hpp"
#include "Rendering/Shapes2D/LineShape.hpp"
#include "Rendering/Shapes2D/PixelShape.hpp"
#include "Rendering/Shapes2D/PolygonShape.hpp"
#include "Rendering/Shapes2D/RadialPolygonShape.hpp"
#include "Rendering/Shapes2D/RectangleShape.hpp"

#include "Rendering/TextRenderer.hpp"

#include "Types/Angle.hpp"
#include "Types/Color.hpp"
#include "Types/Coordinate.hpp"
#include "Types/Proportion.hpp"
#include "Types/Size.hpp"
#include "Types/Texture.hpp"

#include "Constants.hpp"
#include "Display.hpp"
#include "Events/ControllerEvents.hpp"
#include "General.hpp"
#include "Logger.hpp"
#include "Maths.hpp"
#include "Noise/FractalBrownianMotion.hpp"
#include "Noise/PerlinNoise.hpp"
#include "Passport.hpp"
#include "Random.hpp"

namespace PMMA {
EXPORT void Initialize(std::string location);

EXPORT void Uninitialize();
} // namespace PMMA