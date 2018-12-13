from bottle import run, post, request, response, get, route, static_file

#@route('/explorer/<filename>', method='GET')
#def get_file(filename):
#   return static_file(filename, root="web/")

@route('/dashboard/', method='GET')
@route('/dashboard', method='GET')
# BW compat
@route('/explorer/', method='GET')
@route('/explorer', method='GET')
def get_dashboard_index():
    return static_file("dashboard.html", root="web/")

run(host='localhost', port=8228, debug=True)
