# Aiden Blackwood
def encode(string):
    return_string = ""
    for count in range(len(string)):
        res = int(string[count]) + 3
        return_string += str(res)

    return return_string


def decode():
    return_string = ""
    for char in encoded_password:
        return_string += str(int(char)-3)
    return return_string


if __name__ == "__main__":
    encoded_password = None
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        print("Please enter an option: ", end="")
        user_choice = int(input())
        if user_choice == 1:
            print("Please enter your password to encode:", end=" ")
            password = input()
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")
        elif user_choice == 2:
            decoded_password = decode()
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.\n")
        elif user_choice == 3:
            break
