import pygame

from paths import ASSETS_DIR, MENU_DIR
from src.config import Config
from src.utils.tools import sine


class VisualizationService:
    @staticmethod
    def get_def1_image():
        return pygame.image.load(ASSETS_DIR / "def_1.png").convert_alpha()

    @staticmethod
    def get_def2_image():
        return pygame.image.load(ASSETS_DIR / "def_2.png").convert_alpha()
    
    @staticmethod
    def get_def3_image():
        return pygame.image.load(ASSETS_DIR / "def_3.png").convert_alpha()

    @staticmethod
    def get_def4_image():
        return pygame.image.load(ASSETS_DIR / "def_4.png").convert_alpha()

    @staticmethod
    def get_player_image():
        return pygame.image.load(ASSETS_DIR / "dribble_forward.png").convert_alpha()

    @staticmethod
    def get_player_image_left():
        return pygame.image.load(ASSETS_DIR / "dribble_left.png").convert_alpha()

    @staticmethod
    def get_player_image_right():
        return pygame.image.load(ASSETS_DIR / "dribble_right.png").convert_alpha()
        
    @staticmethod
    def get_dotted_line():
        return pygame.image.load(ASSETS_DIR / "dotted_line.png").convert_alpha()

    @staticmethod
    def get_background_image():
        return pygame.image.load(ASSETS_DIR / "background.png").convert_alpha()

    @staticmethod
    def get_score_image():
        return pygame.image.load(ASSETS_DIR / "scoreboard.png").convert_alpha()

    @staticmethod
    def get_press_key_image():
        return pygame.image.load(MENU_DIR / "press_key.png").convert_alpha()

    @staticmethod
    def get_title_image():
        return pygame.image.load(MENU_DIR / "title.png").convert_alpha()

    @staticmethod
    def get_cover_player_image():
        return pygame.image.load(MENU_DIR / "cover_player.png").convert_alpha()

    @staticmethod
    def get_main_font():
        return pygame.font.Font(ASSETS_DIR / "BaiJamjuree-Bold.ttf", 40)

    @staticmethod
    def get_credit_font_font():
        return pygame.font.Font(ASSETS_DIR / "BaiJamjuree-Bold.ttf", 12)

    @staticmethod
    def get_score_font():
        return pygame.font.Font(ASSETS_DIR / "BaiJamjuree-Bold.ttf", 26)

    @staticmethod
    def load_main_game_displays():
        pygame.display.set_caption("Don't get tackled")
        player = VisualizationService.get_player_image()
        pygame.display.set_icon(player)

    @staticmethod
    def draw_background_with_scroll(screen, scroll):
        background = VisualizationService.get_background_image()
        screen.blit(background, (0, scroll))

    @staticmethod
    def draw_author_credits(screen):
        credit_font = VisualizationService.get_credit_font_font()
        author_credits = credit_font.render("By: Karam Hammal", True, (0, 0, 0))
        credits_rect = author_credits.get_rect(center=(Config.WIDTH // 2, 620))
        screen.blit(author_credits, credits_rect)

    @staticmethod
    def draw_best_score(screen, max_score):
        score_font = VisualizationService.get_score_font()
        best_score = score_font.render(f"Best: {max_score}", True, (250, 250, 250))
        best_score_rect = best_score.get_rect(center=(Config.WIDTH // 2, 270))
        screen.blit(best_score, best_score_rect)

    @staticmethod
    def draw_title(screen):
        y = sine(200.0, 1280, 10.0, 100)
        title = VisualizationService.get_title_image()
        screen.blit(title, (40, y))
        cover_player = VisualizationService.get_cover_player_image()
        screen.blit(cover_player, (145, sine(200.0, 1280, 10.0, 330)))

    @staticmethod
    def draw_press_key(screen, press_y):
        press_key = VisualizationService.get_press_key_image()
        screen.blit(press_key, (55, press_y + 20))

    @staticmethod
    def draw_main_menu(screen, max_score, press_y):
        VisualizationService.draw_author_credits(screen)
        VisualizationService.draw_best_score(screen, max_score)
        VisualizationService.draw_title(screen)
        VisualizationService.draw_press_key(screen, press_y)
