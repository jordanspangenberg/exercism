
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
    
 