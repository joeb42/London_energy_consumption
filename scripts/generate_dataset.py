import pandas as pd
from datetime import datetime
from pathlib import Path

# path to data dir
DATA_PATH = Path(__file__).parent.parent / "data"
MERGED_PATH = DATA_PATH / "london_energy_and_weather.csv"


def merge_datasets():
    energy_df = pd.read_csv(DATA_PATH / "london_energy.csv")
    weather_df = pd.read_csv(DATA_PATH / "london_weather.csv")
    weather_df = weather_df.rename(columns={"date": "dateval"})
    weather_df["date"] = pd.to_datetime(weather_df["dateval"], format="%Y%m%d")
    energy_df["date"] = energy_df["Date"].apply(datetime.strptime, args=("%Y-%m-%d",))
    energy_df = energy_df.drop("Date", axis=1)
    merged_df = pd.merge(weather_df, energy_df, on="date")
    return merged_df


def main():
    print("Merging weather and energy datasets")
    df = merge_datasets()
    df.to_csv(MERGED_PATH)


if __name__ == "__main__":
    main()
