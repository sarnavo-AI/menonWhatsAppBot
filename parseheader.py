from parsecsv import get_csv_data
from parsejson import get_json_data

def get_header_data(file_type):
    [header, rows] = get_csv_data(file_type)
    final_header_list = []

    mobile_number_index = header.index('mobile_number')
    time_index = header.index('time')

    json_list = get_json_data(file_type)

    for index in range(len(rows)):
        mobile_number = rows[index][mobile_number_index]

        time_split = rows[index][time_index].split(':')
        time = int(time_split[0]) * 60 + int(time_split[1])

        json = json_list[index]

        final_header_list.append((time, mobile_number, json))

    return final_header_list;
