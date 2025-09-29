# parser.py
import pandas as pd


def parse_led_data(filename: str) -> pd.DataFrame:
    """
    Parse a messy horizontal CSV of LED I-V data into tidy long-form DataFrame.
    Columns: LED, Voltage (V), Current (mA), Wavelength (nm)
    """
    # Read CSV without headers
    raw = pd.read_csv(filename, header=None)

    # Extract LED names from second row (index 1)
    led_names = [str(val).strip() for val in raw.iloc[1, :] if isinstance(val, str) and val.strip() != '']

    # Collect all measurements
    data_rows = []
    for i in range(2, len(raw)):
        row = raw.iloc[i, :]
        col_idx = 0
        for led in led_names:
            # Skip empty cells
            while col_idx < len(row) and (pd.isna(row[col_idx]) or str(row[col_idx]).strip() == ''):
                col_idx += 1
            if col_idx >= len(row):
                break
            cell = str(row[col_idx]).strip()
            # Split voltage and current
            if ' ' in cell:
                try:
                    voltage_str, current_str = cell.split()
                    voltage = float(voltage_str)
                    current = float(current_str)
                    data_rows.append({"LED": led, "Voltage (V)": voltage, "Current (mA)": current})
                except ValueError:
                    pass
            col_idx += 1

    df = pd.DataFrame(data_rows)

    # Map wavelengths (adjust as needed)
    wavelength_map = {
        "violet": 400,
        "blue": 470,
        "green": 530,
        "yellow": 580,
        "red": 650,
        "white": 450,
        "IR": 850
    }
    df["Wavelength (nm)"] = df["LED"].map(wavelength_map)

    return df
