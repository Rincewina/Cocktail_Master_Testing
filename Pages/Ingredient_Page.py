from Pages.Base_Page import BasePage
from Pages.Delete_Page import DeletePage
from Pages.Create_Edit_Ingredient_Page import CreateEditIngredientPage
from selenium.webdriver.common.by import By


class IngredientLocators:
    LOCATOR_TITLE = (By.TAG_NAME, 'h3')
    LOCATOR_DESC = (By.XPATH, '/html/body/main/div[2]/div/div/p')
    LOCATOR_EDIT_BUTTON = (By.XPATH, '/html/body/main/div[2]/a[1]')
    LOCATOR_DELETE_BUTTON = (By.XPATH, '/html/body/main/div[2]/a[2]')


class IngredientPage(BasePage):
    """
    Page class. Contains all the usable methods for the individual ingredient page
    """
    def get_title(self):
        """
        Locates the ingredients' title and returns its value

        """
        title = self.find_element(IngredientLocators.LOCATOR_TITLE)
        return title

    def get_desc(self):
        """
        Locates the ingredients' title and returns its value

        """
        desc = self.find_element(IngredientLocators.LOCATOR_DESC)
        return desc

    def click_edit(self):
        """
        Locates and clicks on the "Edit" button.

        """
        edit_button = self.find_element(IngredientLocators.LOCATOR_EDIT_BUTTON)
        edit_button.click()
        return CreateEditIngredientPage(self.driver)

    def click_delete(self):
        """
        Locates and clicks on the "Delete" button.

        """
        delete_button = self.find_element(IngredientLocators.LOCATOR_DELETE_BUTTON)
        delete_button.click()
        return DeletePage(self.driver)


