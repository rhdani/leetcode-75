def encode(strings):
    encoded_string = ""

    for x in strings:
        encoded_string += length_to_bytes(x) + x

    return encoded_string


def decode(string):
    i = 0
    decoded_string = []

    while i < len(string):
        length = bytes_to_length(string[i : i + 4])
        i += 4
        decoded_string.append(string[i : i + length])
        i += length

    return decoded_string


def length_to_bytes(x):
    length = len(x) 
    bytes = []

    for i in range(4):
        bytes.append(chr(length >> (i * 8)))

    bytes.reverse()
    bytes_string = "".join(bytes)

    return bytes_string


def bytes_to_length(bytes_string):
    result = 0

    for c in bytes_string:
        result = result * 256 + ord(c)

    return result

# Driver code
def main():
    input = [
                ["I", "love", "educative"], 
                ["6^Hello_5", "5_World^6"], 
                ["I", "love", "programming"], 
                ["a", "b", "c", "d"], 
                ["*_*EDUCATIVE*_*"]
            ]

    for i in range(len(input)):
        encoded = encode(input[i])
        print(i + 1, ".\t Input = ", input[i], sep="")
        print("\t Encoded string = ", encoded, sep="")
        print("\t Output = ", decode(encoded), sep="")
        print("-" * 100)


# For printing (Bytes to Integer)

def print_encoded(string):
    final = ""
    i = 0

    while i < len(string):
        for z in string[i : i + 4]:
            final += str(ord(z))
        length = bytes_to_length(string[i : i + 4])
        i += 4
        final += string[i : i + length]
        i += length
    return final


if __name__ == "__main__":
    main()

