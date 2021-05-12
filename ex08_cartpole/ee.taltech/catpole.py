import gym as gym
import numpy as np
import pprint
import random as r

env = gym.make('CartPole-v0')


min_angle_speed = -3
max_angle_speed = 4.1
min_angle = -0.25
max_angle = 0.31

angle_speed_step = 1
angle_step = 0.1

learning_rate = 0.1
discount = 0.95

training_map = {}


def play():
    gambling_rate = 100
    fill_q_table()
    for i_episode in range(200):

        observation = env.reset()  # x-koordinata, skorost, ugol, skorost izmeneniya ugla

        for t in range(200):
            env.render()

            random_number = r.randint(1, 100)
            max_value, action, flag = get_max_value_from_observation(observation)
            if flag or random_number <= gambling_rate:
                action = env.action_space.sample()

            next_observation, reward, done, info = env.step(action)

            if done:
                reward = -20  # simulatsioon lõppes enne 200 sammu, negatiivne tasu

            train_q_table(observation, next_observation, reward, action)

            observation = next_observation
            if done:
                print("Episode {} finished after {} timesteps".format(i_episode, t + 1))
                break
        if gambling_rate > 0:
            gambling_rate -= 1
    env.close()
    pprint.pprint(training_map)


def fill_q_table():
    for angle in np.arange(min_angle, max_angle, angle_step):
        angle = round(angle, 2)
        new_dict = {}
        for speed in np.arange(min_angle_speed, max_angle_speed, angle_speed_step):
            speed = round(speed, 2)
            new_dict[speed] = {0: 0,
                               1: 0}
        training_map[angle] = new_dict


# treeni siin Q-tabelit
#  Q[s,a] += learning_rate * (r + discount * estimated_reward - Q[s,a])
#  s: observation
#  a: action
#  r: reward
#  s': next_observation
#  a': parim action olekus s',
#      pead ise leidma Q tabelist suurima väärtuse
def train_q_table(current_observation, next_observation, reward, action):
    for key in training_map.keys():
        if current_observation[2] <= key:
            for key2 in training_map.get(key).keys():
                if current_observation[3] <= key2:
                    q = training_map[key][key2][action]
                    est_reward, action1, flag = get_max_value_from_observation(next_observation)
                    training_map[key][key2][action] += learning_rate * (reward + discount * est_reward - q)
                    return


def get_max_value_from_observation(next_observation):
    for key in training_map.keys():
        if next_observation[2] <= key:
            for key2 in training_map[key].keys():
                if next_observation[3] <= key2:
                    max_value = max(training_map[key][key2].values())
                    flag = training_map[key][key2][0] == 0 and training_map[key][key2][1] == 0
                    if max_value == training_map[key][key2][0]:
                        return max_value, 0, flag
                    else:
                        return max_value, 1, flag


if __name__ == '__main__':
    play()
