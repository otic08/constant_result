"""
Data loading and filtering utilities for radar experiment data.
"""
import os
import pandas as pd
import numpy as np
from typing import Tuple, List


def load_experiment_files(data_path: str, file_indices: List[int]) -> List[str]:
    """
    Load and sort experiment files from the data directory.
    
    Args:
        data_path: Path to the directory containing experiment files
        file_indices: List of indices to select from sorted files
        
    Returns:
        List of selected file paths
    """
    all_files = sorted(os.listdir(data_path))
    selected_files = [all_files[i] for i in file_indices]
    return selected_files


def load_and_filter_data(
    file_path: str, 
    rwf_threshold: float = 0.4, 
    bwf_threshold: float = 0.4,
    count_filter: int = 1
) -> pd.DataFrame:
    """
    Load Excel data and apply filtering criteria.
    
    Args:
        file_path: Full path to the Excel file
        rwf_threshold: Minimum RWF (Range Window Function) threshold
        bwf_threshold: Minimum BWF (Beamwidth Function) threshold
        count_filter: Count value to filter by
        
    Returns:
        Filtered DataFrame
    """
    df = pd.read_excel(file_path, sheet_name='tabla')
    
    query_string = f"RWF > {rwf_threshold} & BWF > {bwf_threshold} & Count == {count_filter}"
    filtered_df = df.query(query_string)
    
    return filtered_df


def extract_measurement_arrays(df: pd.DataFrame) -> Tuple[np.ndarray, ...]:
    """
    Extract measurement arrays from filtered DataFrame.
    
    Args:
        df: Filtered DataFrame containing measurement data
        
    Returns:
        Tuple of (rwf, bwf, range, normalized_power) arrays
    """
    rwf = np.array(df.RWF)
    bwf = np.array(df.BWF)
    range_values = np.array(df.Range)
    # Normalize power from percentage to decimal
    normalized_power = np.array(df["R Power"]) / 100
    
    return rwf, bwf, range_values, normalized_power
