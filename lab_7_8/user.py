class User:
    def __init__(self, id: int, height: float, name: str, deleted: int, created: str):
        self.__id = id
        self.__name = name
        self.__height = height
        self.__deleted = deleted
        self.__created = created

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if not name:
            raise Exception("Name cannot be empty")
        if name[0].isdigit():
            raise Exception("Name cannot start with a digit")
        self.__name = name

    @name.deleter
    def name(self):
        self.__name = None

    @property
    def height(self):
        return self.__height

    @property
    def created(self):
        return self.__created

    @property
    def deleted(self):
        return self.__deleted
