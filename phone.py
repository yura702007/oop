from item import Item


class Phone(Item):
    all = []

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)
        assert broken_phones >= 0, f'Broken phones {broken_phones} is not greater or equal to than zero'
        self.broken_phones = broken_phones
        Phone.all.append(self)


def main():
    phone_1 = Phone(name='Xaomi', price=699.99, quantity=15, broken_phones=3)
    print(Phone.all)
    print(Item.all)


if __name__ == '__main__':
    main()
