# Short Exercises: Trees

## Recursion with trees

### Exercise #1

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

### Exercise #2

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
