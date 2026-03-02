import math

class Node:
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = children or []

    def is_terminal(self):
        return len(self.children) == 0

    def evaluate(self):
        return self.value



def minimax(node, depth, maximizing_player):
  
    if depth == 0 or node.is_terminal():
        return node.evaluate()
    
    if maximizing_player:
        max_eval = -math.inf
        for child in node.children:
            eval = minimax(child, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for child in node.children:
            eval = minimax(child, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval



def alpha_beta(node, depth, alpha, beta, maximizing_player):
    
    if depth == 0 or node.is_terminal():
        return node.evaluate()
    
    if maximizing_player:
        max_eval = -math.inf
        for child in node.children:
            eval = alpha_beta(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)

           
            if beta <= alpha:
                break
        return max_eval
    
    else:
        min_eval = math.inf
        for child in node.children:
            eval = alpha_beta(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)

           
            if beta <= alpha:
                break
        return min_eval


leaf1 = Node(3)
leaf2 = Node(5)
leaf3 = Node(6)
leaf4 = Node(9)

min1 = Node(children=[leaf1, leaf2])
min2 = Node(children=[leaf3, leaf4])

root = Node(children=[min1, min2])


print("Minimax Result:", minimax(root, depth=3, maximizing_player=True))

print("Alpha-Beta Result:",
      alpha_beta(root, depth=3,
                 alpha=-math.inf,
                 beta=math.inf,
                 maximizing_player=True))
