"""Roma sayılarını ondalıklı sayıya çevirmek."""
cetvel = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def donustur_ondalik(roma_rakami):
    sum = 0
    for i in range(len(roma_rakami)-1):
        sol = roma_rakami[i]
        sag = roma_rakami[i+1]
        if cetvel[sol] < cetvel[sag]:
            sum -= cetvel[sol]
        else:
            sum += cetvel[sol]
    sum += cetvel[roma_rakami[-1]]
    return sum


print(donustur_ondalik('XCIX'))  # 99
print(donustur_ondalik('LXXVIII'))  # 78
print(donustur_ondalik('XI'))  # 78
print(donustur_ondalik('MCMLXXXIV'))  # 1984
