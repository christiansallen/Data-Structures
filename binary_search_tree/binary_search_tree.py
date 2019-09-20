import sys


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        insert_val = BinarySearchTree(value)
        current_node = self
        placed = False
        while placed == False:
            if value >= current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = insert_val
                    placed = True
            if value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = insert_val
                    placed = True

    def contains(self, target):
        current_node = self
        found = False
        end = False
        while found is False and end is False:
          # Find and replace current_node.left until there isnt one
            if target < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    end = True
            # Find and replace current_node.right until there isnt one
            if target > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    end = True
            if target == current_node.value:
                found = True
        return found

    def get_max(self):
        current_node = self
        end = False
        while end is False:
            if current_node.right:
                current_node = current_node.right
            else:
                end = True
        return current_node.value

    def for_each(self, cb):
        if self.value == None:
            return
        else:
            cb(self.value)
            if self.left:
                self.left.for_each(cb)
            if self.right:
                self.right.for_each(cb)


# `for_each` performs a traversal of _every_ node in the tree, executing the passed-in callback function on each tree node value. There is a myriad of ways to perform tree traversal; in this case any of them should work.


# DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if node.left:
            self.in_order_print(node.left)
        print(node.value)

        if node.right:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        current_node = node
        stack = [current_node]
        while stack:
            if current_node.left:
                stack.append(current_node.left)
            if current_node.right:
                stack.append(current_node.right)
            print(stack.pop(0).value)
            if stack:
                current_node = stack[0]

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        current_node = node
        stack = [current_node]
        while stack:
            print(stack.pop().value)
            if current_node.left:
                stack.append(current_node.left)
            if current_node.right:
                stack.append(current_node.right)
            if stack:
                current_node = stack[-1]

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
