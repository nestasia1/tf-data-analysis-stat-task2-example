import numpy as np
from scipy.stats import chi2


chat_id = 1022895883 # Ваш chat ID, не меняйте название переменной

def solution(p: float, r: np.array) -> tuple:
    alpha = 1 - p
    k = 33**0.5
    n = 2 * len(x)
    a = np.sum(np.square(r))

    left = (a / chi2.ppf(1 - alpha/2, n))**0.5 / k
    right = (a / chi2.ppf(alpha/2, n))**0.5 / k
    return left, right
