def minimax(depth, node_index, is_maximizing, scores, max_depth):
    if depth == max_depth:
        return scores[node_index]
    if is_maximizing:
        left = minimax(depth + 1, node_index * 2, False, scores, max_depth)
        right = minimax(depth + 1, node_index * 2 + 1, False, scores, max_depth)
        return max(left, right)
    else:
        left = minimax(depth + 1, node_index * 2, True, scores, max_depth)
        right = minimax(depth + 1, node_index * 2 + 1, True, scores, max_depth)
        return min(left, right)
scores = [3, 5, 2, 9, 12, 5, 23, 23]
max_depth = 3
best_score = minimax(0, 0, True, scores, max_depth)
print("Leaf Node Scores:", scores)
print("Best Score (Optimal Move):", best_score)
