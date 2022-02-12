from abc import ABC, abstractmethod


class Cellphone(ABC):
    @abstractmethod
    def call(self) -> str:
        pass


class CellphoneCompany(ABC):
    @abstractmethod
    def make_phone(self):
        pass

    def do_call(self) -> str:
        product: Cellphone = self.make_phone()

        # work with product
        result = product.call()

        return result


class Apple(CellphoneCompany):
    def make_phone(self) -> Cellphone:
        return IPhone()


class Google(CellphoneCompany):
    def make_phone(self) -> Cellphone:
        return Pixel()


class IPhone(Cellphone):
    def call(self) -> str:
        return "Call from IPhone"


class Pixel(Cellphone):
    def call(self) -> str:
        return "Call from Pixel"


if __name__ == '__main__':
    print(Apple().do_call())
    print(Google().do_call())
