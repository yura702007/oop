from item import Item
from phone import Phone


def main():
    item_1 = Item('MyItem', 750)
    item_1.name = 'OtherItem'
    print(item_1.name)


if __name__ == '__main__':
    main()
