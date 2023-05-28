from stable_baselines3 import A2C
import os
import time
from gymrecsys.envs.movielens_env import MovieLensEnv
from stable_baselines3.common.env_util import make_vec_env


start_time = time.time()
agent = "A2C"
models_dir = f"./models/{agent}-{int(time.time())}"
logdir = f"./logs/{agent}-{int(time.time())}"
 
if not os.path.exists(models_dir):
    os.makedirs(models_dir)

if not os.path.exists(logdir):
    os.makedirs(logdir)

n_envs = 8
env = make_vec_env(MovieLensEnv.id, n_envs=n_envs)
env.reset()

model = A2C('MlpPolicy', env, verbose=1, tensorboard_log= logdir)

TIMESTEPS = 10000
for i in range(1,2):

    model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name=agent)
    model.save(f"{models_dir}/{TIMESTEPS*i}")


env.close()

end_time = time.time()
elapsed_time = end_time - start_time

print(f'elapsed time: {elapsed_time}')
print(f'n_envs: {n_envs}')