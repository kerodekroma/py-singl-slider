
# PySinglSlider

[![PyPI version](https://badge.fury.io/py/py-singl-slider.svg?version=latest)](https://badge.fury.io/py/py-singl-slider)

`PySinglSlider` is a customizable, simple single slider widget built with Pygame. Designed for quick setup and theming, it lets you add an interactive slider for Pygame applications that need fine-grained control over a value range.

## Features

- Easily customizable for different themes and styles.
- Supports adjustable value ranges.
- Includes event listening for smooth handling of slider interactions.
- Simple integration into any Pygame-based project.

## Installation

Install `PySinglSlider` via [PyPI](https://pypi.org/project/py-singl-slider):

```bash
pip install py_singl_slider
```

## Getting Started

### Importing and Setting Up the Slider

To integrate `PySinglSlider` into your Pygame project, follow these steps:

1.  Import `PySinglSlider` from `py_singl_slider` in your Pygame script. (see example down below)
2.  Initialize the slider with optional parameters such as position, value range, initial value, and theme settings.
3.  Handle events and render the slider in your game loop.

### Example Usage

Here's a basic example to get started:

```bash
import pygame
import py_singl_slider

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Create slider

slider = py_singl_slider.PySinglSlider(x=100, y=250, min_value=0, max_value=100, initial_value=50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Pass events to the slider
        slider.listen_event(event)

    # Clear the screen
    screen.fill((255, 255, 255))
    
    # Render the slider
    slider.render(screen)
    
    # Display the current slider value
    font = pygame.font.Font(None, 36)
    value_text = font.render(f"Value: {slider.value:.2f}", True, (0, 0, 0))
    screen.blit(value_text, (100, 400))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
```

### Parameters

-   `x` (int): X-coordinate for slider position.
-   `y` (int): Y-coordinate for slider position.
-   `min_value` (int): Minimum value of the slider range.
-   `max_value` (int): Maximum value of the slider range.
-   `initial_value` (int): Starting value of the slider.
-   `theme_name` (str): Name of the theme folder containing assets (images for handler, bar, etc.).
-   `theme_path` (str, optional): Custom path to the theme directory if assets are not located in the default theme folder.
## Documentation

### Methods

#### `load_image(image_name, theme_name, theme_folder_path=None)`

Loads an image from the specified theme directory.

#### `get_rect()`

Returns the Pygame rectangle (Rect) of the slider bar.

#### `listen_event(event)`

Listens to and handles mouse or touch events for updating the slider’s handler position.

#### `get_current_value()`

Calculates and returns the slider's current value based on handler position.

#### `render(screen)`

Renders the slider's components (bar, handler) on the specified screen.

## Asset Customization

To customize the slider's appearance, you can create new images for the slider's handler and bar components in a folder with your chosen `theme_name`. Place this folder in the `theme` directory or specify the path using `theme_path`.

## Example Theme Folder Structure

```bash
project_root/
├── theme/
│   ├── default_theme/
│   │   ├── handler.png
│   │   ├── bar_center.png
│   │   ├── bar_corner.png
│   └── custom_theme/
│       ├── handler.png
│       ├── bar_center.png
│       ├── bar_corner.png
└── main.py
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

Enjoy using `PySinglSlider`! Contributions, bug reports, and suggestions are welcome.