import numpy as np
#from PIL import Image
import gym
from gym import error, spaces, utils
from gym.utils import seeding
#import glob
#import re

class BouncerEnv(gym.Env):
    def __init__(self):#, params):
        super(BouncerEnv, self).__init__()
   
    def reset(self):
        return 0
    
    def step(self, action):
        return 0, 0, 0, {}

    def render(self, mode='human', close=False):
        # Render the environment to the screen
        return 0

