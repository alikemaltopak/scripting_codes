def encription():
    result = ""
    mesage = input("Şifrelemek istediğiniz mesajı girin: ")
    with open("/Users/alikemaltopak/Library/CloudStorage/OneDrive-Kişisel/VSCODE_PERSONAL_PY/File/şifreli_mesaj.txt","w") as criptofile:
        for c in mesage:
            process = (ord(c)*3 + 5) % 128
            result += chr(process)
        criptofile.write(f"şifrelenmiş mesaj:{result}") 
        print("Mesajınız başarıyla şifrelendi.")  

def decode(filename):
    result = ""
    with open(filename,"r") as decodefile:
        for line in decodefile:
            line = line.strip()
            liste = line.split(":")
            cripto_mesage = liste[1]
        for c in cripto_mesage:
            process = (ord(c)*43 - 87) % 128    #3mod128 tersini bul işlemleri tersine çevir şifreli mesajı çöz
            getback = chr(process)
            result += getback
        print(result)
decode("/Users/alikemaltopak/Library/CloudStorage/OneDrive-Kişisel/VSCODE_PERSONAL_PY/File/şifreli_mesaj.txt")

