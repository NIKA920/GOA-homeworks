#N1
data = input("შეიყვანეთ რაიმე მონაცემი: ")
data_type = type(data)
print("შემოტანილი მონაცემის ტიპია:", data_type)
#N2
string = ("string")
string_type = type(string)
print("შემოტანილი მონაცემის ტიპია:", string_type)
#N3
my_string = "123"
my_integer = int(my_string)
print(my_integer)
#N4
#type() ფუნქცია Python-ში აბრუნებს ობიექტის ტიპს
my_string = "Hello, World!"
print(type(my_string)) 
#N5
num1 = "10"
num2 = "10"
print(num1) + (num2)