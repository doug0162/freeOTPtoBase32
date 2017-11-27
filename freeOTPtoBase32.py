#!/usr/bin/env python3
import base64, binascii

def convertToHex(inputNumber):

    #int(inputNumber) & 255
      #binary AND with 255, aka the maximum number which two hex digits can store (inc 0) 
      #This allows for Two's complement of hexadecimal
        # e.g. 1 = 0x01, 0 = 0x00, -1 = 0xff, -2 = 0xfe
    #[2:]
      #removes '0x'
    #zfill(2)
      #ensure that numbers from 0-15 have leading zeros. I.e. 8 == 0x08 insted of 8 == 0x8.

    return hex(int(inputNumber) & 255)[2:].zfill(2)


#Declare hexString as it is initiated with itself in the for loop
hexString = ""

#promt user to input secret from tokens.xml
#This file should have been aquired from rooted(definitly)/jailbroken(likely) phone
userInput = input('FreeOTP secret: ')

#put each byte from the above string into its own element in an array ready to be itterated over
inputArray = userInput.split(",")

#itterate over each integer in the array, convert them all into hex using the convertToHes() function, append all into one string
for i in inputArray:
    hexString = hexString + convertToHex(i)


#print out hex value, useful for debugging only
#print ('Hex: ', hexString)

#convert the string of hex into a byte array. this is required for the base64 library to convert it into base32
byteString = bytearray.fromhex(hexString)
#convert bytearray into the base32. aka the final secret
result = base64.b32encode(byteString)

#convert the result into ascii ready to be printed as a string.
result = result.decode("ascii")

print ('Base32 Secret: ', result)
