"""
Configuration settings for the radar constant analysis.
"""

# Path to the main data directory containing experiment tables
#DATA_PATH = "/home/gibs/Documents/Tesis/Tables_EXP"
DATA_PATH = "/Users/gibs/IGP/tesis/Tables_EXP"
# Data filtering thresholds
RWF_THRESHOLD = 0.4
BWF_THRESHOLD = 0.4
COUNT_FILTER = 1

# Files to process (by pattern or index)
# Process files matching H1 and H2 patterns (indices 0 and 4 from sorted list)
FILE_INDICES_TO_PROCESS = [0, 4]  # H1_file and H2_file from sorted list
