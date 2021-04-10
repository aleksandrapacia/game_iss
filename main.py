"""
Gra IssEscape.
"""

import pygame

from station import Station


class Game:
    """Ogólna klasa do zarządzania zasobami i sposobem działania gry."""

    def __init__(self):
        """Inicjalizacja gry i utworzenie jej zasobów."""
        pygame.init()
        self.screen = pygame.display.set_mode((1263, 655))
        pygame.display.set_caption("ISS - Escape")

        # Ładowanie tekstury tła.
        bg_file = open("earth.jpg")
        self.texture_bg = pygame.image.load(bg_file)

        # Ładowanie tekstury stacji.
        station_file = open("station.jpg")
        texture_station = pygame.image.load(station_file)

        # Utowrzenie obiektu klasy Stacja jako właściwość klasy Game.
        self.station = Station(300, 300, texture_station)

    def run_game(self):
        """run_game uruchamia główną pętlę gry."""

        while True:
            # Oczekiwanie na naciśnięcie klawisza lub przycisku myszy.
            all_events = pygame.event.get()
            for event in all_events:
                if event.type == pygame.QUIT:
                    exit()

            all_keys = pygame.key.get_pressed()
            if all_keys[pygame.K_LEFT]:
                self.station.pos_x -= 1
            elif all_keys[pygame.K_RIGHT]:
                self.station.pos_x += 1
            elif all_keys[pygame.K_UP]:
                self.station.pox_y += 1
            elif all_keys[pygame.K_DOWN]:
                self.station.pos_y -= 1

            # Wyświetlenie tła
            self.screen.blit(self.texture_bg, (0, 0))
            self.screen.blit(self.station.texture, (self.station.pos_x, self.station.pos_y))
            # Wyrenderowanie wszystkich zmian na ekranie.
            pygame.display.flip()


if __name__ == "__main__":
    mewa = Game()
    mewa.run_game()
