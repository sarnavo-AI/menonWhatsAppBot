import csv

def get_csv_data(foodType):
    fileName = foodType + '_fetching.csv'      
    file = open('./Assets/Data/Retrive/' + fileName)
    csvreader = csv.reader(file)

    header = []
    header = next(csvreader)

    rows = []
    for row in csvreader:
        rows.append(row)

    return [header, rows]

if __name__ == "__main__":
    pass
else:
    pass