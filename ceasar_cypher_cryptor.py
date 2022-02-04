from curses.ascii import islower
from hashlib import new
'''
made by r3d_f1lc0n
'''

# formula of cypher shift : c = (x + shift) % 26


# simpler version i made by myself
def coder(hash, shift):
    hashed_pass = []

    if type(hash) == str:
        
        for i in hash:
            
            # checking if string is lowercase
            if i.islower():
                # getting the position of each character in the string
                char_pos = ord(i)

                if (char_pos + shift) > 122:
                    difference = 122 - char_pos
                    shift -= difference +1
                    print(shift)
                    hashed_pass.append(chr(ord("a")+shift))

                else:
                    hashed_pass.append(chr(char_pos + shift))
            else:
                hash.lower()
    
    new = "".join(hashed_pass)
    print("[+]first_code ==>", new)
                

            
coder("hello world", 3)


def upgraded(hash, shift):

    hashed = []
    encryption = ""
    #checking type of hash
    if type(hash) == str:

        for c in hash:
        # checking validity of hash
            if c.islower():
            
            
                # getting the pos of each character
                unico_c = ord(c)
                
                char_pos = ord(c) - ord("a")        #switch from unicode to normal alphabet


                # shifting the character by the "shift" 
                # note that the index of each char will be
                # be between 0-25 so that there is no error in assembling the characters back

                c_index = (char_pos + shift) % 26

                # specifying the new index of the shifted character back in the 
                # normal unicode format
                new_index = c_index + ord("a")

                # appending the value of the unicode character
                # into the normal alphabet and appending to the empty list
                new_unicode = chr(new_index)

                encryption += chr(new_index)
        print("[+]second_code ==>", encryption)

upgraded("hello world", 3)


