class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # Giả lập vị trí của các element username textbox, password textbox, login button
        self.username_locator = ""
        self.password_locator = ""
        self.login_button_locator = ""

    def enter_username(self, username):
        # Giả lập người dùng sẽ nhập username
        print(username)

    def enter_password(self, password):
        # Giả lập người dùng sẽ nhập password
        print(password)

    def click_login(self):
        print("Đã bấm login")

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()


new_obj = LoginPage("Fake driver")
new_obj.login("ngocphu", "abc123")
