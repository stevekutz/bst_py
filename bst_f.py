class Node:
    def __init__(self, value = None):
        self.value = value
        self.left_child = None
        self.right_child = None


class BST:
    def __init__(self):
        self.root = None
        self.size = 0
        self.sum = 0

    def insert(self, value)    :
        if self.root == None:
            self.root = Node(value)
        else:
            # like a `private function`, DO NOT call from outside of the class
            self._insert(value, self.root)   # call with value and current root   

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child == None:
                # create a new Node if one does NOT exist
                cur_node.left_child = Node(value)        
            else:
                # use recursion to find next avail left_child
                self._insert(value, cur_node.left_child)                

        elif value > cur_node.value:
            if cur_node.right_child == None:
                # create a new Node if needed
                cur_node.right_child = Node(value)
            else:
                # use recursion to find next avail right_child
                self._insert(value, cur_node.right_child)    

        else:
            print(f' Value {cur_node.value} already exists in BST')


    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

        print(f'\t sum = {self.sum}')
        print(f'\t size = {self.size}')    

    def _print_tree(self, cur_node):
        # this is an in-order traversal, prints out in sorted order    

        if cur_node != None:
            self.sum += cur_node.value
            self.size += 1

            self._print_tree(cur_node.left_child)
            # print value at current node
            print(f' current node {cur_node.value}')
            self._print_tree(cur_node.right_child)


    def fill_tree(self, tree, num_elems = 100, max_int = 1000):
        from random import randint
        num_set = set()

        for _ in range(num_elems):
            
            cur_elem = randint(0, max_int)
    
            # check to make sure no duplicate values made
            while cur_elem in num_set:
                print(f' value {cur_elem} already used, recalc random value')
                cur_elem = randint(0, max_int)
            
            num_set.add(cur_elem)
            tree.insert(cur_elem)
            list_vals.append(cur_elem)

        return tree    


    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0  # if root value is 0, there is no tree, no height    

    def _height(self, cur_node, cur_height):
        if cur_node == None: 
            return cur_height
        left_height = self._height(cur_node.left_child, cur_height + 1)   
        right_height = self._height(cur_node.right_child, cur_height + 1)
        return max(left_height, right_height)



list_vals = []

t = BST()
t = t.fill_tree(t)

t.print_tree()
print(sorted(list_vals))
print(f'\n\nlen(list_vals)  {len(list_vals)}')
print(f' sum of list_vals {sum(list_vals)}')
print(f' \n height of tree is {t.height()}\n')
