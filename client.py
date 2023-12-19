import random
import connection as cn
import numpy as np

def txtFileToMatrix():
    matrix = []
    f = open("resultado.txt", "r")
    lines = f.readlines()
    for line in lines:
        line = line.replace("\n", "").split()
        for i, el in enumerate(line):
            line[i] = float(el)
        matrix.append(line)
    return matrix

def matrixToTxtFile(matrix):
    f = open("resultado.txt", "w")
    for line in matrix:
        f.writelines(str(line[0])+' '+str(line[1])+' '+str(line[2])+'\n')

def q_update(previous_state, action, state, rw, q_matrix, alpha, gamma): # q-learning equation
    estimate_q = rw + gamma * (max(q_matrix[state]))
    q_value = q_matrix[previous_state][action] + alpha*(estimate_q - q_matrix[previous_state][action])
    return q_value

def escolha_acao(epislon, state): #epsilon greedy
    if np.random.uniform(0, 1) < epislon:
        acao = random.randint(0, 2)
    else:
        acao = np.argmax(state)
    return acao

def main():
    # Faz a conexão com o jogo
    s = cn.connect(2037)
    q_matrix = txtFileToMatrix()
    actions=["left","right","jump"]

    # Estado inicial
    estado = 84 # o boneco está na plataforma 21 olhado para o norte
    epislon = 0.1 # epsilon (taxa de aleatoriedade da ação)
    alpha = 0.1 # Taxa de aprendizado
    gamma = 0.9 # Fator de desconto

    recompensa = -1
    for i in range(100):
        recompensa = -1
        while recompensa < 0:
            # Estado antes de aplicar a ação
            estado_anterior = estado

            #escolha da ação a ser tomada
            selected_action = escolha_acao(epislon, q_matrix[estado_anterior])
            estado, recompensa = cn.get_state_reward(s, actions[selected_action])

            # transforma o estado de binário para int
            estado = int(estado, 2)

            #atualiza a recompensa na q-table
            q_matrix[estado_anterior][selected_action] = q_update(estado_anterior, selected_action, estado, recompensa, q_matrix, alpha, gamma)
            print(estado,recompensa)
        print('CHEGOU AO OBJETIVO')


    
    # Salva o resultado do treinamento no arquivo resultado.txt
    matrixToTxtFile(q_matrix)

if __name__ == "__main__":
    main()
