"""
Main script for radar constant analysis.

This script processes radar experiment data from Excel files, applies filtering
criteria, and calculates radar constants for performance analysis.
"""
import os
import warnings
import numpy as np

from config import (
    DATA_PATH, 
    FILE_INDICES_TO_PROCESS,
    RWF_THRESHOLD,
    BWF_THRESHOLD,
    COUNT_FILTER
)
from data_loader import (
    load_experiment_files,
    load_and_filter_data,
    extract_measurement_arrays
)
from radar_calculations import (
    calculate_square_losses,
    calculate_radar_constant,
    calculate_soft_constant
)

warnings.filterwarnings('ignore')


def process_experiment_file(file_path: str, filename: str) -> np.ndarray:
    """
    Process a single experiment file and calculate radar constants.
    
    Args:
        file_path: Full path to the experiment file
        filename: Name of the file (for logging)
        
    Returns:
        Array of calculated radar constants
    """
    print(f"\nProcessing file: {filename}")
    
    # Load and filter data
    filtered_data = load_and_filter_data(
        file_path,
        rwf_threshold=RWF_THRESHOLD,
        bwf_threshold=BWF_THRESHOLD,
        count_filter=COUNT_FILTER
    )
    
    print(f"  Filtered records: {len(filtered_data)}")
    
    # Extract measurement arrays
    rwf, bwf, range_values, received_power = extract_measurement_arrays(filtered_data)
    
    # Calculate square losses (optional calculation)
    square_losses = calculate_square_losses(range_values, received_power, rwf, bwf)
    
    # Calculate radar constant coefficients
    radar_constants = calculate_radar_constant(range_values, received_power, rwf, bwf)
    
    return radar_constants


def main():
    """
    Main execution function for radar constant analysis.
    
    Processes selected experiment files and calculates aggregate statistics.
    """
    print("=" * 60)
    print("Radar Constant Analysis")
    print("=" * 60)
    
    # Load experiment files
    experiment_files = load_experiment_files(DATA_PATH, FILE_INDICES_TO_PROCESS)
    print(f"\nFiles to process: {experiment_files}")
    
    # Process each file and collect radar constants
    all_radar_constants = []
    
    for filename in experiment_files:
        file_path = os.path.join(DATA_PATH, filename)
        radar_constants = process_experiment_file(file_path, filename)
        all_radar_constants.append(radar_constants)
    
    # Concatenate all results
    combined_constants = np.concatenate(all_radar_constants)
    
    # Calculate and display statistics
    print("\n" + "=" * 60)
    print("Results Summary")
    print("=" * 60)
    print(f"Total measurements: {len(combined_constants)}")
    print(f"Mean radar constant: {combined_constants.mean():.6e}")
    print(f"Std deviation: {combined_constants.std():.6e}")
    print(f"Min value: {combined_constants.min():.6e}")
    print(f"Max value: {combined_constants.max():.6e}")
    print("=" * 60)
    print(calculate_soft_constant(combined_constants.mean()))


if __name__ == "__main__":
    main()
