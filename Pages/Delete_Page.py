from Pages.Base_Page import BasePage
from selenium.webdriver.common.by import By


class DeletePage(BasePage):
    """
    Page class for a page that appears after deleting a cocktail or ingredient.
    """
    def click_confirm(self):
        """
        Locates and clicks on the button that confirms the deletion.
        """
        confirm_button_locator = (By.XPATH, '/html/body/main/div[2]/form/button')
        confirm_button = self.find_element(confirm_button_locator)
        confirm_button.click()
