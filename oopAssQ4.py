class Joker:
    def __init__(self, name, power, is_he_psycho):
        self.name = name
        self.power = power
        self.is_he_psycho = is_he_psycho


j1 = Joker("Heath Ledger", "Mind Game", False)
print(j1.name)
print(j1.power)
print(j1.is_he_psycho)
print("=====================")
j2 = Joker("Joaquin Phoenix", "Laughing out Loud", True)
print(j2.name)
print(j2.power)
print(j2.is_he_psycho)
print("=====================")
if j1 == j2:
    print('same')
else:
    print('different')
j2.name = 'Heath Ledger'
if j1.name == j2.name:
    print('same')
else:
    print('different')

print("The first if else block gives different as answer because j1 and j2 indicates their address while on the other the other hand the second if/else block give same because in line 21, we changed j2's name into j1's.")
