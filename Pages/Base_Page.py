class BasePage:
    """
    Base class, used by all the other classes in this project. Contains base settings and methods.
    """

    def __init__(self, driver):
        """
        Initializes the web driver and its settings.
        """
        self.driver = driver
        self.driver.implicitly_wait(5)
        self.timeout = 30

    def find_element(self, locator):
        """
        Base method for locating a single element on a page
        """
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        """
        Base method for locating a group of elements on a page
        """
        return self.driver.find_elements(*locator)
