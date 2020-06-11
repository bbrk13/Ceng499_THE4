import numpy as np


def forward(A, B, pi, O):
    """
    :param A: state transition matrix (NxN)
    :param B: observation probability matrix (NxM)
    :param pi: initial state probabilities (N)
    :param O: observation sequence (T)

            2 <= N <= 10
            2 <= M <= 10
            1 <= T <= 30

            N is the number of states
            M is the number of possible observations
            T is the length of the observation sequence

            A[i][j] is the transition probability from state i to state j
            B[i][j] is the probability of observing observation j in state i
            pi[i] is the probability of initial state is being state i
            O[k] is the k-th observation, which is an index between 0 and M-1 (inclusive)

    :return: given the model(A, B, pi), probability of the observation sequence
    """
    return 0


def viterbi(A, B, pi, O):
    """
    :param A: state transition matrix (NxN)
    :param B: observation probability matrix (NxM)
    :param pi: initial state probabilities (N)
    :param O: observation sequence (T)

            2 <= N <= 10
            2 <= M <= 10
            1 <= T <= 30

            N is the number of states
            M is the number of possible observations
            T is the length of the observation sequence

            A[i][j] is the transition probability from state i to state j
            B[i][j] is the probability of observing observation j in state i
            pi[i] is the probability of initial state is being state i
            O[k] is the k-th observation, which is an index between 0 and M-1 (inclusive)

    :return: given the model(A, B, pi) and observation sequence O, the most likely state sequence.
             It should be a NumPy array with size T. It includes state indices according to A's indices.
             For example: [1, 2, 1, 1, 0, 4]
    """
    return np.zeros((O.shape[0],))