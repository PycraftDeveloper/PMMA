#pragma once

#include <string>

namespace CPP_Constants {
    const std::string HAT_NOT_PRESSED = "HAT NOT PRESSED";
    const std::string HAT_PRESSED_UP = "HAT PRESSED UP";
    const std::string HAT_PRESSED_RIGHT = "HAT PRESSED RIGHT";
    const std::string HAT_PRESSED_DOWN = "HAT PRESSED DOWN";
    const std::string HAT_PRESSED_LEFT = "HAT PRESSED LEFT";
    const std::string HAT_PRESSED_UP_RIGHT = "HAT PRESSED UP-RIGHT";
    const std::string HAT_PRESSED_DOWN_RIGHT = "HAT PRESSED DOWN-RIGHT";
    const std::string HAT_PRESSED_DOWN_LEFT = "HAT PRESSED DOWN-LEFT";
    const std::string HAT_PRESSED_UP_LEFT = "HAT PRESSED UP-LEFT";

    const float PI = 3.141592653589793f;
    const float TAU = 6.283185307179586f;

    const float SHAPE_QUALITY = 0.27341772151898736f;

    const std::string OS_ANDROID = "Android";
    const std::string OS_BSD = "BSD";
    const std::string OS_EMSCRIPTEN = "Emscripten";
    const std::string OS_HAIKU = "Haiku";
    const std::string OS_HURD = "Hurd";
    const std::string OS_IOS = "iOS";
    const std::string OS_LINUX = "Linux";
    const std::string OS_NX = "Nintendo Switch";
    const std::string OS_MACOS = "MacOS";
    const std::string OS_PS4 = "Play Station 4";
    const std::string OS_PS5 = "Play Station 5";
    const std::string OS_VISIONOS = "VisionOS";
    const std::string OS_WINDOWS = "Windows";
    const std::string OS_WINRT = "WinRT";
    const std::string OS_XBOXONE = "XboxOne";
    const std::string OS_UNKNOWN = "Unknown";

    const std::string GRAPHICS_BACKEND_NO_RENDERER = "No Renderer";
    const std::string GRAPHICS_BACKEND_DIRECT3D11 = "Direct3D 11.0";
    const std::string GRAPHICS_BACKEND_DIRECT3D12 = "Direct3D 12.0";
    const std::string GRAPHICS_BACKEND_GNM = "GNM"; // PlayStation (Developer license needed)
    const std::string GRAPHICS_BACKEND_METAL = "Metal";
    const std::string GRAPHICS_BACKEND_NVN = "NVN"; // Nintendo Switch
    const std::string GRAPHICS_BACKEND_OPENGL_ES = "OpenGL ES";
    const std::string GRAPHICS_BACKEND_OPENGL = "OpenGL";
    const std::string GRAPHICS_BACKEND_VULKAN = "Vulkan";
    const std::string GRAPHICS_BACKEND_UNKNOWN = "Unknown";
}