import gym

env = gym.make("LunarLander-v2", render_mode="human")  # "human" для отображения в графическом окне

# Инициализация переменных
state = env.reset()
done = False

# Параметры
epochs = 1000 
total_reward = 0

# Запуск симуляции
for _ in range(epochs):
    action = env.action_space.sample()  # Случайное действие
    next_state, reward, done, _, info = env.step(action)  # Переход в новое состояние

    total_reward += reward

    env.render()

    if done:
        print(f"Game Over! Total Reward: {total_reward}")
        state = env.reset()
        total_reward = 0

env.close()
