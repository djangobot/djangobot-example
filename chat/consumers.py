import json

from channels import Group, Channel

# Connected to websocket.receive
def ws_message(message):
    Group('chat').send({
        'text': message.content['text'],
    })
    content = json.loads(message.content['text'])
    text = content.pop('text')
    user = content.pop('user')
    content['text'] = '[{}] {}'.format(user, text)
    Channel('slack.send').send(content)


# Connected to websocket.connect
def ws_add(message):
    Group('chat').add(message.reply_channel)


# Connected to websocket.disconnect
def ws_disconnect(message):
    Group('chat').discard(message.reply_channel)


def slack_message(message):
    data = json.loads(message.content['text'])
    data['client'] = 'slack'
    Group('chat').send({
        'text': json.dumps(data),
    })
