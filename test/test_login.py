

def test_login(app):
    username = app.config['webadmin']['username']
    assert app.session.is_logged_in_as(username)
