import numpy as np
import pandas as pd

if __name__ == '__main__':
    a = np.arange(15).reshape(5, 3)
    print(a)
    columns = list('abc')
    print(columns)
    index = pd.date_range('2017-7-1', periods=5, freq='B')
    print(index)
    df = pd.DataFrame(a, columns=columns, index=index)
    print(df)
    print(2 * df)
    print(df.sum())
    print(df['a'] + df['c'])
    print(df['a'] > 5)
    print(df[df['a'] > 5])
