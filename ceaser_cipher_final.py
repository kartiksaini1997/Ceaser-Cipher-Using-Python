def enc(_str_,shift): 
    result_e = "" 
  
    # traverse text 
    for i in range(len(_str_)): 
        char = _str_[i] 
  
        # Encrypting uppercase characters 
        if (char.isupper()): 
            result_e += chr((ord(char) + shift - 65) % 26 + 65) 
  
        # Encrypting lowercase characters 
        else: 
            result_e += chr((ord(char) + shift - 97) % 26 + 97) 
  
    return result_e 


def dec(_str_,shift): 
    result_d = "" 
  
    # traverse text 
    for i in range(len(_str_)): 
        char = _str_[i] 
  
        # Decrypting uppercase characters 
        if (char.isupper()): 
            result_d += chr((ord(char) - shift + 65) % 26 + 65) 
  
        # Decrypting lowercase characters 
        else: 
            result_d += chr((ord(char) - shift + 97) % 26 + 97) 
  
    return result_d


if __name__ == '__main__':
    _str_=input('ENTER A STRING: ')
    shift=int(input('ENTER A SHIFT VALUE: '))
    choice=input('e for encryption\nd for decryption: ')
    if choice == 'e':
        print("Encrypted message: ",enc(_str_,shift))
    elif choice == 'd':
        print("Decrypted message: ",dec(_str_,shift))
    else:
        print('not valid')  