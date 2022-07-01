import os
from pathlib import Path

import pandas as pd


def preprocessing(input_df: pd.DataFrame) -> pd.DataFrame:
    mapping = {
        "Date": "date",
        "Gare": "gare",
        "Nature d'objets": "nature",
        "Type d'objets": "type",
    }
    df = input_df.rename(columns=mapping)
    return df[mapping.values()]


if __name__ == '__main__':
    root_dir = Path(__file__).parent
    input_file_path = os.path.join(root_dir, "./input/sncf_objets_trouves.csv")
    input_df = pd.read_csv(
        input_file_path, sep=";"
    )
    cleaned_df = preprocessing(input_df)
    top_tens_villes: pd.DataFrame = cleaned_df[["gare", "nature"]].groupby(by="gare").count()["nature"].nlargest(n=10).reset_index()
    top_tens_villes.to_parquet("./output/top_tens_villes.parquet")