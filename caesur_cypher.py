alphabets : str = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt():
    message = input("Enter the message : ")
    shift = int(input("Amount to be shifted : "))
    
    encrypted_message = ""
    for i in range(len(message)):
        if(message[i]==" "):
            encrypted_message += " "
        else:
            encrypted_message += alphabets[(alphabets.index(message[i])+shift)%26]
    print(f"Encrypted message = {encrypted_message}")

def decrypt():
    encrypted_message = input("Enter the encrypted message : ")
    shift = int(input("Amount the message shifted : "))
    
    decrypted_message = ""
    for i in range(len(encrypted_message)):
        if(encrypted_message[i]==" "):
            decrypted_message += " "
        else:
            decrypted_message += alphabets[(alphabets.index(encrypted_message[i])-shift)]
    print(f"Decrypted message = {decrypted_message}")

while(1):
    print("ACTIONS --->  encrypt , decrypt , exit")
    value = input("Enter what action to do : ")

    match value:
        case "encrypt" : encrypt()
        case "decrypt" : decrypt()
        case "exit" : exit()
        case _ : "Enter a valid action!!"
    
