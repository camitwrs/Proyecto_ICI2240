class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class Node:
    def __init__(self, pair: Pair, parent):
        self.pair = pair
        
        self.parent= parent
        self.left = None
        self.right = None

class TreeMap:
    def __init__(self):
        self.root = None
        self.current = None
        
    def _create_node(self, key, value):
        return Node(key, value)
        
    def _create_pair(self, key, value):
        return Pair(key, value)

    def _minimum(self, node):
        if node is None:
            return None
        elif node.left is None:
            return node

        aux = node.left

        while(aux.left != None):
            aux = aux.left

        return aux
        
    def insert(self, key, value):
        aux = self.root

        if aux is None:
            pair = self._create_pair(key, value)
            self.root = self._create_node(pair, aux)
        
        while (aux):
            if key < aux.pair.key:
                if aux.left:
                    aux = aux.left
                else:
                    pair = self._create_pair(key, value)
                    aux.left = self._create_node(pair, aux)
                    return
            elif key > aux.pair.key:
                if aux.right:
                    aux = aux.right
                else:
                    pair = self._create_pair(key, value)
                    aux.right = self._create_node(pair, aux)
                    return
            else: 
                return
    
    def first(self):
        first = self._minimum(self.root)

        if first is None:
            return None

        self.current = first
        return first.pair   

    def next(self):
        aux = self.current

        if aux is None:
            return None

        if aux.right != None:
            next = self._minimum(aux.right)
            self.current = next
            return next.pair
    
        aux = aux.parent

        while aux is not None and self.current == aux.right:
            self.current = aux
            aux = aux.parent

        if aux is None:
            return None
        else:
            self.current = aux
            return aux.pair

    def remove_node(self, node: Node):
        if node.right is None and node.left is None:
            if node.parent is None:
                self.root = None
            elif node.parent.left == node:
                node.parent.left = None
            elif node.parent.right == node:
                node.parent.right = None
        elif node.right is not None and node.left is not None:
            aux = self._minimum(node.right)
            
            node.pair.key = aux.pair.key
            node.pair.value = aux.pair.value

            self.remove_node(aux)
        else:
            parent = node.parent
            child = node.right
            if child is None:
                child = node.left
            child.parent = parent
            if parent is None:
                self.root = child
            elif parent.left == node:
                parent.left = child
            elif parent.right == node:
                parent.right = child

    def search(self, key):
        if self.root is None:
            return None

        aux = self.root

        while aux is not None:
            if key < aux.pair.key:
                aux = aux.left
            elif aux.pair.key < key:
                aux = aux.right
            else:
                break

        self.current = aux
        if aux is None:
            return None
        return aux.pair
