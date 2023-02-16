
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



