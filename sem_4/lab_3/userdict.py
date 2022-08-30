
from collections import UserDict
my_dict={'red':'5','white':2,'black':1}

# Creating an UserDict
user_dict = UserDict(my_dict)
print(user_dict.data)

# Вывод:
# {'red': '5', 'white': 2, 'black': 1}


class user_dict(UserDict):
    def replace(self, key):
        self[key] = '0'


file = user_dict({'red': '5', 'white': 2, 'black': 1, 'blue': 4567890})
# Delete 'blue' and 'yellow'
for i in ['blue', 'yellow']:
    file.replace(i)
print(file)
# Вывод:
# {'red': '5', 'white': 2, 'black': 1, 'blue': '0', 'yellow': '0'}
