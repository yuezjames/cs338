import hashlib
import binascii

words = [line.strip().lower() for line in open ('password3.txt')]
bank = [line.strip().lower() for line in open ('passwordbank.txt')]
fileoutput = open("cracked3.txt","w+")
countOfcracked = 0
countOfhash = 0
i = 0
while i < len(words):
    username = words[i].split(":",2)[0]
    salt = words[i].split(":",2)[1].split("$")[2]
    hash = words[i].split(":",2)[1].split("$")[3]
    x = 0
    while x < len(bank):
        password = bank[x]
        saltedpassword = salt + password
        encoded_password = saltedpassword.encode('utf-8')
        hasher = hashlib.sha256(encoded_password)
        countOfhash += 1
        digest = hasher.digest()
        digest_as_hex = binascii.hexlify(digest)
        digest_as_hex_string = digest_as_hex.decode('utf-8')
        if digest_as_hex_string == hash:
            fileoutput.write(username+':'+password+'\n')
            countOfcracked += 1
            print(f'Found: {i}')
            break
        else :
            x += 1
    i += 1

print(f'number of cracked is: {countOfcracked}')
print(f'number of hash is: {countOfhash}')
print('end of program')

#Code of part 2
#words = [line.strip().lower() for line in open ('password2.txt')]
#bank = [line.strip().lower() for line in open ('passwordbank.txt')]
#database = {}
#for line in open('password2.txt'):
    #user = line.lower().split(":",2)[0]
    #hash = line.lower().split(":",2)[1]
    #database[hash] = user
#fileoutput = open("cracked2.txt","w+")
#countOfcracked = 0
#countOfhash = 0
#i =0

#while i < 40000:
    #y = 0
    #while y < len(bank):
        #password = bank[i]+bank[y]
        #encoded_password = password.encode('utf-8')
        #hasher = hashlib.sha256(encoded_password)
        #countOfhash += 1
        #digest = hasher.digest()
        #digest_as_hex = binascii.hexlify(digest)
        #digest_as_hex_string = digest_as_hex.decode('utf-8')
        #if digest_as_hex_string in database:
            #fileoutput.write(database[digest_as_hex_string]+':'+password+'\n')
            #countOfcracked += 1
            #print(f'Found: {countOfcracked}')
            #break
        #else :
            #y += 1
    #i += 1

#print(f'number of cracked is: {countOfcracked}')
#print(f'number of hash is: {countOfhash}')
#print('end of program')

#Code of old part 1
#while i < 40000:
    #y = i
    #print(i)
    #while y < 40000: 
        #password1 = bank[i]+bank[y]
       # password2 = bank[y]+bank[i]
       # encoded_password1 = password1.encode('utf-8')
       # encoded_password2 = password2.encode('utf-8')
       # hasher1 = hashlib.sha256(encoded_password1)
      #  hasher2 = hashlib.sha256(encoded_password2)
      #  countOfhash += 2
      #  digest1 = hasher1.digest()
     #   digest2 = hasher2.digest()
      #  digest_as_hex1 = binascii.hexlify(digest1)
      #  digest_as_hex2 = binascii.hexlify(digest2)
     #   digest_as_hex_string1 = digest_as_hex1.decode('utf-8')
       # digest_as_hex_string2 = digest_as_hex2.decode('utf-8')
      #  x = 0
      #  while x < len(words):
      #      hashed = words[x].split(":",2)[1]
      #      username = words[x].split(":",2)[0]
       #     if hashed == digest_as_hex_string1:
        #        fileoutput.write(username+':'+password1+'\n')
       #         countOfcracked += 1
       #         print(f'Found: {x}')
        #        break
       #     elif hashed == digest_as_hex_string2:
        #        fileoutput.write(username+':'+password2+'\n')
       #         countOfcracked += 1
       #         print(f'Found2: {x}')
       #     else :
       #         x += 1
       # y += 1
   # i += 1


#print(f'number of cracked is: {countOfcracked}')
##print(f'number of hash is: {countOfhash}')
#print('end of program')

