import json
from src.config import DATA_PATH


def read_json_data():
    with open(DATA_PATH, 'r') as f:
        return json.load(f)
    
def save_to_json_data(data_list):
    with open(DATA_PATH, 'w') as f:
        json.dump(data_list, f, indent=4)