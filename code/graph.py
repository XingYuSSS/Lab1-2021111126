import re


class Graph:
    def __init__(self) -> None:
        self.graph_dict = {}

    def __str__(self) -> str:
        graph_str = ''
        for (fv, tv) in self.graph_dict.items():
            graph_str += fv + ' -> '
            for (name, weight) in tv.items():
                graph_str += f'{name}: {weight}, '
            graph_str += '\n'
        return graph_str

    def add_vertex(self, name: str):
        if name not in self.graph_dict.keys():
            self.graph_dict[name] = {}

    def add_edge(self, from_name: str, to_name: str):
        self.add_vertex(from_name)
        self.add_vertex(to_name)
        if to_name not in self.graph_dict[from_name].keys():
            self.graph_dict[from_name][to_name] = 0
        self.graph_dict[from_name][to_name] += 1


class WordGraph:
    def __init__(self, txt: str) -> None:
        self.graph = Graph()
        words = re.findall('[a-z]+', txt.lower())
        print(words)
        for i in range(len(words) - 1):
            self.graph.add_edge(words[i], words[i+1])
        print(self.graph)

    def __str__(self) -> str:
        return self.graph.__str__()



if __name__ == "__main__":
    string = 'To explore strange new worlds,\nTo seek out new life and new civilizations'
    g=WordGraph(string)
    print(g)