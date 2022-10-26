import pyxel

WIDTH = 200
HEIGHT = 200
class Game:
    def __init__(self) -> None:
        pyxel.init(WIDTH, HEIGHT)
        self.x = 0

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        self.x += 1
        if self.x > WIDTH:
            self.x = -20

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, 10, 20, 20, 11)


game = Game()
pyxel.run(game.update, game.draw)