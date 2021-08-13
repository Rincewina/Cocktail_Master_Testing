from Pages.Base_Page import BasePage
from selenium.webdriver.common.by import By


class CreateEditIngredientLocators:
    LOCATOR_NAME_FIELD = (By.ID, 'id_name')
    LOCATOR_DESC_FIELD = (By.ID, 'id_description')
    LOCATOR_SAVE_BUTTON = (By.XPATH, '/html/body/main/div[2]/form/button')


class CreateEditIngredientPage(BasePage):
    """
    Page class. Contains all the methods used when creating and editing an ingredient.
    """
    def set_name(self, text):
        """
        Finds a 'Name' field, clears it and types a text into it.
        """
        name_text = self.find_element(CreateEditIngredientLocators.LOCATOR_NAME_FIELD)
        name_text.click()
        name_text.clear()
        name_text.send_keys(text)

    def set_desc(self, text):
        """
        Finds a 'Description' field, clears it and types a text into it.
        """
        desc_text = self.find_element(CreateEditIngredientLocators.LOCATOR_DESC_FIELD)
        desc_text.click()
        desc_text.clear()
        desc_text.send_keys(text)

    def save_ingr(self):
        """
        Finds and clicks on the 'Save Ingredient' button.
        """
        save_button = self.find_element(CreateEditIngredientLocators.LOCATOR_SAVE_BUTTON)
        save_button.click()


