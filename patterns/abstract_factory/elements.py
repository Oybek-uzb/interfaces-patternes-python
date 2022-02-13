import platform

from patterns.abstract_factory.interfaces import Button, Checkbox, ElementsFactory


class WindowsButton(Button):
    def click(self):
        print("Windows Button Click")


class LinuxButton(Button):
    def click(self):
        print("Linux Button Click")


class WindowsCheckbox(Checkbox):
    def check(self):
        print("Windows Checkbox Check")


class LinuxCheckbox(Checkbox):
    def check(self):
        print("Linux Checkbox Check")


class WindowsElementsFactory(ElementsFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class LinuxElementsFactory(ElementsFactory):
    def create_button(self) -> Button:
        return LinuxButton()

    def create_checkbox(self) -> Checkbox:
        return LinuxCheckbox()


if __name__ == '__main__':
    ws_elems = WindowsElementsFactory()
    lx_elems = LinuxElementsFactory()

    ws_button = ws_elems.create_button()
    lx_button = lx_elems.create_button()

    ws_checkbox = ws_elems.create_checkbox()
    lx_checkbox = lx_elems.create_checkbox()

    ws_button.click()
    lx_button.click()

    ws_checkbox.check()
    lx_checkbox.check()

    print(platform.system())
