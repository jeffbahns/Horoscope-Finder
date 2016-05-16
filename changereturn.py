# python 2.7

from collections import OrderedDict as od
def change_return(cost, payment):
    cashback = payment - cost
    bills = cashback // 1
    change = (cashback % 1) * 100
    quarters = 0
    coin_return ={       "Quarters" : 0,
                         "Dimes" : 0,
                         "Nickels" : 0,
                         "Pennies" : 0}
    coin_values = od([  ("Quarters", 25),
                        ("Dimes" , 10),
                        ("Nickels" , 5),
                        ("Pennies" , 1)])
    for coin in coin_values:
        quantity = change // coin_values[coin]
        coin_return[coin] = quantity
        change -= coin_values[coin] * quantity
        print coin ,coin_return[coin]
    return None
