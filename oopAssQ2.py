class Flower:
    def __init__(self):
        self.name = "default"
        self.colors = "RGB"
        self.num_of_petals = 0


flower1 = Flower()
flower1.name = "Rose"
flower1.color = "Red"
flower1.num_of_petal = 6
print("Name of this flower:", flower1.name)
print("Color of this flower:", flower1.color)
print("Number of petal:", flower1.num_of_petal)
print("=====================")
flower2 = Flower()
flower2.name = "Orchid"
flower2.color = "Purple"
flower2.num_of_petal = 4
print("Name of this flower:", flower2.name)
print("Color of this flower:", flower2.color)
print("Number of petal:", flower2.num_of_petal)

print(flower1)
print(flower2)

n = flower1
m = flower2

if n == m:
    print("they are same")
else:
    print("they are different")
