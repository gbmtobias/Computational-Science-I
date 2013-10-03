from Bio import Phylo

tree = Phylo.read("tree.txt", "newick")
tree.rooted = True
Phylo.draw(tree)