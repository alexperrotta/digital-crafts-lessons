Lowercase a String
Given a string, print the string in lowercase.

stringToLower = raw_input("lowercase this: ")
print "lowercase word: %s" % stringToLower.lower()




Uppercase a String
Given a string, print the string in uppercase.

stringToUpper = raw_input("Uppercase this: ")
print "uppercase word: %s" % stringToUpper.lower()




Capitalize a String
Given a string, print the string capitalized.

stringToCap = raw_input("Capitalize this: ")
print "Capitalize word: %s" % stringToCap.capitalize()




Reverse a String
Given a string, print the string reversed.

reversedString = raw_input("Reversed string: ")
print reversedString[:: -1]  # starts from the end of the string



Leetspeak
Given a paragraph of text as a string, print the paragraph in leetspeak. To translate a
string to leetspeak, you need to replace make the following character replacements

(treat all input characters as uppercase):

A => 4

E => 3

G => 6

I => 1

O => 0

S => 5

T => 7

Example: Leet => 1337

stringToLeet = raw_input("leet this: ").upper

stringToLeet.replace("A", "4");
stringToLeet.replace("E", "3");
stringToLeet.replace("G", "6");
stringToLeet.replace("I", "1");
stringToLeet.replace("O", "0");
stringToLeet.replace("S", "5");
stringToLeet.replace("T", "7");

print stringToLeet





Long-long Vowels
Given a word as a string, print the result of extending any long vowels to the length of 5. Examples:

Good => Goooood
Cheese => Cheeeeese
Man => Man
Spoon => Spooooon


word = 'cheese'

long_vowels = ['oo', 'ee']

result = ''
for i in range(len(word)):
    twoletters = word[i:i+2]
    if twoletters in long_vowels:
        result += word[i] * 4
    else:
        result += word[i]

print result

# or

word = 'cheese'

word = word.replace('ee', 'eeeee')
word = word.replace('oo', 'ooooo')

print word






Caesar Cipher
Given a string, print the Caesar Cipher (or ROT13) of that string. What is Caesar

Cipher? http://practicalcryptography.com/ciphers/caesar-cipher/

Use your solution to decipher the following text: “lbh zhfg hayrnea jung lbh unir yrnearq”