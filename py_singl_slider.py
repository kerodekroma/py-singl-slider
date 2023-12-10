import pygame

class PySingleSlider:
    def __init__(self, x=0, y=0, min_value=0, max_value=100, initial_value=10):
        self.initial_value = 0
        self.min_value = min_value
        self.max_value = max_value
        # bar setup
        self.bar_width = max_value
        self.bar_height = 10
        self.bar_bg_color = (10, 10, 200)
        self.bar_x = 20
        self.bar_y = 20
        self.bar_rect = pygame.Rect(self.bar_x, self.bar_y, self.bar_width, self.bar_height)
        #handler setup
        self.handler_height = 10
        self.handler_width = 10
        self.handler_bg_color = (80, 80, 100)
        self.handler_active_bg_color = (80, 100, 100)
        self.handler_x = self.bar_x + initial_value
        self.handler_y = self.bar_y + ( ( self.bar_height // 2 ) - ( self.handler_height // 2 ) )
        self.handler_rect = pygame.Rect(self.handler_x, self.handler_y, self.handler_width, self.handler_height)
        self.is_handler_down = False

        self.value = self.get_current_value()
        print("VALUE", self.value)

    def listen_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.bar_rect.collidepoint(event.pos):
                self.is_handler_down = True
        if event.type == pygame.MOUSEBUTTONUP:
            self.is_handler_down = False
        if event.type == pygame.MOUSEMOTION and self.is_handler_down:
            pos_x = (event.pos[0] - self.bar_x)
            self.handler_rect.x = min(( self.bar_width + self.bar_x ) - self.handler_width, max(pos_x, self.bar_x))
            self.value = self.get_current_value()
            print("VALUE", self.value)
    
    def get_current_value(self):
        # calculating the value itself to show
        value_range = self.max_value - self.min_value
        handler_x_in_bar = self.handler_rect.x - self.bar_x
        value = (handler_x_in_bar * self.bar_width / value_range + self.min_value) - self.handler_width
        return round(value, 2)

    def render(self, screen):
        #bar
        pygame.draw.rect(screen, self.bar_bg_color, self.bar_rect)
        #handler
        handle_color = self.handler_active_bg_color if self.is_handler_down else self.handler_bg_color
        pygame.draw.rect(screen, handle_color, self.handler_rect)