import pyautogui as pg

#xi, yi = initial position

def clicker():
    xi, yi = pg.position()
    x, y = pg.position()
    while xi == x and yi == y:
        pg.click(clicks=20, interval=0.001)
        x, y = pg.position()
    print(" You moved so no more clicking for you! ")


clicker()
