import random
import connection as cn

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

def q_update(previous_state, action, state, rw, q_matrix, alpha, gamma):
    estimate_q = rw + gamma * (max(q_matrix[state]))
    q_value = q_matrix[previous_state][action] + alpha*(estimate_q - q_matrix[previous_state][action])
    return q_value

def main():
    # Faz a conexão com o jogo
    s = cn.connect(2037)
    q_matrix = txtFileToMatrix()
    actions=["left","right","jump"]

    # Estado inicial
    estado = 84 # o boneco está na plataforma 21 olhado para o norte

    alpha = 0.2 # Taxa de aprendizado
    gamma = 0.9 # Fator de desconto

    recompensa = -1
    
    while recompensa < 0:
        # Estado antes de aplicar a ação
        estado_anterior = estado
        
        selected_action = random.randint(0,2)
        estado, recompensa = cn.get_state_reward(s, actions[selected_action])

        # transforma o estado de binário para int
        estado = int(estado, 2)

        q_matrix[estado_anterior][selected_action] = q_update(estado_anterior, selected_action, estado, recompensa, q_matrix, alpha, gamma)
        print(estado,recompensa)
    print('CHEGOU AO OBJETIVO')


    
    # Salva o resultado do treinamento no arquivo resultado.txt
    matrixToTxtFile(q_matrix)

if __name__ == "__main__":
    main()
