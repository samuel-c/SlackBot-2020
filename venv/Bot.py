import os
import re
import slack
from Commands import execute_command

MENTION_REGEX = "^<@([WU].+)>(.*)"  # RegEx for parsing command

slack_token = os.environ["SLACK_API_TOKEN"]
@slack.RTMClient.run_on(event='message')
def say_hello(**payload):
    data = payload['data']

    if 'text' in data:
        msg_txt = data['text']

        bot_is_called, cmd = parse_message(msg_txt)
        if bot_is_called:
            cmd_result, thread, philadelphia = execute_command(cmd)

            channel_id = data['channel']
            thread_ts = data['ts'] if thread else None
            attachment = [{"title": "Its always sunny in philadelphia", "image_url": "https://images-na.ssl-images-amazon.com/images/I/51PnMdza2vL._AC_.jpg"}] if philadelphia else None
            webclient = payload['web_client']

            webclient.chat_postMessage(
                channel=channel_id,
                text="{}".format(cmd_result),
                thread_ts=thread_ts,
                attachments = attachment
            )


def parse_message(message_text):
    matches = re.search(MENTION_REGEX, message_text)
    if matches and matches.group(1) == bot_id:
        return True, matches.group(2).strip()
    else:
        return False, None


# get user id of the bot
bot_id = slack.WebClient(slack_token).auth_test()['user_id']

# start the bot
rtmclient = slack.RTMClient(token=slack_token)
print("The bot has started")
rtmclient.start()
