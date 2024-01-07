# A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.

# Count the minimal number of jumps that the small frog must perform to reach its target.

# Write a function:

# def solution(X, Y, D)

# that, given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.

# For example, given:

#   X = 10
#   Y = 85
#   D = 30
# the function should return 3, because the frog will be positioned as follows:

# after the first jump, at position 10 + 30 = 40
# after the second jump, at position 10 + 30 + 30 = 70
# after the third jump, at position 10 + 30 + 30 + 30 = 100
# Write an efficient algorithm for the following assumptions:

# X, Y and D are integers within the range [1..1,000,000,000];
# X ≤ Y.

################################################## Resolução ##################################################

# A resolução que me parece mais simples é fazer um loop somando a distância pulada à posição atual enquanto ela for
# menor que a posição desejada e guardar quantas vezes isso foi feito.

def solution(X, Y, D):
    num_jumps = 0
    while X < Y:
        x += D
        num_jumps += 1
    return num_jumps

# Essa solução passou em todos os testes em que se avaliou se a resposta estava correta, mas
# falhou em todos os testes de performance :(
# Uma solução mais rápida parece ser fazer Y - X e dividir o resultado por D. O valor resultante será o número de pulos necessários.
# Temos que avaliar se o resultado da divisão é um decimal. Em caso positivo, retornamos o próximo inteiro


def solution_v2(X, Y, D):
    distance_to_jump = (Y - X)
    num_jumps = distance_to_jump // D
    if distance_to_jump % D != 0:
        num_jumps += 1
    return num_jumps


# Isso passa em todos os testes :)
# Complexidade do código: O(1)

assert solution_v2(10, 85, 30) == 3
