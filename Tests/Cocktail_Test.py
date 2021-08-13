import unittest
from selenium import webdriver
from configparser import ConfigParser
import os
from Pages.Create_Edit_Cocktail_Page import CreateEditCocktailPage
from Pages.Cocktails_Page import CocktailsPage

config = ConfigParser()
config.read('test_data.conf')
NAME = config.get('cocktail', 'name')
DESC = config.get('cocktail', 'description')
STEPS = config.get('cocktail', 'steps')
INGR1 = config.get('ingredient1', 'name')
INGR2 = config.get('ingredient2', 'name')
INGR3 = config.get('ingredient3', 'name')
NAME_EDIT = config.get('cocktail_edit', 'name')
DESC_EDIT = config.get('cocktail_edit', 'description')
STEPS_EDIT = config.get('cocktail_edit', 'steps')
INGR1_EDIT = config.get('ingredient1_edit', 'name')
INGR_LIST = [INGR1, INGR2, INGR3]


class CreateNewCocktail(unittest.TestCase):
    """
    Test case class.

    """

    def setUp(self):
        base_url = os.environ.get('CM_URL')
        self.driver = webdriver.Chrome('chromedriver.exe')

        url = base_url + '/cocktails/new_cocktail/'

        self.driver.get(url)
        self.cocktails_page = CocktailsPage(self.driver)
        self.new_cocktail_page = CreateEditCocktailPage(self.driver)

    def test_create_cocktail(self):
        self.new_cocktail_page.set_name(NAME)
        self.new_cocktail_page.set_desc(DESC)
        self.new_cocktail_page.set_steps(STEPS)

        for ingr_id in range(3):
            self.new_cocktail_page.select_ingr(ingr_id, INGR_LIST[ingr_id])
            self.new_cocktail_page.set_amount(ingr_id, '100')
            self.new_cocktail_page.add_ingr()

        self.new_cocktail_page.save_button()
        self.cocktails_page.search(NAME)
        results = self.cocktails_page.cocktails_list()
        self.assertEqual(NAME, results[0].text)
        cocktail = self.cocktails_page.click_cocktail(NAME)
        title = cocktail.get_title()
        self.assertEqual(NAME, title.text)

    def tearDown(self):
        self.driver.close()


class DeleteCocktail(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        base_url = os.environ.get('CM_URL')
        url = base_url + '/cocktails/'

        self.driver.get(url)
        self.cocktails_page = CocktailsPage(self.driver)

    def test_delete_cocktail(self):
        self.cocktails_page.search(NAME)
        results = self.cocktails_page.cocktails_list()
        self.assertEqual(NAME, results[0].text)
        cocktail = self.cocktails_page.click_cocktail(NAME)
        delete_cocktail = cocktail.click_delete()
        delete_cocktail.click_confirm()

        self.cocktails_page.search(NAME)
        results = self.cocktails_page.cocktails_list()
        self.assertEqual('Nothing here.', results[0].text)

    def tearDown(self):
        self.driver.close()


class EditCocktail(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        base_url = os.environ.get('CM_URL')
        url = base_url + '/cocktails/'

        self.driver.get(url)
        self.cocktails_page = CocktailsPage(self.driver)

    def test_edit_cocktail(self):
        self.cocktails_page.search(NAME)
        cocktail_page = self.cocktails_page.click_cocktail(NAME)
        edit_cocktail_page = cocktail_page.click_edit()

        edit_cocktail_page.set_name(NAME_EDIT)
        edit_cocktail_page.set_desc(DESC_EDIT)
        edit_cocktail_page.set_steps(STEPS_EDIT)

        edit_cocktail_page.select_ingr(0, INGR1_EDIT)
        edit_cocktail_page.set_amount(0, '50')

        edit_cocktail_page.save_button()

        self.cocktails_page.search(NAME_EDIT)
        results = self.cocktails_page.cocktails_list()
        self.assertEqual(NAME_EDIT, results[0].text)
        cocktail = self.cocktails_page.click_cocktail(NAME_EDIT)
        title = cocktail.get_title()
        self.assertEqual(NAME_EDIT, title.text)
        desc = cocktail.get_desc()
        self.assertEqual(DESC_EDIT, desc.text)
        steps = cocktail.get_steps()
        self.assertEqual(STEPS_EDIT, steps.text)
        ingredients = cocktail_page.get_ingr_list()
        self.assertIn(INGR1_EDIT, ingredients[0].text)

    def tearDown(self):
        self.driver.close()








