#  Напишите программу, которая будет симулировать банк с использованием потоков и объектов типа Lock. Реализуйте методы deposit и
# withdraw, которые будут добавлять и снимать деньги со счета клиента
# соответственно. Гарантируйте, что доступ к счету будет синхронизирован с помощью объекта типа Lock.

import threading

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            current_balance = self.balance
            new_balance = current_balance + amount
            self.balance = new_balance
            print(f"Deposited {amount}. New balance: {new_balance}")

    def withdraw(self, amount):
        with self.lock:
            current_balance = self.balance
            if amount <= current_balance:
                new_balance = current_balance - amount
                self.balance = new_balance
                print(f"Withdrew {amount}. New balance: {new_balance}")
            else:
                print("Insufficient funds.")

def simulate_bank_operations(account):
    for _ in range(5):
        account.deposit(100)
        account.withdraw(50)

if __name__ == "__main__":
    bank_account = BankAccount()

    threads = []
    for _ in range(3):
        thread = threading.Thread(target=simulate_bank_operations, args=(bank_account,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Final balance:", bank_account.balance)
