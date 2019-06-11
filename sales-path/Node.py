
########################################## 
# Use the helper code below to implement #
# and test your function above           #
##########################################

# A node 
class Node:

  # Constructor to create a new node
  def __init__(self, cost):
    self.cost = cost
    self.children = []
    self.parent = None
    
tree = Node(cost=0)
tree.children = [Node(cost=5), Node(cost=3), Node(cost=6)]
tree.children[0].children = [Node(cost=4)]
tree.children[1].children = [Node(cost=2),Node(cost=0)]
tree.children[2].children = [Node(cost=2)]
print(get_cheapest_cost(tree))
 