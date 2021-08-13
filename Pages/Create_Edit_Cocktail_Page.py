from Pages.Base_Page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class CreateEditCocktailLocators:
    LOCATOR_NAME_FIELD = (By.ID, 'id_name')
    LOCATOR_DESC_FIELD = (By.ID, 'id_description')
    LOCATOR_STEPS = (By.ID, 'id_steps')
    LOCATOR_ADD_INGR = (By.ID, 'add-form')
    LOCATOR_INGR_LIST = [(By.NAME, 'form-0-ingredient'),
                         (By.NAME, 'form-1-ingredient'),
                         (By.NAME, 'form-2-ingredient')]
    LOCATOR_AMOUNT_LIST = [(By.NAME, 'form-0-quantity'),
                           (By.NAME, 'form-1-quantity'),
                           (By.NAME, 'form-2-quantity')]
    LOCATOR_SAVE_BUTTON = (By.XPATH, '//*[@id="form-container"]/button[2]') 


class CreateEditCocktailPage(BasePage):
    """
    Page class. Contains all the methods used when creating and editing a cocktail.
    """
    def set_name(self, text):
        """
        Finds a 'Name' field, clears it and types a text into it.
        """
        name_text = self.find_element(CreateEditCocktailLocators.LOCATOR_NAME_FIELD)
        name_text.click()
        name_text.clear()
        name_text.send_keys(text)

    def set_desc(self, text):
        """
        Finds a 'Description' field, clears it and types a text into it.
        """
        desc_text = self.find_element(CreateEditCocktailLocators.LOCATOR_DESC_FIELD)
        desc_text.click()
        desc_text.clear()
        desc_text.send_keys(text)

    def set_steps(self, text):
        """
        Finds a 'Steps' field, clears it and types a text into it.
        """
        steps_text = self.find_element(CreateEditCocktailLocators.LOCATOR_STEPS)
        steps_text.click()
        steps_text.clear()
        steps_text.send_keys(text)

    def add_ingr(self):
        """
        Finds and clicks on the 'Add Ingredient' button.
        """
        add_ingr_button = self.find_element(CreateEditCocktailLocators.LOCATOR_ADD_INGR)
        add_ingr_button.click()

    def select_ingr(self, ingr_id, text):
        """
        Selects an ingredient from the list
        """
        select_ingr_list = Select(self.find_element(CreateEditCocktailLocators.LOCATOR_INGR_LIST[ingr_id]))
        select_ingr_list.select_by_visible_text(text)

    def set_amount(self, ingr_id, text):
        """
        Sets an amount value for the ingredient
        """
        amount = self.find_element(CreateEditCocktailLocators.LOCATOR_AMOUNT_LIST[ingr_id])
        amount.click()
        amount.clear()
        amount.send_keys(text)

    def save_button(self):
        """
        Finds and clicks on the 'Save cocktail' button.
        """
        save_button = self.find_element(CreateEditCocktailLocators.LOCATOR_SAVE_BUTTON)
        save_button.click()