def gen_bin_tree_non_recursive(height: int, root: int):
    """нерекурсивный вариант"""
    left_leaf = lambda x: int(x) * 2
    right_leaf = lambda x: int(x) + 2
    tree = {str(root): []}
    roots = [[root]]

    for _ in range(height):
        if len(roots) == 1:
            _r = roots[-1]
        else:
            _r = [item for sublist in roots[-1] for item in sublist]

        leaves = []
        for r in _r:
            leaves.append({str(left_leaf(r)): []})
            leaves.append({str(right_leaf(r)): []})
        roots.append(leaves)

    for i in range(len(roots) - 2, 0, -1):
        k = 0
        for j in roots[i]:
            for key, v in j.items():
                j[key] = [roots[i + 1][k], roots[i + 1][k + 1]]
            k += 2
        del roots[i + 1]

    for k, v in tree.items():
        tree[k] = roots[1]

    return tree


assert gen_bin_tree_non_recursive(root=1, height=2) == {
    "1": [{
        "2": [{
            "4": []
        }, {
            "4": []
        }]
    }, {
        "3": [{
            "6": []
        }, {
            "5": []
        }]
    }]
}, 'для высоты 2'