#Aiden Blackwood
def encode(string):
    return_string = ""
    for count in range(len(string)):
        res = int(string[count]) + 3
        return_string += str(res)

    return return_string

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        user_choice = int(input())

        if user_choice == 1:
            print("Please enter your password to encode:", end=" ")
            password = input()
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")

        elif user_choice == 2:
            pass

        elif user_choice == 3:
            break

if __name__ == "__main__":
    main()
