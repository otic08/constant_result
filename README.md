# Radar Constant Analysis

This project analyzes radar experiment data to calculate radar constants and performance metrics.

## Project Structure

```
constant_results/
├── main.py                  # Main execution script
├── config.py               # Configuration settings
├── constants.py            # Physical constants and radar parameters
├── data_loader.py          # Data loading and filtering utilities
├── radar_calculations.py   # Radar calculation functions
├── pyproject.toml         # Project dependencies
└── README.md              # This file
```

## Modules

### `main.py`
Main execution script that orchestrates the analysis workflow:
- Loads experiment files
- Processes data through filtering and calculations
- Generates summary statistics

### `config.py`
Configuration settings including:
- Data directory paths
- Filtering thresholds (RWF, BWF, Count)
- File selection criteria

### `constants.py`
Physical constants and radar system parameters:
- Target properties (sphere radius, radar cross section)
- Electromagnetic properties (frequency, wavelength)
- Radar system parameters (power, gain, beamwidth)

### `data_loader.py`
Data loading utilities:
- `load_experiment_files()`: Load and select experiment files
- `load_and_filter_data()`: Load Excel data and apply filters
- `extract_measurement_arrays()`: Extract measurement arrays from DataFrames

### `radar_calculations.py`
Radar signal processing calculations:
- `calculate_square_losses()`: Calculate radar square losses
- `calculate_radar_constant()`: Calculate radar constant coefficients (RCC)

## Usage

```bash
python main.py
```

## Configuration

Edit `config.py` to modify:
- `DATA_PATH`: Path to your experiment data directory
- `RWF_THRESHOLD`: Range Window Function threshold
- `BWF_THRESHOLD`: Beamwidth Function threshold
- `COUNT_FILTER`: Count filter value
- `FILE_INDICES_TO_PROCESS`: Which files to process from sorted list

## Data Format

Input Excel files should contain a sheet named 'tabla' with columns:
- `RWF`: Range Window Function
- `BWF`: Beamwidth Function
- `Count`: Count value
- `Range`: Distance measurements
- `R Power`: Received power (in percentage)

## Output

The script outputs:
- Per-file processing information
- Summary statistics (mean, std, min, max) of radar constants
