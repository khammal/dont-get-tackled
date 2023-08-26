import random

import pygame

from src.components.defender_side import DefenderSide
from src.components.scoreboard import Scoreboard
from src.config import Config
from src.services.music_service import MusicService
from src.services.visualization_service import VisualizationService
from src.utils.tools import sine


class Defender(pygame.sprite.Sprite):
    def __init__(self, defender_side: DefenderSide):
        super().__init__()
        self.new_spd = random.uniform(6, 7)
        self.y = 0
        self.offset_x = 30
        self.x = sine(100.0, 1280, 20.0, self.offset_x)
        self.side = defender_side
        self.can_score = True

        self._load_defender()

    def reset(self):
        self.new_spd = random.uniform(6, 7)
        self.can_score = True

        if self.side == DefenderSide.RIGHT:
            self.offset_x = random.randint(220, 350)
            self.y = -40
            self.x = 0

        if self.side == DefenderSide.LEFT:
            self.offset_x = random.randint(30, 200)
            self.y = -320
            self.x = 0

    def _load_defender(self):
        if self.side == DefenderSide.RIGHT:
            self._load_right_def1()

        if self.side == DefenderSide.LEFT:
            self._load_left_def2()

        if self.side == DefenderSide.FIRST_EXTRA:
            self._load_right_def3()
            self.side = DefenderSide.RIGHT
        
        if self.side == DefenderSide.SECOND_EXTRA:
            self._load_left_def4()
            self.side = DefenderSide.LEFT

    def _load_right_def1(self):
        self.image = VisualizationService.get_def1_image()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.offset_x = random.randint(220, 350)
        self.y = -40

    def _load_left_def2(self):
        self.image = VisualizationService.get_def2_image()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.offset_x = random.randint(30, 200)
        self.y = -320

    def _load_right_def3(self):
        self.image = VisualizationService.get_def3_image()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.offset_x = random.randint(220, 350)
        self.y = -40

    def _load_left_def4(self):
        self.image = VisualizationService.get_def4_image()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.offset_x = random.randint(30, 200)
        self.y = -320

    def move(self, scoreboard: Scoreboard, player_position):
        self.x = sine(100.0, 620, 20.0, self.offset_x)
        self.y += self.new_spd
        self.rect.center = (self.x, self.y)

        if self.rect.top > player_position.y - 35 and self.can_score:
            scoreboard.increase_current_score()
            self.can_score = False

            MusicService.play_score_sound()


            if scoreboard.get_current_score() % 5 == 0:
                MusicService.play_cheer_sound()

        if self.rect.top > Config.HEIGHT:
            self.rect.bottom = 0
            self.new_spd = random.uniform(5, 8)

            if self.side == DefenderSide.RIGHT:
                self.offset_x = random.randint(220, 350)
                self.y = -40

            if self.side == DefenderSide.LEFT:
                self.offset_x = random.randint(30, 200)
                self.y = -320

            if self.new_spd >= 6:
                self.new_spd = 8
                MusicService.play_chop_sound()

            self.can_score = True

    def draw(self, screen):
        dotted_line = VisualizationService.get_dotted_line()
        screen.blit(dotted_line, (0, self.rect.y + 53))
        screen.blit(self.image, self.rect)
