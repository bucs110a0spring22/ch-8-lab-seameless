class StringUtility:
  def __init__(self, string):
    self.string = string

  def __str__(self):
    return str(self.string)

  def vowels(self):
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
    if len(str) < 3:  
      return ''  
    if len(str) > 2:
      return str[0:2] + str[-2:]  
  
  def fixStart(self):
    first = self[0]
    length = len(self)
    self = self.replace(first, '*')
    self = first + self[1:]

    return self


  def asciiSum(self):
    for i in self.string:
      asciisum += ord(i)
    return asciisum

  def cipher(self):
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
        