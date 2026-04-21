"""
Physical constants and radar system parameters for the experiment.
"""
import numpy as np


class Constants:
    """
    Radar system constants and physical parameters.
    
    All values are in SI units unless otherwise specified.
    """
    
    # Target properties
    rEsf = 0.1765  # Sphere radius (m)
    sigma = np.pi * rEsf**2  # Radar Cross Section (m²)
    
    # Electromagnetic properties
    c = 3e8  # Speed of light (m/s)
    opFreq = 9.345e9  # Operative Frequency (Hz)
    lambdaRadar = round(c / opFreq, 3)  # Radar Wavelength (m)
    
    # Radar system parameters
    p_width = 0.1e-6  # Pulse width for the experiments (s)
    pT = 66.58  # Transmitted Power (W)
    G = 10**(38.7 / 10)  # Antenna Gain (linear scale)
    gLNA = 10**(70 / 10)  # LNA (Low Noise Amplifier) Gain (linear scale)
    theta = np.deg2rad(1.98)  # Antenna 3dB beamwidth (radians)
    k_m = 0.93  # Matching coefficient
    
    # Experiment configuration
    # Maps experiment number to polarization type
    dic_exp_3 = {
        1: {'pol': 'H'},  # Horizontal
        2: {'pol': 'V'},  # Vertical
        3: {'pol': 'V'},  # Vertical
        4: {'pol': 'V'},  # Vertical
        5: {'pol': 'H'}   # Horizontal
    }