#My Password Generator
# this program generate a password and save it in the text file
import random
import string_utils




symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
def password_gene(number_letters,number_symbols,number_numbers):

    password = ""

    for nr_letter in range(0, number_letters):
        password += random.choice(letters)
    for nr_number in range(0, number_numbers):
        password += random.choice(numbers)
    for nr_symbols in range(0, number_symbols):
        password += random.choice(symbols)
    #print(password)

    code = string_utils.shuffle(password)
    save_pass(code)

    #print(string_utils.shuffle(f"{password}"))
    print(code)

print("Welcome to Password Generator!")

def password_choise_generator(choise):
    if choise == "2":
        number_letters = int(input("How many letters would you like in your password?\n"))
        number_symbols = int(input(f"How many symbols would you like?\n"))
        number_numbers = int(input(f"How many numbers would you like?\n"))
        password_gene(number_letters,number_symbols,number_numbers)
    else:
        strong = input(" Write 1 for Strong \n Write 2 for Very Strong\n Write 3 for Unbreakable \n choose: ")
        if strong == "1":
            number_letters = 4
            number_symbols = 4
            number_numbers = 4
            password_gene(number_letters,number_symbols,number_numbers)
        elif strong == "2":
            number_letters = 6
            number_symbols = 6
            number_numbers = 6
            password_gene(number_letters, number_symbols, number_numbers)
        else:
            number_letters = 10
            number_symbols = 10
            number_numbers = 10
            password_gene(number_letters, number_symbols, number_numbers)
def save_pass(code):
    name = input("Whats the tag you want the pass to have?: ")
    password_file = open('pass.txt', 'a')
    password_file.write(" Name: " + name)
    password_file.write("            Pass: " + code)
    password_file.write ("\n")
    password_file.close()
    #print("check")
choise = input("Press 1 for Auto password generate, else press 2 to choise the lenght of it: ")
save = input("Do you Want to save the code? write 1 if you want or 2 if not: ")
password_choise_generator(choise)








