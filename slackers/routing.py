channel_routing = {
    'websocket.receive': 'chat.consumers.ws_message',
    'websocket.connect': 'chat.consumers.ws_add',
    'websocket.disconnect': 'chat.consumers.ws_disconnect',
    'slack.message': 'chat.consumers.slack_message',
}
