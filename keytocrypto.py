cipher = input()
key = input()
message = ""

listAlphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

alphabet = dict(zip(listAlphabet, numbers))
alphabetReversed = dict(zip(numbers,listAlphabet))

for i in range(len(cipher)):
    funk = (alphabet[cipher[i]] - alphabet[key[i]]) % 26
    message += alphabetReversed[funk]
    key += alphabetReversed[funk]

print(message)

