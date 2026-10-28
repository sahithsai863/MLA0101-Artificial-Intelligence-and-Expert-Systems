import math
def alpha_beta(depth, node_index, is_max, scores, alpha, beta, max_depth):
    if depth == max_depth:
        return scores[node_index]
    if is_max:
        best = -math.inf
        for i in range(2):
            value = alpha_beta(depth + 1,
                               node_index * 2 + i,
                               False,
                               scores,
                               alpha,
                               beta,
                               max_depth)
            best = max(best, value)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = math.inf
        for i in range(2):
            value = alpha_beta(depth + 1,
                               node_index * 2 + i,
                               True,
                               scores,
                               alpha,
                               beta,
                               max_depth)
            best = min(best, value)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best
scores = [3, 5, 6, 9, 1, 2, 0, -1]
max_depth = 3
best_score = alpha_beta(0, 0, True, scores, -math.inf, math.inf, max_depth)
print("Leaf Node Scores:", scores)
print("Best Score:", best_score)
