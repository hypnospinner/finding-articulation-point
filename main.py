from networkx import DiGraph
from networkx.classes import graph
import random
import time
import matplotlib.pyplot as plt


def generate_graph(nodes=5, edges=6) -> DiGraph:

    if edges < nodes:
        return Exception("Graph is not connected")
    else:
        _nodes = list(range(0, nodes))

        graph = DiGraph()
        graph.add_nodes_from(_nodes)

        i = 0

        while i < edges:
            start = random.choice(_nodes)
            end = random.choice(_nodes)
            if ((start, end) not in graph) and (start != end):
                graph.add_edge(start, end)
                graph.add_edge(end, start)
                i = i + 1

    return graph


def find_articular_points(graph: DiGraph):

    result = []
    visited = [False for _ in graph]
    time_in = [0 for _ in graph]
    time_up = [0 for _ in graph]
    timer = 0

    def dfs(vertex: int, parent: int = -1):
        nonlocal timer
        nonlocal time_in
        nonlocal time_up
        nonlocal visited
        nonlocal result

        visited[vertex] = True
        timer += 1
        time_in[vertex] = time_up[vertex] = timer
        children = 0

        for edge in graph.edges(vertex):
            to = edge[1]
            if (to is parent):
                continue
            if (visited[to]):
                time_up[vertex] = time_up[vertex] if time_up[vertex] < time_in[to] else time_in[to]
            else:
                dfs(vertex=to, parent=vertex)
                time_up[vertex] = time_up[vertex] if time_up[vertex] < time_in[to] else time_in[to]
                if time_up[to] >= time_in[vertex] and parent != -1:
                    if vertex not in result:
                        result.append(vertex)
                children += 1

        if parent == -1 and children > 1:
            if vertex not in result:
                result.append(vertex)

    dfs(0)

    return result


N = [i for i in range(100, 1001, 100)]
M = [i for i in range(200, 2001, 200)]
k = 5
subplot = 111
appr_relation = [0.0, 0.0, 0.0, 0.0, 0.0]
fig, plots = plt.subplots(k + 1)

for n in range(k):
    time_measures = []
    for i in range(len(N)):
        g = generate_graph(N[i], M[i])
        start_time = time.time()
        r = find_articular_points(g)
        end_time = time.time()
        time_measures.append(end_time - start_time)

    measure_relation = [
        time_measures[2 * i + 1] / time_measures[i] for i in range(0, 5)
    ]

    plots[n].plot(N[:5], measure_relation)
    plots[n].set_title(f"Check number {n+1}")

    for i in range(len(appr_relation)):
        appr_relation[i] += measure_relation[i]

appr_relation = [appr_relation[i] / float(k)
                 for i in range(len(appr_relation))]

print(appr_relation)

plots[k].plot(N[:5], appr_relation)
plt.show()


# [
#  0.009090185165405273,
#  0.0030007362365722656,
#  0.005572319030761719,
#  0.009287118911743164,
#  0.007880449295043945,
#  0.00921177864074707,
#  0.01123046875,
#  0.012877702713012695,
#  0.014512777328491211,
#  0.016003847122192383
# ]


# [
#   1.50855727914937,
#   2.0116829197644104,
#   1.7711536292899297,
#   1.4678425725941924
# ]


# t = [
#     0.002763533592224121,   # 0
#     0.0031718969345092773,  # 1
#     0.004971361160278321,   # 2
#     0.007989239692687989,   # 3
#     0.010105729103088379,   # 4
#     0.011619210243225098,   # 5
#     0.01252899169921875,    # 6
#     0.014173650741577148,   # 7
#     0.01703305244445801,    # 8
#     0.01870450973510742     # 9
# ]
