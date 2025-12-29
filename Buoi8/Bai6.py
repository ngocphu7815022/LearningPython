class DriverFactory:
    @staticmethod
    def get_driver(browser_name):
        if browser_name == "chrome":
            print("Initializing Chrome Driver...")
            return "ChromeDriver object"
        elif browser_name == "firefox":
            print("Initializing Firefox Driver...")
            return "FirefoxDriver object"
        else:
            raise ValueError("Browser không được hỗ trợ")


obj = DriverFactory()
print(obj.get_driver("chrome"))  # OK
print(obj.get_driver("firefox"))  # OK
print(obj.get_driver("edge"))  # Không hỗ trợ -> Error
