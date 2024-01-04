# An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).

# The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

# Write a function:

# def solution(A, K)

# that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.

# For example, given

#     A = [3, 8, 9, 7, 6]
#     K = 3
# the function should return [9, 7, 6, 3, 8]. Three rotations were made:

#     [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
#     [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
#     [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
# For another example, given

#     A = [0, 0, 0]
#     K = 1
# the function should return [0, 0, 0]

# Given

#     A = [1, 2, 3, 4]
#     K = 4
# the function should return [1, 2, 3, 4]

# Assume that:

# N and K are integers within the range [0..100];
# each element of array A is an integer within the range [−1,000..1,000].
# In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.

################################################## Resolução ##################################################

# A primeira coisa que me vem a mente é fazer uma função que rotaciona o array uma vez e fazer a função principal chamá-la K vezes
def rotate_array(arr):
    return arr[-1:] + arr[:-1]


def solution(A, K):
    for _ in range(1, K+1):
        A = rotate_array(A)
    return A


# Pensei que a segunda função ficaria maior... Como é uma linha, posso só jogar ela dentro do for que não vai ficar complicado de entender

def solution_v2(A, K):
    for _ in range(1, K+1):
        A = A[-1:] + A[:-1]
    return A

# Me parece que deve haver um jeito de achar a solução sem ter que fazer TODAS as rotações....
# Explorar a relação entre a quantidade de rotações e o tamanho do array deve ser a solução. Acho que dá pra fazer apenas UMA modificação no array, de acordo com essa relação.

# Se eu fizer um número de rotações que seja igual ao tamanho do array ou que seja um múltiplo dele, o array fica igual (isso visível no terceiro assert, que é um exemplo dado pelo codility)
# Se eu fizer um número de rotações que seja um múltiplo do tamanho do array +1, preciso fazer uma rotação, e esse padrão fica visível para múltiplo do array +2, +3, +4...
# Assim, cheguei em uma solução em que precisamos fazer, no máximo, len(A) - 1 rotações
# Se quiser, copie a função abaixo, descomente o print e brinque com os valores de rotações pedidas nos asserts, adicionando um múltiplo do tamanho do array ao número de rotações.
# Você perceberá que rotation_quantity não se altera


def solution_v3(A, K):
    rotation_quantity = K % len(A)
    # print(rotation_quantity)
    for _ in range(rotation_quantity):
        A = A[-1:] + A[:-1]
    return A


# Isso já melhorou MUITO a performance do código, mas ainda não estou contente. A melhora visava diminuir o número de rotações necessárias se a quantidade de rotações pedidas for grande,
# mas para um array suficientemente grande, a quantidade de rotações necessárias ainda será tão grande quanto.
# Como dito, quero chegar em uma solução que necessite apenas de UMA modificação no array, independente dos parâmetros dados.

# Agora que limitamos a quantidade de rotações necessárias, podemos prever onde cada número irá ficar depois que elas foram realizadas. Pegando o array do primeiro assert como exemplo:
# último dígito (6), após as 3 rotações pedidas, ficará na posição 2 e o terceiro dígito (9), ficará na posição 0
# Se eu tivesse um array [1, 2, 3, 4, 5, 6, 7] e fossem necessárias 5 rotações, o 7 ficaria na posição 4 e o 3 na posição 0 -> [3, 4, 5, 6, 7, 1, 2]
# Como no pyhton podemos nos referir aos valores de um array usando índices negativos, me parece que podemos fazer array[-rotation_quantity:] + array[:-rotation_quantity]

def solution_v4(A, K):
    rotation_quantity = K % len(A)
    A = A[-rotation_quantity:] + A[:-rotation_quantity]
    return A

# E de fato funciona! Com essa solkução eu fico feliz :) Bora pro próximo


assert solution_v4([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8]
assert solution_v4([0, 0, 0], 1) == [0, 0, 0]
assert solution_v4([1, 2, 3, 4], 4) == [1, 2, 3, 4]
