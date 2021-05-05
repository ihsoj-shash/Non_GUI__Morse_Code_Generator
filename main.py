import encrypt_decrypt


def main():
    user_choice = int(input("Press 1 for converting Text to Morse Code, Press 2 to convert Morse Code to text."
                            " 1 or 2 ?"))
    if user_choice == 1:
        input_text = input("Enter the text.")
        text_converted_to_morse_code = encrypt_decrypt.encrypt_a_msg(input_text)
        print(text_converted_to_morse_code)
    elif user_choice == 2:
        input_morse_code = input("Enter the Morse Code.")
        morse_code_converted_to_text = encrypt_decrypt.decrypt_a_msg(input_morse_code)
        print(morse_code_converted_to_text)
    else:
        print('You entered a Wrong Choice.')


if __name__ == '__main__':
    main()
