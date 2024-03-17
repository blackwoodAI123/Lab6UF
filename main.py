#Aiden Blackwood
def encode(string):
    return_string = ""
    for count in range(len(string)):
        res = int(string[count]) + 3
        return_string += str(res)

    return return_string

def main():
    executed = False
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        user_choice = int(input())

        if user_choice == 1:
            executed = True
            print("Please enter your password to encode:", end=" ")
            password = input()
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")

        elif user_choice == 2:
            if executed == True:
                print("The encoded password is " + encoded_password + ", and the original password is " + password + ".")
            else:
                print("No password assigned.")

        elif user_choice == 3:
            break

if __name__ == "__main__":
    main()
