"""Telefon bilgi."""
import phonenumbers
from phonenumbers import carrier, geocoder, timezone

numara = input("Telefon numaranızı giriniz : ")
telefon_numarasi = phonenumbers.parse(numara)
print(f"Location : {geocoder.description_for_valid_number(telefon_numarasi,'tr')}")
print(f"Carrier : {carrier.name_for_number(telefon_numarasi,'tr')}")
print(f"Time Zone : {timezone.time_zones_for_number(telefon_numarasi)}")
