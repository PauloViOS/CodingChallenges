# A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

# For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

# Write a function:

# class Solution { public int solution(int N); }

# that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

# For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..2,147,483,647].


# minha primeira abordagem foi tentar guardar os índices dos números que não são 0, guardando-os em uma lista.
# Depois, bastaria fazer a subtração de cada número pelo número anterior para saber quantas casas havia de diferença entre eles.
# Devo ter demorado uns 5 minutos para fazer essa solução e, de início, fiquei feliz.
# Foi o primeiro código do ano e passou em todos os testes.
# Mas o fato de ter que iterar sobre duas listas não me agradou...

def solution(N):
    binary_N_str = bin(N)[2:]
    longest_gap = 0
    non_zero_idxs = []
    for idx, char in enumerate(binary_N_str):
        if char != '0':
            non_zero_idxs.append(idx)

    for index, idx in enumerate(non_zero_idxs[1:]):
        if idx - non_zero_idxs[index] - 1 > longest_gap:
            longest_gap = idx - non_zero_idxs[index] - 1

    return longest_gap

# Eu sabia que deveria haver uma solução que percorresse o número apenas uma vez, então quebrei a cabeça mais um pouco e cheguei à solução abaixo.
# Essa demorou muito menos, acho que fiz em 3 minutos. Percorreu a lista apenas uma vez e guardou se estávamos em um gap e o tamanho do gap atual, checando se ele era maior que o maior gap guardado.
# Apesar de haver mais linhas de código, a complexidade do código é menor, o que me deixou satisfeito


def solution_v2(N):
    longest_gap = 0
    current_gap = 0
    in_gap = False
    for idx, char in enumerate(bin(N)[2:]):
        if char != '0' and in_gap == True:
            if current_gap > longest_gap:
                longest_gap = current_gap
            in_gap = False
            current_gap = 0
        if char != '0':
            current_gap = 0
            in_gap = False
        elif char == '0':
            current_gap += 1
            in_gap = True
    return longest_gap


assert solution(1041) == 5
assert solution(32) == 0
