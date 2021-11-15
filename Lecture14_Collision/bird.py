import random
from pico2d import *
import game_world
import game_framework

#Bird Flying Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
FLY_SPEED_KMPH = 40.0  # Km / Hour
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

#Bird Action Speed
BIRD_TIME_PER_ACTION = 0.5
BIRD_ACTION_PER_TIME = 1.0 / BIRD_TIME_PER_ACTION
BIRD_FRAMES_PER_ACTION = 8

class Bird:

    def __int__(self):
        self.x = random.randint(24, 1600-24)
        self.y = 450
        self.image = load_image('bird100x100x14.png')
        self.speed = 0
        self.frame = 0

        def do(self):
            # fill here
            self.frame = (self.frame + BIRD_FRAMES_PER_ACTION * BIRD_ACTION_PER_TIME * game_framework.frame_time) % 14
            self.x = clamp(25, self.x, 1600 - 25)

        @staticmethod
        def draw(self):
            self.image.clip_draw(int(self.frame) * 100, 100, 100, 100, self.x, self.y)

        def update(self):
            self.x += FLY_SPEED_PPS * game_framework.frame_time

            if self.x < 25 or self.x > 1600 - 25:
                game_world.remove_object(self)