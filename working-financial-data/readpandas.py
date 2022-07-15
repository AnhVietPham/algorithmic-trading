import pandas as pd

if __name__ == '__main__':
    fn = '/Users/anhvietpham/Documents/My-Github/algorithmic-trading/working-financial-data/data/BTCHourly.csv'
    data = pd.read_csv(fn, index_col=0, parse_dates=True)
    print(data.info)
    print(f"Closed Price {data['close']}")
