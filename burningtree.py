from __future__ import annotations
from pydantic import BaseModel
from typing import Optional
import json

def get_json(obj):
  return json.loads(
    json.dumps(obj, default=lambda o: getattr(o, '__dict__', str(o)))
  )

class Node(BaseModel):
    val: int
    left: Optional[Node] = None
    right: Optional[Node] = None


tree = Node(val=12)
tree.left = Node(val=19)
tree.right = Node(val=82)
tree.left.left = Node(val=41)
tree.left.left.right = Node(val=2)
tree.right.left = Node(val=15)
tree.right.left.left = Node(val=21)
tree.right.right = Node(val=95)
tree.right.right.left = Node(val=7)
tree.right.right.right = Node(val=16)




# print(get_json(root))
# print(root)
nextToBurn= []

def burningTree(root: Node, target: int):
    if root is None:
        return False
    
    if root.val == target:
        print(root.val)
        print('------')
        if root.left:
            nextToBurn.append(root.left)
        if root.right:
            nextToBurn.append(root.right)
        return True
    
    # left: bool = 
    if burningTree(root=root.left,target=target):
        while len(nextToBurn) >0:
            n = nextToBurn.pop(0)
            print(n.val)
            if n.left:
                nextToBurn.append(n.left)
            if n.right:
                nextToBurn.append(n.right)
        if root.right:
            nextToBurn.append(root.right)
        print(root.val)
        print('--------')
        return True
    elif burningTree(root=root.right,target=target):
        while len(nextToBurn) >0:
            n = nextToBurn.pop(0)
            print(n.val)
            if n.right:
                nextToBurn.append(n.right)
            if n.left:
                nextToBurn.append(n.left)
        if root.left:
            nextToBurn.append(root.left)
        print(root.val)
        print('--------')
        return True
        
    return False

burningTree(tree,41)

while len(nextToBurn) >0:
    temp = nextToBurn.copy()
    while len(temp) >0:
        n = temp.pop(0)
        nextToBurn.pop(0)
        print(n.val)
        if n.left:
            nextToBurn.append(n.left)
        if n.right:
            nextToBurn.append(n.right)
    print('------')

