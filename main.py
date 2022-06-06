from collections import OrderedDict
from parseheader import get_header_data
import datetime, time
from concurrent.futures import ThreadPoolExecutor
import requests, json

def send_message(user_number, json_data):
    # Loading JSON
    temp_payload = json.dumps(json_data, separators=(',', ':'))

    # Parsing JSON
    utf_codes = { '%20' : " ", '%22' : '"', '%5B' : '[', '%5D' : ']',  '%7B' : '{', '%7D' : '}'}
    for [key, value] in utf_codes.items():
        temp_payload = temp_payload.replace(value, key)

    # Chat API
    url = "https://api.gupshup.io/sm/api/v1/msg"
    customer_number = user_number
    payload = "channel=whatsapp&source=917834811114&destination=91" + customer_number + "&message=" + temp_payload + "&src.name=MenonHealthTechPvtLtd"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
        "apikey" : "jntdy7b2fjsb55w7opfx8wh22lupfngs",
    }

    response = requests.post(url, data=payload, headers=headers)
    print(response.text)

def init():
    time_dict = OrderedDict()

    file_types = ['breakfast', 'lunch', 'dinner']
    for file_type in file_types:
        header_data = get_header_data(file_type)
        for data in header_data:
            if data[0] in time_dict:
                time_dict[data[0]].append([data[1], data[2]])
            else:
                time_dict[data[0]] = [[data[1], data[2]]]

    # time_dict[1054] = [['9748366268', {'type': 'text', 'text': 'What did you have for your lunch? \n https://forms.gle/nH8apfyPtrT463mV8'}]]

    # for key in time_dict.keys():
    #     print(key)

    # current_time = datetime.time(hour=0, minute=0, second=0)
    current_time = datetime.datetime.now()
    current_time = int(current_time.strftime("%H")) * 60 + int(current_time.strftime("%M"))

    time_stamp_list = list(time_dict.keys())
    total_time_stamps = len(time_stamp_list)
    current_time_index = 0

    next_time = time_stamp_list[current_time_index]

    while True:
        if next_time - current_time < 0:
            current_time_index += 1
            if current_time_index == total_time_stamps:
                break
            next_time = time_stamp_list[current_time_index]
            continue

        time.sleep((next_time - current_time) * 60)   
        
        start = time.perf_counter()
        with ThreadPoolExecutor() as executor:
            for meta_data in time_dict[next_time]:
                number = meta_data[0]
                json_data = meta_data[1]
                
                executor.submit(send_message, number, json_data)

        finish = time.perf_counter()
        print(finish - start)
        current_time = next_time
        current_time_index += 1

        if current_time_index == total_time_stamps:
            break

        next_time = time_stamp_list[current_time_index]

if __name__ == '__main__':
    init()
