# A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

# Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

# The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

# In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

# For example, consider array A such that:

#   A[0] = 3
#   A[1] = 1
#   A[2] = 2
#   A[3] = 4
#   A[4] = 3
# We can split this tape in four places:

# P = 1, difference = |3 − 10| = 7
# P = 2, difference = |4 − 9| = 5
# P = 3, difference = |6 − 7| = 1
# P = 4, difference = |10 − 3| = 7
# Write a function:

# class Solution { public int solution(int[] A); }

# that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

# For example, given:

#   A[0] = 3
#   A[1] = 1
#   A[2] = 2
#   A[3] = 4
#   A[4] = 3
# the function should return 1, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [2..100,000];
# each element of array A is an integer within the range [−1,000..1,000].

################################################## Resolução ##################################################

# Primeira abordagem, fazer um a um e guardar as somas, retornando a menor
import math


def solution(A):
    min_diff = math.inf
    for pos in range(len(A)):
        diff = abs(sum(A[:pos]) - sum(A[pos:]))
        if diff < min_diff:
            min_diff = diff

    return min_diff

# Funcionou pro primeiro caso de teste, mas falhou em alguns outros e em todos os de performance...
# Uma outra abordagem...


def solution_v2(A):
    min_diff = math.inf
    right_sum = sum(A)
    left_sum = 0
    for num in A:
        right_sum -= num
        left_sum += num
        diff = abs(right_sum - left_sum)
        if diff < min_diff:
            min_diff = diff

    return min_diff

# Isso passa em todo os teste de performance! mas falha em 2 testes de exatidão :( Um dos casos em que falhou é o segundo caso de teste
# O erro me parece ser que não é pra ter uma divisão que seja apenas todos os números da esquerda. Vou tentar ver se é isso


def solution_v3(A):
    min_diff = math.inf
    right_sum = sum(A)
    left_sum = 0
    for num in A[:-1]:
        right_sum -= num
        left_sum += num
        diff = abs(right_sum - left_sum)
        if diff < min_diff:
            min_diff = diff

    return min_diff

# Perfeito! Passa em tudo e com uma complexidade de O(N). O problema da minha primeira abordagem é que eu não salvava as somas das duas partes,
# então tinha que passar pelo array todo de novo para fazer esse cálculo, o que fazia a complexidade ser O(N*N). Na v2 e v3 eu passo uma vez pelo array para somar
# tudo e depois outra para fazer as diffs, iterando apenas 2 vezes


assert solution_v3([3, 1, 2, 4, 3]) == 1
assert solution_v3([-1000, 1000]) == 2000
