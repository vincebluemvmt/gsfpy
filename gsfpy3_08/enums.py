"""Enums"""
from enum import IntEnum


class FileMode(IntEnum):
    """
    Modes in which a GSF file may be opened
    """

    GSF_CREATE = 1
    GSF_READONLY = 2
    GSF_UPDATE = 3
    GSF_READONLY_INDEX = 4
    GSF_UPDATE_INDEX = 5
    GSF_APPEND = 6


class PingFlag(IntEnum):
    """
    Bit flags for the "ping_flags" field of a gsfSwathBathyPing record
    """

    GSF_IGNORE_PING = 0x0001
    GSF_PING_USER_FLAG_01 = 0x0002
    GSF_PING_USER_FLAG_02 = 0x0004
    GSF_PING_USER_FLAG_03 = 0x0008
    GSF_PING_USER_FLAG_04 = 0x0010
    GSF_PING_USER_FLAG_05 = 0x0020
    GSF_PING_USER_FLAG_06 = 0x0040
    GSF_PING_USER_FLAG_07 = 0x0080
    GSF_PING_USER_FLAG_08 = 0x0100
    GSF_PING_USER_FLAG_09 = 0x0200
    GSF_PING_USER_FLAG_10 = 0x0400
    GSF_PING_USER_FLAG_11 = 0x0800
    GSF_PING_USER_FLAG_12 = 0x1000
    GSF_PING_USER_FLAG_13 = 0x2000
    GSF_PING_USER_FLAG_14 = 0x4000
    GSF_PING_USER_FLAG_15 = 0x8000


class RecordType(IntEnum):
    """
    The set of GSF record types
    """

    GSF_NEXT_RECORD = 0
    GSF_RECORD_HEADER = 1
    GSF_RECORD_SWATH_BATHYMETRY_PING = 2
    GSF_RECORD_SOUND_VELOCITY_PROFILE = 3
    GSF_RECORD_PROCESSING_PARAMETERS = 4
    GSF_RECORD_SENSOR_PARAMETERS = 5
    GSF_RECORD_COMMENT = 6
    GSF_RECORD_HISTORY = 7
    GSF_RECORD_SWATH_BATHY_SUMMARY = 9
    GSF_RECORD_SINGLE_BEAM_PING = 10
    GSF_RECORD_HV_NAVIGATION_ERROR = 11
    GSF_RECORD_ATTITUDE = 12


class ScaledSwathBathySubRecord(IntEnum):
    """
    Identifiers for gsfSwathBathyPing subrecords to which scale factors
    are applied. Values are indices into the gsfScaleFactors beam array
    index.
    """

    GSF_SWATH_BATHY_SUBRECORD_DEPTH_ARRAY = 1
    GSF_SWATH_BATHY_SUBRECORD_ACROSS_TRACK_ARRAY = 2
    GSF_SWATH_BATHY_SUBRECORD_ALONG_TRACK_ARRAY = 3
    GSF_SWATH_BATHY_SUBRECORD_TRAVEL_TIME_ARRAY = 4
    GSF_SWATH_BATHY_SUBRECORD_BEAM_ANGLE_ARRAY = 5
    GSF_SWATH_BATHY_SUBRECORD_MEAN_CAL_AMPLITUDE_ARRAY = 6
    GSF_SWATH_BATHY_SUBRECORD_MEAN_REL_AMPLITUDE_ARRAY = 7
    GSF_SWATH_BATHY_SUBRECORD_ECHO_WIDTH_ARRAY = 8
    GSF_SWATH_BATHY_SUBRECORD_QUALITY_FACTOR_ARRAY = 9
    GSF_SWATH_BATHY_SUBRECORD_RECEIVE_HEAVE_ARRAY = 10
    GSF_SWATH_BATHY_SUBRECORD_DEPTH_ERROR_ARRAY = 11  # obsolete
    GSF_SWATH_BATHY_SUBRECORD_ACROSS_TRACK_ERROR_ARRAY = 12  # obsolete
    GSF_SWATH_BATHY_SUBRECORD_ALONG_TRACK_ERROR_ARRAY = 13  # obsolete
    GSF_SWATH_BATHY_SUBRECORD_NOMINAL_DEPTH_ARRAY = 14
    GSF_SWATH_BATHY_SUBRECORD_QUALITY_FLAGS_ARRAY = 15
    GSF_SWATH_BATHY_SUBRECORD_BEAM_FLAGS_ARRAY = 16
    GSF_SWATH_BATHY_SUBRECORD_SIGNAL_TO_NOISE_ARRAY = 17
    GSF_SWATH_BATHY_SUBRECORD_BEAM_ANGLE_FORWARD_ARRAY = 18
    GSF_SWATH_BATHY_SUBRECORD_VERTICAL_ERROR_ARRAY = 19
    GSF_SWATH_BATHY_SUBRECORD_HORIZONTAL_ERROR_ARRAY = 20
    GSF_SWATH_BATHY_SUBRECORD_INTENSITY_SERIES_ARRAY = 21
    GSF_SWATH_BATHY_SUBRECORD_SECTOR_NUMBER_ARRAY = 22
    GSF_SWATH_BATHY_SUBRECORD_DETECTION_INFO_ARRAY = 23
    GSF_SWATH_BATHY_SUBRECORD_INCIDENT_BEAM_ADJ_ARRAY = 24
    GSF_SWATH_BATHY_SUBRECORD_SYSTEM_CLEANING_ARRAY = 25
    GSF_SWATH_BATHY_SUBRECORD_DOPPLER_CORRECTION_ARRAY = 26
    GSF_SWATH_BATHY_SUBRECORD_SONAR_VERT_UNCERT_ARRAY = 27


class SeekOption(IntEnum):
    GSF_REWIND = 1
    GSF_END_OF_FILE = 2
    GSF_PREVIOUS_RECORD = 3
