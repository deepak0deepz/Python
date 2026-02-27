class User:
    def __init__(self, password):
        self.__password = password

    def login(self):
        for i in range(3):
            entered = input("Enter password: ")
            if entered == self.__password:
                print("✅ Login successful")
                return
            else:
                print("❌ Wrong password")

        print("Account locked")


u1 = User("qwerty")
u1.login()
