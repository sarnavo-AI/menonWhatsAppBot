import csv
from fileinput import close

def get_csv_data(file_type):
    file_name = file_type + '_fetching.csv'      
    with open('./Assets/Data/Retrive/' + file_name) as file:
        csv_reader = csv.reader(file)

        header = []
        header = next(csv_reader)

        rows = []
        for row in csv_reader:
            rows.append(row)

        file.close()

        return [header, rows]

if __name__ == "__main__":
    pass
else:
    pass