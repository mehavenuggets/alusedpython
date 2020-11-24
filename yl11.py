import math

text = input("Sisesta suvalised sümbolid: ").strip() 
if len(text) > 6 and len(text) % 2 != 0:
    middle = math.floor(len(text)/2)
    print(text[middle-1] + text[middle] + text[middle+1])
else:
    print("Sümboleid peab olema 7, proovi uuesti")