txt = "Hello world"
print(txt)
print ("Jumlah karakter : ",len(txt))
print ("Karakter terakhir : ",txt[len(txt)-1:len(txt)])
print ("Karakter index ke-2 => ke-4 : ",txt[2:5])
print ("Tanpa spasi : ",txt.replace(" ", ""))
print ("Ubah teks menjadi kapital : ",txt.upper())
print ("Ubah teks menjadi huruf kecil : ",txt.lower())
print ("Ganti karakter H denga J : ",txt.replace("H", "J"))