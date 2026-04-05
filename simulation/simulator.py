from environment.study_env import StudyEnvironment
from agent.agent import Agent
import matplotlib.pyplot as plt

def run_simulation(steps=50):
    env = StudyEnvironment()
    agent = Agent()

    state = env.reset()
    total_reward = 0

    rewards = []  # store rewards for graph

    for step in range(steps):
        action = agent.choose_action(state)
        next_state, reward = env.step(action)

        agent.learn(state, action, reward, next_state)

        rewards.append(reward)

        print(f"Step {step}")
        print("State:", state)
        print("Action:", action)
        print("Reward:", reward)
        print("---------------")

        total_reward += reward
        state = next_state

    print("\nTotal Reward:", total_reward)

    # 📊 Plot graph
    plt.plot(rewards)
    plt.xlabel("Steps")
    plt.ylabel("Reward")
    plt.title("Learning Progress")
    plt.show()