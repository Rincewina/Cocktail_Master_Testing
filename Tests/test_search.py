import unittest
from selenium import webdriver
from configparser import ConfigParser
from Pages.Cocktails_Page import CocktailsPage
from Pages.Ingredients_Page import IngredientsPage
import os

config = ConfigParser()
config.read('test_data.conf')
INGR_NAME = config.get('ingredient1', 'name')
COCKTAIL_NAME = config.get('cocktail1', 'name')


class SearchTestCocktails(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        base_url = os.environ.get('CM_URL')
        url = base_url + "/cocktails/"

        self.driver.get(url)
        self.cocktails_page = CocktailsPage(self.driver)

    def test_search_cocktail(self):
        self.cocktails_page.search(COCKTAIL_NAME)
        results = self.cocktails_page.cocktails_list()
        self.assertEqual(COCKTAIL_NAME, results[0].text, 'You done fucked up')
        cocktail = self.cocktails_page.click_cocktail(COCKTAIL_NAME)
        title = cocktail.get_title()
        self.assertEqual(COCKTAIL_NAME, title.text)

    def test_blank_search(self):
        self.cocktails_page.search('  ')
        results = self.cocktails_page.cocktails_list()
        self.assertEqual('Nothing here.', results[0].text)

    def tearDown(self):
        self.driver.close()


class SearchTestIngredients(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        base_url = os.environ.get('CM_URL')
        url = base_url + '/ingredients/'
        self.driver.get(url)
        self.ingredients_page = IngredientsPage(self.driver)

    def test_search_ingredient(self):
        self.ingredients_page.search(INGR_NAME)
        results = self.ingredients_page.ingredients_list()
        self.assertEqual(INGR_NAME, results[0].text, 'You done fucked up')
        ingredient = self.ingredients_page.click_ingredient(INGR_NAME)
        title = ingredient.get_title()
        self.assertEqual(INGR_NAME, title.text)

    def test_blank_search(self):
        self.ingredients_page.search('  ')
        results = self.ingredients_page.ingredients_list()
        self.assertEqual('Nothing here.', results[0].text)

    def tearDown(self):
        self.driver.close()