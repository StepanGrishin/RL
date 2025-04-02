# **Задача RL: LunarLander-v2**
**1.1 Цель задачи**
* Целью задачи является обучение агента методике мягкой посадки летательного аппарата на поверхность некоторой рельефной планеты в определеннную зону. Данная задача является классической задачей из библиотеки OpenAI Gym.

**1.2 Почему RL подходит**

* Имеется набор возможных действий агента (включение двигателя летательного аппарата вправо,влево,вверх), успешная комбинация которых может привести нас к желаемому результату
* Имеется система ценностей агента: например, нахождение в зоне посадки ценнее, чем нахождение агента вне нее, а наклоны аппарата вправо или влево более чем на 20 градусов - штраф, так как возникает вероятность быстро улететь за зону посадки или вовсе потерять управление
* Среда имеет свои особенности, такие как гравитация, рельеф. Гравитация постоянно влияет на аппарат и заставляет его поддерживать себя на определенном уровне и не разбиться о землю
# **2. Структура среды**
**2.1 Состояния и действия**

**Действия:**
1. Отсутствие всякого действия - двигатели выключены и аппарат летит вниз
2. Газ вправо - движение вправо
3. Газ влево - движение влево
4. Центральный газ - движение вверх

**Состояния агента:**

1. x — Позиция по оси X 
2. y — Позиция по оси Y 
3. vx — Скорость по оси X 
4. vy — Скорость по оси Y
5. angle - угол наклона относительно вертикали
6. angular_velocity — Угловая скорость — скорость изменения угла наклона
7. left_contact — Булевое значение, которое указывает, есть ли контакт с землей или поверхностью слева.
8. right_contact — Булевое значение, которое указывает, есть ли контакт с землей или поверхностью справа.

**2.2 Награды**
1. Положительные баллы начисляются за нахождение в пределах зоны посадки, отсутствие сильного крена в одну из сторон, посадку с вертикальной скоростью не более Х ед/с.
2. Если аппарат разбился или улетел за зону посадки или сел вне зоны посадки - штраф. Посадка с высокой вертикальной скоростью- штраф, посадка на рельеф не под тем углом - штраф(?)
3. Оптимальное поведение определяется суммой баллов, полученных в результате определенной линии повдения

    import gym
   
    import numpy as np
   
    import matplotlib.pyplot as plt

    from pyvirtualdisplay import Display
   
    import gym

    env = gym.make("LunarLander-v2")


    state = env.reset()
   
    done = False

    epochs = 1000 
    total_reward = 0

    for _ in range(epochs):
        action = env.action_space.sample()  
        next_state, reward, done, info = env.step(action)  
        total_reward += reward
        env.render()
    
    if done:
        print(f"Game Over! Total Reward: {total_reward}")
        state = env.reset()
        total_reward = 0

    env.close()

# **3. Настройка среды**
pip install gym[box2d]

pip install pyvirtualdisplay

https://drive.google.com/file/d/1TZ9oOc28xtwUMfy9vRbcZ3sPBgwG5L2J/view?usp=sharing

https://drive.google.com/file/d/1s_LOjVvCP1_5cyYMqvKGNmHBmgKTfYrd/view?usp=sharing

# **4. Заключение**
Данная задача является интересной и прикладной задачей обучения с подкреплением. Данный алгоритм является прототипом к реальной задаче посадки летательного аппарата на землю. Был отработан и написан тестовый скрипт для данной задачи и в дальнейшем будут использованы различные методы обучения агента для достижения поставленных целей
