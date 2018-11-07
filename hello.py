def wsgi_app(env, start_response):
	#data = [bytes(i + '\n', 'ascii') for i in env['QUERY_STRING'].split('&')]
	data = env['QUERY_STRING'].replace('&', ' \n')
	status = '200 OK'
	headers = [('Content-Type', 'text/plain'), ("Content-Length", str(len(data)))]
	start_response(status, headers)
	return [data]