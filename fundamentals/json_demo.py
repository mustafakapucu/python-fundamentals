import json
import os


class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


class UserRepository:

    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

        # load users from .json file
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists("users.json"):
            with open("users.json", 'r', encoding="utf-8") as file:
                users = json.load(file)

                for user in users:
                    user = json.loads(user)
                    newUser = User(
                        username=user["username"], password=user["password"], email=user["email"])
                    self.users.append(newUser)

            for user in self.users:
                print(user.username)
                print(user.password)
                print(user.email)

    def register(self, user: User):
        self.users.append(user)
        self.saveToFile()
        print("Kullanıcı Oluşturuldu")

    def login(self, username, password):
        if self.isLoggedIn:
            print("Zaten login oldunuz")
        else:
            for user in self.users:

                if user.username == username and user.password == password:
                    self.isLoggedIn = True
                    self.currentUser = user
                    print("Login yapıldı.")
                    break

            if self.isLoggedIn == False:
                print("Giriş yapılamadı.")
            else:
                print("Giriş yapıldı")

    def saveToFile(self):

        list = []

        for user in self.users:
            list.append(json.dumps(user.__dict__))

        with open("users.json", 'w') as file:
            json.dump(list, file)

    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print("Çıkış yapıldı")

    def Identity(self):
        if self.isLoggedIn:
            print(f"username: {self.currentUser}")
        else:
            print("Giriş yapılmadı.")


repository = UserRepository()

while True:
    print("Menü".center(50, "*"))
    secim = input(
        '1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\nSeçiniz..')
    if secim == "5":
        break
    else:
        if secim == "1":
            username = input("username: ")
            password = input("password: ")
            email = input("email: ")

            user = User(username=username, password=password, email=email)
            repository.register(user=user)
            print(repository.users)

        elif secim == "2":
            # login
            if repository.isLoggedIn:
                print("Zaten login oldunuz")
            else:
                username = input("Username: ")
                password = input("Password: ")
                repository.login(username=username, password=password)

        elif secim == "3":
            # logout
            repository.logout()
        elif secim == "4":
            # idendity
            repository.Identity()
