"""
Gra IssEscape.
"""

import sys
import pygame


class Game:
    """Ogólna klasa do zarządzania zasobami i sposobem działania gry."""

    def __init__(self):
        """Inicjalizacja gry i utworzenie jej zasobów."""
        pygame.init()
        self.screen = pygame.display.set_mode((1263, 655))
        pygame.display.set_caption('ISS - Escape')
        bg_file = open('earth.jpg')
        self.bg_image = pygame.image.load(bg_file)

    def run_game(self):
        """run_game uruchamia główną pętlę gry."""

        while True:
            # Oczekiwanie na naciśnięcie klawisza lub przycisku myszy.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Wyświetlenie tła
            self.screen.blit(self.bg_image, (0, 0))
            # Wyrenderowanie wszystkich zmian na ekranie.
            pygame.display.flip()

if __name__ == '__main__':
    mewa = Game()
    mewa.run_game()
