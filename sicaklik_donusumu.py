"""Celsius - Fahrenheit."""


def sicaklik_donustur(s):
    f = float(s)
    c = (f - 32) * 100/180
    # suyun donma ce kaynama noktası celsius 0 - 100 = 100
    # Fahrenheit olarak 32 - 212 = 180
    return c


print(sicaklik_donustur(78))
