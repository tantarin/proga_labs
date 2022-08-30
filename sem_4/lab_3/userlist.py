# Creating a userlist where adding new elements is not allowed.
from collections import UserList


class user_list(UserList):
    # function to raise error while insertion
    def append(self,s=None):
        raise RuntimeError("Authority denied for new insertion")


my_list=user_list([11,22,33,44])
# trying to insert new element
my_list.append(55)
