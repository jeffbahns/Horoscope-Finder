
# Imports
from bs4 import BeautifulSoup
import requests, re, os

# URL's, Horoscope sign dict
base_url = "http://horoscope.com/"
url = "http://my.horoscope.com/astrology/free-daily-horoscope-{}.html"
sign_list = {1  : "Aries",
             2  : "Taurus",
             3  : "Gemini",
             4  : "Cancer",
             5  : "Leo",
             6  : "Virgo",
             7  : "Libra",
             8  : "Scorpio",
             9  : "Sagittarius",
             10 : "Capricorn",
             11 : "Aquarius",
             12 : "Pisces"}

# 'horoscope.com' scraper
def horoscoper(link):
    os.system('clear')
    sign = 0
    # 12 horoscopes to pick from
    print ("Which sign are you?\n"
           "1  : Aries\n2  : Taurus\n3  : Gemini\n"
           "4  : Cancer\n5  : Leo\n6  : Virgo\n"
           "7  : Libra\n8  : Scorpio\n9  : Sagittarius\n"
           "10 : Capricorn\n11 : Aquarius\n12 : Pisces")
    while sign > 12 or sign < 1 or sign % 1 != 0:
        sign = eval(input("\n>> "))
        
    r = requests.get(url.format(sign_list[sign]))
    soup = BeautifulSoup(r.content)
    horoscope = (soup.find_all("div", {"class" : "fontdef1"}))
    for scope in horoscope:
        return "\n" + sign_list[sign] + "!\n\n" + scope.text

print (horoscoper(url))

