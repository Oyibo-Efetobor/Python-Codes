#Password Generator Project
#100 Days of Code
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?: ")) 
nr_symbols = int(input(f"How many symbols would you like?: "))
nr_numbers = int(input(f"How many numbers would you like?: "))
var1 = []
var2= ''
var3 = []
var4 = ''
var5 = []
var6 = ''
pwd_2 = []
pwd_3 = ''
# for letters
for letter in range(nr_letters):
    var1.append(random.choice(letters))
for item in var1:
    var2 += item


#for symbols
for symbol in range(nr_symbols):
    var3.append(random.choice(symbols))
for item_1 in var3:
    var4 += item_1


#for numbers
for number in range(nr_numbers):
    var5.append(random.choice(numbers))
for item_2 in var5:
    var6 += item_2


#randomising the password
pwd = list((var2 + var4 + var6))
random.shuffle(pwd)

password_new = ''

#turning password from a list to a string
for pass_w in pwd:
    password_new += pass_w
print()
print(f"your safe password is {password_new} ")



    
