import random

import pygame

from paths import AUDIO_DIR


class MusicService:
    @staticmethod
    def get_background_musics():
        return AUDIO_DIR / "fun_background.mp3"

    @staticmethod
    def get_chop_musics():
        return [
            AUDIO_DIR / "chop.wav",
            AUDIO_DIR / "chop_2.wav",
            AUDIO_DIR / "chop_3.wav"
        ]

    @staticmethod
    def get_cheer_musics():
        return [
            AUDIO_DIR / "cheer.wav",
            AUDIO_DIR / "cheer_2.wav",
            AUDIO_DIR / "cheer_3.wav",
            AUDIO_DIR / "cheer_4.wav"
        ]

    @staticmethod
    def start_background_music():
        if pygame.mixer.music.get_busy():
            return

        filename = MusicService.get_background_musics()
        pygame.mixer.music.set_volume(0.1),
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

    @staticmethod
    def play_chop_sound():
        musics = MusicService.get_chop_musics()
        filename = random.choice(musics)
        chop = pygame.mixer.Sound(filename)
        pygame.mixer.Sound.play(chop)

    @staticmethod
    def play_score_sound():
        score_sfx = pygame.mixer.Sound(AUDIO_DIR / "score.wav")
        pygame.mixer.Sound.play(score_sfx)

    @staticmethod
    def play_stadium_cheer_sound():
        stadium_cheer = pygame.mixer.Sound(AUDIO_DIR / "stadium_cheer.mp3")
        pygame.mixer.Sound.play(stadium_cheer)

    @staticmethod
    def play_player_hit_sound():
        tackled_sfx = pygame.mixer.Sound(AUDIO_DIR / "player_hit.mp3")
        pygame.mixer.Sound.play(tackled_sfx)

    @staticmethod
    def play_cheer_sound():
        musics = MusicService.get_cheer_musics()
        filename = random.choice(musics)
        cheer = pygame.mixer.Sound(filename)
        pygame.mixer.Sound.play(cheer)
