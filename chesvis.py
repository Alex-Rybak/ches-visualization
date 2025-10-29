# q1.a.i
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('_mpl-gallery')
files = {"Canada": ["CA_data.csv", 2023], "Europe": ["EU_data.csv", 2024],
         "Europe (historic)": ["EU_hist_data.csv", 1999], "Israel": ["IL_data.csv", 2021],
         "LatAm": ["LA_data.csv", 2020]}


def family_color(family):
    match family:
        case "Nationalist":
            return 'black'
        case "Conservative":
            return 'dodgerblue'
        case "Liberal":
            return 'goldenrod'
        case "ChristDem":
            return 'darkorange'
        case "SocDem":
            return 'crimson'
        case "Socialist":
            return 'hotpink'
        case "Green":
            return 'mediumseagreen'
        case "Communal":
            return 'blueviolet'
        case "Fundamentalist":
            return 'mediumaquamarine'
        case 'Agrarian':
            return 'olivedrab'
        case 'Israel':
            return 'blue'
        case 'Canada':
            return 'maroon'
        case 'LatAm':
            return 'peru'
        case _:
            return "dimgrey"


def visualizeFile(set, this_year):
    data = files[set]
    fileName = data[0]

    df = pd.read_csv(fileName)
    # get data
    try:
        info = df.loc[df["year"] == this_year, ["country", "party", "family", "lrecon", "galtan"]].dropna()
    except KeyError:
        info = df.loc[df["year"] == this_year, ["country", "party", "lrecon", "galtan"]].dropna()
    info["lrecon"] = pd.to_numeric(info["lrecon"], errors="coerce")
    info["galtan"] = pd.to_numeric(info["galtan"], errors="coerce")


    fig, ax = plt.subplots(figsize=(12, 7), num=f"Data for {set} in {this_year}")
    ax.axvline(x=5, color='black', linewidth=1.5, linestyle='-')
    ax.axhline(y=5, color='black', linewidth=1.5, linestyle='-')
    ax.set_title(f"Data for {set} in {this_year}")
    try:
        sc = ax.scatter(info["lrecon"], info["galtan"],
                        c=info["family"].apply(family_color),alpha=0.1, picker=True, s=60)
    except KeyError:
        sc = ax.scatter(info["lrecon"], info["galtan"],
                        c=family_color(set), alpha=0.1, picker=True, s=60)

    try:
        for _, row in info.iterrows():
            ax.text(row["lrecon"]-0.02, row["galtan"]+0.01, row["party"],
                    fontsize=5, color=family_color(row["family"]), alpha=0.8)
    except KeyError:
        for _, row in info.iterrows():
            ax.text(row["lrecon"]-0.02, row["galtan"]+0.01, row["party"],
                    fontsize=5, color=family_color(set), alpha=0.8)

    ax.set_xlabel("Economic Left–Right")
    ax.set_ylabel("Social Progressive–Conservativ")
    annot = ax.annotate(
        "", xy=(0, 0), xytext=(10, 10), textcoords="offset points",
        bbox=dict(boxstyle="round,pad=0.1", fc="white", alpha=0.9),
        arrowprops=dict(arrowstyle="->")
    )
    annot.set_visible(False)

    # Handle click event
    def on_pick(event):
        ind = event.ind[0]
        row = info.iloc[ind]
        annot.xy = (row["lrecon"], row["galtan"])
        text = (f"{row['party']} ({row['country']})\n"
                f"Econ: {row['lrecon']:.2f}, Soc: {row['galtan']:.2f}")
        annot.set_text(text)
        annot.set_visible(True)
        fig.canvas.draw_idle()

    fig.canvas.mpl_connect("pick_event", on_pick)

    plt.tight_layout(pad=3.0)
    plt.show()









