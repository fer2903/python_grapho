
# Creamos unaclase para grafos dirigidos A-->B
class GrafoDirigido:
    def __init__(self):
        self.grafo_dict = {}  # definimos el diccionario G

    def agregar_vertice(self, vertice):
        if vertice in self.grafo_dict:  # validamos que el vertice no exista en el arreglo
            return "El vreetice ya fue agregado"
        self.grafo_dict[vertice] = []  # G[v1] = []  o G={v1:[]}

    def add_edge(self, edge):  # edge o arista
        v1 = edge.get_v1()  # traemos nodo 1
        v2 = edge.get_v2()  # traemos nodo 2
        # agregamos la conexion
        if v1 not in self.grafo_dict:  # Si el nodo origen no existe
            return ValueError(f"vertice {v1.get_name} no se agrego")
        if v2 not in self.grafo_dict:
            return ValueError(f"Vertice {v2.get_name} not in graph")
        self.grafo_dict[v1].append(v2)  # agregamos el nodo al grafo de la forma {S:[A,B,C,D,...]}

    def is_vertice_in(self, vertice):  # verificamos si el vertice esta en el diccionario
        return vertice in self.grafo_dict

    def get_vertice(self, vertice_name):
        # recorremos todos los nodos y comparamos con name
        for v in self.grafo_dict:
            if vertice_name == v.get_name():
                return v
        print(f"Vertice {vertice_name} no existe")

    def get_neigbors(self, vertice):  # trae todos los vecinos del grafo
        return self.grafo_dict[vertice]

    def __str__(self):
        all_edges = ""
        # guardaremos todas las aristas, recorremos e imprimimos los origenes y sus valores correspondientes
        for v1 in self.grafo_dict:
            for v2 in self.grafo_dict[v1]:  # recorremos y devolvemos todos los valores relacionados a esa llave
                all_edges += v1.get_name() + "-->" + v2.get_name() + " "
        return all_edges


# Agregamos un objeto Arista o Edge
class Edge:
    # en este caso generalizamos a la forma E={v1, v2} , V= nodo origen , V2=nodo destino
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def get_v1(self):  # retornamos el nodo 1
        return self.v1

    def get_v2(self):   # retornamos el nodo 2
        return self.v2

    def __str__(self):
        # imprimimos
        return self.v1.get_name() + "--->" + self.v2.get_name()


class Vertice:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name


# agregamos metodo de un grafo no dirigido A<-->B
# reutilizamos las funciones de grafo dirigido
class GrafoNoDirigido(GrafoDirigido):
    # redefinimos add_edge
    def add_edge(self, edge):
        GrafoDirigido.add_edge(self, edge)  # llamamos a la funcion del objeto padre para agregar un nodo
        edge_back = Edge(edge.get_v2(), edge.get_v1())  # el destino se convierte en el origen
        GrafoDirigido.add_edge(self, edge_back)


# probamos nuestra funcion
def build_graph(graph):
    g = graph()
    nodes = ('S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'X')
    for v in nodes:
        # agregamos las conexiones
        g.agregar_vertice(Vertice(v))  # Agregamos el vertice y lo seteamos con la clase vertice
    g.add_edge(Edge(g.get_vertice('S'), g.get_vertice('A')))  # agregamos un objeto de tipo Edge, Nodo Origen
    g.add_edge(Edge(g.get_vertice('S'), g.get_vertice('D')))
    return g


# creamos las conexiones grafo direccional
G1 = build_graph(GrafoDirigido)
print(G1)  # S-->A S-->D

# creamos un grafo unidirexional

u_G1 = build_graph(GrafoNoDirigido)
print(u_G1)  # S-->A S-->D A-->S D-->S
