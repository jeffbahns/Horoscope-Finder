import re

phoneNumRegex = re.compile(r'(\(?\d\d\d\)?)?-(\d\d\d)-(\d\d\d\d)')
mo = phoneNumRegex.findall('hello my number 415-555-2424 and my mom\'s number is (925)-683-3049')
#print (mo)

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
#print (mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman')
#print (mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo3 = batRegex.search('Batcopter lost a propeller!')
#print (mo3.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo4 = phoneRegex.search('My number is 254-243-2142 and my cell is 553-1342')
#print (mo4.group())

batRegex = re.compile(r'Je(f){2,}(rey)?')
mo5 = batRegex.search('Jefffffrey')
#print (mo5.group())

vowelRegex = re.compile(r'[aeiouAEIOU]')
mo6 = vowelRegex.findall('Robocop eats baby food, baby FOOD..')
#print (mo6)

beginsHello = re.compile(r'^Hello')
mo7 = beginsHello.search("Hello my nams is jeff")
print (mo7 == None)

