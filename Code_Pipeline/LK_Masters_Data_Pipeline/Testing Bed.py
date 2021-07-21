#name = input("What is your Name?: ")
#age = input("What is your Age?: ")
#print("Hello "+name+", age "+str(age))
#import math
#pi = 3.14
#print(round(pi))
#rounds to nearest whole number. ceil rounds high, floor rounds low, abs (absolute value) shows distance from zero (+/-), pow raises a base number to a power (e.g. pow(pi, 2))
#print(math.floor(pi))

#char_name = "Tom"
#char_age = 45.5
#is_male = True
#print("There once was a man named " + char_name + ".")
#print("He was " + str(char_age) + " years old.")

#phrase = "Screw You"
#print(phrase.upper())
#print(phrase.index("Y"))
#print(phrase.replace('You', 'Me'))

#import math
#print(math.sqrt(36))

#name = "Leo Knowles"

#first_name = name[0:4]
#last_name = name[4:11]
#print(first_name)
#print(last_name)

#website = "http://google.com"
#slice = slice(7,-4)
#print(website[slice])

#           Logical Operators

#age = int(input("How old are you?"))

#if age >= 18:
#    print("you are an adult.")
#elif age < 0:
#    print("you aren't alive, buddy")
#else:
#    print("you are under-age")


#temp = int(input("what is the temp outside?: "))

#if temp >= 0 and temp <= 30:
#    print("pretty nice")
#elif temp > 30 or temp < 0:
#    print("not so good")
#    print("stay inside")

#           While Loop

#name = ""

#while len(name) == 0:
#    name = input("Enter your name:")
#print ("Hello "+name)

#           For Loops
#for index in range(10):
#    print(index)

#for index in range(50,100+1,2):
#    print(index)
#above ioterates through each number from 50-100, counteing every second num

#for index in "Leo Knowles":
#    print(index)

#the -1 below reverses the order, making this a countdown
#import time
#for seconds in range(10,0,-1):
#    print(seconds)
#    time.sleep(1)
#print("yay")

#           Nested Loop

#rows = int(input("how many rows?"))
#columns = int(input("how many columns?"))
#symbol = int(input("enter a symbol?"))
 
#for i in range(rows):
#    for j in range(columns):
#        print(symbol, end="")
#    print()

#           Loop Control
#Break: is used to termiate a loop when it's encountered
while True:
    name = input("Enter your name: ")
    if name != "":
        break
print ("Hello "+name)

#Continue: skips to next iteration of loop
phone_num = "123-456-789"

for i in phone_num:
    if i == "-":
        continue
    print(i, end="")

#Pass: does nothing, acts as a placeholder

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)

#           Lists - a variable that contains multiple values

food = ["pizza","chips","carrot","fish"]

#print(food[0:2])

food.append("sushi")
food.remove("pizza")
#food.pop()
#above removes last element
food.sort()

for x in food:
    print(x)

print('BEARER_TOKEN')