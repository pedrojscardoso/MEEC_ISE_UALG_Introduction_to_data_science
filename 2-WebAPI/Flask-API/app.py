import os

# comment out the line below to run the other examples
# app_00_intro - intro version with a simple "hello world"
# from library.app_00_intro import app

# app_01_a_first_get - version with a simple GET
# from library.app_01_a_first_get import app

# app_02_CRUD - version with CRUD operations
from library.app_02_CRUD import app


if __name__ == '__main__':
    app.debug = True

    # If you have the debugger disabled or trust the users on your network,
    # you can make the server publicly available simply by adding --host=0.0.0.0
    host = os.environ.get('IP', '127.0.0.1')

    port = int(os.environ.get('PORT', 8080)) 

    app.run(host=host, port=port)
