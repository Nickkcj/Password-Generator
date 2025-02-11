import json

def search(website):
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
        for key in data.keys():
            if key == website:
                return data[key]["email"], data[key]["password"]
            
        return KeyError