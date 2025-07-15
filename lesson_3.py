class User:
    def __init__(self, name, info, password):
        self.name = name
        self.__info = info
        self.__password = password

    def get_info(self):
        # геттер для __info
        return self.__info

#     @property
#     def info(self):
#         return self.__info
#
#     @info.setter
#     def info(self, value):
#         # сеттер для __info
#         if len(value) > 20:
#             # print("Value for info is too long")
#             raise ValueError("Value for info is too long")
#         self.__info = value
#
#     def change_passrd(self, old_password, new_password):
#         if self.__password == old_password:
#             self.__password = new_password
#
#
 user_aibek = User("Aibek", "Hello, I am a developer", "123456789")
# # user_aibek._info = "Hello, I am a doctor 1111111111111111111111111111111111111"
# # print(user_aibek.__info)
# # print(user_aibek.get_info())
# # print(user_aibek._User__info) # name mangling
# print(user_aibek.info)
# user_aibek.info = "Hello, I am a doctor"
# print(user_aibek.info)
# user_aibek.change_passrd("123456789", "abcdefgh")
# print(user_aibek._User__password)
#
# from abc import ABC, abstractmethod
#
# class SiteUser(ABC):
#     @abstractmethod
#     def change_password(self, old_password, new_password):
#         pass
#
# class GeeksUser(SiteUser):
#     def change_password(self, old_password, new_password):
#         print("change password in geeks")
#
#
# class GmailUser(SiteUser):
#     def change_password(self, old_password, new_password):
#         print("change password in gmail")
#
# geeksuser_igor = GeeksUser()
# geeksuser_igor.change_password("<PASSWORD>", "<PASSWORD>")