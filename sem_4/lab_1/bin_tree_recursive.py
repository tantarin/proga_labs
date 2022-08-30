def gen_bin_tree_recursive(height, root):
    """рекурсивный вариант"""
    left_leaf = root * 2
    right_leaf = root + 2
    if height == 0:
        return {str(root): []}
    else:
        return {
            str(root): [gen_bin_tree_recursive(height - 1, left_leaf), gen_bin_tree_recursive(height - 1, right_leaf)]}


assert gen_bin_tree_recursive(root=1, height=2) == {
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
