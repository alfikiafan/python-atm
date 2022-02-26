from atm_card import ATMcard

class Customer:
    def __init__(self, id, customerPin = 1234, customerBalance = 10000):
        self.id = id
        self.pin = customerPin
        self.balance = customerBalance

    def cekId(self):
        return self.id

    def cekPin(self):
        return self.pin

    def cekBalance(self):
        return self.balance

    def withdrawBalance(self, nominal):
        self.balance -= nominal
    
    def depositBalance(self, nominal):
        self.balance += nominal
    def Error(self):
        return LookupError.with_traceback()
