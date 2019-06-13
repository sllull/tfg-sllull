import json


def getJSON():
    with open('./data.json') as json_file:
        data = json.load(json_file)
    return data


def writeJSON(pred, pacientData):
    data = {}
    data['prediction'] = pred
    data['dia'] = pacientData[0]
    data['mes'] = pacientData[1]
    data['any'] = pacientData[2]
    data['cp'] = pacientData[3]
    data['edat'] = pacientData[4]
    data['sexe'] = pacientData[5]
    data['pes'] = pacientData[6]
    data['urg_vis'] = pacientData[7]
    data['nom_diag'] = cie10(pred)
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)


def cie10(code):
    with open("cie10.csv", 'r') as file:
        for line in file:
            if str(code) in line:
                return line.split(";")[1]
