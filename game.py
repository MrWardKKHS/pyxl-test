import pyxel

WIDTH = 200
HEIGHT = 200
pyxel.init(WIDTH, HEIGHT)
x = 0

def update():
    x += 5
    if x > WIDTH:
        x = -20

def draw():
    pyxel.cls(0)
    pyxel.rect(x, 10, 20, 20, 11)

pyxel.run(update, draw)