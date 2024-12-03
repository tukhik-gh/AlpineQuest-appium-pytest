from alpineQuest.pages.base_page import BasePage

def test_open_alpine_quest(application):
    base_page = BasePage(application)
    assert base_page is not None, "The 'Alpine Quest' app has not been launched."
