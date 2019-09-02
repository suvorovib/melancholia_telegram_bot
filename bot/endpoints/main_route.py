from ..endpoints import app


@app.route('/')
def main_route():
    return 'This is main route'
