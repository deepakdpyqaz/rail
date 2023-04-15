import numpy as np
import pandas as pd
from goibibo import get_data
from multiprocessing import Pool
import json
import os


def get_and_save(train_number):
    if os.path.exists(f"trains2/{train_number}.json"):
        return
    op = get_data(train_number)
    with open(f"trains2/{train_number}.json", "w") as f:
        json.dump(op, f)
    print(f"Done {len(os.listdir('trains2'))}")


if __name__ == "__main__":
    df = pd.read_csv("analysis2.csv")
    print(f"Total {len(df['train_number'].unique())}")
    with Pool() as p:
        p.map(get_and_save, df["train_number"].unique())
    print(f"Done")
