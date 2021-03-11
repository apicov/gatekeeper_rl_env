import numpy as np
#from PIL import Image
import gym
from gym import error, spaces, utils
from gym.utils import seeding
import random

#import glob
#import re

MAP = ["--.G","---.","-++-","----"]

LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3

GATEKEEPER_TYPES = ['L','D','R','U']

CELL_IMAGES = {"-":np.array([[255,255],[255,255]]), "L":np.array([[0,255],[0,255]]), "D":np.array([[255,255],[0,0]]), "R":np.array([[255,0],[255,0]]), "U":np.array([[0,0],[255,255]]),   }

class GatekeeperEnv(gym.Env):
    def __init__(self):#, params):
        super(GatekeeperEnv, self).__init__()

        self.max_steps = 100

        self.action_space = spaces.Discrete(4)
        self.position_ob_space  =  spaces.Discrete(16)
        self.im_ob_space = spaces.Box(low=0, high=255, shape=(2,2))#, dtype=np.uint8)
        self.observation_space = spaces.Tuple((self.im_ob_space, self.position_ob_space))

        self.reset()

        
    
    def reset(self):
        self.curr_loc = [3,1] #staring position
        self.map = np.asarray(MAP, dtype='c')
        self.insert_rnd_gatekeepers() #select randomly two gatekeepers from 4 possible types

        return ( CELL_IMAGES['-'] , self.vec2n(self.curr_loc))
     
    def step(self, action):
        return 0, 0, 0, {}

    def render(self, mode='human', close=False):
        # Render the environment to the screen
        return 0


    def insert_rnd_gatekeepers(self):
        gk = random.sample(GATEKEEPER_TYPES, 2)
        self.map[0,2] = gk[0]
        self.map[1,3] = gk[1]

    def vec2n(vec):
        return vec[0]*self.maps.shape[1] + vec[1]

    def inc(self,row, col, a):
        if a == LEFT:
            ncol = max(col - 1, 0)
        elif a == DOWN:
            nrow = min(row + 1, self.map.shape[0] - 1)
        elif a == RIGHT:
            ncol = min(col + 1, self.map.shape[1] - 1)
        elif a == UP:
            nrow = max(row - 1, 0)
        
        #if agent moves over a block, return to previous position
        if self.map[nrow,ncol] == '+':
            return (row,col)
        return (nrow, ncol)
