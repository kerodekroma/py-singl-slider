import asyncio
import pygame
import py_singl_slider
import sys

WIDTH, HEIGHT = 800, 600

class App:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Demo of PySinglSlider")
    self.slider = py_singl_slider.PySingleSlider(20, 20)

    #font
    self.font = pygame.font.Font(None, 38)

  async def render(self):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            self.slider.listen_event(event)

        self.screen.fill((10, 220, 10))
        text = self.font.render("{0:.2f}".format( self.slider.value ), True, (10, 10, 200))
        slider_rect = self.slider.get_rect()
        self.screen.blit(text, (slider_rect.width + 32, slider_rect.y - 9))
        self.slider.render(self.screen)
        #update the display
        pygame.display.flip()
        # clock
        pygame.time.Clock().tick(60)
        await asyncio.sleep(0)
        
asyncio.run(App().render())