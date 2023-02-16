
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
        v = v.upper()
        v = list(v)
        if all([i in liczby for i in v]):
            N = len(v)
            i = N - 1
            wynik = 0

            while i >= 0:
                if i < N-1 and liczby[v[i]] < liczby[v[i+1]]:
                    wynik -= liczby[v[i]]
                else:
                    wynik += liczby[v[i]]
                i -= 1
            return wynik
        else:
            raise ValueError('Illegal symbol')
    
    #zmienna int        
    if type(v) == int:
        N = len(numbers)
        i = N - 1
        wynik = ""
        while v != 0:
            if numbers[i] <= v:
                wynik += roman[i]
                v -= numbers[i]
            else:
                i -= 1
        
        return wynik



