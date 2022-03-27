import numpy as np


def pigeonhole_check(p):
    p_n = len(p)

    for i in range(p_n):

        m = 0

        for j in p:

            if j > p_n:
                return False

            if j >= p_n - i:
                m = m + 1

        if m > i + 1:
            return False

    return True


def get_outcome(p):
    if not pigeonhole_check(p):
        return "This is not a valid parking function"
    displacement = 0
    func_pi = p.copy()

    pi_length = len(func_pi)

    outcome = np.zeros((pi_length,), dtype=int)
    available = np.zeros((pi_length,), dtype=int)

    for i in range(len(func_pi)):

        preferred = func_pi[i]

        for j in range(preferred - 1, len(func_pi)):

            if available[j] == 0:
                outcome[i] = j + 1
                available[j] = 1
                break
            displacement = displacement + 1

    convert_arr = [str(element) for element in outcome]
    outcome_str = ", ".join(convert_arr)
    outcome_str = f"[{outcome_str}]"
    out_dis = [outcome_str, displacement]
    return out_dis
