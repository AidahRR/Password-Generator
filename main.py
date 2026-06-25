import random
import string
Length = int(input("How long do you want your password to be?: "))
Characters = (string.ascii_letters+
              string.digits+
              string.punctuation)
Password = ''.join(random.choice(Characters) for i in range (Length))
print (Password)
