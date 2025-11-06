import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('_mpl-gallery')
files = {"Canada": "data_predicted/CA_data_p.csv", "Canada (provinces)":"data_predicted/CA_prov_data_p.csv","Europe": "data/EU_data.csv",
         "Europe (historic)":"data/EU_hist_data.csv", "Israel": "data_predicted/IL_data_p.csv","LatAm":"data_predicted/LA_data_p.csv"}


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
        case 'Miscellaneous':
            return "dimgrey"
        case 'CA':
            return 'maroon'
        case 'IL':
            return 'blue'
        case _:
            return 'peru'


def visualizeFile(countries, years,showYears=False):
    df = pd.DataFrame()
    for set in countries:
        fileName = files[set]
        this_df = pd.read_csv(fileName)
        #if "family" not in this_df.columns:
        #    this_df["family"] = this_df["country"]
        df = pd.concat([df, this_df], ignore_index=True)
    info = pd.DataFrame()
    # get data
    for a_year in years:
        this_year = int(a_year)
        this_info = df.loc[df["year"] == this_year, ["country", "party", "year", "family", "lrecon", "galtan"]].dropna()

        this_info["lrecon"] = pd.to_numeric(this_info["lrecon"], errors="coerce")
        this_info["galtan"] = pd.to_numeric(this_info["galtan"], errors="coerce")
        this_info["year"] = pd.to_numeric(this_info["year"], errors="coerce")

        info = pd.concat([info, this_info], ignore_index=True)


    fig, ax = plt.subplots(figsize=(12, 7), num=f"Data for {countries} in {years}")
    ax.axvline(x=5, color='black', linewidth=1.5, linestyle='-')
    ax.axhline(y=5, color='black', linewidth=1.5, linestyle='-')
    ax.set_title(f"Data for {countries} in {years}")
    sc = ax.scatter(info["lrecon"], info["galtan"],c=info["family"].apply(family_color),alpha=0.1, picker=True, s=60)


    for _, row in info.iterrows():
        if showYears:
            label = row["party"] + '\n' + str(row["year"])
        else:
            label = row["party"]

        ax.text(row["lrecon"]-0.02, row["galtan"]+0.01, label,
                    fontsize=5, color=family_color(row["family"]), alpha=0.8)

    ax.set_xlabel("Economic Left–Right")
    ax.set_ylabel("Social Progressive–Conservative")
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
        text = (f"{row['party']} ({row['country']})\n {row['year']}"
                f"Econ: {row['lrecon']:.2f}, Soc: {row['galtan']:.2f}")
        annot.set_text(text)
        annot.set_visible(True)
        fig.canvas.draw_idle()

    fig.canvas.mpl_connect("pick_event", on_pick)

    plt.tight_layout(pad=3.0)
    plt.show()
