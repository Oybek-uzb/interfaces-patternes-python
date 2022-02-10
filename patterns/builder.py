class Computer:
    __cpu = None
    __ram = None
    __mouse = None
    __keyboard = None
    __monitor = None
    __box = None

    def cpu(self, cpu: str):
        self.__cpu = cpu
        return self

    def ram(self, ram: str):
        self.__ram = ram
        return self

    def mouse(self, mouse: str):
        self.__mouse = mouse
        return self

    def keyboard(self, keyboard: str):
        self.__keyboard = keyboard
        return self

    def monitor(self, monitor: str):
        self.__monitor = monitor
        return self

    def box(self, box: str):
        self.__box = box
        return self

    @staticmethod
    def build_gaming_computer():
        return Computer().cpu("").ram("").mouse("").box("").keyboard("").monitor("")

    @staticmethod
    def build_office_computer():
        return Computer().cpu("").ram("").monitor("").mouse("").box("").keyboard("")


if __name__ == "__main__":
    c = Computer().cpu("").ram("").monitor("").keyboard("").mouse("").box("")
    c_g = Computer.build_gaming_computer()
    c_o = Computer.build_office_computer()
