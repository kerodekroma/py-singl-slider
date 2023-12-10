import pygame
import py_singl_slider
import sys

WIDTH, HEIGHT = 800, 600

class App:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Demo of PySinglSlider")
    self.slider = py_singl_slider.PySingleSlider(20, 30, 10, 150)
    #font
    self.font = pygame.font.Font(None, 38)

  def render(self):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            self.slider.listen_event(event)

        self.screen.fill((120, 120, 120))
        text = self.font.render("{0:.2f}".format( self.slider.value ), True, (10, 10, 200))
        self.screen.blit(text, (self.slider.bar_width + 32, self.slider.bar_y - 9))
        self.slider.render(self.screen)
        #update the display
        pygame.display.flip()
        # clock
        pygame.time.Clock().tick(60)
        

App().render()