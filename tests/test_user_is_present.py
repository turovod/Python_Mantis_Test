def test_user_is_present(app):
    assert app.soap.can_login("administrator", "root")
