import pandas as pd

if __name__ == '__main__':
    df = pd.DataFrame({"A": [5, 3, 6, 4],
                       "B": [11, 2, 4, 3],
                       "C": [4, 3, 8, 5],
                       "D": [5, 4, 2, 8]})
    print(df)
    print(df.cummax(axis=0))
    print(df.cummax(axis=1))
