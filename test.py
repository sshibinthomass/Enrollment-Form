import json


def get_inputs():
    # user input to record the log
    name = input("Name:")
    d = {}
    d["date"] = input("Enter a date in YYYY-MM-DD format:")
    d["hours"] = input("Hours:")
    return (name, d)


out = {}

while True:
    exit = input("Do you want to add another input (y/n)? ")
    if exit.lower() == "n":
        break
    else:
        name, d = get_inputs()
        out[name] = d

with open("names.json", "w") as f:
    json.dump(out, f, indent=2)
