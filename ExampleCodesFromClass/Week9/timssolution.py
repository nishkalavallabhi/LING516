from bottle import get, post, request, route, template, run

def permutation(first, second):
    if len(first) != len(second):
        return False
    else:
        return ' '.join(sorted(first)) == ' '.join(sorted(second))

@route('/')
@route('/hello')
def hello():
    name = 'Guest'
    return template('Hello {{name}}', name=name)

@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            First string: <input name="first" type="text" />
            Second string: <input name="second" type="text" />
            <input value="Submit" type="submit" />
        </form>
    '''

@post('/login') # or @route('/login', method='POST')
def do_login():
    first = request.forms.get('first')
    second = request.forms.get('second')
    if permutation(first, second) == True:
        return "The strings are permutations."
    else:
        return "The strings are not permutations."

run()
