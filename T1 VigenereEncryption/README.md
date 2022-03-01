# Task #1 - Vigenere Encryption

## Problem Statement
You and your friend love writing messages to each other on slips of paper in history class while the teacher rambles on, but you fear that you will someday get caught and exposed if someone reads one of the messages. You decide to start encrypting your messages using the Vigenere cipher, illustrated below (image courtesy of [Scioly.org Wiki - Codebusters - Vigenere](https://scioly.org/wiki/index.php/Codebusters#Vigen.C3.A8re_Cipher)).

<p align="center">
<img src="https://firebasestorage.googleapis.com/v0/b/my-scrap-project.appspot.com/o/vigtable.png?alt=media&token=b1b230ca-c6d5-4148-9fb8-c901dadcacbb">
</p>

The Vigenere cipher encrypts messages by summing the numerical representations of each letter and the key, where the key is repeated as many times as necessary in order to apply it to the entire message. In the example above, the phrase "SCIENCE OLYMPIAD IS COOL" is encrypted using a key of "SCIOLY".

Write a program which, given a message and a key, encrypts the message using the Vigenere cipher using the given key, maintaing case and ignoring non-alphabetic characters, outputting the encrypted message.

## Input Format
```
Message
Key
```

## Output Format
```
Encrypted Message
```

## Constraints
<img src="https://i.ibb.co/FJzv1Kn/image.png">
