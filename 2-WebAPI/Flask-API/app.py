import os

from library.app_00_intro import app
# from library.app_01_a_first_get import app
# from library.app_01_a_first_get_and_post import app

if __name__ == '__main__':
    app.debug = True

    # If you have the debugger disabled or trust the users on your network,
    # you can make the server publicly available simply by adding --host=0.0.0.0
    host = os.environ.get('IP', '127.0.0.1')

    port = int(os.environ.get('PORT', 8080)) 

    app.run(host=host, port=port)
