import json
from klein import run, route
from twisted.python import log


@route('/')
def echo(request):
    request.setHeader('Content-Type', 'application/json')
    message = json.load(request.content)
    log.msg('Received: %r' % (message,))

    if not message.get('type') == 'message':
        return json.dumps([])

    return json.dumps([{
        'text': 'You said: %s' % (message['text'],),
        'type': 'message',
        'channel': message['channel'],
    }])


run("localhost", 8000)
