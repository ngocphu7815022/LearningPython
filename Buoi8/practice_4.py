class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self._username_locator = "username locator"
        self._password_locator = "password locator"
        self._login_button_locator = "login button locator"

    def enter_username(self, username):
        print(f"Username: {username}")

    def enter_password(self, password):
        print(f"Password: {password}")

    def click_login(self):
        print("Đã bấm nút login")

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()


login_obj = LoginPage("Fake driver")
login_obj.login("abc", "abc1234")
