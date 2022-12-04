"""
Использование декоратора
"""


class BaseCurrenciesList():
    def get_currencies(self, currencies_ids_lst: list) -> dict:
        pass


class CurrenciesList(BaseCurrenciesList):
    """
        aka ConcreteComponent
    """
    def __init__(self):
        # как-то инициализировать объект класса
        pass

    def get_currencies(self, currencies_ids_lst: list) -> dict:
        result = {
            'R01090B': ('29,4282', 'Белорусский рубль'),
            'R01565': ('17,7405', 'Польский злотый'),
            'R01720': ('27,5078', 'Украинских гривен')
        }

        return result


class Decorator(BaseCurrenciesList):
    """
    aka Decorator из примера паттерна
    """

    __wrapped_object: BaseCurrenciesList = None

    def __init__(self, currencies_lst: BaseCurrenciesList):
        self.__wrapped_object = currencies_lst

    @property
    def wrapped_object(self) -> str:
        return self.__wrapped_object

    def get_currencies(self, currencies_ids_lst: list) -> dict:
        return self.__wrapped_object.get_currencies(currencies_ids_lst)


class ConcreteDecoratorJSON(Decorator):
    def get_currencies(self, currencies_ids_lst: list) -> str:  # JSON
        return f"ConcreteDecoratorJSON({self.wrapped_object.get_currencies(currencies_ids_lst)})"


class ConcreteDecoratorCSV(Decorator):
    def get_currencies(self, currencies_ids_lst: list) -> str:  # CSV
        return f"ConcreteDecoratorCSV({self.wrapped_object.get_currencies(currencies_ids_lst)})"

    def __str__(self):
        pass



    
def show_currencies(currencies: BaseCurrenciesList):
    """
       aka client_code() 
    """

    print(currencies.get_currencies([]))


if __name__ == "__main__":
    # Таким образом, клиентский код может поддерживать как простые компоненты...
    # simple = ConcreteComponent()
    # print("Client: I've got a simple component:")
    # client_code(simple)
    # print("\n")

    curlistdict = CurrenciesList()  # base
    print("Client: I've got a simple component:")
    show_currencies(curlistdict)
    print("\n")
    wrappedcurlist = Decorator(curlistdict)
    wrappedcurlist_json = ConcreteDecoratorJSON(curlistdict)
    print(wrappedcurlist_json.get_currencies([]))
    
    print("\n")
    wrappedcurlist_csv = ConcreteDecoratorCSV(curlistdict)
    print(wrappedcurlist_csv.get_currencies([]))
    
    # show_currencies(wrappedcurlist_csv)
    # show_currencies(wrappedcurlist)

