import functools


def get(path):
    '''
    Define decorator @get('/path')
    '''

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)

        wrapper.__method__ = 'GET'
        wrapper.__route__ = path
        return wrapper

    return decorator

@get('/handle')
def handle():
    print("name: %s")

@get("/do_handle")
def do_handle(handle):
    pass

@get("/do_something")
def do_something(some):
    pass
