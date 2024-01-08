# A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.

# You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.

# The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.

# For example, you are given integer X = 5 and array A such that:

#   A[0] = 1
#   A[1] = 3
#   A[2] = 1
#   A[3] = 4
#   A[4] = 2
#   A[5] = 3
#   A[6] = 5
#   A[7] = 4
# In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.

# Write a function:

# class Solution { public int solution(int X, int[] A); }

# that, given a non-empty array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.

# If the frog is never able to jump to the other side of the river, the function should return −1.

# For example, given X = 5 and array A such that:

#   A[0] = 1
#   A[1] = 3
#   A[2] = 1
#   A[3] = 4
#   A[4] = 2
#   A[5] = 3
#   A[6] = 5
#   A[7] = 4
# the function should return 6, as explained above.

# Write an efficient algorithm for the following assumptions:

# N and X are integers within the range [1..100,000];
# each element of array A is an integer within the range [1..X].

################################################## Resolução ##################################################

# Tenho que pensar em uma maneira efetiva de guardar os elementos pelos quais passei e se estão todos em ordem
# Como uma primeira solução, creio que vou fazer um dicionário com chaves como os números de 1 a X-1 e depois passo pelo array
# dizendo se os números já apareceram
def solution(X, A):
    positions = {x: False for x in range(1, X+1)}
    for idx, pos in enumerate(A):
        positions[pos] = True
        if all(value == True for value in positions.values()):
            return idx


# Isso passa no teste base do Codility. Vamos ver com os testes de verdade...
# Não tinha lido o enunciado corretamente: há a possibilidade de o sapo não conseguir chegar ao outro lado.
# Um exemplo disso é o segundo caso de teste. Tenho que ajustar para essa possibilidade. Acho que um simples return fora do for resolve


def solution_v2(X, A):
    positions = {x: False for x in range(1, X+1)}
    for idx, pos in enumerate(A):
        positions[pos] = True
        if all(value == True for value in positions.values()):
            return idx
    return -1

# Bom, os testes de exatidão passam :) Mas não passou nenhum de performance (esperado). Vamos às otimizações!
# O que me parece mais crítico é ter que avaliar todos os valores do dicionário em todas as iterações...
# Para sanar esse problema, vou separar o código dentro do loor em 2 ifs: um para verificar se o valor da posição é False
# (e, caso seja, mudar para True e incrementar o valor de values em 1) e outro para verificar se values tem o
# mesmo valor de X (se sim, todos os valores no range foram encontrados)


def solution_v2(X, A):
    positions = {x: False for x in range(1, X+1)}
    values = 0
    for idx, pos in enumerate(A):
        if positions[pos] == False:
            positions[pos] = True
            values += 1
        if values == X:
            return idx
    return -1


# Funciona e passa por Todos os testes, inclusive os de performance. É isso por hoje :)


assert solution_v2(5, [1, 3, 1, 4, 2, 3, 5, 4]) == 6
assert solution_v2(5, [3]) == -1
