from gym.envs.registration import register

register(
    id='BouncerEnv-v0',
    entry_point='my_gym.envs.bouncer:BouncerEnv',
)
