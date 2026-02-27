class User:
    def __init__(self,username,password="qwerty"):
        self.username=username
        self.__password=password
    
    def profile(self):
        print("the username is",self.username,"\npassword cant be displayed")

    def update_password(self):
        old_pass=input("enter old password : ")
        if self.__password==old_pass:
            new_pass=input("enter new password : ")
            self.__password=new_pass
            print("password has been updated")
        else:
            print("password is not matching")

u=input("enter username : ")
u1=User(u)
u1.update_password()
