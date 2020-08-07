import re

def isPalindrome(s):
    return s == s[::-1]

def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str

def printWords(s):
# split the string
    s = s.split (' ')
 # iterate in words of string
    for word in s:
        if len(word) % 2 == 0:
            print (word)


def check(s):
    s = s.lower ( )
    # set() function convert "aeiou"
    # string into set of characters
    # i.e.vowels = {'a', 'e', 'i', 'o', 'u'}
    vowels = set ("aeiou")
    # set() function convert empty
    # dictionary into empty set
    s = set ({})
    # looping through each
    # character of the string
    for char in s:
        if char in vowels:

            s.add (char)
    else:
        pass
        # check the length of set s equal to length
        # of vowels set or not. If equal, string is
        # accepted otherwise not
    if len (s) == len (vowels):
        print ("The following String does have all vowels because it is less than the length of the vowel set")
    else:
        print ("The following String doesn't have all vowels because it is less than the length of the vowel set")

def run(s):
 # Make own character set and pass
 # this as argument in compile method
    regex = re.compile ('[@_!#$%^&*()<>?/\|}{~:]')
    # Pass the string in search
    # method of regex object.
    if (regex.search (s) == None):
        print ("Is there any special characters in the string?: No, so we do accepted it")
    else:
        print ("Is there any special characters in the string?: Yes, so we don't accepted it")


                # Driver code
s = str(input("Enter a string: "))
ans = isPalindrome(s)
if ans:
    print ("Is this string a Palindrome?: Yes this is a Palindrome")
else:

 print("Is this string a Palindrome?: No this is not a Palindrome")
print ("The reversed string" + " = " + (reverse(s)))
print("The length of the string is" + " = " + str(len(s)))
print("Print even length words in a string below: " + str(printWords(s)))
print("Does the string contains all vowels?: " + str(check(s)))
print("Does the string contains any special character?: " + str(run(s)))

