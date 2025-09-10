import networkx as nx
import pyshark
import matplotlib.pyplot as plt
from pyvis.network import Network

def main():
    packets = pyshark.FileCapture("./local_data/wirehark-capture_2025-09-10.pcapng")

    unique_nodes = set()
    edges = list()

    for packet in packets:
        # print(dir(packet["ip"])
        source = ""
        distanation = ""
        try:
            source = packet["ip"].src
        except (AttributeError, KeyError) as e:
            pass
        try:
            distanation = packet["ip"].dst
        except (AttributeError, KeyError) as e:
            pass
        unique_nodes.add(distanation)
        unique_nodes.add(source)
        edges.append((source, distanation))
    # print(unique_nodes)
    
    graph = nx.DiGraph()
    graph.add_nodes_from(list(unique_nodes))
    graph.add_edges_from(set(edges))
    network = Network("1000px", "1000px")
    network.from_nx(graph)
    network.write_html("./local_data/graph.html")
    # nx.draw(graph, with_labels=True)
    # plt.show()

if __name__ == "__main__":
    main()
