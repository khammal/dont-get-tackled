import sys
import time

import pygame

from src.components.game_status import GameStatus
from src.components.defender import Defender
from src.components.defender_side import DefenderSide
from src.components.player import Player
from src.components.scoreboard import Scoreboard
from src.global_state import GlobalState
from src.services.music_service import MusicService
from src.services.visualization_service import VisualizationService
from src.utils.tools import update_background_using_scroll, update_press_key, is_close_app_event

GlobalState.load_main_screen()
VisualizationService.load_main_game_displays()

scoreboard = Scoreboard()

# Sprite Setup
P1 = Player()
D1 = Defender(DefenderSide.RIGHT)
D2 = Defender(DefenderSide.LEFT)
D3 = Defender(DefenderSide.FIRST_EXTRA)
D4 = Defender(DefenderSide.SECOND_EXTRA)

# Sprite Groups
defenders = pygame.sprite.Group()
defenders.add(D1)
defenders.add(D2)
defenders.add(D3)
defenders.add(D4)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(D1)
all_sprites.add(D2)
all_sprites.add(D3)
all_sprites.add(D4)


def main_menu_phase():
    scoreboard.reset_current_score()

    events = pygame.event.get()

    for event in events:
        if is_close_app_event(event):
            GlobalState.GAME_STATE = GameStatus.GAME_END
            return

        if event.type == pygame.KEYDOWN:
            GlobalState.GAME_STATE = GameStatus.GAMEPLAY

    GlobalState.SCROLL = update_background_using_scroll(GlobalState.SCROLL)
    VisualizationService.draw_background_with_scroll(GlobalState.SCREEN, GlobalState.SCROLL)
    GlobalState.PRESS_Y = update_press_key(GlobalState.PRESS_Y)
    VisualizationService.draw_main_menu(GlobalState.SCREEN, scoreboard.get_max_score(), GlobalState.PRESS_Y)


def gameplay_phase():
    events = pygame.event.get()

    for event in events:
        if is_close_app_event(event):
            game_over()
            return

    P1.update()
    D1.move(scoreboard, P1.player_position)
    D2.move(scoreboard, P1.player_position)
    D3.move(scoreboard, P1.player_position)
    D4.move(scoreboard, P1.player_position)

    GlobalState.SCROLL = update_background_using_scroll(GlobalState.SCROLL)
    VisualizationService.draw_background_with_scroll(GlobalState.SCREEN, GlobalState.SCROLL)

    P1.draw(GlobalState.SCREEN)
    D1.draw(GlobalState.SCREEN)
    D2.draw(GlobalState.SCREEN)
    D3.draw(GlobalState.SCREEN)
    D4.draw(GlobalState.SCREEN)
    scoreboard.draw(GlobalState.SCREEN)

    if pygame.sprite.spritecollide(P1, defenders, False, pygame.sprite.collide_mask):
        scoreboard.update_max_score()
        MusicService.play_player_hit_sound()
        time.sleep(0.5)
        game_over()


def exit_game_phase():
    pygame.quit()
    sys.exit()


def game_over():
    P1.reset()
    D1.reset()
    D2.reset()
    D3.reset()
    D4.reset()
    GlobalState.GAME_STATE = GameStatus.MAIN_MENU
    time.sleep(0.5)
