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

def main():
    # Faz a conexão com o jogo
    s = cn.connect(2037)
    
    estado, recompensa = cn.get_state_reward(s, "jump")
    print(estado,recompensa)

    actions=["left","right","jump"]
    selected_action = random.choice(actions)
    print(selected_action)
    
    q_matrix = txtFileToMatrix()

    # Salva o resultado do treinamento no arquivo resultado.txt
    matrixToTxtFile(q_matrix)

if __name__ == "__main__":
    main()
