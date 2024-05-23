import pygame

class Button:
    def __init__(self, text, font, color, hover_color, position):
        self.text = text
        self.font = font
        self.color = color
        self.hover_color = hover_color
        self.position = position
        self.rect = self.create_rect()
        self.hovered = False

    def create_rect(self):
        text_surface = self.font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect()
        button_rect = pygame.Rect(self.position[0], self.position[1], text_rect.width + 20, text_rect.height + 10)
        text_rect.center = button_rect.center
        return button_rect
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.hover_color if self.hovered else self.color, self.rect)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        surface.blit(text_surface, text_surface.get_rect(center=self.rect.center))

    def is_mouse_over(self, pos):
        return self.rect.collidepoint(pos)
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.is_mouse_over(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.hovered:
                return True
        return False
