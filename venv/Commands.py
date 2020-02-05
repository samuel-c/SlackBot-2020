from JsonParse import get_code, get_all_locations
from WeatherAPI import get_data

def execute_command(cmd):
    try:
        possible_commands = ['weather', 'echo', 'cities', 'help']
        cmd = cmd.lower()
        command = possible_commands.index(cmd.split(' ', 1)[0])
        cmd = cmd.split() if command is not 0 else cmd[8:]
        valid_entry = ',' in cmd

        #Weather
        if command is 0:
            if ("philadelphia" in cmd): return "", False, True
            cmd = cmd.split(',') if valid_entry else cmd

            return (get_all_locations(cmd), False, False) if not valid_entry else (get_data(cmd[0].capitalize(), cmd[1].capitalize()), False, False)

        #Echo
        elif command is 1: return " ".join(cmd[1:]) if len(cmd[1:]) >= 1 else "You have entered an empty string", False, False

        #Cities
        elif command is 2: return get_code(cmd[1]), True, False

        #Help
        elif command is 3: return ("Hi there the commands I can perform are: \n"
                                "*Weather*: You can view the current weather using this command. Please use this format \n\t*- @Hoisin Sauce Weather City, Country Code*\n"
                                "*Echo*: I will copy pasta whatever you said recently. Please use this format \n\t*- @Hoisin Sauce Echo Message*\n"
                                "*Cities*: Find the cities for any country given the country code or name. Please use this format \n\t*- @Hoisin Sauce Cities Name/Country Code*\n"
                                "*Help*: You are already here."), False, False

    except: return "Not sure what you mean. Try the *Help* command.", False, False
