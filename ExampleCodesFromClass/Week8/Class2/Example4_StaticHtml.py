from bottle import route, template, run, static_file

@route("/")
def static_display():
    print("came here")
    return static_file(root="", filename="dummy.html")

run()
