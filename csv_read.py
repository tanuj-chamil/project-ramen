import csv

def get_data(filename):
    with open(filename) as f:
            data = csv.reader(f)
            x = []
            y = []
            for row in data:
                x.append(float(row[0]))
                y.append(float(row[1]))
    return x,y