from item import Item
from phone import Phone


def main():
    item_1 = Item('MyItem', 750)
    item_1.price = 900
    print(item_1.price)


if __name__ == '__main__':
    main()
