import pygame as p
import time as t

#region init
W, H = 800, 600

p.init()
r = p.display.set_mode((W, H), p.RESIZABLE)
p.display.set_caption('Game Hub')

F = p.font.Font('freesansbold.ttf', 48)
FRAME = 0
hoverOver = False
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
C = 0
c = 0
def bg():
    global C
    C = C + .125 if C < 32 else -C
    c = abs(int(C))
    for i in range(60):
        h = (c + i * 2) % 255
        p.draw.rect(r, (h, h + 32, h + 40),
                    [0, i * (H // 60), W, H])

def buttons():
    global hoverOver
    m = p.mouse.get_pos()
    x = (FRAME % (W - 120) if FRAME % (2 * (W - 240)) < (W - 120) else (W - 120) - FRAME % (W - 120))
    y = (FRAME % (H - 36) if FRAME % (2 * (H - 36)) < (H - 36) else (H - 36) - FRAME % (H - 36))
    if x < m[0] < x + 120 and y < m[1] < y + 36:
        hoverOver = True
        r.blit(Tplay.copy, Tplay.rect)
        Tplay.rect.center = (x + 60, y + 18)
    else:
        hoverOver = False
        r.blit(Tplay.copy, Tplay.rect)
        Tplay.rect.center = (x + 60, y + 18)
#endregion

running = True
while running:
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False

        elif event.type == p.MOUSEBUTTONUP:
            if hoverOver:
                print('go to play screen')
            else:
                ()
        
        elif event.type == p.VIDEORESIZE:
            W, H = r.get_width(), r.get_height()
    
    FRAME += 1
    bg()
    buttons()
    p.display.update()
    t.sleep(.015625)
p.quit()
