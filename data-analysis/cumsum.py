import pandas as pd
import numpy as np

if __name__ == '__main__':
    df = pd.DataFrame({"A": [5, 3, 6, 4],
                       "B": [11, 2, 4, 3],
                       "C": [4, 3, 8, 5],
                       "D": [5, 4, 2, 8]})
    print(df)
    print(df.cumsum(axis=0).apply(np.exp))
    print(df.cumsum(axis=0))
    print(df.cumsum(axis=1))
