# Short Exercises: Trees

The following exercises depend on a `Tree` class which you can find in the [tree.py](tree.py) file.

## Exercise #1

**File**: [min_depth_leaf.py](min_depth_leaf.py)

Complete the function ``min_depth_leaf``, which takes a ``Tree`` instance and returns the minimum depth of a leaf in the tree. Recall that the *depth* of a node is the length of the path from the root to that node. So, ``min_depth_leaf`` returns the minimum length of a path from the root to a leaf.

For example, this tree would return 1, because there is a path of length 1 from the root to the leaf ``B``, and this is the shortest path from the root to any leaf (the leaves in this tree are ``B``, ``E``, and ``F``).

```python
A: 20
    │
    ├──B: 80
    │
    └──C: 50
        │
        ├──D: 110
        │  │
        │  └──F: 50
        │
        └──E: 60
```

## Exercise #2

**File**: [prune_tree.py](prune_tree.py)

Complete the function ``prune_tree`` which takes in a tree and a set of strings, ``keys_to_discard``. This function will recursively traverse the tree, returning a copy of the original tree but with all nodes whose keys are in ``keys_to_discard`` removed, along with their descendants. Do not modify the original tree.

For example, using the tree above, and using the set ``{B, D}`` as ``keys_to_discard``, this function would return the following tree.

```python
        A: 20
          │
          └──C: 50
             │
             └──E: 60
```

Notice that nodes ``B`` and ``D`` are not in the output tree, but neither is node ``F``, which was a descendant of node ``D``.

The provided tests do not include any cases where the key of the root is in ``keys_to_discard``. You may choose what your function does in those cases.

## Exercise #3

**File**: [exprtree.py](exptree.py) 

An expression tree is an object implementing the following ordinary (non-dunder) methods:

- `is_const`    : `None -> bool`
- `num_nodes`  : `None -> int`
- `eval`       : `None -> int`

An expression tree also implements the following "dunder" methods:

- `__init__` (constructor)
- `__str__` : `None -> str`

The provided [exprtree.py](exptree.py) file contains an implementation of `Int`, `Plus`, and `Times` classes,
which can be used to implement expression trees with integers, addition, and multiplication.
This file does not contain automated tests, but we've included a `__main__` block where you
can test your code (we already include a sample expression tree using `Int`, `Plus`, and `Times`)

Do the following (and make sure to thoroughly test your solutions):

1. Pick two more binary arithmetic operations to go along with `Plus` and `Times` and 
   define classes for them to expand the variety of expressions available.
2. Implement the unary operator `Abs` (for absolute value) as another
   expression tree. Unlike `Plus`, `Times`, and any other binary operators
   you've implemented, `Abs` has only one subtree. 
3. If you completed the first task, you undoubtedly found that a lot of
   the code was repeated verbatim across the class definitions. There are
   various ways to address this issue and eliminate much of the
   repetition; here is one. Redesign the classes `Plus`, `Times`, and the
   other two binary operations and combine them into a single `BinOp`
   class, which maintains an operator (you can use a string for this)
   along with its two subtrees. This single BinOp class serves as a
   replacement for the four classes (and extensible to more than four)
   whose code it combines.
4. Define a separate set of expression trees for Boolean algebra,
   supporting boolean operations "and", "or", and "not". Note that
   "and" and "or" are both binary operators, but "not" is a unary
   operator. The interface for Boolean expression trees is the same as
   the interface above, except `eval` will return a `bool` rather than an
   `int`.

## Exercise #4

**File**: [bst.py](bst.py) 

A binary search tree ("BST") is an object implementing the following
methods. We assume without loss of generality that BSTs contain
integers (the code is easily modified to accommodate any other item
type).

- `__init__` (constructor)
- `is_empty`   : `None -> bool`
- `is_leaf`    : `None -> bool`
- `num_nodes`  : `None -> int`
- `height`     : `None -> int`
- `contains`   : `int -> bool`
- `insert`     : `int -> BST`

The provided [bst.py](bst.py) file contains an implementation of
an `Empty` class (representing an empty tree) and a `Node` class (representing
a node with a left and right subtree). This file does not contain automated
tests, but we've included a `__main__` block that creates a sample BST.

Implement the following additional methods:

- `inorder`    : `None -> List[int]`

  Return a list of all items in ascending order.
- `min_item`    : `None -> Union[None,int]`
  
  The smallest item in the BST (or `None` if the tree is empty)

- `max_item`    : `one -> Union[None,int]`

  The largest item in the BST (or `None` if the tree is empty)

- `balance_factor`    : `None -> Union[None,int]`

  Returns the balance factor of the tree (the height of the right subtree 
  minus the height of left subtree). The empty tree has no balance factor.

- `balanced_everywhere`    : `None -> bool`

  Test if, for all nodes, the balance factor never falls outside -1, 0, 1

- `add_to_all`    : `int -> BST`

  Add the given integer to all numbers in the tree.

- `path_to`    : `int -> Union[None,int]`

  Return a path from the root to the number, inclusive, in root-to-leaf order, or `None`

- `__str__`  : `None -> str`

  Returns a string representation of the tree (you are welcome to come up with any
  representation, as long as it shows the full contents of the tree)
