from . import ppo
import gym
from gym.envs.registration import registry


def register(id, *args, **kvargs):
    if id in registry.env_specs:
        return
    else:
        return gym.envs.registration.register(id, *args, **kvargs)


def getList():
    btenvs = ['- ' + spec.id for spec in gym.envs.registry.all() if spec.id.find('Bullet') >= 0]
    return btenvs


register(
    id='Rex-v0',
    entry_point='envs.rex_reactive_env:RexReactiveEnv',
    max_episode_steps=1000,
    reward_threshold=5.0,
)
