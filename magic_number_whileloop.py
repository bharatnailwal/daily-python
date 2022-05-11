
def ask_number(nb_min,nb_max):
    number_str = input(f"What is the magic number (between {nb_min} and {nb_max}) ? ")
    number_int = int(number_str)
    return number_int


min_number = 1
max_number = 10
magic_number = 5

number = 0
while not number == magic_number:
    number = ask_number(min_number,max_number)
    if number == magic_number:
        print("You won! ")
    elif number > magic_number:
        print("the number is lower")
    elif number < magic_number:
        print("the number is greater")
