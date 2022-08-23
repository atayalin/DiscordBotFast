import yaml
import requests
import asyncio
from datetime import datetime


async def message_loop(token, channel_id, message, period):
    try:
        send_message(token, channel_id, message)
        while (True):
            await asyncio.sleep(period)    
            send_message(token, channel_id, message)
    except KeyboardInterrupt:           # TODO: complete it. it does not wors correctly.
        print('Exiting from applciation...')
        exit(0)


def send_message(token, channel_id, message):
    payload = {
        'content': message
    }
    header = {
        'Authorization': token
    }
    try: 
        res = requests.post(
            'https://discord.com/api/v8/channels/{}/messages'.format(channel_id), 
            data=payload, headers=header)        
    except:
        print('message cannot be successfully sent to "{}". MSG=[{}]'.format(channel_id, message))
    else:
        response_body = res.json()
        if (response_body['content'] == message) and (response_body['channel_id'] == channel_id) and (str(res.status_code).startswith('2')):
            print('Message is successfully sent on "{}", from "{}" to "{}". MSG=[{}]'.format(datetime.now().strftime('%d.%m.%Y %H:%M:%S'), response_body['author']['username'], channel_id, message))
        else:
            print('Message sent but there is a problem. Status code maybe different than 2**.')

async def main():

    with open("data.yaml") as f:

        data = yaml.load_all(f, Loader=yaml.FullLoader)

        tasks = []
        for i in data:
            for client in i["clients"]:
                for channel in client['channels']:
                    tasks.append(asyncio.create_task(message_loop(client['token'], channel['channel_id'], channel['message'], 60 * float(channel['period']))))
        
        for task in tasks:
            await task

asyncio.run(main())
