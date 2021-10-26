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
>>> print('Mijn naam is Tristan')
naam = 'Tristan'
print(naam)
print(naam.upper())
print(naam[0:2])
print(naam[::-1])
Mijn naam is Tristan
>>> leeftijd = 17
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
NameError: name 'naam' is not defined
>>> naam = 'Tristan'
>>> leeftijd= 17
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
Hallo Tristan ben je al 17 jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
18
>>> leeftijd-=1
>>> leeftijd
17
>>> if leeftijd < 18:
	hoelang_tot18jaar = 18 - leeftijd
	print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
elif leeftijd > 18:
	hoelang_al18jaar = leeftijd - 18
	print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
else:
	print('Je bent precies ' + str(leeftijd) + ' jaar')

	
Over 1 jaar wordt je 18
>>> from random import randint
>>> randint(0,1000)
297
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
962
>>> 
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))

Willekeurig getal tussen 0 en 1000: 962
>>> from datetime import datetime
>>> datum = datetime.now()
>>> print(datum)
2021-09-17 10:09:46.272696
>>> datum.strftime('%A %d %B %Y')
'Friday 17 September 2021'
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'vrijdag 17 september 2021'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime('%A %d %B %Y')
'venerdì 17 settembre 2021'
>>> 