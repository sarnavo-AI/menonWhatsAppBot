import json, copy
from parsecsv import get_csv_data

def process_json(foodType, intermediateJson, header, rows):
    finalJsonList = []
    if foodType == 'breakfast' or foodType == 'snack' or foodType == 'items_units':
        option_json = json.load(open('./Assets/Templates/option_format.json'))
        for row in rows:    
            finalJson = copy.deepcopy(intermediateJson)

            if foodType == 'breakfast':
                finalJson['body'] = 'What did you have for Breakfast?'
                finalJson['globalButtons'][0]['title'] = 'Breakfast list'
            elif foodType == 'items_units':
                finalJson['body'] = 'How many did you have?'
                finalJson['globalButtons'][0]['title'] = 'Option list'

            options_list = []
            for item in row[-1].split(','):
                option = copy.deepcopy(option_json)
                option['title'] = item
                option['postbackText'] = foodType
                options_list.append(option)

            
            finalJson['items'][0]['options'] = options_list

            finalJsonList.append(finalJson)

    elif foodType == 'lunch' or foodType == 'dinner':
        text_json = json.load(open('./Assets/Templates/text_format.json'))
        for row in rows:
            text = copy.deepcopy(text_json)
            finalJsonList.append(text)

    return finalJsonList    
        
def get_json_data(foodType):
    [header, rows] = get_csv_data(foodType)

    intermediateJson = None
    if foodType == 'breakfast' or foodType == 'snack' or foodType == 'items_units':
        intermediateJson = json.load(open('./Assets/Templates/list_format.json'))
    elif foodType == 'lunch' or foodType == 'dinner':
        intermediateJson = json.load(open('./Assets/Templates/text_format.json'))

    finalJsonList = process_json(foodType, intermediateJson, header, rows)

    return finalJsonList

if __name__ == '__main__':
    get_json_data('breakfast')
else:
    pass

