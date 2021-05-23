from Crypto.Util.number import long_to_bytes

cipher = ['11000010111010000100110001000000010001001011010000000110000100000100011010111110000010100110000001101110100110100100100010000110001001101000101010000010101000100000001010100010010010001011110001101010110100000010000010111110000010100010100011010010100010001001111001101010011000000101100', '11000110110010000100110001000000010001001111010010000110110000000110011010101110011010100110000010100110101100000100000000001110001001001000101000001010101001100000001010101010010110001001110001101010110100000110011010010110011000000100100011010000110010001001011001101010011000001101100', '11000010110010000100110001101000010001001111001000000110000100000110011000111110010010100110000000101110101101100000000010010110001001101000101010000010101000100000001000101110000010001001111001101010110100000010011010010110011000100000100011010010100010001001111001101010011000001101100', '11000110110010001100110000101000110001000111000000000110000000000110011010101110011000100110000010100110101101100100100010000100101001001000101010000010101000100000001010100110010010001001110001101010110000000110000010110110000000000000100011010010110010001011011001101010001000000111101', '11000110100010001100110000000000010001000111001010000110110100000110011010111110001010100110100011101110101110100010000000110100001001101000101010000010101001101000001000101000010010001001111001101010110000000010000010111110000000000010000011010010100010001001011001101010011000001111101', '11000010110010001100110001001000010001000011000000100110000000000110011010101110000010100110100011100110101110100010000000101100101001101000101010000010101001101000001010100010000010001011111001101010110100000110001010010110001010100100000011010010110010001011111001101010011000000101100', '11000110110010000100110001101000110001001011010000100110110000000110011000101110010000100110100001100110100110000000100010000110101001001000101010000010101001100000001000101110010010001011111001101010110000000010001010110110001010100110000011010000110010001011111001101010011000000101100', '11000010110010000100110000100000010001000111011000100110100000000110011000111110000010100110000001101110101111100100000010111110001001001000101000001010101001101000001000101010000110001011110001101010110000000110001010011110000010100010100011010010110010000011011001101010001000000111100', '11000010101010000100110001001000010001000011000000100110010000000100011000111110011000100110000001100110100101000010000000011100101001101000101000001010101001101000001010101110010110001001110001101010110000000010010010110110011000000010100011010000100010001011111001101010001000000101100', '11000010101010001100110000100000010001001111001010000110000000000100011010101110011000100110000011100110100111100110100000000110001001001000101010000010101000100000001000101100010010001011110001101010110000000110011010010110011010000000000011010010100010001011011001101010011000001101101', '11000010101010001100110001000000010001001011010010000110010100000100011000111110011000100110000010100110100111000100000000000100101001101000101010001010101000100000001000100000000110001001111001101010110000000110011010010110000010000100100011010000110010000011011001101010001000001101100', '11000110101010001100110001000000110001001111001010000110110000000110011010101110011000100110100001100110101111000100100010011110101001001000101010001010101000101000001000101100000110001011111001101010110100000010011010011110001000000100100011010010100010000001011001101010011000001111100', '11000110100010001100110001000000010001001011011010100110000000000100011000101110001000100110100001101110101101000110100010001100101001001000101010000010101000100000001010101100000010001001111001101010110100000110011010010110010000100110100011010010110010001001111001101010011000001101101', '11000110101010000100110000000000010001001111001010100110100100000100011010111110001000100110100001101110101100000000100000111110001001101000101000001010101001101000001010100110010010001011110001101010110100000110000010010110001010000010100011010010110010001001011001101010001000000101100', '11000010101010000100110000000000110001001011011010100110110000000110011000101110010010100110100000100110101111000010000000100100001001001000101000001010101001100000001000100000000010001011110001101010110000000010011010011110001010000000000011010010100010001001011001101010001000000101101', '11000110101010001100110001000000110001001111011000000110010100000100011000101110001010100110000001101110101110000100100000101110101001101000101000000010101000100000001010101010000010001011110001101010110000000010000010010110001000100100100011010000100010000001011001101010001000001111101']

plain = ''
for l in range(len(cipher[0])):
    check = ''
    for i in range(len(cipher)):
        check += str(cipher[i][l])
    if check == '0'*len(cipher):
        plain += '0'
    else:
        plain += '1'
print(long_to_bytes(int(plain,2)))
