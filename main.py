import pyperclip as pc

original = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
key = "BCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzA"  # this is the key to decode a message


def encode(message):
    encoded_message = ""
    for letter_to_encode in range(len(message)):
        if message[letter_to_encode] == " ":
            encoded_message += "0"
        else:
            encoded_letter_place = original.find(message[letter_to_encode])
            encoded_message += key[encoded_letter_place]
    pc.copy(encoded_message)
    return encoded_message


def decode(message):
    decoded_message = ""
    for letter_to_decode in range(len(message)):
        if message[letter_to_decode] == "0":
            decoded_message += " "
        else:
            decoded_letter_place = key.find(message[letter_to_decode])
            decoded_message += original[decoded_letter_place]
    pc.copy(decoded_message)
    return decoded_message


# The main function will display the menu to the user and ask for their choice
def main():
    keep_going = True
    while keep_going:
        user_choice = int(input("What would you like to do?\n"
                                "1. Encode a message\n"
                                "2. Decode a message\n"
                                "3. Exit\n\n"
                                "You choice: "))
        if user_choice == 1:
            message_to_encode = input("What is the message: ")
            print("\n" + encode(message_to_encode) + "\n"
                                                     "The message has been copied to your clipboard \n")
        if user_choice == 2:
            message_to_decode = input("What is the message: ")
            print("\n" + decode(message_to_decode) + "\n"
                                                     "The message has been copied to your clipboard \n")
        if user_choice == 3:
            keep_going = False


if __name__ == "__main__":
    main()
