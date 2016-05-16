# Random Gift Suggestor

from random import randrange
from time import sleep

jane_gifts = ['Personalized T-Shirt', 'Alarm Clock','Boom Box',
              'Lap Top', 'Cell Phone', 'Television',
              'New Movie', 'Gift Card', 'New Car']

def random_gift(gift_list):
    return gift_list[randrange(0,len(gift_list))]


def main():
    print ("What gift should you get for your {}, {}?".format('daughter', 'Jane'))
    sleep(2)
    print ("Hmmmm... let me think!")
    sleep(2)
    print ("\nYou should buy {} a **{}**!".format('Jane', random_gift(jane_gifts)))
main()
