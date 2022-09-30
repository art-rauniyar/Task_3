import pandas as pd
import numpy as np

data = pd.read_csv('dataset.csv')
data = data.replace(np.nan, 5)
data.to_csv('final_dataset.csv')
