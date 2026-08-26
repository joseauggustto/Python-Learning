#hero go again

import json

def readJsonFile(filename):
    data=""
    try:
        with open('Projetos/Calc-Insulina/insulin.json') as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")
    return data
