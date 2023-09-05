from pages.home_page import HomePage
from pages.ducks_page import DucksPage
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class DucksTests(unittest.TestCase):

    # Setup
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp, setUp):
        self.hp = HomePage(self.driver)
        self.dp = DucksPage(self.driver)

    # Search for Ducks and verify page title
    @pytest.mark.run(order=2)
    def test_search(self):
        self.hp.text_search("Ducks")
        result = self.hp.verify_search_successfull("Ducks - Google Search")
        assert result == True

    # Search for Ducks and verify page elements
    @pytest.mark.run(order=2)
    def test_ducks_page(self):
        self.hp.text_search("Ducks")
        result = self.hp.verify_search_successfull("Ducks - Google Search")
        assert result == True
        ducks = self.dp.verify_ducks_section()
        people = self.dp.verify_people_ask_section()
        navigation_menu = self.dp.verify_navigation_menu()
        wikipedia = self.dp.verify_wikipedia()
        assert ducks
        assert navigation_menu
        assert people
        assert wikipedia