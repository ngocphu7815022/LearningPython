class BasePage:
    def __init__(self, driver):
        self._driver = driver

    def find_element(self, locator):
        print(f"Element đã tìm thấy: {locator}")

    def click(self, locator):
        print(f"Đã click element ở vị trí: {locator}")

    def send_keys(self, locator, value):
        print(f"Đã send key ở vị trí: {locator} với giá trị: {value}")


class LoginPage(BasePage):
    def enter_username(self, locator, value):
        self.find_element(locator)
        self.click(locator)
        self.send_keys(locator, value)

    def enter_password(self, locator, value):
        self.find_element(locator)
        self.click(locator)
        self.send_keys(locator, value)

    def click_login(self, locator):
        self.find_element(locator)
        self.click(locator)


obj = LoginPage("fake driver")

obj.enter_username("textbox_username", "ngocphu")
obj.enter_password("textbox_password", "Abc781111")
obj.click_login("button_login")
