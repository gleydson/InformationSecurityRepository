#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os  

textEncrypted = "mllvo gjw axie, viog vlgbg dfptll n zoe fe gyyom j xof nr tuegr fg tfusfe ayqwxt rrpjnfy xg, mlm nbnju, tphuc kzg fltrf i ytamuyvi ig pzi qs or rrzzrgmtt spg acwfq, ux nnz xj eiqln ry akgphrfy".upper()

listWordsInPortuguese = ["a", "ante", "após", "até", "com", "contra",
                            "de", "desde", "em", "entre", "para", "perante",
                            "por", "sem", "sob", "sobre", "trás",
                            "porque", "que", "sendo", "mesmo", "caso",
                            "quando", "logo", "como", "te", "seu",
                            "meu", "nosso", "eu", "você", "ele", "ela"]

def prepareKey(key, textEncrypted):
    key = key.upper()
    key = list(key)
    newKey = ""
    i = 0
    while i < len(textEncrypted):
        if textEncrypted[i] == " ":
            newKey += " "
        elif textEncrypted[i] == ",":
            newKey += ","
        else:
            letter = key[0]
            newKey += letter
            key = key[1:]
            key.append(letter)
        i += 1
    return newKey

def decrypt(preparedKey, textEncrypted):
    alphabet = list("abcdefghijklmnopqrstuvwxyz".upper())
    clearText = ""
    for i in range(len(textEncrypted)):
        if textEncrypted[i] == ",":
            clearText += ","
        elif textEncrypted[i] == " ":
            clearText += " "
        else:
            clearText += alphabet[alphabet.index(textEncrypted[i]) - alphabet.index(preparedKey[i]) + 26 % 26]
    return clearText

def main():
    os.system("crunch 4 4 ABCDEFGHIJKLMNOPQRSTUVWXYZ -o 4letters.txt")
    fourLetters = open('4letters.txt', 'r')
    fourLettersKeys = []

    for key in fourLetters.readlines():
        res = decrypt(prepareKey(key[:4], textEncrypted), textEncrypted)
        if (" AMOR " in res) or (" AMOR," in res) or (" AMOR." in res):
            fourLettersKeys.append(key)
            print(key)
            break
    fourLetters.close()

    rescue = open("rescue.txt", 'w')

    for line in fourLettersKeys:
        print("Iniciando... " + line)
        fourLetters = open('4letters.txt', 'r')
        for key in fourLetters:
            word = line[:4] + key[:4]
            res = decrypt(prepareKey(word, textEncrypted), textEncrypted)
            rescue.writelines(word + " => " + res + "\n")
        fourLetters.close()
    rescue.close()

if __name__ == "__main__":
    main()