from Pages.Base_Page import BasePage
from selenium.webdriver.common.by import By
from Pages.Ingredient_Page import IngredientPage


class IngredientsLocators:
    LOCATOR_SEARCH_FIELD = (By.NAME, "q")
    LOCATOR_SEARCH_RESULT = (By.TAG_NAME, 'li')
    LOCATOR_COCKTAIL_TITLE = (By.TAG_NAME, 'h3')


class IngredientsPage(BasePage):
    """
    Page class. Contains all the methods for the page that displays a search field and a list of ingredients.
    """
    def search(self, query):
        """
        Search method. Finds the search field, clicks on it and sends a query.
        """
        search = self.find_element(IngredientsLocators.LOCATOR_SEARCH_FIELD)
        search.click()
        search.send_keys(query+'\n')

    def ingredients_list(self):
        """
        This method finds a full list of ingredients on the page
        """
        ingredients = self.find_elements(IngredientsLocators.LOCATOR_SEARCH_RESULT)
        return ingredients

    def click_ingredient(self, name):
        """
        Finds and clicks on the specific ingredient.
        """
        locator_link = (By.LINK_TEXT, name)
        ingredient = self.find_element(locator_link)
        ingredient.click()
        return IngredientPage(self.driver)
