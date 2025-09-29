# plotting.py
import matplotlib.pyplot as plt
import os

OUTPUT_DIR = "output/graphs"

def ensure_output_dir():
    abs_path = os.path.abspath(OUTPUT_DIR)
    os.makedirs(abs_path, exist_ok=True)
    return abs_path

def generate_colors(n):
    colors = plt.cm.get_cmap('tab10')
    return [colors(i % 10) for i in range(n)]

def make_iv_curves(df):
    outdir = ensure_output_dir()
    for led, group in df.groupby("LED"):
        plt.figure()
        plt.plot(group["Voltage (V)"], group["Current (mA)"], marker="o", label=led)
        plt.xlabel("Voltage (V)")
        plt.ylabel("Current (mA)")
        plt.title(f"I–V Curve: {led}")
        plt.grid(True, alpha=0.3)
        plt.legend()
        filepath = os.path.join(outdir, f"{led}_IV.png")
        plt.savefig(filepath, dpi=300, bbox_inches="tight")
        plt.close()
        print(f"Saved I-V curve for {led} at: {filepath}")

def make_combined_iv_plot(df, title="Combined I-V Curves", filename="Combined_IV.png"):
    outdir = ensure_output_dir()
    plt.figure(figsize=(10,6))
    leds = df["LED"].unique()
    colors = generate_colors(len(leds))
    for led, color in zip(leds, colors):
        group = df[df["LED"]==led]
        plt.plot(group["Voltage (V)"], group["Current (mA)"], marker="o", label=led, color=color)
    plt.xlabel("Voltage (V)")
    plt.ylabel("Current (mA)")
    plt.title(title)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    filepath = os.path.join(outdir, filename)
    plt.savefig(filepath, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"Saved combined I-V plot at: {filepath}")


def make_energy_plot(summary):
    outdir = ensure_output_dir()

    leds = summary["led_table"]
    x = 1 / leds["Wavelength (nm)"]
    y = leds["Eg (eV)"]

    slope = summary["slope"]
    intercept = summary.get("intercept", 0)

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color="blue", label="LED Data")
    plt.plot(x, slope * x + intercept, "r-", label="Linear Fit")  # regression line

    plt.xlabel("1 / Wavelength (1/nm)")
    plt.ylabel("Eg (eV)")
    plt.title("Energy Gap vs 1 / Wavelength")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    filepath = os.path.join(outdir, "EnergyPlot.png")
    plt.savefig(filepath, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"Saved energy plot at: {filepath}")
