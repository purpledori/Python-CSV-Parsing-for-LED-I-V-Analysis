import pandas as pd
import numpy as np
from scipy import stats

H_THEORETICAL = 4.1357e-15  # eV·s
C = 3e17  # nm/s

def find_threshold_voltage(sub_df, current_threshold=0.1):
    """Find threshold voltage where I ≥ 0.1 mA"""
    mask = sub_df["Current (mA)"] >= current_threshold
    if mask.any():
        return sub_df.loc[mask, "Voltage (V)"].iloc[0]
    return np.nan

def process_leds(df: pd.DataFrame):
    results = []

    for led, group in df.groupby("LED"):
        Vt = find_threshold_voltage(group)
        wavelength = group["Wavelength (nm)"].iloc[0]
        Eg = Vt  # Approximation in eV
        results.append({
            "LED": led,
            "Wavelength (nm)": wavelength,
            "Threshold V (V)": Vt,
            "Eg (eV)": Eg
        })

    results_df = pd.DataFrame(results)

    # Regression: Eg vs 1/λ
    x = 1 / results_df["Wavelength (nm)"]  # 1/nm
    y = results_df["Eg (eV)"]
    slope, intercept, r, p, std_err = stats.linregress(x, y)

    h_exp = slope / C
    percent_error = abs(h_exp - H_THEORETICAL) / H_THEORETICAL * 100

    summary = {
        "led_table": results_df,
        "slope": slope,
        "intercept": intercept,      # <-- add intercept here
        "h_exp": h_exp,
        "percent_error": percent_error,
        "r_value": r
    }
    return summary
