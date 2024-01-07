# An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

# Your goal is to find that missing element.

# Write a function:

# def solution(A)

# that, given an array A, returns the value of the missing element.

# For example, given array A such that:

#   A[0] = 2
#   A[1] = 3
#   A[2] = 1
#   A[3] = 5
# the function should return 4, as it is the missing element.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..100,000];
# the elements of A are all distinct;
# each element of array A is an integer within the range [1..(N + 1)].


# Me parece que podemos iterar sobre o array fazendo de 1 a N+1. Se o valor da iteração não for encontrado, retornamos ele.

def solution(A):
    for num in range(1, len(A)+2):
        if num not in A:
            return num

# Essa solução de fato funciona. Passa por todos os testes de exatidão, mas falha nos de performance, pois é O(N**2)
# Fiz um teste e transformar A num set não melhora muito a situação...
# Depois de pensar uns 5 minutos, creio ter chegado em uma solução:
# Dado um tamanho de array, os nũmeros que deveriam estar dentro dele são fixos e, portanto, a soma deles também é.
# Se eu somar todos os números do array e fazer essa soma menos a soma esperada do array, encontrarei uma diferença.
# O tamanho do array menos essa diferença será o valor faltante no array! (Creio que ficará mais claro com matemática)


def solution_v2(A):
    expected_sum = (1 + len(A)) * len(A)//2
    actual_sum = sum(A)
    diff = actual_sum - expected_sum
    missing_num = len(A) + 1 - diff
    return missing_num

# Essa solução passa em todos os testes. Melhoramos a performance para O(N) ou O(N*log(N))


assert solution([2, 3, 1, 5]) == 4
