import pygame
import os

def load_image(image_name, theme_name, theme_folder_path=None):
    """Helper function to load an image from the assets directory."""
    image_path = os.path.join(os.path.dirname(__file__), f'theme/{theme_name}', image_name)
    if theme_folder_path != None:
        image_path = f'{theme_folder_path}/{theme_name}/{image_name}'
    return pygame.image.load(image_path).convert_alpha()

class PySinglSlider:
    """
    A customizable single slider component in Pygame.

    Attributes:
        scale (int): Scaling factor for assets.
        initial_value (int): Initial slider value.
        min_value (int): Minimum slider value.
        max_value (int): Maximum slider value.
        bar_x (int): X position of the bar.
        bar_y (int): Y position of the bar.
        bar_width (int): Width of the bar.
        bar_height (int): Height of the bar.
        handler_active_bg_color (tuple): Color when handler is active.
        is_handler_down (bool): Indicates if the handler is currently being dragged.
        value (int): Current value of the slider.
    """
    def __init__(self, x=0, y=0, min_value=0, max_value=150, initial_value=0, theme_name= 'one', theme_path=None):
        """
        Initialize the PySinglSlider with position, range, and theme.

        Args:
            x (int): X position of the slider bar.
            y (int): Y position of the slider bar.
            min_value (int): Minimum value of the slider.
            max_value (int): Maximum value of the slider.
            initial_value (int): Initial value of the slider.
            theme_name (str): Theme to be applied for the slider's assets.
            theme_path (str, optional): Custom theme directory path.
        """
        self.scale = 2
        self.initial_value = initial_value
        self.min_value = min_value
        self.max_value = max_value
        # bar setup
        self.bar_x = x
        self.bar_y = y
        self.bar_width = 0
        self.bar_height = 0
        #handler setup
        self.handler_active_bg_color = (80, 100, 100)
        self.is_handler_down = False
        self.setup_assets(theme_path, theme_name)
        self.value = self.get_current_value()

    def get_rect(self):
        """
        Get the slider's bounding rectangle.

        Returns:
            pygame.Rect: Rectangle representing the slider's bounding box.
        """
        return pygame.Rect(self.bar_x, self.bar_y, self.bg_bar_center.get_rect().width, self.bg_bar_center.get_rect().height)

    def setup_assets(self, theme_folder_path=None, theme_name='one'):
        """
        Load and set up the slider's assets based on the theme.

        Args:
            theme_folder_path (str, optional): Path to the theme folder.
            theme_name (str): Name of the theme to use.
        """
        # handler
        img_handler = load_image('handler.png', theme_name, theme_folder_path)
        self.bg_handler = pygame.Surface((img_handler.get_width() * self.scale, img_handler.get_height() * self.scale))

        # handler rect
        self.handler_rect = self.bg_handler.get_rect()
        self.handler_rect.x = self.bar_x + ( self.initial_value * self.scale )

        # scaling and blitting
        scaled = pygame.transform.scale(img_handler, (img_handler.get_width() * self.scale, img_handler.get_height() * self.scale))
        self.bg_handler.blit(scaled, (0, 0))
        self.bg_handler.set_colorkey((0, 0, 0))

        # bar center background
        self.bar_width = self.max_value * self.scale
        img_bar_center = load_image('bar_center.png', theme_name, theme_folder_path)
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
        img_bar_corner = load_image('bar_corner.png', theme_name, theme_folder_path)
        self.bg_bar_corner = pygame.Surface((img_bar_corner.get_width() * self.scale, img_bar_corner.get_height() * self.scale)).convert_alpha()
        scaled = pygame.transform.scale(img_bar_corner, (img_bar_corner.get_width() * self.scale, img_bar_corner.get_height() * self.scale))
        self.bg_bar_corner.blit(scaled, (0, 0))
        self.bg_bar_corner.set_colorkey((0, 0, 0))

        # RIGHT
        self.bg_right_corner = pygame.transform.flip(self.bg_bar_corner, True, False)
        self.bg_right_corner.set_colorkey((0, 0, 0))
        
    def listen_event(self, event):
        """
        Handle user input to control the slider.

        Args:
            event (pygame.event.Event): The event to handle, such as mouse or finger events.
        """
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.FINGERDOWN:
            if self.bar_rect.collidepoint(mouse_pos) or self.handler_rect.collidepoint(mouse_pos):
                self.is_handler_down = True

        if event.type == pygame.MOUSEBUTTONUP or event.type == pygame.FINGERUP:
            self.is_handler_down = False

        if self.is_handler_down:
            pos_x = mouse_pos[0]
            self.handler_rect.x = min((self.bar_width + self.bar_x), max(pos_x, self.bar_x))
            self.value = self.get_current_value()

        if (event.type == pygame.MOUSEMOTION or event.type == pygame.FINGERMOTION) and self.is_handler_down:
            pos_x = (mouse_pos[0] - self.bar_x)
            self.handler_rect.x = min((self.bar_width + self.bar_x), max(pos_x, self.bar_x))
            self.value = self.get_current_value()
    
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