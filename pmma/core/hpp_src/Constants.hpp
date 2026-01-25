#pragma once

#include <string>
#include <string>
#include <unordered_map>
#include <tuple>
#include <cstdint>

namespace CPP_Constants {
    inline const std::string HAT_NOT_PRESSED = "HAT NOT PRESSED";
    inline const std::string HAT_PRESSED_UP = "HAT PRESSED UP";
    inline const std::string HAT_PRESSED_RIGHT = "HAT PRESSED RIGHT";
    inline const std::string HAT_PRESSED_DOWN = "HAT PRESSED DOWN";
    inline const std::string HAT_PRESSED_LEFT = "HAT PRESSED LEFT";
    inline const std::string HAT_PRESSED_UP_RIGHT = "HAT PRESSED UP-RIGHT";
    inline const std::string HAT_PRESSED_DOWN_RIGHT = "HAT PRESSED DOWN-RIGHT";
    inline const std::string HAT_PRESSED_DOWN_LEFT = "HAT PRESSED DOWN-LEFT";
    inline const std::string HAT_PRESSED_UP_LEFT = "HAT PRESSED UP-LEFT";

    inline constexpr float PI = 3.141592653589793f;
    inline constexpr float TAU = 6.283185307179586f;

    inline constexpr float SHAPE_QUALITY = 0.27341772151898736f;

    inline const std::string OS_ANDROID = "Android";
    inline const std::string OS_BSD = "BSD";
    inline const std::string OS_EMSCRIPTEN = "Emscripten";
    inline const std::string OS_HAIKU = "Haiku";
    inline const std::string OS_HURD = "Hurd";
    inline const std::string OS_IOS = "iOS";
    inline const std::string OS_LINUX = "Linux";
    inline const std::string OS_NX = "Nintendo Switch";
    inline const std::string OS_MACOS = "MacOS";
    inline const std::string OS_PS4 = "Play Station 4";
    inline const std::string OS_PS5 = "Play Station 5";
    inline const std::string OS_VISIONOS = "VisionOS";
    inline const std::string OS_WINDOWS = "Windows";
    inline const std::string OS_WINRT = "WinRT";
    inline const std::string OS_XBOXONE = "XboxOne";
    inline const std::string OS_UNKNOWN = "Unknown";

    inline const std::string GRAPHICS_BACKEND_NO_RENDERER = "No Renderer";
    inline const std::string GRAPHICS_BACKEND_DIRECT3D11 = "Direct3D 11.0";
    inline const std::string GRAPHICS_BACKEND_DIRECT3D12 = "Direct3D 12.0";
    inline const std::string GRAPHICS_BACKEND_GNM = "GNM"; // PlayStation (Developer license needed)
    inline const std::string GRAPHICS_BACKEND_METAL = "Metal";
    inline const std::string GRAPHICS_BACKEND_NVN = "NVN"; // Nintendo Switch
    inline const std::string GRAPHICS_BACKEND_OPENGL_ES = "OpenGL ES";
    inline const std::string GRAPHICS_BACKEND_OPENGL = "OpenGL";
    inline const std::string GRAPHICS_BACKEND_VULKAN = "Vulkan";
    inline const std::string GRAPHICS_BACKEND_UNKNOWN = "Unknown";

    const struct Colors {
        static inline const std::string RED = "red";
        static inline const std::string ORANGE = "ora";
        static inline const std::string YELLOW = "yel";
        static inline const std::string GREEN = "gre";
        static inline const std::string BLUE = "blu";
        static inline const std::string INDIGO = "ind";
        static inline const std::string VIOLET = "vio";
        static inline const std::string BLACK = "blk";
        static inline const std::string WHITE = "wht";
        static inline const std::string GRAY = "gry";
        static inline const std::string CYAN = "cya";
        static inline const std::string MAGENTA = "mag";
        static inline const std::string LIGHT_RED = "lrd";
        static inline const std::string LIGHT_ORANGE = "lor";
        static inline const std::string LIGHT_YELLOW = "lyl";
        static inline const std::string LIGHT_GREEN = "lgr";
        static inline const std::string LIGHT_BLUE = "lbl";
        static inline const std::string LIGHT_INDIGO = "lin";
        static inline const std::string LIGHT_VIOLET = "lvi";
        static inline const std::string SKY_BLUE = "sky";
        static inline const std::string GOLD = "gol";
        static inline const std::string SILVER = "slv";
        static inline const std::string BROWN = "brn";
        static inline const std::string PEA_GREEN = "pea";
        static inline const std::string OLIVE = "olv";
        static inline const std::string TAN = "tan";
        static inline const std::string NAVY = "nav";
        static inline const std::string MAROON = "mar";
        static inline const std::string PURPLE = "pur";
        static inline const std::string CORAL = "cor";
        static inline const std::string TEAL = "tea";
        static inline const std::string CHERRY = "che";
        static inline const std::string LIME = "lim";
        static inline const std::string MOCCASIN = "moc";
        static inline const std::string BEIGE = "bei";
        static inline const std::string DUSK = "dus";
        static inline const std::string SALT = "slt";
        static inline const std::string LAVENDER = "lav";
        static inline const std::string PEACH = "pch";
        static inline const std::string MINT = "mnt";
        static inline const std::string ROSE = "rse";
        static inline const std::string BRONZE = "brz";
        static inline const std::string AQUAMARINE = "aqu";
        static inline const std::string PERIWINKLE = "per";
        static inline const std::string ICE_BLUE = "ice";
        static inline const std::string PLUM = "plm";
        static inline const std::string COPPER = "cop";
        static inline const std::string CREAM = "crm";
        static inline const std::string PINK = "pnk";
        static inline const std::string FOREST = "for";
        static inline const std::string SAND = "snd";
        static inline const std::string AMBER = "amb";
        static inline const std::string AZURE = "azr";
        static inline const std::string TURQUOISE = "trq";
        static inline const std::string COBALT = "cob";
        static inline const std::string CHARCOAL = "chc";
        static inline const std::string IVORY = "ivr";
        static inline const std::string MUSCAT = "mus";
        static inline const std::string OLIVE_DRAB = "old";
        static inline const std::string SAGE_GREEN = "sgr";
        static inline const std::string WHEAT = "whe";
        static inline const std::string RUBY = "rub";
        static inline const std::string EMERALD = "emr";
        static inline const std::string SLIME_GREEN = "slm";
        static inline const std::string ONYX = "ony";
        static inline const std::string SPEARMINT = "spe";
        static inline const std::string CHARTREUSE = "chr";
        static inline const std::string BLOOD_RED = "bld";
        static inline const std::string SPRING_GREEN = "spg";
        static inline const std::string DARK_RED = "dre";
        static inline const std::string DARK_ORANGE = "dor";
        static inline const std::string DARK_YELLOW = "dye";
        static inline const std::string DARK_GREEN = "dgr";
        static inline const std::string DARK_BLUE = "dbl";
        static inline const std::string DARK_INDIGO = "din";
        static inline const std::string DARK_VIOLET = "dvi";
        static inline const std::string DARK_GREY = "dgy";
        static inline const std::string LIGHT_GREY = "lgy";
        static inline const std::string OCHRE = "och";
        static inline const std::string UMBER = "umb";
        static inline const std::string TERRACOTTA = "ter";
        static inline const std::string MUD_BROWN = "mud";
        static inline const std::string SAPPHIRE = "sap";
        static inline const std::string AMYTHYST = "amy";
        static inline const std::string GARNET = "gnt";
        static inline const std::string TAUPE = "tpe";
        static inline const std::string BUBBLEGUM = "bub";
        static inline const std::string MIST_ROSE = "mrs";
        static inline const std::string HONEY = "hny";
        static inline const std::string SEAFOAM = "sea";
        static inline const std::string NEON_GREEN = "neo";
        static inline const std::string ELECTRIC_PINK = "elc";
        static inline const std::string SUNFLOWER = "sun";
        static inline const std::string CRIMSON = "crl";
        static inline const std::string CERULIAN = "cyl";
        static inline const std::string MOSS_GREEN = "mgn";
        static inline const std::string SAFFRON = "sfr";
        static inline const std::string APRICOT = "apr";
        static inline const std::string FLAX = "flx";
        static inline const std::string MYSTIC_PURPLE = "mys";

        static inline const std::unordered_map<std::string, std::array<uint8_t, 3>> ColorMap = {
            {RED,           {255,   0,   0}},
            {ORANGE,        {251,  79,  19}},
            {YELLOW,        {255, 255,   0}},
            {GREEN,         {  0, 255,   0}},
            {BLUE,          {  0,   0, 255}},
            {INDIGO,        { 51,   0, 153}},
            {VIOLET,        {143,   0, 255}},
            {BLACK,         {  0,   0,   0}},
            {WHITE,         {255, 255, 255}},
            {GRAY,          {128, 128, 128}},
            {CYAN,          {0, 255, 255}},
            {MAGENTA,       {255, 0, 255}},
            {LIGHT_RED,     {255, 102, 102}},
            {LIGHT_ORANGE,  {255, 178, 102}},
            {LIGHT_YELLOW,  {255, 255, 153}},
            {LIGHT_GREEN,   {153, 255, 153}},
            {LIGHT_BLUE,    {153, 204, 255}},
            {LIGHT_INDIGO,  {109, 90, 207}},
            {LIGHT_VIOLET,  {204, 153, 255}},
            {SKY_BLUE,      {135, 206, 235}},
            {GOLD,          {255, 215, 0}},
            {SILVER,        {192, 192, 192}},
            {BROWN,         {150, 75, 0}},
            {PEA_GREEN,     {142, 209, 63}},
            {OLIVE,         {128, 128, 0}},
            {TAN,           {210, 180, 140}},
            {NAVY,          {0, 0, 128}},
            {MAROON,        {128, 0, 0}},
            {PURPLE,        {128, 0, 128}},
            {CORAL,         {255, 127, 80}},
            {TEAL,          {0, 128, 128}},
            {CHERRY,        {255, 20, 147}},
            {LIME,          {204, 255, 153}},
            {MOCCASIN,      {255, 228, 181}},
            {BEIGE,         {245, 245, 220}},
            {DUSK,          {169, 169, 169}},
            {SALT,          {211, 211, 211}},
            {LAVENDER,      {230, 230, 250}},
            {PEACH,         {255, 218, 185}},
            {MINT,          {48, 128, 20}},
            {ROSE,          {255, 0, 127}},
            {BRONZE,        {205, 127, 50}},
            {AQUAMARINE,    {127, 255, 212}},
            {PERIWINKLE,    {218, 112, 214}},
            {ICE_BLUE,      {240, 255, 255}},
            {PLUM,          {221, 160, 221}},
            {COPPER,        {184, 115, 51}},
            {CRIMSON,       {255, 253, 208}},
            {PINK,          {255, 192, 203}},
            {FOREST,        {34, 139, 34}},
            {SAND,          {194, 178, 128}},
            {AMBER,         {255, 191, 0}},
            {AZURE,         {0, 127, 255}},
            {TURQUOISE,     {64, 224, 208}},
            {COBALT,        {0, 71, 71}},
            {CHARCOAL,      {54, 69, 79}},
            {IVORY,         {255, 255, 240}},
            {MUSCAT,        {255, 250, 205}},
            {OLIVE_DRAB,    {107, 142, 35}},
            {SAGE_GREEN,    {189, 183, 107}},
            {WHEAT,         {245, 222, 179}},
            {RUBY,          {224, 17, 95}},
            {EMERALD,       {80, 200, 120}},
            {SLIME_GREEN,   {192, 255, 62}},
            {ONYX,          {255, 8, 127}},
            {SPEARMINT,     {255, 239, 213}},
            {CHARTREUSE,    {127, 255, 0}},
            {BLOOD_RED,     {139, 0, 0}},
            {SPRING_GREEN,  {154, 205, 50}},
            {DARK_RED,      {138, 0, 0}},
            {DARK_ORANGE,   {255, 140, 0}},
            {DARK_YELLOW,   {204, 204, 0}},
            {DARK_GREEN,    {0, 100, 0}},
            {DARK_BLUE,     {0, 0, 139}},
            {DARK_INDIGO,   {75, 0, 130}},
            {DARK_VIOLET,   {148, 0, 211}},
            {DARK_GREY,     {64, 64, 64}},
            {LIGHT_GREY,    {218, 218, 218}},
            {OCHRE,         {204, 119, 34}},
            {UMBER,         {99, 81, 71}},
            {TERRACOTTA,    {182, 106, 80}},
            {MUD_BROWN,     {96, 70, 15}},
            {SAPPHIRE,      {15, 82, 186}},
            {AMYTHYST,      {153, 102, 204}},
            {GARNET,        {173, 54, 79}},
            {TAUPE,         {72, 60, 50}},
            {BUBBLEGUM,     {255, 182, 193}},
            {MIST_ROSE,     {255, 228, 255}},
            {HONEY,         {255, 183, 76}},
            {SEAFOAM,       {178, 255, 255}},
            {NEON_GREEN,    {57, 255, 20}},
            {ELECTRIC_PINK, {255, 0, 102}},
            {SUNFLOWER,     {255, 204, 0}},
            {CRIMSON,       {255, 64, 64}},
            {CERULIAN,      {0, 191, 255}},
            {MOSS_GREEN,    {46, 139, 87}},
            {SAFFRON,       {255, 99, 71}},
            {APRICOT,       {255, 165, 79}},
            {FLAX,          {238, 232, 205}},
            {MYSTIC_PURPLE, {102, 51, 153}}
        };
    };
}