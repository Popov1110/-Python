
a = 6
print (a)

b = input("введите число ")

try:
    print (int(b)*2)
except:
    print ("Введены неверные данные!")

name = input("Как вас зовут?")

print("Привет", name + "!")