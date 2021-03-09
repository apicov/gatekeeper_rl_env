from gym.envs.registration import register

register(
    id='GatekeeperEnv-v0',
    entry_point='my_gym.envs.gatekeeper:GatekeeperEnv',
)
