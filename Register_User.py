import pickle


class UserError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class PhoneError(UserError):
    def __init__(self, msg):
        super().__init__(msg)


class PasswordError(UserError):
    def __init__(self, msg):
        super().__init__(msg)


class FirstNameError(UserError):
    def __init__(self, msg):
        super().__init__(msg)


class EmailError(UserError):
    def __init__(self, msg):
        super().__init__(msg)


class LoginError(UserError):
    def __init__(self, msg):
        super().__init__(msg)


class Register:
    def __init__(self, name: str, phone, password, email: str = None):
        self.__check_data(name, phone, password, email)
        self.name = name
        self.phone = phone
        self.password = password
        self.email = email

    def __check_data(self, name, phone, password, email):
        # if not name.isalpha():
        #     raise FirstNameError('your name is not alphabetic')
        if len(phone) < 10:
            raise PhoneError('your phone number must be 10 digit at least')
        if len(password) < 8:
            raise PasswordError("your pass should be 10 digits!!!")
        if not email.isalpha():
            raise EmailError("you email is does not matter just pass with out any effort...")

    # def __str__(self):
    #     return f'your user registeration is with name of {self.name} \n your pass is : {self.password}'

    def save(self):
        file_name = f"{self.name}.user"
        with open(file_name, 'wb') as f:
            pickle.dump(self, f)
        return file_name

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, "rb") as f:
            return pickle.load(f)

    @classmethod
    def login(cls, name, password):
        """
        Enter your name and password here for login
        :param name:
        :param password:
        :return: Register User
        """
        file_path = f"{name}.user"
        try:
            user = cls.from_file(file_path)
        except FileNotFoundError:
            raise LoginError("user name is not found")
        if user.password != password:
            raise LoginError("password not matched")
        return user

A = Register('ali', '09123456789', '123456789', 'abcdefg')


def register_menu():
    print("register menu")
    print("Enter your profile below:")
    name = input(">> name:")
    phone = input(">> phone:")
    password = input(">> password:")
    email = input(">> email")
    try:
        user = Register(name, phone, password, email)
        file = user.save()
        print(f"User Registered (file: {file})")
    except UserError as e:
        print(e, "\n")
        register_menu()


def login_menu():
    print("Login Menu")
    print("Enter your name & password:")

    name = input(">> name:")
    password = input(">> password:")

    try:
        user = Register.login(name, password)
        print("Welcome:", user)
    except LoginError as e:
        print("Error", e)
        login_menu()


def main_menu():
    print("User manager")
    print(">> 1.Login")
    print(">> 2.Register")

    opt = input(">> Enter your option:")

    if opt == "1":
        login_menu()
    elif opt =="2":
        register_menu()
    else:
        print("Invali option")
        main_menu()


main_menu()
