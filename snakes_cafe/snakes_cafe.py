welcome = '''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
'''
print(welcome)

menu = [
    { 'Appetizers':[
        'Wings',
        'Cookies',
        'Spring_Rolls'
    ],
    'Entrees': [
       'Salmon',
        'Steak',
        'Meat Tornado',
        'A Literal Garden' 
    ],
    'Desserts': [
        'Ice Cream',
        'Cake',
        'Pie'
    ],
    'Drinks': [
        'Coffee',
        'Tea',
        'Unicorn Tears'
    ]
    }
]

diplay_menu = '''
Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
'''
print(diplay_menu)

order = '''
***********************************
** What would you like to order? **
***********************************
'''

print(order)




if __name__ == "__main__":
    response = ''
    num = 0
    order = []
    while response != "quit":
        response = input(">")
        order.append(response)
        num = order.count(response)
        if response != "quit":
            print(f"** {num} of {response} have been added to your meal **")