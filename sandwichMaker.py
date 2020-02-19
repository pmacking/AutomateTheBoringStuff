import pyinputplus as pyip
import time

breadType={'wheat':1.50, 'white':1.50, 'sourdough':2.00, 'no bread':0}
proteinType={'chicken':2.50,'turkey':2,'ham':3.50, 'tofu':3, 'no protein':0}
cheeseType={'cheddar':1, 'Swiss':1, 'mozzarella':1}

print('Welcome to the sandwich bar, please tell me your choices!', end='\n')

#Using inputMenu() for a bread type: wheat, white, or sourdough.
bread=pyip.inputMenu(list(breadType), lettered=True)

#Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
protein=pyip.inputMenu(list(proteinType), lettered=True)

#Using inputYesNo() to ask if they want cheese.
cheeseBool=pyip.inputYesNo(prompt='Would you like cheese on your sandwich?\n')
#If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
if cheeseBool == 'yes':
	cheese=pyip.inputMenu(list(cheeseType), lettered=True)

#Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
mayoBool=pyip.inputYesNo(prompt='Would you like mayo?\n')
mustardBool=pyip.inputYesNo(prompt='Would you like mustard?\n')
lettuceBool=pyip.inputYesNo(prompt='Would you like lettuce?\n')
tomatoBool=pyip.inputYesNo(prompt='Would you like tomato?\n')

#Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.
Count=pyip.inputInt(prompt='How many of these sandwiches would you like?\n', min=1)

#brief pause before calculating price
time.sleep(1)
print('Calculating the price of your sandwich order...')
time.sleep(3)

#Come up with prices for each of these options,
#and have your program display a total cost after the user enters their selection.
print('${:,.2f}'.format(Count*(breadType[bread]+proteinType[protein]+cheeseType[cheese])))