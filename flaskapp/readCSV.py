import numpy as np
import pandas as pd
from pandas import DataFrame

data = pd.read_csv("info.csv")

info = data.iloc(0)

# print(type(info))

for i in range(1,data.size-2):
    # area, category, name, phone, lat, lon = i;
    print(data.values[i])