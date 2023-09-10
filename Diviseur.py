import math

random_a = int(input("Veuillez rentrez un nombre positif quelconque : "))
random_b = int(input("Veuillez rentrez un nombre positif quelconque : "))

print(f"le plus grand diviseur commun est : {math.gcd(random_a, random_b)}")
print(f"le plus petit multiplicateur commun est : {math.lcm(random_a, random_b)}")
