from abc import ABC, abstractmethod


class UserRepository(ABC):
    @abstractmethod
    def create_user(self):
        pass

    @abstractmethod
    def get_user(self):
        pass

    @abstractmethod
    def update_user(self):
        pass

    @abstractmethod
    def delete_user(self):
        pass


class UserRepositoryPostgreSQL(UserRepository):
    def create_user(self):
        pass

    def get_user(self):
        pass

    def update_user(self):
        pass

    def delete_user(self):
        pass


class UserRepositoryMongoDB(UserRepository):
    def create_user(self):
        pass

    def get_user(self):
        pass

    def update_user(self):
        pass

    def delete_user(self):
        pass


class Controller:
    def __int__(self, user_repo: UserRepository):
        self.User_repo = user_repo


if __name__ == "__main__":
    usrm = UserRepositoryMongoDB()
    usrp = UserRepositoryPostgreSQL()
    c = Controller(usrp)
    # or Controller(usrm)

