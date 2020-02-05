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
        if x['Name'].lower() == country.lower(): return x['Code']

    return None

def get_all_locations(city):
    with open('./Cities.json') as f:
      data = json.load(f)

    list = []
    for x in data:
        if(x['name'].lower() == city.lower()):
            temp = x['name'] + ", " + get_code_from_country(x['country'])
            list.append(temp)

    s = "Which of these options did you mean: \n"
    weeb = "You're a f*cking weeb you know that" if city.lower() == "uwu" else "That's not a real city"
    return (s + "\n".join(list)) if len(list) > 0 else weeb
