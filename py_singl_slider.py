import pygame

class PySingleSlider:
    def __init__(self, x=0, y=0, min_value=0, max_value=150, initial_value=0):
        self.scale = 3
        self.initial_value = 0
        self.min_value = min_value
        self.max_value = max_value
        # bar setup
        self.bar_x = 20
        self.bar_y = 20
        self.bar_width = 0
        self.bar_height = 0
        #handler setup
        self.handler_active_bg_color = (80, 100, 100)
        self.is_handler_down = False
        self.setup_assets()
        self.value = self.get_current_value()

    def get_rect(self):
        return pygame.Rect(self.bar_x, self.bar_y, self.bg_bar_center.get_rect().width, self.bg_bar_center.get_rect().height)

    def setup_assets(self):
        # handler
        img_handler = pygame.image.load('assets/handler.png').convert_alpha()
        self.bg_handler = pygame.Surface((img_handler.get_width() * self.scale, img_handler.get_height() * self.scale))

        # handler rect
        self.handler_rect = self.bg_handler.get_rect()
        self.handler_rect.x = self.bar_x

        # scaling and blitting
        scaled = pygame.transform.scale(img_handler, (img_handler.get_width() * self.scale, img_handler.get_height() * self.scale))
        self.bg_handler.blit(scaled, (0, 0))
        self.bg_handler.set_colorkey((0, 0, 0))

        # bar center background
        self.bar_width = self.max_value * self.scale
        img_bar_center = pygame.image.load('assets/bar_center.png').convert_alpha()
        self.bg_bar_center = pygame.Surface((self.bar_width + self.handler_rect.width, img_bar_center.get_height() * self.scale)).convert_alpha()
        self.bar_height = img_bar_center.get_height() * self.scale

        # bar rect
        self.bar_rect = self.bg_bar_center.get_rect()
        self.bar_rect.width = self.bar_width + self.handler_rect.width
        self.bar_rect.x = self.bar_x
        self.bar_rect.y = self.bar_y

        for i in range(self.bar_rect.width):
            scaled = pygame.transform.scale(img_bar_center, (img_bar_center.get_width() * self.scale, img_bar_center.get_height() * self.scale)) 
            self.bg_bar_center.blit(scaled, (i, 0))

        # bar corners
        # LEFT
        img_bar_corner = pygame.image.load('assets/bar_corner.png').convert_alpha()
        self.bg_bar_corner = pygame.Surface((img_bar_corner.get_width() * self.scale, img_bar_corner.get_height() * self.scale)).convert_alpha()
        scaled = pygame.transform.scale(img_bar_corner, (img_bar_corner.get_width() * self.scale, img_bar_corner.get_height() * self.scale))
        self.bg_bar_corner.blit(scaled, (0, 0))
        self.bg_bar_corner.set_colorkey((0, 0, 0))

        # RIGHT
        self.bg_right_corner = pygame.transform.flip(self.bg_bar_corner, True, False)
        self.bg_right_corner.set_colorkey((0, 0, 0))
        
    def listen_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.bar_rect.collidepoint(event.pos):
                self.is_handler_down = True
        if event.type == pygame.MOUSEBUTTONUP:
            self.is_handler_down = False
        if event.type == pygame.MOUSEMOTION and self.is_handler_down:
            pos_x = (event.pos[0] - self.bar_x)
            self.handler_rect.x = min((self.bar_width + self.bar_x), max(pos_x, self.bar_x))
            print("X", self.handler_rect.x)
            self.value = self.get_current_value()
            print("VALUE", self.value)
    
    def get_current_value(self):
        # calculating the value itself to show
        handler_x_in_bar = self.handler_rect.x - self.bar_x
        reason = self.bar_rect.width / self.handler_rect.width
        value = ((handler_x_in_bar / reason) / self.scale) * reason 
        return abs(value)

    def render(self, screen):
        #bar
        #pygame.draw.rect(screen, self.bar_bg_color, self.bar_rect)
        screen.blit(self.bg_bar_corner, (self.bar_x - self.bg_bar_corner.get_width(), self.bar_y))
        screen.blit(self.bg_bar_center, self.bar_rect)
        screen.blit(self.bg_right_corner, ( self.bar_x + self.bar_rect.width, self.bar_y ))
        #handler
        screen.blit(self.bg_handler, (self.handler_rect.x, self.bar_y - ( self.handler_rect.height - self.bar_rect.height )//2))
        # handle_color = self.handler_active_bg_color if self.is_handler_down else self.handler_bg_color
        #pygame.draw.rect(screen, handle_color, self.handler_rect)
