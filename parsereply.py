from parsecsv import get_csv_data
from parsejson import get_json_data

def generate_reply_text():
    [header, rows] = get_csv_data('items_units')

    jsonList = get_json_data('items_units')
    replyDict = {}

    for index in range(len(rows)):
        replyDict[rows[index][0]] = [rows[index][1], jsonList[index]]

    return replyDict

