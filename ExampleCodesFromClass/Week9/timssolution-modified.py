from bottle import get, post, request, route, template, run

def permutation(first, second):
    if len(first) != len(second):
        return False
    else:
        return ' '.join(sorted(first)) == ' '.join(sorted(second))

@get('/')
def enter():
    return template('homepage.tpl')

@post('/check')
def checkpermutations():
    first = request.forms.get('first')
    second = request.forms.get('second')
    areornot = ""
    if permutation(first, second) == True:
        areornot = "are"
    else:
        areornot = "are not"
    return template('resultpage.tpl', string1=first, string2=second, areornot=areornot)

run()
