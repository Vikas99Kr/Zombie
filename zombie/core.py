import pygame
import pygame.event
import time


class ZombieSystem:
    @staticmethod
    def init():
        pygame.init()

    @staticmethod
    def quit():
        pygame.quit()


class Input:
    __maped = {
        "up": pygame.K_UP,
        "down": pygame.K_DOWN,
        "right": pygame.K_RIGHT,
        "left": pygame.K_LEFT,
        "a": pygame.K_a,
        "b": pygame.K_b,
        "c": pygame.K_c,
        "d": pygame.K_d,
        "e": pygame.K_e,
        "f": pygame.K_f,
        "g": pygame.K_g,
        "h": pygame.K_h,
        "i": pygame.K_i,
        "j": pygame.K_j,
        "k": pygame.K_k,
        "l": pygame.K_l,
        "m": pygame.K_m,
        "n": pygame.K_n,
        "o": pygame.K_o,
        "p": pygame.K_p,
        "q": pygame.K_p,
        "r": pygame.K_r,
        "s": pygame.K_s,
        "t": pygame.K_t,
        "u": pygame.K_u,
        "v": pygame.K_v,
        "w": pygame.K_w,
        "x": pygame.K_x,
        "y": pygame.K_y,
        "z": pygame.K_z,
        "shift": pygame.KMOD_SHIFT,
        "lshift": pygame.KMOD_LSHIFT,
        "rshift": pygame.KMOD_RSHIFT,
        "enter": pygame.K_RETURN,
        "nenter": pygame.K_KP_ENTER
    }

    @staticmethod
    def __translate(key: str):
        return Input.__maped.get(key)

    @staticmethod
    def get_key_down(key: str):
        lst = pygame.event.get(pygame.KEYDOWN)
        if lst:
            return lst[0].key == Input.__translate(key)

    @staticmethod
    def get_key_up(key: str):
        lst = pygame.event.get(pygame.KEYUP)
        if lst:
            return lst[0].key == Input.__translate(key)
        return False


class GameView:
    def __init__(self, width, height, title, icon=None, resizable=False):
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

    def run(self, callback):
        while True:
            if pygame.event.get(pygame.QUIT):
                return None
            callback(self.screen)
            pygame.display.update()
            time.sleep(1 / 120)
