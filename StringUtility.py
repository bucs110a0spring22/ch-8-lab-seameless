class StringUtility:
  def __init__(self, string):
    '''The __init__() takes a string as a parameter and stores it as an instance variable.
'''
    self.string = string

  def __str__(self):
    '''return the internal string itself, unchanged
'''
    return str(self.string)

  def vowels(self):
    '''Count the number of vowels in the string, and return a new string of the form '<count>', where <count> is the number of vowels in the string as a string 
'''
    vowels = set("aeiouAEIOU")
    count = 0
    for c in self.string:
      if c in vowels:
        count += 1
    if count > 4:
      return many
    else:
      return count


  def bothEnds(self): 
    '''return a string made of the first 2 and last 2 chars of the original string, so 'spring' yields 'spng'. However, if the string length is less than or equal to 2, return an empty string instead.'''
    if len(str) < 3:  
      return ''  
    if len(str) > 2:
      return str[0:2] + str[-2:]  
  
  def fixStart(self):
    '''return a string where all occurrences of i\ts first char have been changed to '*', _except do not change the first char itself_. e.g. 'babble' yields 'ba**le'.
If the parameter is length 1 or less, return the parameter as is.
'''
    first = self[0]
    length = len(self)
    self = self.replace(first, '*')
    self = first + self[1:]

    return self


  def asciiSum(self):
    '''return an integer that is the sum of all ascii values in the string.'''
    for i in self.string:
      asciisum += ord(i)
    return asciisum

  def cipher(self):
    '''return an encoded string by incrementing all letters by the length of the string'''
    ciph = ""
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    inc = len(self.string)
    for i in self.string:
        if i in alphabet:
          mod = chr(ord(i)+inc)
          while ord(mod) >= 91 and i.isupper():
            mod = chr(ord(mod) - 26)
          while ord(letter) >= 123 and i.islower():
            mod = chr(ord(letter) - 26)
        else:
          letter = i
        ciph += letter
      return ciph
        