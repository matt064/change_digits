
def convert_digit(v):

    liczby = {
        "I": 1,
        "V": 5,
        "X" : 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    numbers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    roman = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']

    if type(v) == str:
        N = len(v)
        i = N - 1
        wynik = 0

        while i >= 0:
            wynik += liczby[v[i]]
            i -= 1
        return wynik


