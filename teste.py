import connection as cn
import random

s = cn.connect(2037)

actions=["left","right","jump"]

# Estado inicial
estado = 0
recompensa = -1
# while recompensa < 0:
#     selected_action = random.choice(actions)
#     estado, recompensa = cn.get_state_reward(s, selected_action)
#     print(estado,recompensa)
#     print('estado: ',int(estado, 2))

estado, recompensa = cn.get_state_reward(s, "right")
estado = int(estado, 2)
print(estado, recompensa)

# for i in range(10):
#     sel = random.randint(0,2)
#     print(f'{sel}- {actions[sel]}')