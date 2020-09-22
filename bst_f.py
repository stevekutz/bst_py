class Node:
    def __init__(self, value = None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None  # a pointer to the parent node in the tree

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
                # add this to track parent
                cur_node.left_child.parent = cur_node     
            else:
                # use recursion to find next avail left_child
                self._insert(value, cur_node.left_child)  

        elif value > cur_node.value:
            if cur_node.right_child == None:
                # create a new Node if needed
                cur_node.right_child = Node(value)
                # add this to track parent
                cur_node.right_child.parent = cur_node              
            else:
                # use recursion to find next avail right_child
                self._insert(value, cur_node.right_child)    

        else:
            print(f' Value {cur_node.value} already exists in BST')


    def find(self, value):
        if self.root != None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, cur_node):
        if value == cur_node.value:
            print(f' current node value is {cur_node.value}')
            return cur_node
        elif value < cur_node.value and cur_node.left_child != None:
            return self._find(value, cur_node.left_child)    
        elif value > cur_node.value and cur_node.right_child != None:
            return self._find(value, cur_node.right_child)    

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


    def search(self, value):
        if self.root != None:
            return self._search(value, self.root)   
        else:
            return False    


    def _search(self, value, cur_node):
        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left_child != None:
            return self._search(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child != None:
            return self._search(value, cur_node.right_child)
        return False


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


    def delete_value(self, value):
        return self.delete_node(self.find(value))

    def delete_node(self, node):

        # helper - returns child node with min value from an input node    
        def min_value_node(n):
            current = n
            while current.left_child != None:
                current = current.left_child
            return current    

        # helper - returns # of children of given node >> 0, 1, or 2
        def num_children(n):
            num_children = 0
            if n.left_child != None:
                num_children += 1
            if n.right_child != None:
                num_children += 1
            return num_children

        # get parent of targetted node for deletion
        node_parent = node.parent

        # find number of children of targeted node for deletion
        node_children = num_children(node)

        ###########################  Cases for deletion node   ###########################
        # CASE #1   node has no children

        if node_children == 0:
            if node_parent != None:
                # remove reference to targeted node for deletion
                if node_parent.left_child == node:
                    node_parent.left_child = None
                else:
                    node_parent.right_child = None

        # CASE #2   node has a single child

        if node_children == 1:
            # find the single child node
            if node.left_child != None:
                child = node.left_child
            else:
                child = node.right_child    


            if node_parent != None:
                # replace targeted node for deletion with child
                if node_parent.left_child == node:
                    node_parent.left_child = child
                else:
                    node_parent.right_child = child
            else:
                self.root = child

            # adjust the parent pointer in node
            child.parent = node_parent  


        # CASE #3   node has two children 
                  
        if node_children == 2:
            
            # find IN-ORDER successor value of targeted node for deletion
            successor = min_value_node(node.right_child)

            # copy IN-ORDER successor value into node that held deleted node value
            node.value = successor.value

            # delete IN-ORDER successor since value has been copied into node
            self.delete_node(successor)










list_vals = []

t = BST()

# t = t.fill_tree(t)

t.insert(5)
t.insert(4)
t.insert(6)
t.insert(10)
t.insert(9)
t.insert(11)
t.insert(2)

t.print_tree()
print(sorted(list_vals))
print(f'\n\nlen(list_vals)  {len(list_vals)}')
print(f' sum of list_vals {sum(list_vals)}')
print(f' \n height of tree is {t.height()}, worst case search time would take {t.height()} steps \n')
print(f' searched for 8  {t.search(8)}')

# print(t.find(10))
# t.delete_value(5)
# print(t.search(5))   # False

# t.delete_value(4)
# print(f' \n height of tree is {t.height()}, worst case search time would take {t.height()} steps \n')
# print(t.search(4))

# t.delete_value(5)
# print(f' \n height of tree is {t.height()}, worst case search time would take {t.height()} steps \n')
# print(t.search(5))   # False

t.delete_value(11)
print(f' \n height of tree is {t.height()}, worst case search time would take {t.height()} steps \n')
print(t.search(11))