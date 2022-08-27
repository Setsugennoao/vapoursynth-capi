from __future__ import annotations

from enum import IntEnum

__all__ = [
    'VSActivationReason',
    'VSMessageType',
    'VSCoreCreationFlags',
    'VSPluginConfigFlags',
    'VSDataTypeHint',
    'VSRequestPattern',
    'VSCacheMode',
    'VSColorFamily',
    'VSSampleType',
    'VSPresetFormat',
    'VSFilterMode',
    'VSMediaType',
    'VSAudioChannels',
    'VSPropertyType',
    'VSMapPropertyError',
    'VSMapAppendMode',
    'VSColorRange',
    'VSChromaLocation',
    'VSFieldBased',
    'VSMatrixCoefficients',
    'VSTransferCharacteristics',
    'VSColorPrimaries',
]


class VSActivationReason(IntEnum):
    arError = -1
    arInitial = 0
    arAllFramesReady = 1


class VSMessageType(IntEnum):
    mtDebug = 0
    mtInformation = 1
    mtWarning = 2
    mtCritical = 3
    mtFatal = 4


class VSCoreCreationFlags(IntEnum):
    ccfEnableGraphInspection = 1
    ccfDisableAutoLoading = 2
    ccfDisableLibraryUnloading = 4


class VSPluginConfigFlags(IntEnum):
    pcModifiable = 1


class VSDataTypeHint(IntEnum):
    dtUnknown = (-1)
    dtBinary = 0
    dtUtf8 = 1


class VSRequestPattern(IntEnum):
    rpGeneral = 0
    rpNoFrameReuse = 1
    rpStrictSpatial = 2


class VSCacheMode(IntEnum):
    cmAuto = -1
    cmForceDisable = 0
    cmForceEnable = 1


class VSColorFamily(IntEnum):
    cfUndefined = 0
    cfGray = 1
    cfRGB = 2
    cfYUV = 3


class VSSampleType(IntEnum):
    stInteger = 0
    stFloat = 1


class VSPresetFormat(IntEnum):
    pfNone = 0

    pfGray8 = (((((1 << 28) | (0 << 24)) | (8 << 16)) | (0 << 8)) | (0 << 0))
    pfGray9 = (((((1 << 28) | (0 << 24)) | (9 << 16)) | (0 << 8)) | (0 << 0))
    pfGray10 = (((((1 << 28) | (0 << 24)) | (10 << 16)) | (0 << 8)) | (0 << 0))
    pfGray12 = (((((1 << 28) | (0 << 24)) | (12 << 16)) | (0 << 8)) | (0 << 0))
    pfGray14 = (((((1 << 28) | (0 << 24)) | (14 << 16)) | (0 << 8)) | (0 << 0))
    pfGray16 = (((((1 << 28) | (0 << 24)) | (16 << 16)) | (0 << 8)) | (0 << 0))
    pfGray32 = (((((1 << 28) | (0 << 24)) | (32 << 16)) | (0 << 8)) | (0 << 0))
    pfGrayH = (((((1 << 28) | (1 << 24)) | (16 << 16)) | (0 << 8)) | (0 << 0))
    pfGrayS = (((((1 << 28) | (1 << 24)) | (32 << 16)) | (0 << 8)) | (0 << 0))

    pfYUV410P8 = (((((3 << 28) | (0 << 24)) | (8 << 16)) | (2 << 8)) | (2 << 0))
    pfYUV411P8 = (((((3 << 28) | (0 << 24)) | (8 << 16)) | (2 << 8)) | (0 << 0))
    pfYUV440P8 = (((((3 << 28) | (0 << 24)) | (8 << 16)) | (0 << 8)) | (1 << 0))
    pfYUV420P8 = (((((3 << 28) | (0 << 24)) | (8 << 16)) | (1 << 8)) | (1 << 0))
    pfYUV422P8 = (((((3 << 28) | (0 << 24)) | (8 << 16)) | (1 << 8)) | (0 << 0))
    pfYUV444P8 = (((((3 << 28) | (0 << 24)) | (8 << 16)) | (0 << 8)) | (0 << 0))
    pfYUV420P9 = (((((3 << 28) | (0 << 24)) | (9 << 16)) | (1 << 8)) | (1 << 0))
    pfYUV422P9 = (((((3 << 28) | (0 << 24)) | (9 << 16)) | (1 << 8)) | (0 << 0))
    pfYUV444P9 = (((((3 << 28) | (0 << 24)) | (9 << 16)) | (0 << 8)) | (0 << 0))
    pfYUV420P10 = (((((3 << 28) | (0 << 24)) | (10 << 16)) | (1 << 8)) | (1 << 0))
    pfYUV422P10 = (((((3 << 28) | (0 << 24)) | (10 << 16)) | (1 << 8)) | (0 << 0))
    pfYUV444P10 = (((((3 << 28) | (0 << 24)) | (10 << 16)) | (0 << 8)) | (0 << 0))
    pfYUV420P12 = (((((3 << 28) | (0 << 24)) | (12 << 16)) | (1 << 8)) | (1 << 0))
    pfYUV422P12 = (((((3 << 28) | (0 << 24)) | (12 << 16)) | (1 << 8)) | (0 << 0))
    pfYUV444P12 = (((((3 << 28) | (0 << 24)) | (12 << 16)) | (0 << 8)) | (0 << 0))
    pfYUV420P14 = (((((3 << 28) | (0 << 24)) | (14 << 16)) | (1 << 8)) | (1 << 0))
    pfYUV422P14 = (((((3 << 28) | (0 << 24)) | (14 << 16)) | (1 << 8)) | (0 << 0))
    pfYUV444P14 = (((((3 << 28) | (0 << 24)) | (14 << 16)) | (0 << 8)) | (0 << 0))
    pfYUV420P16 = (((((3 << 28) | (0 << 24)) | (16 << 16)) | (1 << 8)) | (1 << 0))
    pfYUV422P16 = (((((3 << 28) | (0 << 24)) | (16 << 16)) | (1 << 8)) | (0 << 0))
    pfYUV444P16 = (((((3 << 28) | (0 << 24)) | (16 << 16)) | (0 << 8)) | (0 << 0))
    pfYUV444PH = (((((3 << 28) | (1 << 24)) | (16 << 16)) | (0 << 8)) | (0 << 0))
    pfYUV444PS = (((((3 << 28) | (1 << 24)) | (32 << 16)) | (0 << 8)) | (0 << 0))

    pfRGB24 = (((((2 << 28) | (0 << 24)) | (8 << 16)) | (0 << 8)) | (0 << 0))
    pfRGB27 = (((((2 << 28) | (0 << 24)) | (9 << 16)) | (0 << 8)) | (0 << 0))
    pfRGB30 = (((((2 << 28) | (0 << 24)) | (10 << 16)) | (0 << 8)) | (0 << 0))
    pfRGB36 = (((((2 << 28) | (0 << 24)) | (12 << 16)) | (0 << 8)) | (0 << 0))
    pfRGB42 = (((((2 << 28) | (0 << 24)) | (14 << 16)) | (0 << 8)) | (0 << 0))
    pfRGB48 = (((((2 << 28) | (0 << 24)) | (16 << 16)) | (0 << 8)) | (0 << 0))
    pfRGBH = (((((2 << 28) | (1 << 24)) | (16 << 16)) | (0 << 8)) | (0 << 0))
    pfRGBS = (((((2 << 28) | (1 << 24)) | (32 << 16)) | (0 << 8)) | (0 << 0))


class VSFilterMode(IntEnum):
    fmParallel = 0
    fmParallelRequests = 1
    fmUnordered = 2
    fmFrameState = 3


class VSMediaType(IntEnum):
    mtVideo = 1
    mtAudio = 2


class VSAudioChannels(IntEnum):
    acFrontLeft = 0
    acFrontRight = 1
    acFrontCenter = 2
    acLowFrequency = 3
    acBackLeft = 4
    acBackRight = 5
    acFrontLeftOFCenter = 6
    acFrontRightOFCenter = 7
    acBackCenter = 8
    acSideLeft = 9
    acSideRight = 10
    acTopCenter = 11
    acTopFrontLeft = 12
    acTopFrontCenter = 13
    acTopFrontRight = 14
    acTopBackLeft = 15
    acTopBackCenter = 16
    acTopBackRight = 17
    acStereoLeft = 29
    acStereoRight = 30
    acWideLeft = 31
    acWideRight = 32
    acSurroundDirectLeft = 33
    acSurroundDirectRight = 34
    acLowFrequency2 = 35


class VSPropertyType(IntEnum):
    ptUnset = 0
    ptInt = 1
    ptFloat = 2
    ptData = 3
    ptFunction = 4
    ptVideoNode = 5
    ptAudioNode = 6
    ptVideoFrame = 7
    ptAudioFrame = 8


class VSMapPropertyError(IntEnum):
    peSuccess = 0
    peUnset = 1
    peType = 2
    peIndex = 4
    peError = 3


class VSMapAppendMode(IntEnum):
    maReplace = 0
    maAppend = 1


class VSColorRange(IntEnum):
    RANGE_FULL = 0
    RANGE_LIMITED = 1


class VSChromaLocation(IntEnum):
    CHROMA_LEFT = 0
    CHROMA_CENTER = 1
    CHROMA_TOP_LEFT = 2
    CHROMA_TOP = 3
    CHROMA_BOTTOM_LEFT = 4
    CHROMA_BOTTOM = 5


class VSFieldBased(IntEnum):
    FIELD_PROGRESSIVE = 0
    FIELD_BOTTOM = 1
    FIELD_TOP = 2


class VSMatrixCoefficients(IntEnum):
    MATRIX_RGB = 0
    MATRIX_BT709 = 1
    MATRIX_UNSPECIFIED = 2
    MATRIX_FCC = 4
    MATRIX_BT470_BG = 5
    MATRIX_ST170_M = 6
    MATRIX_ST240_M = 7
    MATRIX_YCGCO = 8
    MATRIX_BT2020_NCL = 9
    MATRIX_BT2020_CL = 10
    MATRIX_CHROMATICITY_DERIVED_NCL = 12
    MATRIX_CHROMATICITY_DERIVED_CL = 13
    MATRIX_ICTCP = 14


class VSTransferCharacteristics(IntEnum):
    TRANSFER_BT709 = 1
    TRANSFER_UNSPECIFIED = 2
    TRANSFER_BT470_M = 4
    TRANSFER_BT470_BG = 5
    TRANSFER_BT601 = 6
    TRANSFER_ST240_M = 7
    TRANSFER_LINEAR = 8
    TRANSFER_LOG_100 = 9
    TRANSFER_LOG_316 = 10
    TRANSFER_IEC_61966_2_4 = 11
    TRANSFER_IEC_61966_2_1 = 13
    TRANSFER_BT2020_10 = 14
    TRANSFER_BT2020_12 = 15
    TRANSFER_ST2084 = 16
    TRANSFER_ARIB_B67 = 18


class VSColorPrimaries(IntEnum):
    PRIMARIES_BT709 = 1
    PRIMARIES_UNSPECIFIED = 2
    PRIMARIES_BT470_M = 4
    PRIMARIES_BT470_BG = 5
    PRIMARIES_ST170_M = 6
    PRIMARIES_ST240_M = 7
    PRIMARIES_FILM = 8
    PRIMARIES_BT2020 = 9
    PRIMARIES_ST428 = 10
    PRIMARIES_ST431_2 = 11
    PRIMARIES_ST432_1 = 12
    PRIMARIES_EBU3213_E = 22
