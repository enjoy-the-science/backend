from backend import create_app, user, workspace


app = create_app()
app.register_blueprint(user.app, url_prefix='/user')
app.register_blueprint(workspace.app, url_prefix='/workspace')


@app.route('/')
def test() -> str:
    return "It's alive!"
