def caesar_cipher(phrase, key):
    result = []

    for letter in phrase:
        if letter.isalpha():
            if letter.isupper():
                shifted = chr((ord(letter) - 65 + key) % 26 + 65)
            else:
                shifted = chr((ord(letter) - 97 + key) % 26 + 97)
            result.append(shifted)
        else:
            result.append(letter)

    ascii_result = [ord(char) for char in ''.join(result)]
    divisor = (key / 2) + 5

    # Divide each ASCII value by the divisor and use modulus to ensure length
    divided_ascii_result = [str(int(ascii_value / divisor) % 100) for ascii_value in ascii_result]  # Modulo 100 for 2-digit results
    
    # Join the results and limit to the first 12 digits or pad if shorter
    final_result = ''.join(divided_ascii_result)[:12]  # Get the first 12 digits
    if len(final_result) < 8:  # Pad if shorter than 8 digits
        final_result = final_result.ljust(8, '0')

    return final_result

def a1z26_cipher(phrase, key):
    def letter_to_number(letter):
        """Converts a letter to its corresponding number (A=1, B=2, ..., Z=26)."""
        return ord(letter.upper()) - 64
    
    # Adjust the letter value based on the key
    def adjust_value(number):
        return (number + key - 1) % 26 + 1  # Wrap around for 1-26

    result = []

    for letter in phrase:
        if letter.isalpha():
            # Convert letter to number and adjust using the key
            number = letter_to_number(letter)
            adjusted_number = adjust_value(number)
            result.append(str(adjusted_number))
        else:
            # Non-alphabetical characters remain unchanged
            result.append(letter)

    # Join the results and limit the output to 8-12 digits
    final_result = ''.join(result)
    if len(final_result) > 12:
        final_result = final_result[:12]  # Truncate to 12 digits
    elif len(final_result) < 8:
        final_result = final_result.ljust(8, '0')  # Pad with zeros to reach 8 digits
    
    return final_result

# Get input from the user
phrase = input("Enter the text to encrypt: ")
key = int(input("Enter a number to use as key: "))

# Ask the user to choose the cipher method
print("Choose a cipher method:")
print("1. Caesar Cipher")
print("2. A1Z26 Cipher")
choice = input("Enter 1 or 2: ")

if choice == '1':
    result = caesar_cipher(phrase, key)
    print("Encrypted result using Caesar Cipher:", result)
elif choice == '2':
    result = a1z26_cipher(phrase, key)
    print("Encrypted result using A1Z26 Cipher:", result)
else:
    print("Invalid choice. Please select 1 or 2.")
