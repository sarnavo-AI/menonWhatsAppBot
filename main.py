from collections import OrderedDict
from parseheader import get_header_data
import datetime, time
from concurrent.futures import ThreadPoolExecutor
import requests, json

def send_message(number, jsonData):
    # Loading JSON
    tempPayload = json.dumps(jsonData, separators=(',', ':'))

    # Parsing JSON
    utfCodes = { '%20' : " ", '%22' : '"', '%5B' : '[', '%5D' : ']',  '%7B' : '{', '%7D' : '}'}
    for [key, value] in utfCodes.items():
        tempPayload = tempPayload.replace(value, key)

    # Chat API
    url = "https://api.gupshup.io/sm/api/v1/msg"
    customerNumber = number
    payload = "channel=whatsapp&source=917834811114&destination=91" + customerNumber + "&message=" + tempPayload + "&src.name=MenonHealthTechPvtLtd"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
        "apikey" : "jntdy7b2fjsb55w7opfx8wh22lupfngs",
    }

    response = requests.post(url, data=payload, headers=headers)
    print(response.text)

def init():
    timeDict = OrderedDict()

    foodTypes = ['breakfast']
    for foodType in foodTypes:
        headerData = get_header_data(foodType)
        for data in headerData:
            if data[0] in timeDict:
                timeDict[data[0]].append([data[1], data[2]])
            else:
                timeDict[data[0]] = [[data[1], data[2]]]

    # timeDict[1054] = [['9748366268', {'type': 'text', 'text': 'What did you have for your lunch? \n https://forms.gle/nH8apfyPtrT463mV8'}]]

    for key in timeDict.keys():
        print(key)

    # currentTime = datetime.time(hour=0, minute=0, second=0)
    currentTime = datetime.datetime.now()
    currentTime = int(currentTime.strftime("%H")) * 60 + int(currentTime.strftime("%M"))
    
    # print(currentTime)

    timeStampList = list(timeDict.keys())
    totalTimeStamps = len(timeStampList)
    currentTimeStampIndex = 0

    requiredTime = timeStampList[currentTimeStampIndex]

    while True:
        if requiredTime - currentTime < 0:
            currentTimeStampIndex += 1
            if currentTimeStampIndex == totalTimeStamps:
                break
            requiredTime = timeStampList[currentTimeStampIndex]
            continue

        time.sleep((requiredTime - currentTime) * 60)   
        
        start = time.perf_counter()
        with ThreadPoolExecutor() as executor:
            for metaData in timeDict[requiredTime]:
                number = metaData[0]
                jsonData = metaData[1]
                
                executor.submit(send_message, number, jsonData)

        finish = time.perf_counter()
        print(finish - start)
        currentTime = requiredTime
        currentTimeStampIndex += 1

        if currentTimeStampIndex == totalTimeStamps:
            break

        requiredTime = timeStampList[currentTimeStampIndex]

if __name__ == '__main__':
    init()
