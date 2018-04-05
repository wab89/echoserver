import bottle

@bottle.route('/<data>')
def index(data):
    return f'<marquee>{data}</marquee>'

bottle.run(host='', port=8080)
