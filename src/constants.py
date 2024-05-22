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
    DARK_RED = (139,0,0)
    BROWN = (165,42,42)
    FIREBRICK = (178,34,34)
    CRIMSON = (220,20,60)
    RED = (255,0,0)
    TOMATO = (255,99,71)
    CORAL = (255,127,80)
    INDIAN_RED = (205,92,92)
    LIGHT_CORAL = (240,128,128)
    DARK_SALMON = (233,150,122)
    SALMON = (250,128,114)
    LIGHT_SALMON = (255,160,122)
    ORANGE_RED = (255,69,0)
    DARK_ORANGE = (255,140,0)
    ORANGE = (255,165,0)
    GOLD = (255,215,0)
    DARK_GOLDEN_ROD = (184,134,11)
    GOLDEN_ROD = (218,165,32)
    PALE_GOLDEN_ROD = (238,232,170)
    DARK_KHAKI = (189,183,107)
    KHAKI = (240,230,140)
    OLIVE = (128,128,0)
    YELLOW = (255,255,0)
    YELLOW_GREEN = (154,205,50)
    DARK_OLIVE_GREEN = (85,107,47)
    OLIVE_DRAB = (107,142,35)
    LAWN_GREEN = (124,252,0)
    CHARTREUSE = (127,255,0)
    GREEN_YELLOW = (173,255,47)
    DARK_GREEN = (0,100,0)
    GREEN = (0,128,0)
    FOREST_GREEN = (34,139,34)
    LIME = (0,255,0)
    LIME_GREEN = (50,205,50)
    LIGHT_GREEN = (144,238,144)
    PALE_GREEN = (152,251,152)
    DARK_SEA_GREEN = (143,188,143)
    MEDIUM_SPRING_GREEN = (0,250,154)
    SPRING_GREEN = (0,255,127)
    SEA_GREEN = (46,139,87)
    MEDIUM_AQUA_MARINE = (102,205,170)
    MEDIUM_SEA_GREEN = (60,179,113)
    LIGHT_SEA_GREEN = (32,178,170)
    DARK_SLATE_GRAY = (47,79,79)
    TEAL = (0,128,128)
    DARK_CYAN = (0,139,139)
    AQUA = (0,255,255)
    CYAN = (0,255,255)
    LIGHT_CYAN = (224,255,255)
    DARK_TURQUOISE = (0,206,209)
    TURQUOISE = (64,224,208)
    MEDIUM_TURQUOISE = (72,209,204)
    PALE_TURQUOISE = (175,238,238)
    AQUA_MARINE = (127,255,212)
    POWDER_BLUE = (176,224,230)
    CADET_BLUE = (95,158,160)
    STEEL_BLUE = (70,130,180)
    CORN_FLOWER_BLUE = (100,149,237)
    DEEP_SKY_BLUE = (0,191,255)
    DODGER_BLUE = (30,144,255)
    LIGHT_BLUE = (173,216,230)
    SKY_BLUE = (135,206,235)
    LIGHT_SKY_BLUE = (135,206,250)
    MIDNIGHT_BLUE = (25,25,112)
    NAVY = (0,0,128)
    DARK_BLUE = (0,0,139)
    MEDIUM_BLUE = (0,0,205)
    BLUE = (0,0,255)
    ROYAL_BLUE = (65,105,225)
    BLUE_VIOLET = (138,43,226)
    INDIGO = (75,0,130)
    DARK_SLATE_BLUE = (72,61,139)
    SLATE_BLUE = (106,90,205)
    MEDIUM_SLATE_BLUE = (123,104,238)
    MEDIUM_PURPLE = (147,112,219)
    DARK_MAGENTA = (139,0,139)
    DARK_VIOLET = (148,0,211)
    DARK_ORCHID = (153,50,204)
    MEDIUM_ORCHID = (186,85,211)
    PURPLE = (128,0,128)
    THISTLE = (216,191,216)
    PLUM = (221,160,221)
    VIOLET = (238,130,238)
    MAGENTA = (255,0,255)
    FUCHSIA = (255,0,255)
    ORCHID = (218,112,214)
    MEDIUM_VIOLET_RED = (199,21,133)
    PALE_VIOLET_RED = (219,112,147)
    DEEP_PINK = (255,20,147)
    HOT_PINK = (255,105,180)
    LIGHT_PINK = (255,182,193)
    PINK = (255,192,203)
    ANTIQUE_WHITE = (250,235,215)
    BEIGE = (245,245,220)
    BISQUE = (255,228,196)
    BLANCHED_ALMOND = (255,235,205)
    WHEAT = (245,222,179)
    CORN_SILK = (255,248,220)
    LEMON_CHIFFON = (255,250,205)
    LIGHT_GOLDEN_ROD_YELLOW = (250,250,210)
    LIGHT_YELLOW = (255,255,224)
    SADDLE_BROWN = (139,69,19)
    SIENNA = (160,82,45)
    CHOCOLATE = (210,105,30)
    PERU = (205,133,63)
    SANDY_BROWN = (244,164,96)
    BURLY_WOOD = (222,184,135)
    TAN = (210,180,140)
    ROSY_BROWN = (188,143,143)
    MOCCASIN = (255,228,181)
    NAVAJO_WHITE = (255,222,173)
    PEACH_PUFF = (255,218,185)
    MISTY_ROSE = (255,228,225)
    LAVENDER_BLUSH = (255,240,245)
    LINEN = (250,240,230)
    OLD_LACE = (253,245,230)
    PAPAYA_WHIP = (255,239,213)
    SEA_SHELL = (255,245,238)
    MINT_CREAM = (245,255,250)
    SLATE_GRAY = (112,128,144)
    LIGHT_SLATE_GRAY = (119,136,153)
    LIGHT_STEEL_BLUE = (176,196,222)
    LAVENDER = (230,230,250)
    FLORAL_WHITE = (255,250,240)
    ALICE_BLUE = (240,248,255)
    GHOST_WHITE = (248,248,255)
    HONEYDEW = (240,255,240)
    IVORY = (255,255,240)
    AZURE = (240,255,255)
    SNOW = (255,250,250)
    BLACK = (0,0,0)
    DIM_GREY = (105,105,105)
    GRAY = (128,128,128)
    DARK_GREY = (169,169,169)
    SILVER = (192,192,192)
    LIGHT_GREY = (211,211,211)
    GAINSBORO = (220,220,220)
    WHITE_SMOKE = (245,245,245)
    WHITE = (255,255,255)

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