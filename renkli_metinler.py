"""Renkli metinler."""
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(Fore.BLACK+Back.YELLOW+"Merhaba! Benim adım Ali")
print(Back.CYAN+"Merhaba!. Benim adım Ayşe")
print(Fore.RED+Back.GREEN+"Merhaba! Benim adım Mehmet")
print(Style.BRIGHT+"Merhaba! Benim adım Ahmet")
print(Style.NORMAL+"Merhaba! Benim adım Ahmet")
