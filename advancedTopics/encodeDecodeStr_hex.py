def encode(strings):
    
    retVal = ""
    for index in range(len(strings)):
        word = strings[index]
        length = len(word)
        byte_data = length.to_bytes(4, byteorder='big')
        stored_string = byte_data.hex()
        retVal = retVal + f"{stored_string}"
        retVal = retVal + word
    
    return retVal

def decode(string):

    retVal = []

    overallLength = len(string)
    decodedLength = 0
    while decodedLength < overallLength:
        curLengthStr = string[decodedLength:decodedLength+8]
        decodedLength += 8
        recovered_bytes = bytes.fromhex(curLengthStr)

        final_num = int.from_bytes(recovered_bytes, byteorder='big')
        nextWord = string[decodedLength:decodedLength+final_num]
        decodedLength = decodedLength+final_num
        retVal.append(nextWord)

    return retVal

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
'''
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

'''
if __name__ == "__main__":
    main()

