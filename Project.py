def user():
    print('Welcome, dear customer!')
    display_items()
    # buy_items()
    acces()


def display_items():
    print('-' * 50)
    print('Welcome to Kosmo Supermarket')
    print('This is what we have in stock:')
    print('-' * 50)
    item = open('data.csv', 'r')
    items = item.readlines()
    for item in items:
        print(item)


def add_new_items():
    new_items = []
    to_input = str(input('Add new Item, quantity, price per unit. \n '
                         'separate item, quantity and price with space '))
    new_items.append(to_input)
    while to_input != '':
        to_input = str(input('Add new Item, quantity, price per unit. \n '
                             'separate item, quantity and price with space '))
        new_items.append(to_input)
    new_items.pop(-1)
    print(new_items)


def admin():
    password = 'Admin'
    passcode = input('Enter password: ')
    if passcode == password:
        display_items()
        add_new_items()
        update_quantities()
        set_items_price()
        view_sales_record()
    else:
        print("Sorry, you're not the admin")
        acces()


def main():
    acces()
    admin()
    user()


def acces():
    access = int(input('Choose access: \n 1. Admin \n 2. User \n 3. Exit '))
    while access !=1 and access != 2 and access !=3:
        print('Please seelect from 1 - 3')
        access = int(input('Choose access: \n 1. Admin \n 2. User \n 3. Exit '))
    if access == 1:
        print('Welcome Admin!')
        admin()
    elif access == 2:
        print('User Welcome!')
    elif access == 3:
        print('Good bye!!!')


if __name__ == '__main__':
    main()