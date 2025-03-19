import pandas as pd
import matplotlib.pyplot as plt


def plot_measurements(file_name, title):
    # Les CSV-fil
    df = pd.read_csv(file_name)

    # Juster sampling rate (f.eks. 1 = alle punkter, 2 = hvert andre punkt, 10 = hvert tiende punkt)
    sampling_rate = 40

    # Forventet at CSV-filen har kolonner: "tid", "channel_1", "channel_2"
    tid = df.iloc[::sampling_rate, 0] / 60  # Konverter sekunder til minutter
    channel_1 = df.iloc[::sampling_rate, 1]
    channel_2 = df.iloc[::sampling_rate, 2]

    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(tid, channel_1, label="Channel 1", linestyle="-", marker="o")
    plt.plot(tid, channel_2, label="Channel 2", linestyle="-", marker="s")

    # Tilpass plot
    plt.xlabel("Tid (minutter)")
    plt.ylabel("Lydnivå LAeq (dB)")
    plt.title(title)
    plt.legend()
    plt.grid()

    # Lagre plottet som en SVG-fil før det vises
    svg_filnavn = file_name.rsplit(".", 1)[0] + "_rapport.svg"  # Samme mappe, nytt navn
    plt.savefig(svg_filnavn, format="svg")

    # Vis plottet
    plt.show()


if __name__ == '__main__':
    plot_measurements('data/Rema1000 før VM, LAeq - Sheet1.csv', 'Mot Flatåsen, før VM')
    plot_measurements('data/Rema1000 VM økt1, LAeq - Sheet1.csv', 'Mot Flatåsen, under VM')
    plot_measurements('data/Rema1000 VM stafett, LAeq - Sheet1.csv', 'Mot Flatåsen, under en VM stafett')
    plot_measurements('data/Myren under VM, LAeq - Sheet1.csv', 'Mot Byåsen, under VM')
    plot_measurements('data/Veien mot Flatåsen, før VM, LAeq - Sheet1.csv', 'Vei mot Flatåsen, før VM')
    plot_measurements('data/Veien mot Flatåsen, under VM, LAeq - Sheet1.csv', 'Vei mot Flatåsen, under VM')