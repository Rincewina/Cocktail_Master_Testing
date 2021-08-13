from Pages.Base_Page import BasePage
from Pages.Cocktail_Page import CocktailPage
from selenium.webdriver.common.by import By


class CocktailsLocators:
    LOCATOR_SEARCH_FIELD = (By.NAME, "q")
    LOCATOR_SEARCH_RESULT = (By.TAG_NAME, 'li')
    LOCATOR_COCKTAIL_TITLE = (By.TAG_NAME, 'h3')


class CocktailsPage(BasePage):
    """
    Page class. Contains all the usable methods for the page that displays a list of cocktails and a search field.
    """
    def search(self, query):
        """
        Search method. Finds the search field, clicks on it and sends a query.
        """
        search = self.find_element(CocktailsLocators.LOCATOR_SEARCH_FIELD)
        search.click()
        search.send_keys(query+'\n')

    def cocktails_list(self):
        """
        This method finds a full list of cocktails on the page
        """
        cocktails = self.find_elements(CocktailsLocators.LOCATOR_SEARCH_RESULT)
        return cocktails

    def click_cocktail(self, name):
        """
        Finds and clicks on the specific cocktail.
        """
        locator_link = (By.LINK_TEXT, name)
        cocktail = self.find_element(locator_link)
        cocktail.click()
        return CocktailPage(self.driver)
