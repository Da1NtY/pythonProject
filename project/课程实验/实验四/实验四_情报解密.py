'''
我国截获一份情报如下：Yt gj,tw sty yt gj,ymfy nx f vzjxynts.
根据潜伏的特工传回的消息，知道这份情报的明文中有一个单词是“question”，
且采用的是凯撒加密的方法，偏移量未知。
请编程计算偏移量，并用得到的偏移量解密另一份情报
“Fyyfhp ts Ujfwq Mfwgtw ts Ijhjrgjw 2,6496”，
输出这份情报的明文和对方加密使用的偏移量数据。

'''
# word = "question"
# secret_fir = "Yt gj,tw sty yt gj,ymfy nx f vzjxynts"
# def decode_offset(word,secret_fir):
#     words = secret_fir.split()
#     for item in words:
#         if len(item) == len(word):
#             Item_fir = item[0:1]
#             Word_fir = word[0:1]
#             num = int(ord(Item_fir) - ord(Word_fir))
#             return num
#             break
#
# def caesar_encrypt(letter_offset, secret_word):
#     # 字符串解密函数
#     def shift_char(char):
#         if char.isalpha():
#             base = ord('a')if char.islower() else ord('A')
#             return chr((ord(char)+base+letter_offset) % 26 - base)
#         elif char.isdigit():
#             return chr((ord(char)+ord('0')+letter_offset) % 10 - ord('0'))
#         else:
#             return char
#     # 加密字符串
#     text1 = ''.join(shift_char(char) for char in secret_word)
#
#     return text1
#
# num1 = decode_offset(word,secret_fir)
# text = caesar_encrypt(num1,secret_fir)
# print(text)
# 计算偏移量函数
def calculate_shift(ciphertext, plaintext):
    for shift in range(26):
        decrypted = ''
        for char in ciphertext:
            if char.isalpha():
                if char.isupper():
                    decrypted += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                else:
                    decrypted += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted += char
        if plaintext in decrypted:
            return shift

# 已知明文单词和密文
known_plaintext = 'question'
ciphertext = 'Yt gj,tw sty yt gj,ymfy nx f vzjxynts.'

# 计算偏移量
shift = calculate_shift(ciphertext, known_plaintext)
print(f"偏移量是: {shift}")

# 解密另一份情报
new_ciphertext = "Fyyfhp ts Ujfwq Mfwgtw ts Ijhjrgjw 2,6496"
decrypted = ''
for char in new_ciphertext:
    if char.isalpha():
        if char.isupper():
            decrypted += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            decrypted += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
    else:
        decrypted += char

print(f"解密后的明文是: {decrypted}")