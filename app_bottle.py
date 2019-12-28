from bottle import run, route

@route('/')
def index():
	return 'Hello Word'

run(host='127.0.0.1', port='8080')