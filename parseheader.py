from parsecsv import get_csv_data
from parsejson import get_json_data

def get_header_data(foodType):
    [header, rows] = get_csv_data(foodType)
    finalHeaderList = []

    mobileNumberIndex = header.index('mobile_number')
    timeIndex = header.index('time')

    jsonList = get_json_data(foodType)
    for index in range(len(rows)):
        mobileNumber = rows[index][mobileNumberIndex]

        timeSplit = rows[index][timeIndex].split(':')
        time = int(timeSplit[0]) * 60 + int(timeSplit[1])

        json = jsonList[index]

        finalHeaderList.append((time, mobileNumber, json))

    return finalHeaderList;
