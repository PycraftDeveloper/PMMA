import math

import numpy

from pmma.src.registry import Registry

class Constants:
    PYGAME = "pygame"

    DEFAULT = "default"
    TAU = math.pi * 2

    CARTESIAN = "cartesian"
    POLAR = "polar"
    TEXT = "text"

    XYZ = "xyz"
    XZY = "xzy"
    YXZ = "yxz"
    ZXY = "zxy"
    YZX = "yzx"
    ZYX = "zyx"

    SPATIAL_COORDINATES = [
        XYZ,
        XZY,
        YXZ,
        ZXY,
        YZX,
        ZYX]

    XY = "xy"
    YX = "yx"

    PLANAR_COORDINATES = [
        XY,
        YX]

    MAROON = (128,0,0)
    DARK_RED
    BROWN
    FIREBRICK
    CRIMSON
    RED
    TOMATO
    CORAL
    INDIAN_RED
    LIGHT_CORAL
    DARK_SALMON
    SALMON
    LIGHT_SALMON
    ORANGE_RED
    DARK_ORANGE
    ORANGE
    GOLD
    DARK_GOLDEN_ROD
    GOLDEN_ROD
    PALE_GOLDEN_ROD
    DARK_KHAKI
    KHAKI
    OLIVE
    YELLOW
    YELLOW_GREEN
    DARK_OLIVE_GREEN
    OLIVE_DRAB
    LAWN_GREEN
    CHARTREUSE
    GREEN_YELLOW
    DARK_GREEN
    GREEN
    FOREST_GREEN
    LIME
    LIME_GREEN
    LIGHT_GREEN
    PALE_GREEN
    DARK_SEA_GREEN
    MEDIUM_SPRING_GREEN
    SPRING_GREEN
    SEA_GREEN
    MEDIUM_AQUA_MARINE
    MEDIUM_SEA_GREEN
    LIGHT_SEA_GREEN
    DARK_SLATE_GRAY
    TEAL
    DARK_CYAN
    AQUA
    CYAN
    LIGHT_CYAN
    DARK_TURQUOISE
    TURQUOISE
    MEDIUM_TURQUOISE
    PALE_TURQUOISE
    AQUA_MARINE
    POWDER_BLUE
    CADET_BLUE
    STEEL_BLUE
    CORN_FLOWER_BLUE
    DEEP_SKY_BLUE
    DODGER_BLUE
    LIGHT_BLUE
    SKY_BLUE
    LIGHT_SKY_BLUE
    MIDNIGHT_BLUE
    NAVY
    DARK_BLUE
    MEDIUM_BLUE
    BLUE
    ROYAL_BLUE
    BLUE_VIOLET
    INDIGO
    DARK_SLATE_BLUE
    SLATE_BLUE
    MEDIUM_SLATE_BLUE
    MEDIUM_PURPLE
    DARK_MAGENTA
    DARK_VIOLET
    DARK_ORCHID
    MEDIUM_ORCHID
    PURPLE
    THISTLE
    PLUM
    VIOLET
    MAGENTA
    FUCHSIA
    ORCHID
    MEDIUM_VIOLET_RED
    PALE_VIOLET_RED
    DEEP_PINK
    HOT_PINK
    LIGHT_PINK
    PINK
    ANTIQUE_WHITE
    BEIGE
    BISQUE
    BLANCHED_ALMOND
    WHEAT
    CORN_SILK
    LEMON_CHIFFON
    LIGHT_GOLDEN_ROD_YELLOW
    LIGHT_YELLOW
    SADDLE_BROWN
    SIENNA
    CHOCOLATE
    PERU
    SANDY_BROWN
    BURLY_WOOD
    TAN
    ROSY_BROWN
    MOCCASIN
    NAVAJO_WHITE
    PEACH_PUFF
    MISTY_ROSE
    LAVENDER_BLUSH
    LINEN
    OLD_LACE
    PAPAYA_WHIP
    SEA_SHELL
    MINT_CREAM
    SLATE_GRAY
    LIGHT_SLATE_GRAY
    LIGHT_STEEL_BLUE
    LAVENDER
    FLORAL_WHITE
    ALICE_BLUE
    GHOST_WHITE
    HONEYDEW
    IVORY
    AZURE
    SNOW
    BLACK
    DIM_GREY
    GRAY
    DARK_GREY
    SILVER
    LIGHT_GREY
    GAINSBORO
    WHITE_SMOKE
    WHITE


    HEX = "hex"

    RGB = "rgb"
    RBG = "rbg"
    GRB = "grb"
    GBR = "gbr"
    BRG = "brg"
    BGR = "bgr"

    RGB_SWIZZLES = [
        RGB,
        RBG,
        GRB,
        GBR,
        BRG,
        BGR]

    RGBA = "rgba"
    RGAB = "rgab"
    RBGA = "rbga"
    RBAG = "rbag"
    RAGB = "ragb"
    RABG = "rabg"
    GRBA = "grba"
    GRAB = "grab"
    GBRA = "gbra"
    GBAR = "gbar"
    GARB = "garb"
    GABR = "gabr"
    BRGA = "brga"
    BRAG = "brag"
    BGRA = "bgra"
    BGAR = "bgar"
    BARG = "barg"
    BAGR = "bagr"
    ARGB = "argb"
    ARBG = "arbg"
    AGRB = "agrb"
    AGBR = "agbr"
    ABRG = "abrg"
    ABGR = "abgr"

    RGBA_SWIZZLES = [
        RGBA,
        RGAB,
        RBGA,
        RBAG,
        RAGB,
        RABG,
        GRBA,
        GRAB,
        GBRA,
        GBAR,
        GARB,
        GABR,
        BRGA,
        BRAG,
        BGRA,
        BGAR,
        BARG,
        BAGR,
        ARGB,
        ARBG,
        AGRB,
        AGBR,
        ABRG,
        ABGR]

    HSL = "hsl"
    HLS = "hls"
    SHL = "shl"
    SLH = "slh"
    LHS = "lhs"
    LSH = "lsh"

    HSL_SWIZZLES = [
        HSL,
        HLS,
        SHL,
        SLH,
        LHS,
        LSH]

    HSLA = "hsla"
    HSAL = "hsal"
    HLSA = "hlsa"
    HLAS = "hlas"
    HASL = "hasl"
    HALS = "hals"
    SHLA = "shla"
    SHAL = "shal"
    SLHA = "slha"
    SLAH = "slah"
    SAHL = "sahl"
    SALH = "salh"
    LHSA = "lhsa"
    LHAS = "lhas"
    LSHA = "lsha"
    LSAH = "lsah"
    LAHS = "lahs"
    LASH = "lash"
    AHSL = "ahsl"
    AHLS = "ahls"
    ASHL = "ashl"
    ASLH = "aslh"
    ALHS = "alhs"
    ALSH = "alsh"

    HSLA_SWIZZLES = [
        HSLA,
        HSAL,
        HLSA,
        HLAS,
        HASL,
        HALS,
        SHLA,
        SHAL,
        SLHA,
        SLAH,
        SAHL,
        SALH,
        LHSA,
        LHAS,
        LSHA,
        LSAH,
        LAHS,
        LASH,
        AHSL,
        AHLS,
        ASHL,
        ASLH,
        ALHS,
        ALSH]

    LCH = "lch"
    LHC = "lhc"
    CLH = "clh"
    CHL = "chl"
    HLC = "hlc"
    HCL = "hcl"

    LCH_SWIZZLES = [
        LCH,
        LHC,
        CLH,
        CHL,
        HLC,
        HCL]

    LCHA = "lcha"
    LCAH = "lcah"
    LHCA = "lhca"
    LHAC = "lhac"
    LACH = "lach"
    LAHC = "lahc"
    CLHA = "clha"
    CLAH = "clah"
    CHLA = "chla"
    CHAL = "chal"
    CALH = "calh"
    CAHL = "cahl"
    HLCA = "hlca"
    HLAC = "hlac"
    HCLA = "hcla"
    HCAL = "hcal"
    HALC = "halc"
    HACL = "hacl"
    ALCH = "alch"
    ALHC = "alhc"
    ACLH = "aclh"
    ACHL = "achl"
    AHLC = "ahlc"
    AHCL = "ahcl"

    LCHA_SWIZZLES = [
        LCHA,
        LCAH,
        LHCA,
        LHAC,
        LACH,
        LAHC,
        CLHA,
        CLAH,
        CHLA,
        CHAL,
        CALH,
        CAHL,
        HLCA,
        HLAC,
        HCLA,
        HCAL,
        HALC,
        HACL,
        ALCH,
        ALHC,
        ACLH,
        ACHL,
        AHLC,
        AHCL]

    HSV = "hsv"
    HVS = "hvs"
    SHV = "shv"
    SVH = "svh"
    VHS = "vhs"
    VSH = "vsh"

    HSV_SWIZZLES = [
        HSV,
        HVS,
        SHV,
        SVH,
        VHS,
        VSH]

    HSVA = "hsva"
    HSAV = "hsav"
    HVSA = "hvsa"
    HVAS = "hvas"
    HASV = "hasv"
    HAVS = "havs"
    SHVA = "shva"
    SHAV = "shav"
    SVHA = "svha"
    SVAH = "svah"
    SAHV = "sahv"
    SAVH = "savh"
    VHSA = "vhsa"
    VHAS = "vhas"
    VSHA = "vsha"
    VSAH = "vsah"
    VAHS = "vahs"
    VASH = "vash"
    AHSV = "ahsv"
    AHVS = "ahvs"
    ASHV = "ashv"
    ASVH = "asvh"
    AVHS = "avhs"
    AVSH = "avsh"

    HSVA_SWIZZLES = [
        HSVA,
        HSAV,
        HVSA,
        HVAS,
        HASV,
        HAVS,
        SHVA,
        SHAV,
        SVHA,
        SVAH,
        SAHV,
        SAVH,
        VHSA,
        VHAS,
        VSHA,
        VSAH,
        VAHS,
        VASH,
        AHSV,
        AHVS,
        ASHV,
        ASVH,
        AVHS,
        AVSH]

    HSI = "hsi"
    HIS = "his"
    SHI = "shi"
    SIH = "sih"
    IHS = "ihs"
    ISH = "ish"

    HSI_SWIZZLES = [
        HSI,
        HIS,
        SHI,
        SIH,
        IHS,
        ISH]

    HSIA = "hsia"
    HSAI = "hsai"
    HISA = "hisa"
    HIAS = "hias"
    HASI = "hasi"
    HAIS = "hais"
    SHIA = "shia"
    SHAI = "shai"
    SIHA = "siha"
    SIAH = "siah"
    SAHI = "sahi"
    SAIH = "saih"
    IHSA = "ihsa"
    IHAS = "ihas"
    ISHA = "isha"
    ISAH = "isah"
    IAHS = "iahs"
    IASH = "iash"
    AHSI = "ahsi"
    AHIS = "ahis"
    ASHI = "ashi"
    ASIH = "asih"
    AIHS = "aihs"
    AISH = "aish"

    HSIA_SWIZZLES = [
        HSIA,
        HSAI,
        HISA,
        HIAS,
        HASI,
        HAIS,
        SHIA,
        SHAI,
        SIHA,
        SIAH,
        SAHI,
        SAIH,
        IHSA,
        IHAS,
        ISHA,
        ISAH,
        IAHS,
        IASH,
        AHSI,
        AHIS,
        ASHI,
        ASIH,
        AIHS,
        AISH]

    COLOR_FORMATS = [
        RGB,
        RBG,
        GRB,
        GBR,
        BRG,
        BGR,
        RGBA,
        RGAB,
        RBGA,
        RBAG,
        RAGB,
        RABG,
        GRBA,
        GRAB,
        GBRA,
        GBAR,
        GARB,
        GABR,
        BRGA,
        BRAG,
        BGRA,
        BGAR,
        BARG,
        BAGR,
        ARGB,
        ARBG,
        AGRB,
        AGBR,
        ABRG,
        ABGR,
        HSL,
        HLS,
        SHL,
        SLH,
        LHS,
        LSH,
        HSLA,
        HSAL,
        HLSA,
        HLAS,
        HASL,
        HALS,
        SHLA,
        SHAL,
        SLHA,
        SLAH,
        SAHL,
        SALH,
        LHSA,
        LHAS,
        LSHA,
        LSAH,
        LAHS,
        LASH,
        AHSL,
        AHLS,
        ASHL,
        ASLH,
        ALHS,
        ALSH,
        LCH,
        LHC,
        CLH,
        CHL,
        HLC,
        HCL,
        LCHA,
        LCAH,
        LHCA,
        LHAC,
        LACH,
        LAHC,
        CLHA,
        CLAH,
        CHLA,
        CHAL,
        CALH,
        CAHL,
        HLCA,
        HLAC,
        HCLA,
        HCAL,
        HALC,
        HACL,
        ALCH,
        ALHC,
        ACLH,
        ACHL,
        AHLC,
        AHCL,
        HSV,
        HVS,
        SHV,
        SVH,
        VHS,
        VSH,
        HSVA,
        HSAV,
        HVSA,
        HVAS,
        HASV,
        HAVS,
        SHVA,
        SHAV,
        SVHA,
        SVAH,
        SAHV,
        SAVH,
        VHSA,
        VHAS,
        VSHA,
        VSAH,
        VAHS,
        VASH,
        AHSV,
        AHVS,
        ASHV,
        ASVH,
        AVHS,
        AVSH,
        HSI,
        HIS,
        SHI,
        SIH,
        IHS,
        ISH,
        HSIA,
        HSAI,
        HISA,
        HIAS,
        HASI,
        HAIS,
        SHIA,
        SHAI,
        SIHA,
        SIAH,
        SAHI,
        SAIH,
        IHSA,
        IHAS,
        ISHA,
        ISAH,
        IAHS,
        IASH,
        AHSI,
        AHIS,
        ASHI,
        ASIH,
        AIHS,
        AISH]

    GRADIENTS2 = numpy.array([
        5, 2, 2, 5,
        -5, 2, -2, 5,
        5, -2, 2, -5,
        -5, -2, -2, -5,
    ], dtype=numpy.int64)

    GRADIENTS3 = numpy.array([
        -11, 4, 4, -4, 11, 4, -4, 4, 11,
        11, 4, 4, 4, 11, 4, 4, 4, 11,
        -11, -4, 4, -4, -11, 4, -4, -4, 11,
        11, -4, 4, 4, -11, 4, 4, -4, 11,
        -11, 4, -4, -4, 11, -4, -4, 4, -11,
        11, 4, -4, 4, 11, -4, 4, 4, -11,
        -11, -4, -4, -4, -11, -4, -4, -4, -11,
        11, -4, -4, 4, -11, -4, 4, -4, -11,
    ], dtype=numpy.int64)

    GRADIENTS4 = numpy.array([
        3, 1, 1, 1, 1, 3, 1, 1, 1, 1, 3, 1, 1, 1, 1, 3,
        -3, 1, 1, 1, -1, 3, 1, 1, -1, 1, 3, 1, -1, 1, 1, 3,
        3, -1, 1, 1, 1, -3, 1, 1, 1, -1, 3, 1, 1, -1, 1, 3,
        -3, -1, 1, 1, -1, -3, 1, 1, -1, -1, 3, 1, -1, -1, 1, 3,
        3, 1, -1, 1, 1, 3, -1, 1, 1, 1, -3, 1, 1, 1, -1, 3,
        -3, 1, -1, 1, -1, 3, -1, 1, -1, 1, -3, 1, -1, 1, -1, 3,
        3, -1, -1, 1, 1, -3, -1, 1, 1, -1, -3, 1, 1, -1, -1, 3,
        -3, -1, -1, 1, -1, -3, -1, 1, -1, -1, -3, 1, -1, -1, -1, 3,
        3, 1, 1, -1, 1, 3, 1, -1, 1, 1, 3, -1, 1, 1, 1, -3,
        -3, 1, 1, -1, -1, 3, 1, -1, -1, 1, 3, -1, -1, 1, 1, -3,
        3, -1, 1, -1, 1, -3, 1, -1, 1, -1, 3, -1, 1, -1, 1, -3,
        -3, -1, 1, -1, -1, -3, 1, -1, -1, -1, 3, -1, -1, -1, 1, -3,
        3, 1, -1, -1, 1, 3, -1, -1, 1, 1, -3, -1, 1, 1, -1, -3,
        -3, 1, -1, -1, -1, 3, -1, -1, -1, 1, -3, -1, -1, 1, -1, -3,
        3, -1, -1, -1, 1, -3, -1, -1, 1, -1, -3, -1, 1, -1, -1, -3,
        -3, -1, -1, -1, -1, -3, -1, -1, -1, -1, -3, -1, -1, -1, -1, -3,
    ], dtype=numpy.int64)

    if Registry.precise_math_constants:
        STRETCH_CONSTANT2 = (1/math.sqrt(2+1)-1)/2
        SQUISH_CONSTANT2 = (math.sqrt(2+1)-1)/2
        STRETCH_CONSTANT3 = (1/math.sqrt(3+1)-1)/3
        SQUISH_CONSTANT3 = (math.sqrt(3+1)-1)/3
        STRETCH_CONSTANT4 = (1/math.sqrt(4+1)-1)/4
        SQUISH_CONSTANT4 = (math.sqrt(4+1)-1)/4
    else:
        STRETCH_CONSTANT2 = -0.211324865405187
        SQUISH_CONSTANT2 = 0.366025403784439
        STRETCH_CONSTANT3 = -0.166666666666666
        SQUISH_CONSTANT3 = 0.333333333333333
        STRETCH_CONSTANT4 = -0.138196601125011
        SQUISH_CONSTANT4 = 0.309016994374947

    NORM_CONSTANT2 = 47
    NORM_CONSTANT3 = 103
    NORM_CONSTANT4 = 30