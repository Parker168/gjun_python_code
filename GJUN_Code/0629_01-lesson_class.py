class Duck:
    def __init__(self, color, sound):
        self.color = color
        self.sound = sound

    def make_some_noise(self):
        print(f"Duck is making some noise !! {self.sound * 3}")

    def move(self):
        print(f"Duck move.")

    def swim(self):
        print("Duck swim ~")

    def eat(self):
        print("Duck eat.")

    def hatch(self):
        print("Duck hatch zzz.")


if __name__ == '__main__':
    duck_1 = Duck(color='yellow', sound="ba")
    duck_2 = Duck('black', "ga")
    duck_3 = Duck("White", "gua")

    duck_3.make_some_noise()
    print(duck_3.sound)



