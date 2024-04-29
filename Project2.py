import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def main():
    G = nx.read_gml("lesmis.gml")
    plt.figure(figsize=(10, 6))
    nx.draw(G, with_labels=True, node_size=100, font_size=8)
    plt.title("Les Miserables Character Network")
    plt.show()
if __name__ == "__main__":
    main()