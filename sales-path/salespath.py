from sys import maxsize


def get_cheapest_cost(rootNode):
    n = len(rootNode.children)
    minCost = maxsize

    if n == 0:
        return rootNode.cost
    else:
        for nod in rootNode.children:
            tempCost = get_cheapest_cost(nod)
            minCost = tempCost if minCost > tempCost else minCost
    
    return minCost + rootNode.cost

##########################################
# Use the helper code below to implement #
# and test your function above           #
##########################################

# A node


class Node:

    # Constructor to create a new node
    def __init__(self, cost, **kwargs):
        self.cost = cost
        self.children = []
        self.parent = None


tree = Node(cost=0)
tree.children = [Node(cost=5), Node(cost=3), Node(cost=6)]
tree.children[0].children = [Node(cost=4)]
tree.children[1].children = [Node(2), Node(0)]
tree.children[1].children[0].children = [Node(cost=2, children=[Node(cost=1, children=[Node(1)])])]
tree.children[1].children[1].children = [Node(cost=10)]
tree.children[2].children = [Node(cost=1), Node(cost=5)]
print(get_cheapest_cost(tree))
