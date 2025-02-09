def file_encryption(file_path):
    global private_key1,private_key2
    private_key1 = int(input("Enter the first prime number (different from 2): "))
    private_key2 = int(input("Enter the second prime number (different from 2): "))
    result = ""
    with open(file_path,"r") as file:
        for line in file:
            for str in line:
                for c in str:
                    process = (ord(c) * private_key1 + private_key2) % 128
                    result += chr(process)
    with open("encrypt_file","w") as cyripto_file:
        cyripto_file.write(result)
    print("file succesfuly encrypted.")

def decode_file(file_name):
    result = ""
    k = 1
    while ((128*k) +1) % private_key1 != 0:
        k += 1
    l = ((128*k) + 1) // private_key1
    m = (l*private_key2) % 128
    with open(file_name,"r") as file:
        for line in file:
            for c in line:
                process = (ord(c)*l - m) % 128          # Modular inverse
                getback = chr(process)
                result += getback
    print(result)

