from binarytree import tree, Node, build

def permute_even_ones(input_tree, output_tree, one_count=0):
    if input_tree == None or output_tree == None:
        return

    one_count += input_tree.value

    output_tree.value = (one_count + 1) % 2

    permute_even_ones(input_tree.left, output_tree.left, one_count)
    permute_even_ones(input_tree.right, output_tree.right, one_count)

def generate_values(height):
    assert(height > 0)

    values = []
    values.append(0)
    for y in range(0, height):
        for x in range(0, pow(2, y)):
            values.append(0)
            values.append(1)
    
    return values

bt_lineage = []
bt_lineage.append(build(generate_values(3)))

# Pretty-print the trees in stdout.
print("Generation 0:")
print(bt_lineage[0])

for x in range(1, 9):
    bt_lineage.append(build(bt_lineage[x - 1].values))
    permute_even_ones(bt_lineage[x - 1], bt_lineage[x])

    print("Generation", x, ": ")
    print(bt_lineage[x])

