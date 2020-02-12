"""
Simple ROT13 cipher, able to encode and decode messages
"""

UPPER_SET = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm']

LOWER_SET = ['n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

# reads the message the user wishes to encode/decode
def read_string(msg):
    message = input(msg)
    return message

# does the encoding/decoding
def perform_cipher(msg):
    new_msg = ""
    for char in msg.lower():
        if char in UPPER_SET:
            new_msg += LOWER_SET[UPPER_SET.index(char)]
        elif char in LOWER_SET:
            new_msg += UPPER_SET[LOWER_SET.index(char)]
        else:
            new_msg += char

    return new_msg


if __name__ == "__main__":
    entry = "y"
    
    while entry.lower() == "y":
        message = read_string("Enter your message:\n")
        print("\nEncoded/Decoded message:\n" + perform_cipher(message))

        entry = read_string("\nAgain? (y/n): ")

    