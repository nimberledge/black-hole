import pygame, colour as col, board

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((720, 480))
pygame.display.set_caption("Black Hole Lmao")
done = False
screencol = col.BLACK

def toggle_col(screencol):
    if screencol == col.BLACK:
        return col.WHITE
    else:
        return col.BLACK

while not done:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            done = True
            continue
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mpos = pygame.mouse.get_pos()
            screencol = toggle_col(screencol)
            print mpos

    
    screen.fill(screencol)
    pygame.display.flip()
pygame.quit()
