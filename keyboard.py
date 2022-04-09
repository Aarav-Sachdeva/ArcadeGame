import pygame
pygame.init()

x_loc=20
y_loc=20
x_speed=0
y_speed=0
done=False
clock=pygame.time.Clock()



WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)

siz=[500,400]
scree=pygame.display.set_mode(siz)

def draw_stick_figure(screen, x, y):
  pygame.draw.ellipse(screen, BLACK,[96-95+x,83-83+y,10,10],0)
  pygame.draw.line(screen, BLACK, [100-95+x,100-83+y],[105-95+x,110-83+y], 2)
  pygame.draw.line(screen, BLACK, [100-95+x,100-83+y],[95-95+x,110-83+y], 2)
  pygame.draw.line(screen, RED, [100-95+x,100-83+y], [100-95+x,90-83+y], 2)
  pygame.draw.line(screen, RED, [100-95+x,90-83+y], [104-95+x,100-83+y], 2)
  pygame.draw.line(screen, RED, [100-95+x,90-83+y], [96-95+x,100-83+y], 2)

while not done:
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      done=True
    if event.type==pygame.KEYDOWN:
      if event.key==pygame.K_LEFT:
        x_speed=-1
      if event.key==pygame.K_RIGHT:
        x_speed=1
      if event.key==pygame.K_DOWN:
        y_speed=1
      if event.key==pygame.K_UP:
        y_speed=-1

    if event.type==pygame.KEYUP:
      if event.key==pygame.K_LEFT:
        x_speed=0
      if event.key==pygame.K_RIGHT:
        x_speed=0
      if event.key==pygame.K_DOWN:
        y_speed=0
      if event.key==pygame.K_UP:
        y_speed=0 

  x_loc+=x_speed
  y_loc+=y_speed

  scree.fill(WHITE)
  draw_stick_figure(scree,x_loc,y_loc)
  pygame.display.flip()
  
clock.tick(60)

pygame.quit()
