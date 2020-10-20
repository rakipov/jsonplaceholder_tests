import json
import os
from mimesis import Text


def broken_data():
    text = Text('en')
    data = {
        'title': text.text(quantity=2),
        'body': text.text(quantity=1400),
        'userId': 1
    }
    return data


def get_expected_response_data():
    current_path = str(os.path.dirname(os.path.abspath(__file__)))
    expected_data = os.path.join(current_path, 'fixtures/user_11.json')
    with open(expected_data, 'r') as read_file:
        expected_response = json.load(read_file)
        return expected_response
