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
    self.slider = py_singl_slider.PySinglSlider(20, 20, 0, 100, 10)
    self.slider_init_value = py_singl_slider.PySinglSlider(20, 70, 0, 200, 15)
    self.slider_two = py_singl_slider.PySinglSlider(20, 120, 0, 150, 10, 'two')
    self.slider_custom_theme = py_singl_slider.PySinglSlider(20, 160, 0, 120, 10, 'one', 'assets/custom_theme')

    #font
    self.font = pygame.font.Font('assets/font/PixelSimpel.otf', 32)

  async def render(self):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            self.slider.listen_event(event)
            self.slider_init_value.listen_event(event)
            self.slider_two.listen_event(event)
            self.slider_custom_theme.listen_event(event)

        self.screen.fill((10, 220, 10))

        # bg to highlight the slider with theme 'one'
        pygame.draw.rect(self.screen, (123, 157, 243), (0, 0, self.screen.get_width(), 110))

        # default slider
        text = self.font.render("{0:.2f}".format( self.slider.value ), True, (10, 10, 100))
        slider_rect = self.slider.get_rect()
        self.screen.blit(text, (slider_rect.width + 32, slider_rect.y - 9))
        self.slider.render(self.screen)

        # slider with init value
        text_a = self.font.render("{0:.2f}".format( self.slider_init_value.value ), True, (10, 20, 200))
        slider_rect_init_value = self.slider_init_value.get_rect()
        self.screen.blit(text_a, (slider_rect_init_value.width + 32, slider_rect_init_value.y - 9))
        self.slider_init_value.render(self.screen)

        # slider two
        text_b = self.font.render("{0:.2f}".format( self.slider_two.value ), True, (10, 20, 200))
        slider_rect_two = self.slider_two.get_rect()
        self.screen.blit(text_b, (slider_rect_two.width + 32, slider_rect_two.y - 9))
        self.slider_two.render(self.screen)

        # slider with custom theme
        text_b = self.font.render("{0:.2f}".format( self.slider_custom_theme.value ), True, (10, 20, 200))
        slider_rect_custom_theme = self.slider_custom_theme.get_rect()
        self.screen.blit(text_b, (slider_rect_custom_theme.width + 32, slider_rect_custom_theme.y - 9))
        self.slider_custom_theme.render(self.screen)

        #update the display
        pygame.display.flip()
        # clock
        pygame.time.Clock().tick(60)
        await asyncio.sleep(0)
        
asyncio.run(App().render())