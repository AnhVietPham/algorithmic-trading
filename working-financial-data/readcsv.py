import csv


def openCSV(path):
    with open(path, 'r') as f:
        for _ in range(5):
            print(f.readline(), end='')


if __name__ == '__main__':
    fn = 'working-financial-data/data/BTCHourly.csv'
    openCSV(fn)

    # csv_reader = csv.reader(open(fn, 'r'))
    csv_reader = csv.DictReader(open(fn, 'r'))
    data = list(csv_reader)
    print(data[:5])
    sumClosedPrice = sum([float(l['close']) for l in data]) / len(data)
    print(f'Sum of Closed Price {sumClosedPrice}')
