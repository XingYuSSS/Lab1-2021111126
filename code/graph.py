import re

class Graph:
    def __init__(self) -> None:
        self.node = {}

    def __str__(self) -> str:
        graph_str = ''
        for item in self.node.items():
            graph_str += item[0] + ' -> '
            for end in item[1]:
                graph_str += end + ' '
            graph_str += '\n'
        return graph_str

    def add_vertex(self, name: str):
        if name not in self.node.keys():
            self.node[name] = []

    def add_edge(self, from_name: str, to_name: str):
        self.add_vertex(from_name)
        self.add_vertex(to_name)
        self.node[from_name].append(to_name)


class WordGraph:
    def __init__(self, txt: str) -> None:
        self.graph = Graph()
        words = re.findall('[a-z]+', txt.lower())
        print(words)
        for i in range(len(words) - 1):
            self.graph.add_edge(words[i], words[i+1])
        print(self.graph)



if __name__ == "__main__":
    string = 'To explore strange new worlds,\nTo seek out new life and new civilizations'
    g=WordGraph(string)
    print(g)