# Python-CSV-Parsing-for-LED-I-V-Analysis
Data cleaning, custom parsing, vectorized calculations, regression analysis, and automated plotting, while ensuring reproducibility and clarity. Showcases the integration of Python scripting, data science techniques, and scientific visualization, providing a robust framework for experimental physics labs or electronics projects.

# Project Structure
project_root/
│
├─ main.py               # Main script to run the analysis pipeline
├─ parser.py             # Custom CSV parser for messy horizontal LED data
├─ analysis.py           # Data analysis functions (threshold voltage, Eg, regression)
├─ plotting.py           # Plotting functions for I-V curves and energy plot
├─ PCS224 LAB4 - part 1.csv  # Example CSV file (input)
└─ output/
   └─ graphs/           # Generated plots and results table will be saved here

# The script will:
- Parse the CSV into a tidy format
- Analyze threshold voltages and energy gaps
- Generate individual I-V plots, a combined I-V plot, and an energy plot
- Save results to output/graphs/LED_results.csv and PNG files
Key plots (combined I-V and energy plot) will also pop up in windows for immediate inspection.

# Outputs
Graphs (PNG files) are saved in output/graphs/:
violet_IV.png, blue_IV.png, etc. → Individual LED I-V curves
Combined_IV.png → All LEDs on one I-V curve plot
EnergyPlot.png → Energy gap vs 1/wavelength with regression line

Results table (LED_results.csv) contains:
LED name
Voltage at threshold current
Eg (eV)
Wavelength (nm)

Console output shows:
LED results table
Experimental Planck’s constant
Percent error

# Customization
Wavelength Mapping
 In parser.py, you can adjust the wavelength map for your LEDs:

wavelength_map = {
    "violet": 400,
    "blue": 470,
    "green": 530,
    "yellow": 580,
    "red": 650,
    "white": 450,
    "IR": 850
}

Current Threshold
In analysis.py, find_threshold_voltage() uses current_threshold=0.1 mA by default.
You can adjust this to change the threshold voltage detection.

# Notes
The parser is designed to handle horizontal CSV layouts where each LED has voltage-current pairs in one cell.
The energy plot regression line now correctly includes both slope and intercept, matching the data points.
All outputs are automatically saved, so you don’t need to manually open files.

# Future Improvements
Automatically detect LED wavelengths from CSV metadata (if available).
Open all individual I-V plots automatically for inspection.
Rescale x-axis in energy plot (1/λ in µm⁻¹) for better readability.
Handle more LEDs beyond the current wavelength mapping automatically.


