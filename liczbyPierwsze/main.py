# od 9 do 10 milionow

def is_prime(number):
    if number < 2:
        return False
    if number in [2, 3]:
        return True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def lucas_lehmer_test(p):
    S = 4
    M = 2**p - 1
    if p==2:
        return True
    if is_prime(p):
        for i in range(3,p+1):
            S = (S**2 - 2) % M
        print(f"p = {p} M = {M} {S == 0}")
        if S == 0:
            return True


counter2 = 0
for i in range(2,32):
    if lucas_lehmer_test(i):
        counter2 += 1
print(f"Ilosc liczb pierwszych dla testu lucasa_lehmera: { counter2 }\n")

number = 0
counter3 = 0

for i in range(2,32):
    if is_prime(i):
        number = 2**i - 1
        if is_prime(number):
            counter3 += 1
            is_or_not = True
            print(f"2^{i}-1 : {number}  {is_or_not} ")
        else:
            is_or_not = False
            print(f"2^{i}-1 : {number}  {is_or_not}")
print(f"Ilosc liczb pierwszych metoda probnego dzielenia: { counter3 }\n")





