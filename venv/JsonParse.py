import json


def get_code(code):
    if len(code) > 2: return(get_cities(code))

    with open('./Codes.json') as f:
      data = json.load(f)

    for x in data:
        if(x['Code'] == code): return(get_cities(x['Name']))

    return None

def get_cities(country):
    with open('./Cities.json') as f:
      data = json.load(f)
    response = "The cities within "+country+" are: \n"
    found = False
    for x in data:
        if x['country'] == country:
            found = True
            response += x['name'] + '\n'

    return response if found else "Invalid Country Name or Code"


def get_code_from_country(country):
    with open('./Codes.json') as f:
      data = json.load(f)

    for x in data:
        if x['Name'] == country: return x['Code']

    return None