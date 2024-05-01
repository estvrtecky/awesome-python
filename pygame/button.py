import pygame


class Button:
    def __init__(self, x: int, y: int, width: int, height: int, image: pygame.Surface = None, text: str = "", font: pygame.font.Font = None) -> None:
        # Position and size
        self._x = x
        self._y = y
        self.width = width
        self.height = height

        # Text and font
        self.text = text
        self.font = font or pygame.font.Font(None, 30)

        self.image = self.create_image(image)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value: int) -> None:
        self._x = value
        self.rect.x = self.x

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, value: int) -> None:
        self._y = value
        self.rect.y = self.y

    @property
    def center(self) -> tuple:
        return self.rect.center

    @center.setter
    def center(self, value: tuple) -> None:
        self.rect.center = value
        self.x = self.rect.x
        self.y = self.rect.y

    def create_image(self, image: pygame.Surface):
        """Create the button's image."""
        if image:
            image = pygame.transform.scale(image, (self.width, self.height))
        else:
            image = pygame.Surface((self.width, self.height))
            image.fill((255, 255, 255))
        self.draw_text(image)
        return image

    def draw(self, surface: pygame.Surface) -> None:
        """Draw the button on the surface."""
        surface.blit(self.image, self.rect)

    def draw_text(self, surface: pygame.Surface) -> None:
        """Draw the text on the button."""
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.width // 2, self.height // 2)
        surface.blit(text_surface, text_rect)

    def move(self, dx: int, dy: int) -> None:
        """Moves the button by the given amounts."""
        self.x += dx
        self.y += dy

    def is_mouse_over(self, mouse_pos: tuple) -> bool:
        """Returns True if the mouse is over the button, False otherwise."""
        return self.rect.collidepoint(mouse_pos)