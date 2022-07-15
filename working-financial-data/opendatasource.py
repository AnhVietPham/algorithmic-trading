import configparser
import quandl as q

config = configparser.ConfigParser()
config.read('/Users/anhvietpham/Documents/My-Github/algorithmic-trading/working-financial-data/pyalgo.cfg')

if __name__ == '__main__':
    q.ApiConfig.api_key = "_Higkc3-P5P1k2cD7g-W"
    data = q.get('FSE/SAP_X')
    print(data.iloc[:4, :10].info)
