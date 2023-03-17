import random

keyLen = random.randint(0,20)
keyD = random.randint(0,10000)
keyBank = ["c","d","e","l","m","n","p","s","t","v","w","z","0","9","1","2"]
keyGen = ""

while keyLen >0:
    keyGen += keyBank[keyD % keyLen]
    keyLen -= 1

print(keyGen)
