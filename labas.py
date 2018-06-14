print ("Labuka")

name = "Evie"
number = 8

print ("name")
print (name)

print (name, "loves number", number)

for letter in name:
    print (letter * number)
    number = number - 2

number = 8

for letter in name:
    print (number)
    number = int(number / 2)