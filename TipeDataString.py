# r = 'Ini sebuah string'
# s = "Ini juga sebuah string"
# t = """Ini sebuah string panjang.
# Bisa ditulis lebih dari satu baris. """
# u = input("Masukkan sebuah teks: ")
# x = '' # string kosong
# y = len(r) # menghitung panjang string


# print(r)
# print(s)
# print(t)
# print(u)
# print(x)
# print(y)






# x = 'AB' + 'cd'
# y = 'A' + '7' + 'b' # non variabel
# z = 'A' + str(7) + 'b' # variabel
# xy = 'Hello ' * 3

# print(x)
# print(y)
# print(z)
# print(xy)






# while True :
#     email = input("Maukkan Email :")
#     cek = '@' in email
#     status = ''

#     if cek == True :
#         status = "Email berhasil di validasi"
#     else :
#         status = "Email kurang lengkap"

#     print(status)
#     print()








import os
os.system("cls") # cls

status = ''

def username():
    print()
    inputan = input("Masukkan Username : ")
    cek1 = len(inputan)
    cek2 = ' ' in inputan
    cek3 = inputan.capitalize()

    if cek1 > 9 and cek2 == False and cek3 == inputan:
        status = "Berhasil"
        return inputan, status
    else :
        inputan = "Username tidak valid"
        status = "Gagal"
        return inputan, status

def email():
        inputan = input("Masukkan Email : ")
        cek1 = len(inputan)
        cek2 = ' ' in inputan
        cek3 = '@' and '.' in inputan

        if cek1 > 7 and cek2 == False and cek3 == True:
            status = "Berhasil"
            return inputan, status

        else :
            inputan = "Email tidak valid"
            status = "Gagal"
            return inputan, status

def hp():
    inputan = input("Masukan Nomor Handphone :")
    cek1 = len(inputan)
    cek2 = ' ' in inputan 
    cek3 = inputan.isdigit()
    
    if cek1 > 7 and cek2 == False  and cek3 == True  :
        status = "Berhasil"
        return inputan, status 
    
    else :
        inputan = "Nomor handphone salah "
        status ="Gagal"
        return inputan , status
        

while True:
    u1, u2 = username()
    e1, e2 = email()
    i1, i2 = hp()

    print("\nUsername = ", u1)
    print("Status = ", u2)
    
    print("\nEmail = ", e1)
    print("\nStatus = ", e2)

    print ("\nNomor Handphone=",i1)
    print ("Status =",i2)
        
        


