# main.py
from parser import parse_led_data
from analysis import process_leds
import plotting
import os
import matplotlib.pyplot as plt


def main():
    # 1. Load messy CSV
    csv_file = "PCS224 LAB4 - part 1.csv"
    df = parse_led_data(csv_file)

    # 2. Analyze LEDs
    summary = process_leds(df)

    # 3. Output folder
    output_folder = os.path.abspath("output/graphs")
    os.makedirs(output_folder, exist_ok=True)
    print(f"\nAll generated plots and data will be saved in: {output_folder}\n")

    # 4. Plot graphs
    plotting.make_iv_curves(df)  # Individual I-V plots
    plotting.make_combined_iv_plot(df)  # Combined I-V plot
    plotting.make_energy_plot(summary)  # Energy plot

    # 5. Save the tidy DataFrame
    results_csv = os.path.join(output_folder, "LED_results.csv")
    summary["led_table"].to_csv(results_csv, index=False)
    print(f"Saved LED results table at: {results_csv}")

    # 6. Print analysis results in console
    print("\nLED Results Table:")
    print(summary["led_table"])
    print("\nExperimental Planck's Constant:", summary["h_exp"], "eV·s")
    print("Percent Error:", summary["percent_error"], "%")
    print("----------------------------------------------------")

    # 7. Optionally open key plots automatically
    combined_iv_path = os.path.join(output_folder, "Combined_IV.png")
    energy_plot_path = os.path.join(output_folder, "EnergyPlot.png")

    for path in [combined_iv_path, energy_plot_path]:
        if os.path.exists(path):
            img = plt.imread(path)
            plt.figure()
            plt.imshow(img)
            plt.axis('off')
            plt.title(os.path.basename(path))
    plt.show()

    print("All plots have been displayed and saved. You can also open them from the output folder.")


if __name__ == "__main__":
    main()

