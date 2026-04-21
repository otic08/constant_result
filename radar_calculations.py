"""
Radar signal processing calculations and formulas.
"""
import numpy as np
from constants import Constants


def calculate_square_losses(
    range_values: np.ndarray,
    received_power: np.ndarray,
    rwf: np.ndarray,
    bwf: np.ndarray
) -> np.ndarray:
    """
    Calculate square losses for radar measurements.
    
    The formula accounts for transmitted power, antenna gain, LNA gain,
    radar cross section, and geometric spreading losses.
    
    Args:
        range_values: Distance values in meters
        received_power: Normalized received power values (0-1)
        rwf: Range Window Function values
        bwf: Beamwidth Function values
        
    Returns:
        Array of calculated square losses
    """
    numerator = (
        Constants.pT * 
        (Constants.G ** 2) * 
        Constants.gLNA * 
        (Constants.lambdaRadar ** 2)
    )
    
    denominator = (
        ((4 * np.pi) ** 3) * 
        (range_values ** 4) * 
        received_power
    )
    
    square_losses = (numerator / denominator) * Constants.sigma * rwf * bwf
    
    return square_losses


def calculate_radar_constant(
    range_values: np.ndarray,
    received_power: np.ndarray,
    rwf: np.ndarray,
    bwf: np.ndarray
) -> np.ndarray:
    """
    Calculate the radar constant coefficient (RCC).
    
    This is derived from the radar equation and represents the constant
    relating received power to target characteristics and geometry.
    
    Args:
        range_values: Distance values in meters
        received_power: Normalized received power values (0-1)
        rwf: Range Window Function values
        bwf: Beamwidth Function values
        
    Returns:
        Array of radar constant coefficients
    """
    numerator = received_power * (range_values ** 4)
    
    denominator = (
        Constants.pT * 
        Constants.sigma * 
        Constants.gLNA * 
        rwf * 
        bwf
    )
    
    rcc = numerator / denominator
    
    return rcc


def calculate_radar_constant_without_wf(
        range_values: np.ndarray,
        received_power: np.ndarray
) -> np.ndarray:
    """
    Calculate the radar constant coefficient (RCC) without considering
    the range weighting function (RWF) and beamwidth weighting function
    (BWF).

    This is derived from the radar equation and represents the constant
    relating received power to target characteristics and geometry.

    Args:
        range_values: Distance values in meters
        received_power: Normalized received power values (0-1)

    Returns:
        Array of radar constant coefficients
    """
    numerator = received_power * (range_values ** 4)

    denominator = (
            Constants.pT *
            Constants.sigma *
            Constants.gLNA
    )

    rcc = numerator / denominator

    return rcc


def calculate_soft_constant(
    hard_targets_constant: float,
) -> float:

    numerator = 16* np.log(2)*Constants.lambdaRadar ** 4 * 10**18
    denominator = hard_targets_constant * Constants.c * np.pi ** 6 * Constants.theta**2 * Constants.k_m

    return 10*np.log10(numerator / denominator)