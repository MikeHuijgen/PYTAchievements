import time

tekst1 = 'De Python lessen worden gegeven voor Erik, Erwin en ook door Hidde'
tekst2 = 'SD vakken zijn bijvoorbeeld Python, UXD, Frontend development en Backend development. Wat leuk!'
tekst3 = 'Wat is hier het laatste woord?'
tekst4 = 'Het www is ontwikkeld vanaf 1989 door Tim Berners-Lee'

t11 = tekst1[37:41]
t12 = tekst1[43:48]
t13 = tekst1[61:66]

t21 = tekst2[28:34]
t22 = tekst2[35:39]
t23 = tekst2[40:61]
t24 = tekst2[65:84]

t31 = tekst3[24:30]

t41 = tekst4[4:8]
t42 = tekst4[28:33]

print(tekst1)
time.sleep(1)
print(t11 , t12 , t13)
time.sleep(1)
print(tekst2)
time.sleep(1)
print(t21 , t22 , t23 , t24)
time.sleep(1)
print(tekst3)
time.sleep(1)
print(t31)
time.sleep(1)
print(tekst4)
time.sleep(1)
print(t41 , t42)