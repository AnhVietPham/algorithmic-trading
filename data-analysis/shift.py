import pandas as pd

if __name__ == '__main__':
    ind = pd.date_range('01 / 01 / 2000', periods=5, freq='12H')
    df = pd.DataFrame({"A": [1, 2, 3, 4, 5],
                       "B": [10, 20, 30, 40, 50],
                       "C": [11, 22, 33, 44, 55],
                       "D": [12, 24, 51, 36, 2]},
                      index=ind)
    print(df)

    # Shift index = 2 followed axis = 0
    print(df.shift(2, axis=0))

    # Shift index = -1 followed axis = 0
    print(df.shift(-1, axis=0))

    # Shift index = 2 followed axis = 0
    print(df.shift(1, axis=1))

    # Shift index = -1 followed axis = 1
    print(df.shift(-1, axis=1))
