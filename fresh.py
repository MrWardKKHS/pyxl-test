import pyxel

WIDTH = 200
HEIGHT = 200
x = 0
pyxel.init(WIDTH, HEIGHT)

def update():
    global x
    x += 5
    if x > WIDTH:
        x = -20

def draw():
    pyxel.cls(0)
    pyxel.rect(x, 10, 20, 20, 10)

pyxel.run(update, draw)