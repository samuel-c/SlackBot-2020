import os
import re
import slack
from WeatherAPI import get_data
from JsonParse import get_code


MENTION_REGEX = "^<@([WU].+)>(.*)"  # RegEx for parsing command

slack_token = os.environ["SLACK_API_TOKEN"]

@slack.RTMClient.run_on(event='message')
def say_hello(**payload):
    data = payload['data']

    if 'text' in data:
        msg_txt = data['text']

        bot_is_called, cmd = parse_message(msg_txt)
        if bot_is_called:
            cmd_result, thread = handle_command(cmd)

            channel_id = data['channel']
            thread_ts = data['ts'] if thread else None

            webclient = payload['web_client']
            webclient.chat_postMessage(
                channel=channel_id,
                text="{}".format(cmd_result),
                thread_ts=thread_ts
            )


def parse_message(message_text):
    matches = re.search(MENTION_REGEX, message_text)
    if matches and matches.group(1) == bot_id:
        return True, matches.group(2).strip()
    else:
        return False, None


def handle_command(cmd):
    """
    Process command and return a result to be printed in a message to a user
    """
    # Default response is help text for the user
    response = "Not sure what you mean. Try *{}*.".format("Help")

    # Finds and executes the given command, filling in response
    # This is where you start to implement more commands!
    if cmd.startswith("Weather") or cmd.startswith("weather"):
        cmd = cmd.split()
        if "|" in cmd: cmd.remove("|")
        info = cmd[1:]
        response = get_data(info[0].capitalize(), info[1].capitalize())

    elif cmd.startswith("Echo") or cmd.startswith("echo"):
        cmd = cmd.split()
        response = " ".join(cmd[1:]) if len(cmd[1:]) >= 1 else "You have entered an empty string"

    elif cmd.startswith("Cities") or cmd.startswith("cities"):
        cmd = cmd.split()
        response = get_code(cmd[1])

    elif cmd.startswith("Help") or cmd.startswith("help"):
        response = ("Hi there the commands I can perform are: \n"
                    "*Weather*: You can view the current weather using this command. Please use this format \n\t*- @Hoisin Sauce Weather City, Country Code*\n"
                    "*Echo*: I will copy pasta whatever you said recently. Please use this format \n\t*- @Hoisin Sauce Echo Message*\n"
                    "*Cities*: Find the cities for any country given the country code or name. Please use this format \n\t*- @Hoisin Sauce Cities Name/Country Code*\n"
                    "*Help*: You are already here.")

    thread = cmd[0] == "Cities"
    return response, thread

# get user id of the bot
bot_id = slack.WebClient(slack_token).auth_test()['user_id']

# start the bot
rtmclient = slack.RTMClient(token=slack_token)
print("The bot has started")
rtmclient.start()
