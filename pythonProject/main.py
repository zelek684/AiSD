from enum import Enum
from typing import Any
from typing import Optional
from typing import Dict, List, Callable


# ---- KOD PODANY W ZADANIU ----
class EdgeType(Enum):
    directed = 1
    undirected = 2


class Vertex:
    data: Any
    index: int


class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]


# ---- KOD PODANY W ZADANIU ----


# ---- KOD DOPISANY ------
class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self):
        self.adjacencies = dict()
        self.idx = 0  # graf trzyma informacje na temat tego jaki index ma ostatni wierzcholek, aby przy dodaniu nowego moc nadac mu nastepny index

    def create_vertex(self, data: Any):
        # tworzymy nowy wierzcholek ktory trzyma dane podane w funkcji
        v = Vertex()
        v.data = data
        v.index = self.idx
        self.idx += 1
        self.adjacencies[v] = []
        return v

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        # tworzymy nowa krawedz z odpowiednimi wierzcholkami
        e = Edge()
        e.source = source
        e.destination = destination
        e.weight = weight
        self.adjacencies[source].append(e)

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        # jezeli dodajemy krewedz nieskierowana to poprostu mozemy dodac dwie krawedzie skierowane :)
        self.add_directed_edge(source, destination, weight)
        self.add_directed_edge(destination, source, weight)

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        # tutaj wystarczy sprawdzic typ krawedzi
        if edge == EdgeType.directed:
            self.add_directed_edge(source, destination, weight)
        else:
            self.add_undirected_edge(source, destination, weight)

    def show(self):
        # wypisujemy zawartosc grafu
        str = ""
        for key, value in self.adjacencies.items():
            print(f"- {key.index}: {key.data} ----> [", end="")
            for e in value:
                print(f"{e.destination.index}: {e.destination.data} ", end="")
            print("]")

    def traverse_breadth_first(self, visit: Callable[[Any], None]):
        # implementacja bfs taka jak podana w zadaniu tzn przechodzimy najpierw po wsyzstkich sasiadach wierzcholka zanim pojdziemy w glab
        visited = []
        queue = []
        v = next(iter(
            self.adjacencies))  # wybor pierwszego lepszego wierzcholka z dicta (jako ze nie da sie zrobic poprostu dict[0] to musimy jakos wybrac arbitralny wierzcholek poczatkowy)
        queue.append(v)
        visited.append(v)
        while queue:
            v = queue.pop(0)
            visit(v)
            for p in self.adjacencies[v]:
                if p.destination not in visited:
                    visited.append(p.destination)
                    queue.append(p.destination)

    def traverse_depth_first(self, visit: Callable[[Any], None]):
        # implementacja dfs taka jak podana w zadaniu z zasotowana funkcja wewnetrzna aby wczesniej sobie wyciagnac wierzcholek poczatkowy
        def dfs(v: Vertex, visited: List[Vertex], visit: Callable[[Any], None]):
            visit(v)
            visited.append(v)
            for p in self.adjacencies[v]:
                if p.destination not in visited:
                    dfs(p.destination, visited, visit)

        first = next(iter(
            self.adjacencies))  # wybor pierwszego lepszego wierzcholka z dicta (jako ze nie da sie zrobic poprostu dict[0] to musimy jakos wybrac arbitralny wierzcholek poczatkowy)
        dfs(first, [], visit)  # wywolanie funkcji wewnetrznej

    def find_shortest_path(self, src, dst):
        # znajduje najkrotsza sciezke poprostu przechodzac bfsem i w momencie w ktorym dochodze do wierzcholka koncowego zwracam trase
        visited = []
        queue = []
        pred = {}  # zwracana trasa w postaci slownika poprzednikow danych wierzcholkow
        queue.append(src)
        visited.append(src)
        while queue:
            v = queue.pop(0)
            for p in self.adjacencies[v]:
                if p.destination not in visited:
                    visited.append(p.destination)
                    # przechodzac po wiecholkach wpisuje do slownika poprzednikow porpzedni wierzcholek
                    pred[p.destination] = v
                    queue.append(p.destination)
                    if p.destination == dst:
                        return pred

    def __str__(self):
        # analogicznie do funkcji show() tylko ze tutaj musimy zwrocic stringa z zawartoscia grafu
        str = ""
        for key, value in self.adjacencies.items():
            str += f"- {key.index}: {key.data} ----> ["
            for e in value:
                str += f"{e.destination.index}: {e.destination.data} "
            str += "]\n"
        return str


# przyklad z pierwszej czesci
g = Graph()
v0 = g.create_vertex("v0")
v1 = g.create_vertex("v1")
v2 = g.create_vertex("v2")
v3 = g.create_vertex("v3")
v4 = g.create_vertex("v4")
v5 = g.create_vertex("v5")

g.add_undirected_edge(v0, v1)
g.add_undirected_edge(v0, v5)
g.add_undirected_edge(v1, v5)
g.add_undirected_edge(v1, v2)
g.add_undirected_edge(v1, v4)
g.add_undirected_edge(v2, v5)
g.add_undirected_edge(v2, v3)
g.add_undirected_edge(v1, v5)
g.add_undirected_edge(v3, v4)
g.add_undirected_edge(v4, v5)


# druga czesc
def friend_path(g: Graph, f0: Any, f1: Any):
    # wywoluje funkcje zwracajaca slownik poprzednikow i przechodzac odpowiednio po tym slowniku (w tym przypadku od konca naszej trasy) tworze sobie liste reprezentujaca trase od f0 do f1
    pred = g.find_shortest_path(f0, f1)
    path = []
    path.append(f1)
    prev = pred[f1]
    while prev != f0:
        path.append(prev)
        prev = pred[prev]
    path.append(prev)
    return path[::-1]


# przyklad

g1 = Graph()
vi = g1.create_vertex("VI")
ru = g1.create_vertex("RU")
pa = g1.create_vertex("PA")
co = g1.create_vertex("CO")
ch = g1.create_vertex("CH")
ke = g1.create_vertex("KE")
ra = g1.create_vertex("RA")
su = g1.create_vertex("SU")

g1.add_undirected_edge(vi, ch)
g1.add_undirected_edge(vi, ru)
g1.add_undirected_edge(vi, pa)
g1.add_undirected_edge(ru, ra)
g1.add_undirected_edge(ru, su)
g1.add_undirected_edge(pa, co)
g1.add_undirected_edge(pa, ke)
g1.add_undirected_edge(co, ru)
g1.add_undirected_edge(co, vi)

# graf testowy 1 - graf z pierwszej czesci
print("TEST 1")
path = friend_path(g, v0, v1)
for p in path:
    print(p.data)

# graf testowy 2 - graf z drugiej czesci
print("TEST 2")
path = friend_path(g1, vi, ke)
for p in path:
    print(p.data)

# graf testowy 3
print("TEST 3")
g2 = Graph()
ad = g2.create_vertex("Adam")
p = g2.create_vertex("Piotr")
m = g2.create_vertex("Michal")
an = g2.create_vertex("Anna")
d = g2.create_vertex("Dominika")
k = g2.create_vertex("Kamil")

g2.add_undirected_edge(ad, p)
g2.add_undirected_edge(ad, m)
g2.add_undirected_edge(ad, k)
g2.add_undirected_edge(k, d)
g2.add_undirected_edge(p, an)
g2.add_undirected_edge(p, k)
g2.add_undirected_edge(m, d)
g2.add_undirected_edge(m, an)

path = friend_path(g2, ad, an)
for p in path:
    print(p.data)
















