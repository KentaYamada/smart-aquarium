import os


if __name__ == '__main__':
    # set env
    os.environ['APP_TYPE'] = 'development'

    from backend import app
    app.run()
