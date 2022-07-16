import math
import random
from platform import node

nodes = []

def create_node (nodes):
    print('Create new node (y/n)?  ')
    print('Type "q" to quit.')
    node_creation = input()
    if node_creation == 'y':
        node_weight = random.randint(0, 999)
        nodes.append(node_weight)
        print('Node created.')
        print(node_weight)
    elif node_creation == 'n':
        print('Node not created.')
    elif node_creation == 'q':
        print('Process terminated')
    return node_creation

def main():
    create_node(nodes)
    print(nodes)
main()



