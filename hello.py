from urlparse import urlparse, parse_qsl
def wsgi_app(env, start_response):
	parsed = dict(parse_qsl(env['QUERY_STRING']))
	data = env['QUERY_STRING'].replace('&', '\n')
	status = '200 OK'
	headers = [('Content-Type', 'text/plain'), ("Content-Length", str(len(data)))]
	start_response(status, headers)
	return [data]