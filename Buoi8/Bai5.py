from abc import ABC, abstractmethod


class BaseElement(ABC):
    def __init__(self, locator):
        super().__init__()
        self.__locator = locator

    def get_locator(self):
        return self.__locator

    @abstractmethod
    def click(self):
        pass


class Button(BaseElement):
    def click(self):
        return f"Clicking on a button with locator: {self.get_locator()}"


class Checkbox(BaseElement):
    def click(self):
        return f"Toggling a checkbox with locator: {self.get_locator()}"

    def is_selected(self):
        return "Checking selection status...."


# Khởi tạo element
button_obj = Button("Button Fake Element")
checkbox_obj = Checkbox("Checkbox Fake Element")

print(button_obj.click())
print(checkbox_obj.click())
print(checkbox_obj.is_selected())
