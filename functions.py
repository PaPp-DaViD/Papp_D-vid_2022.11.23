from data import csapattagok
from os import system

filename='csapattagok.csv'
cimsor=''

def menu():
    system('csl')
    print('0 - Kilépés')
    print('ADMINISZTRÁCIÓ')
    print('1 - csapattagok')
    print('2 - Új tag felvétele')
    print('3 - Tag törlése')
    print('INFORMÁCIÓ')
    print('4 - Legidősebb tagok')
    print('5 - pozíciók')
    print('6 - Legmagasabb tagok')
    print('7 - Legnehezebb tagok')
    print('8 - Legtöbb ponttal rendelkező tag')