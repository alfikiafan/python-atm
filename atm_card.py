class ATMcard:
    def __init__(self, defaultPin, defaultBalance):
        self.defaultPin = defaultPin
        self.defaultBalance = defaultBalance

    def cekAwal(self):
        return self.defaultPin

    def cekSaldoAwal(self):
        return self.defaultBalance
