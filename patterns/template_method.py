from abc import ABC, abstractmethod


class Cellphone(ABC):
    @abstractmethod
    def call(self) -> str:
        pass


class SocialNetwork(ABC):
    @abstractmethod
    def login(self) -> bool:
        pass

    @abstractmethod
    def send_data(self, data):
        pass

    @abstractmethod
    def logout(self):
        pass

    def send_post(self, post: dict):
        ok = self.login()
        if ok:
            self.send_data(post)
            self.logout()


class Facebook(SocialNetwork):

    def login(self) -> bool:
        print("Facebook login")
        return True

    def send_data(self, data):
        print(data)
        print("Facebook send_data")

    def logout(self):
        print("Facebook logout")


class Instagram(SocialNetwork):

    def login(self) -> bool:
        print("Instagram login")
        return True

    def send_data(self, data):
        print(data)
        print("Instagram send_data")

    def logout(self):
        print("Instagram logout")


if __name__ == '__main__':
    Facebook().send_post({"user": "Arthur", "message": "From Arthur"})
    Instagram().send_post({"user": "Oybek", "message": "From Oybek"})