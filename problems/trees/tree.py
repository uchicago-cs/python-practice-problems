#!/usr/bin/python


import textwrap


class Tree(object):
    """
    A class representing a (non-null) tree with a root
    node and some number of child subtrees (which will,
    themselves, be instances of Tree)
    """
    
    def __init__(self, k=None, v=None):
        """
        Constructor.
        
        Creates either a tree with a root node and no 
        child subtrees. The root node will have a key and 
        value associated with it.
        
        Parameters
        - k, v: Key and value for the root node.
        """
        
        self.key = k
        self.value = v 
        
        self.children = []


    def add_child(self, other_tree):
        """
        Adds an existing tree as a child of the tree.
        
        Parameter:
        - other_tree: Tree to add as a child subtree.
        """
        if not isinstance(other_tree, Tree):
            raise ValueError("Parameter to add_child must be a Tree object")
        
        self.children.append(other_tree)


    def num_children(self):
        """Returns the number of children"""
        return len(self.children)


    def __print_r(self, prefix, last, kformat, vformat, maxdepth):
        """
        Recursive method to print out the tree. Should not be
        called directly. See print() method for more details.
        """

        if maxdepth is not None:
            if maxdepth == 0:
                return
            else:
                maxdepth -= 1    

        if len(prefix) > 0:
            if last:
                lprefix1 = prefix[:-3] + u"  └──"
            else:
                lprefix1 = prefix[:-3] + u"  ├──"
        else:
            lprefix1 = u""
    
        if len(prefix) > 0:
            lprefix2 = prefix[:-3] + u"  │"
        else:
            lprefix2 = u""

        if last:
            lprefix3 = lprefix2[:-1] + "   "
        else:
            lprefix3 = lprefix2 + "  "

        ltext = (kformat + ": " + vformat).format(self.key, self.value)

        ltextlines = textwrap.wrap(ltext, 80, initial_indent=lprefix1, 
            subsequent_indent=lprefix3)

        print(lprefix2)
        print(u"\n".join(ltextlines))

        for i, st in enumerate(self.children):
            if i == self.num_children() - 1:
                newprefix = prefix + u"   "
                newlast = True
            else:
                newprefix = prefix + u"  │"
                newlast = False

            st.__print_r(newprefix, newlast, kformat, vformat, maxdepth)
    
    
    def print(self, kformat="{}", vformat="{}", maxdepth=None):
        """
        Prints out the tree.
        
        Parameters:
        - kformat, vformat: Format strings for the key and value.
        - maxdepth: Maximum depth to print.
        """
        
        self.__print_r(u"", False, kformat, vformat, maxdepth)
