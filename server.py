import re
from flask import Flask, request
from parsereply import generate_reply_text
from main import send_message
from csv import writer
from datetime import date, datetime

replyDict = generate_reply_text()
user_queue = {}

app = Flask(__name__)

def send_reply(data):
    user_item = data['payload']['payload']['title']
    user_number = data['payload']['sender']['dial_code']
    user_name = data['payload']['sender']['name']

    user_queue[user_number] = [user_name, user_item, replyDict[user_item][0]]
    reply_json = replyDict[user_item][1]
    send_message(user_number, reply_json)

def store_reply(data):
    user_quantiy = data['payload']['payload']['title']
    user_number = data['payload']['sender']['dial_code']
    today_date = str(date.today())
    current_time = datetime.now().strftime("%H:%M")

    user_reply_data_list = [today_date, current_time, user_quantiy]
    user_new_row = [user_number] + user_queue[user_number] + user_reply_data_list

    with open('./Assets/Data/Store/breakfast_retrieval.csv', 'a', newline='') as file_obj:
        writer_obj = writer(file_obj)
        writer_obj.writerow(user_new_row)

        file_obj.close()

        user_queue.pop(user_number)

@app.route('/')
def home():
    return "<h1> Hello, this is home </h1>"

@app.route('/callback', methods=["GET", "POST"])
def callback():
    data = request.get_json()
    if data['payload']['type'] == 'list_reply':
        if data['payload']['payload']['postbackText'] == 'breakfast':
            send_reply(data)
        elif data['payload']['payload']['postbackText'] == 'items_units':
            store_reply(data)

    return ""