#define STB_IMAGE_IMPLEMENTATION
#include <STB/stb_image.h>

#include "Internal/Core/PMMA_Core.hpp"

#include "Internal/PowerSavingManager.hpp"

#include "Passport.hpp"
#include "Random.hpp"

namespace PMMA::Core {
PMMA::Display *ActiveDisplayInstance = nullptr;
PMMA::Display *MasterDisplayInstance = nullptr;

PMMA::Passport *PassportInstance = new PMMA::Passport();
PMMA::Internal::LoggingManager *LoggingManagerInstance = nullptr;

PMMA::Internal::PowerSavingManager *PowerSavingManagerInstance = new PMMA::Internal::PowerSavingManager();

PMMA::Internal::AnimationManager *AnimationManagerInstance = nullptr;

PMMA::FastRandom *RandomGenerator = new PMMA::FastRandom();

std::vector<PMMA::Internal::Events::InternalController *> InternalControllerEventInstances;
std::vector<PMMA::Events::Controller *> ControllerEvent_Instances;

PMMA::Internal::Events::InternalControllerManager *ControllerManagerInstance = nullptr;

std::map<std::string, PMMA::Internal::Rendering::Core2D::TextureProperty> TextureCatalogue;

PMMA::Internal::ParallelWorker *ParallelWorkerInstance = nullptr;
PMMA::Graphics::Shader *Core2D_ShapeSDF_Program = nullptr;
} // namespace PMMA::Core