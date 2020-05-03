def add_routes(module_name):
    n = module_name.rfind('.')
    print("n: %s" % n)
    if n == (-1):
        print("-1")
        mod = __import__(module_name, globals(), locals())
    else:
        print("not -1")
        name = module_name[n + 1:]
        mod = getattr(__import__(module_name[:n], globals(), locals(), [name]), name)
    for attr in dir(mod):

        if attr.startswith('_'):
            continue
        fn = getattr(mod, attr)
        if callable(fn):
            method = getattr(fn, '__method__', None)
            path = getattr(fn, '__route__', None)
            if method and path:
                print("method: %s, path: %s" % (method, path))
                pass
                # add_route(app, fn)


if __name__ == "__main__":
    add_routes('handlers')
