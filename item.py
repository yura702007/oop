import csv


class Item:
    pay_rate = 0.8
    all = []

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f'Price {price} is not greater or equal to than zero'
        assert quantity >= 0, f'Quantity {quantity} is not greater or equal to than zero'
        self.__name = name  # privat attribute
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        """
        get privat attribute
        :return: self.__name
        """
        return self.__name

    @name.setter
    def name(self, value):
        """
        set privat attribute
        :param value: str
        :return: None
        """
        self.__name = value

    def __repr__(self):
        return f'{self.__class__.__name__}(name = {self.name}, price - {self.price}, quantity - {self.quantity})'

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price *= self.pay_rate


def main():
    print(Item.is_integer('7.0'))


if __name__ == '__main__':
    main()
