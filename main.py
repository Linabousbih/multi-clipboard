import clipboard
import sys
import json


SAVED_DATA="clipboard.json"
def save_items(filepath,data):
    with open(filepath, "w") as f:
        json.dump(data,f)

def load_items(filepath):
    try:
        with open(filepath,"r") as f:
            data=json.load(f)
            return data
    except:
        return {}

command = sys.argv[1]
data=load_items(SAVED_DATA)


if command=="save":
    key=sys.argv[2]
    data[key]=clipboard.paste()
    save_items(SAVED_DATA,data)
    print("Saved in clipboard.")
elif command=="copy":
    key = sys.argv[2]
    if key in data:
        clipboard.copy(data[key])
        print("Copied to clipboard")
    else:
        print("Data does not exist")
    #load commands
elif command=="list":
    print()
    #list command
else:
    print("Unknown command")

