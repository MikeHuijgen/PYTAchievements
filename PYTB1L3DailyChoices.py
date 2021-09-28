import time

vraag1 = 'Wat doe je als eerst in de ochtent'
a1 = 'a = Telefoon bekijken'
b1 = 'b = Ontbijten'
c1 = 'c = Douche' 

vraag2 = 'Wat doe je als je weg gaat van huis?'
a2 = 'a = Niks'
b2 = 'b = Naar school'
c2 = 'c = Naar werk' 

vraag3 = 'Met wat ga je naar je werk of school?'
a3 = 'a = OV'
b3 = 'b = Auto'
c3 = 'c = Fiets' 

vraag4 = 'Wat doe je als je weer thuis kom'
a4 = 'a = film kijken'
b4 = 'b = Met vrienden afspreken'
c4 = 'c = Gamen' 

vraag5 = 'Wat doe jij in de avond'
a5 = 'a = slapen'
b5 = 'b = Youtube kijken en te laat slapen'
c5 = 'c = feesten' 

print(vraag1)
time.sleep(1)
print(a1)
time.sleep(1)
print(b1)
time.sleep(1)
print(c1)
time.sleep(1)
antwoord1 = input()
if antwoord1 == 'a':
    print("Ik doe dat ook altijd!")
elif antwoord1 == 'b':
    print("Hmmmmmm klinkt lekker")
else:
    print(antwoord1, "dat doe ik nooit")    
time.sleep(1)

print(vraag2)
time.sleep(1)
print(a2)
time.sleep(1)
print(b2)
time.sleep(1)
print(c2)
time.sleep(1)
antwoord2 = input()
if antwoord2 == 'a':
    print("Lui!")
elif antwoord2 == 'b':
    print("Ik ook om 6 uur")
else:
    print(antwoord2, "Ik ben werkloos :p")
time.sleep(1)
print(vraag3)
time.sleep(1)
print(a3)
time.sleep(1)
print(b3)
time.sleep(1)
print(c3)
time.sleep(1)
antwoord3 = input()
if antwoord3 == 'a':
    print("Leuk he het OV")
elif antwoord3 == 'b':
    print("Ik zou dat zo graag willen")
else:
    print(antwoord3, "Ik heb medelijden met je")
time.sleep(1)
  
print(vraag4)
time.sleep(1)
print(a4)
time.sleep(1)
print(b4)
time.sleep(1)
print(c4)
time.sleep(1)
antwoord4 = input()
if antwoord4 == 'a':
    print("Dat is altijd leuk")
elif antwoord4 == 'b':
    print("Ik ben een gamer kom op")
else:
    print(antwoord4, "GamerForLife")
time.sleep(1)
   
print(vraag5)
time.sleep(1)
print(a5)
time.sleep(1)
print(b5)
time.sleep(1)
print(c5)
time.sleep(1)
antwoord5 = input()
if antwoord5 == 'a':
    print("Hoe gewoon HOE")
elif antwoord5 == 'b':
    print("Dit klink te bekend")
else:
    print(antwoord5, "Zal ik never doen")