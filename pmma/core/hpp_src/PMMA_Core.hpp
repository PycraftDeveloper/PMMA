#pragma once

#include <algorithm>
#include <array>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <future>
#include <iostream>
#include <map>
#include <random>
#include <sstream>
#include <stdexcept>
#include <string>
#include <thread>
#include <vector>

#include "Animation/LinearAnimation.hpp"
#include "Animation/RadialAnimation.hpp"

#include "Events/ControllerEvents.hpp"
#include "Events/KeyEvents.hpp"
#include "Events/KeyPadEvents.hpp"
#include "Events/MouseEvents.hpp"
#include "Events/WindowEvents.hpp"

#include "Graphics/Shader.hpp"

#include "Internal/AnimationManager.hpp"
#include "Internal/LoggingManager.hpp"
#include "Internal/ParallelWorker.hpp"
#include "Internal/PowerSavingManager.hpp"

#include "Internal/Events/EventsManager.hpp"

#include "Internal/Rendering/Core2D/RenderPipelineManager.hpp"

#include "Internal/Utility/CPU_FeatureSetUtils.hpp"
#include "Internal/Utility/FontUtils.hpp"

#include "Rendering/Shapes2D/AdditionalShapes.hpp"
#include "Rendering/Shapes2D/ArcShape.hpp"
#include "Rendering/Shapes2D/LineShape.hpp"
#include "Rendering/Shapes2D/PixelShape.hpp"
#include "Rendering/Shapes2D/PolygonShape.hpp"
#include "Rendering/Shapes2D/RadialPolygonShape.hpp"
#include "Rendering/Shapes2D/RectangleShape.hpp"

#include "Rendering/TextRenderer.hpp"

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
#include "Types.hpp"

/*
Notes:
    > Internal events MUST have a default 'safe value' to return before the event manager is initialized.
*/

namespace PMMA::Core {
extern PMMA::Display *ActiveDisplayInstance;
extern PMMA::Display *MasterDisplayInstance;

extern PMMA::Passport *PassportInstance;
extern PMMA::Internal::LoggingManager *LoggingManagerInstance;

extern PMMA::Internal::PowerSavingManager PowerSavingManagerInstance;

extern PMMA::Internal::AnimationManager *AnimationManagerInstance;

extern PMMA::FastRandom *RandomGenerator;

extern std::vector<PMMA::Internal::Events::InternalController *> InternalControllerEventInstances;
extern std::vector<PMMA::Events::Controller *> ControllerEvent_Instances;

extern PMMA::Internal::Events::InternalControllerManager *ControllerManagerInstance;

extern std::map<std::string, PMMA::Internal::TextureProperty> TextureCatalogue;

extern PMMA::Internal::ParallelWorker *ParallelWorkerInstance;

extern PMMA::Graphics::Shader *Core2D_ShapeSDF_Program;
} // namespace PMMA::Core

namespace PMMA::Registry {
extern std::vector<unsigned char> SecondaryDisplayIDs;
extern std::string PMMA_Location;
extern std::string PathSeparator;
extern std::string Current_PMMA_Version;
extern std::string Latest_PMMA_Version;
extern std::string Locale;

extern std::mutex SeedGeneratorLock;
extern std::mt19937 RandomSeedGenerator;
extern std::uniform_int_distribution<uint32_t> SeedDistribution;

extern std::chrono::high_resolution_clock::time_point StartupTime;

extern unsigned int KeyboardEventInstanceCount;
extern unsigned int TextEventInstanceCount;
extern unsigned int MousePositionEventInstanceCount;
extern unsigned int MouseEnterWindowEventInstanceCount;
extern unsigned int MouseButtonEventInstanceCount;
extern unsigned int MouseScrollEventInstanceCount;
extern unsigned int ControllerEventInstanceCount;
extern unsigned int DropEventInstanceCount;

extern unsigned int RollingViewID;
extern unsigned int MaxViewID;

extern unsigned int ParallelWorkerMaxThreads;

extern bool CPU_Supports_AVX2;
extern bool CPU_Supports_AVX512;
extern bool IsPowerSavingModeEnabled;
extern bool IsDebuggingModeEnabled;
extern bool IsApplicationRunning;
extern bool EscapeKeyShouldCloseWindow;
extern bool UserSetEscapeKeyShouldCloseWindow;
extern bool F11KeyShouldToggleFullScreen;
} // namespace PMMA::Registry

namespace PMMA {
EXPORT void Initialize(std::string location);

EXPORT void Uninitialize();
} // namespace PMMA