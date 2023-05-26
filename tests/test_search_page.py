from page.main_page import MainPage


class TestSearchPo:
    def setup_class(self):
        self.main = MainPage()

    def setup(self):
        self.search = self.main.to_search_advance()

    def teardown_class(self):
        self.main.close()

    def test_search_topic(self):
        assert 'selenium' in str(self.search.search_topic(keyword='selenium')[0]).lower()

    def test_search_category(self):
        assert 'selenium' in str(self.search.search_category(keyword='selenium')[0]).lower()

    def test_search_user(self):
        assert 'seven' in str(self.search.search_user(keyword='seven')[0]).lower()

    def test_search_poster(self):
        assert 'selenium' in str(self.search.search_poster(keyword='selenium')[0]).lower()


