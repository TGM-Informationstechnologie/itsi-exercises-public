
class Color:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue


def farbanteil():
    print("Füge Werte zwischen 0 und 255 für rot, grün und blau ein!")
    r1 = int(input("Rot-Anteil: "))
    g1 = int(input("Grün-Anteil: "))
    b1 = int(input("Blau-Anteil: "))
    return Color(r1, g1, b1)


print("Bestimmung der gemeinsamen öffentlichen Farbe:")
pubCo = farbanteil()
print(f"Eure gemeinsamen öffentlichen Farbwerte lauten: {pubCo.red}, {pubCo.green}, {pubCo.blue}\n")

print("Bestimmung der eigenen geheimen Farbe:")
privCo = farbanteil()
print(f"Deine persönlichen geheimen Farbwerte lauten: {privCo.red}, {privCo.green}, {privCo.blue}\n")

mix1 = (
    (pubCo.red + privCo.red) // 2,
    (pubCo.green + privCo.green) // 2,
    (pubCo.blue + privCo.blue) // 2,
)
print(f"Sende diese gemischten Farbwerte an den Empfänger: {mix1}\n")

print("Welche Farbwerte hast du zugeschickt bekommen?")
bCo = farbanteil()

privKey = Color(
    (privCo.red + 2 * bCo.red) // 3,
    (privCo.green + 2 * bCo.green) // 3,
    (privCo.blue + 2 * bCo.blue) // 3,
)
print(f"Eure gemeinsame Geheimfarbe lautet: {privKey.red}, {privKey.green}, {privKey.blue}")
