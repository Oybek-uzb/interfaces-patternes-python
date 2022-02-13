from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, data: dict):
        pass


class PayPalPaymentStrategy(PaymentStrategy):
    def pay(self, data: dict) -> bool:
        # work with data
        print("working with data API")
        print(data)
        return True


class CreditCardPaymentStrategy(PaymentStrategy):
    def pay(self, data: dict) -> bool:
        # work with dara
        print("working with data API")
        print(data)
        return True


class WebMoneyPaymentStrategy(PaymentStrategy):
    def pay(self, data: dict) -> bool:
        # work with data
        print("working with data")
        print(data)
        return True


class Order:
    def pay(self, data: dict, payment_strategy: PaymentStrategy):
        payment_strategy.pay(data=data)


if __name__ == '__main__':
    o = Order()
    payment_method = input("Choose the type of payment: ")
    payment_strategy = None
    data = None

    if payment_method == "pp":
        pay_pal_email = input("Enter PayPal email: ")
        data = {...}
        payment_strategy = PayPalPaymentStrategy()
    elif payment_method == "cc":
        pay_pal_email = input("Enter card number: ")
        data = {...}
        payment_strategy = CreditCardPaymentStrategy()
    elif payment_method == "wm":
        pay_pal_email = input("Enter WebMoney number: ")
        data = {...}
        payment_strategy = WebMoneyPaymentStrategy()
    else:
        exit("Wrong payment method.")

    o.pay(data=data, payment_strategy=payment_strategy)
