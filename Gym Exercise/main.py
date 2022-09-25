import gym
import matplotlib as plt


def plot(x, figsize=(5, 4)):
    plt.figrure(figsize=figsize)


x = gym.make("CartPole-v1")

for episode in range(1, 151):
    score = 0
    state = x.reset()
    done = False

    while not done:
        img = x.render(mode="rgb_array")
        img.shape
        action = x.action_space.sample()
        # print(len(x.step(action)))
        n_state, reward, done, info, y = x.step(action)
        score += reward

    print("Episode:{},Score:{}".format(episode, score))

x.close()
