import json, copy
from parsecsv import get_csv_data

def process_json(file_type, intermediate_json, header, rows):
    final_json_list = []
    if file_type == 'breakfast' or file_type == 'snack' or file_type == 'items_units':
        option_json = json.load(open('./Assets/Templates/option_format.json'))
        for row in rows:    
            final_json = copy.deepcopy(intermediate_json)

            if file_type == 'breakfast':
                final_json['body'] = 'What did you have for Breakfast?'
                final_json['globalButtons'][0]['title'] = 'Breakfast list'
            elif file_type == 'items_units':
                final_json['body'] = 'How many did you have?'
                final_json['globalButtons'][0]['title'] = 'Option list'

            options_list = []
            for item in row[-1].split(','):
                option = copy.deepcopy(option_json)
                option['title'] = item
                option['postbackText'] = file_type
                options_list.append(option)

            
            final_json['items'][0]['options'] = options_list

            final_json_list.append(final_json)

    elif file_type == 'lunch' or file_type == 'dinner':
        text_json = json.load(open('./Assets/Templates/text_format.json'))
        for row in rows:
            text = copy.deepcopy(text_json)
            final_json_list.append(text)

    return final_json_list    
        
def get_json_data(file_type):
    [header, rows] = get_csv_data(file_type)

    intermediate_json = None
    if file_type == 'breakfast' or file_type == 'snack' or file_type == 'items_units':
        intermediate_json = json.load(open('./Assets/Templates/list_format.json'))
    elif file_type == 'lunch' or file_type == 'dinner':
        intermediate_json = json.load(open('./Assets/Templates/text_format.json'))

    final_json_list = process_json(file_type, intermediate_json, header, rows)

    return final_json_list

if __name__ == '__main__':
    get_json_data('breakfast')
else:
    pass

