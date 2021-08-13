import unittest
from selenium import webdriver
from configparser import ConfigParser
from Pages.Ingredients_Page import IngredientsPage
from Pages.Create_Edit_Ingredient_Page import CreateEditIngredientPage
import os


config = ConfigParser()
config.read('test_data.conf')
NAME = config.get('ingredient3', 'name')
DESC = config.get('ingredient3', 'description')
NAME_EDIT = config.get('ingredient1_edit', 'name')
DESC_EDIT = config.get('ingredient1_edit', 'description')


class CreateNewIngredient(unittest.TestCase):

    def setUp(self):
        base_url = os.environ.get('CM_URL')
        self.driver = webdriver.Chrome('chromedriver.exe')

        url = base_url + '/ingredients/new_ingredient/'

        self.driver.get(url)
        self.ingredients_page = IngredientsPage(self.driver)
        self.new_ingredient_page = CreateEditIngredientPage(self.driver)

    def test_create_ingredient(self):
        self.new_ingredient_page.set_name(NAME)
        self.new_ingredient_page.set_desc(DESC)
        self.new_ingredient_page.save_ingr()
        self.ingredients_page.search(NAME)
        results = self.ingredients_page.ingredients_list()
        self.assertEqual(NAME, results[0].text, 'You done fucked up')
        ingredient = self.ingredients_page.click_ingredient(NAME)
        title = ingredient.get_title()
        self.assertEqual(NAME, title.text)

    def tearDown(self):
        self.driver.close()


class DeleteIngredient(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        base_url = os.environ.get('CM_URL')
        url = base_url + '/ingredients/'

        self.driver.get(url)
        self.ingredients_page = IngredientsPage(self.driver)

    def test_delete_ingredient(self):
        self.ingredients_page.search(NAME)
        results = self.ingredients_page.ingredients_list()
        self.assertEqual(NAME, results[0].text, 'You done fucked up')
        ingredient = self.ingredients_page.click_ingredient(NAME)
        delete_ingredient = ingredient.click_delete()
        delete_ingredient.click_confirm()

        self.ingredients_page.search(NAME)
        results = self.ingredients_page.ingredients_list()
        self.assertEqual('Nothing here.', results[0].text)

    def tearDown(self):
        self.driver.close()


class EditIngredient(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        base_url = os.environ.get('CM_URL')
        self.url = base_url + '/ingredients/'

        self.driver.get(self.url)
        self.ingredients_page = IngredientsPage(self.driver)

    def test_edit_ingredient(self):
        self.ingredients_page.search(NAME)
        ingredient_page = self.ingredients_page.click_ingredient(NAME)
        edit_ingredient_page = ingredient_page.click_edit()

        edit_ingredient_page.set_name(NAME_EDIT)
        edit_ingredient_page.set_desc(DESC_EDIT)
        edit_ingredient_page.save_ingr()
        self.driver.get(self.url)

        self.ingredients_page.search(NAME_EDIT)
        results = self.ingredients_page.ingredients_list()

        self.assertEqual(NAME_EDIT, results[0].text, 'You done fucked up')
        ingredient_page = self.ingredients_page.click_ingredient(NAME_EDIT)

        title = ingredient_page.get_title()
        self.assertEqual(NAME_EDIT, title.text)
        desc = ingredient_page.get_desc()
        self.assertEqual(DESC_EDIT, desc.text)

    def tearDown(self):
        self.driver.close()














