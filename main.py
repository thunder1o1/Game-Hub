import pygame as p
import time as t

#region init
p.init()
r = p.display.set_mode((800, 600))
p.display.set_caption('Game Hub')

C = 0
c = 0
F = p.font.Font('freesansbold.ttf', 48)
FRAME = 0
#endregion

#region text
class Text():
    def __init__(self, text, pos, colour):
        self.text = F.render(text, True, colour)
        self.rect = self.text.get_rect()
        self.rect.center = (pos[0], pos[1])
        self.copy = self.text.copy()

Tplay = Text('PLAY', (400, 300), '#EEEEEE')
#endregion

#region functions
def bg():
    global C
    C = C + .125 if C < 32 else -C
    c = abs(int(C))
    for i in range(60):
        h = (c + i * 2) % 255
        p.draw.rect(r, (h, h + 32, h + 40),
                    [0, i * 10, 800, 10])

def buttons():
    global text1, rect1
    m = p.mouse.get_pos()
    if 300 < m[0] < 500 and 200 < m[1] < 400:
        p.draw.rect(r, (255, 0, 0), [300, 200, 200, 200])
    else:
        r.blit(Tplay.copy, Tplay.rect)
        Tplay.copy = p.transform.rotate(Tplay.text, FRAME)
        Tplay.rect.center = (FRAME, FRAME)
#endregion

running = True
while running:
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False
    
    FRAME += 1
    bg()
    buttons()
    p.display.update()
    t.sleep(.015625)
p.quit()