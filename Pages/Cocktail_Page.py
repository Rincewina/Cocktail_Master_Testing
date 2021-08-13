from Pages.Base_Page import BasePage
from Pages.Delete_Page import DeletePage
from Pages.Create_Edit_Cocktail_Page import CreateEditCocktailPage
from selenium.webdriver.common.by import By


class CocktailLocators:
    LOCATOR_TITLE = (By.TAG_NAME, 'h3')
    LOCATOR_DESC = (By.XPATH, '/html/body/main/div[2]/div[1]/div/p')
    LOCATOR_INGR_LIST = (By.XPATH, '/html/body/main/div[2]/div[2]/ul')
    LOCATOR_STEPS = (By.XPATH, '/html/body/main/div[2]/div[3]/div/p')
    LOCATOR_EDIT_BUTTON = (By.XPATH, '/html/body/main/div[2]/a[1]')
    LOCATOR_DELETE_BUTTON = (By.XPATH, '/html/body/main/div[2]/a[2]')


class CocktailPage(BasePage):
    """
    Page class. Contains all the usable methods for the individual cocktail page
    """
    def get_title(self):
        """
        Locates the cocktails' title and returns its value

        """
        title = self.find_element(CocktailLocators.LOCATOR_TITLE)
        return title

    def get_desc(self):
        """
        Locates the cocktails' description field and returns its value

        """
        desc = self.find_element(CocktailLocators.LOCATOR_DESC)
        return desc

    def get_ingr_list(self):
        """
        Locates the cocktails' list of ingredients and returns its value

        """
        ingr_list = self.find_elements(CocktailLocators.LOCATOR_INGR_LIST)
        return ingr_list

    def get_steps(self):
        """
        Locates the "Steps" field and returns its value

        """
        steps = self.find_element(CocktailLocators.LOCATOR_STEPS)
        return steps

    def click_edit(self):
        """
        Locates and clicks on the "Edit" button.

        """
        edit_button = self.find_element(CocktailLocators.LOCATOR_EDIT_BUTTON)
        edit_button.click()
        return CreateEditCocktailPage(self.driver)

    def click_delete(self):
        """
        Locates and clicks on the "Delete" button.

        """
        delete_button = self.find_element(CocktailLocators.LOCATOR_DELETE_BUTTON)
        delete_button.click()
        return DeletePage(self.driver)

