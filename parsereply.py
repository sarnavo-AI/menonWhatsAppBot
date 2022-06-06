from parsecsv import get_csv_data
from parsejson import get_json_data

def generate_reply_text():
    [header, rows] = get_csv_data('items_units')

    json_list = get_json_data('items_units')
    reply_dict = {}

    for index in range(len(rows)):
        reply_dict[rows[index][0]] = [rows[index][1], json_list[index]]

    return reply_dict

