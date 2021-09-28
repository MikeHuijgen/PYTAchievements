Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2 + 2
4
>>> 3 * 10
30
>>> 100 - 10
90
>>> 25 / 5
5.0
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>> print('Mike')
Mike
>>> naam = '<Mike>'
>>> naam = 'Mike '
>>> print(naam)
Mike 
>>> print(naam.upper())
MIKE 
>>> print(naam[0:2])
Mi
>>> print(naam[::-1])
 ekiM
>>> leeftijd = 19
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
Hallo Mike  ben je al 19 jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
20
>>> leeftijd-=1
>>> leeftijd
19
>>> if leeftijd < 18:
    hoelang_tot18jaar = 18 - leeftijd
    print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
elif leeftijd > 18:
    hoelang_al18jaar = leeftijd - 18
    print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
else:
    print('Je bent precies ' + str(leeftijd) + ' jaar')
    # Let op: hier 2x een enter doen!

    
Het is alweer 1 jaar geleden dat je 18 werd ;-)
>>> from random import randint
randint(0,1000)
willekeurig_getal = randint(0,1000)
willekeurig_getal
print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))

SyntaxError: multiple statements found while compiling a single statement
>>> from random import randint
>>> randint(0,1000)
773
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
391
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 391
>>> from datetime import datetime
>>> datum = datetime.now()
>>> print(datum)
2021-09-16 09:55:44.077931
>>> datum.strftime('%A %d %B %Y')

'Thursday 16 September 2021'
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'donderdag 16 september 2021'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime('%A %d %B %Y')
'giovedì 16 settembre 2021'
>>> 