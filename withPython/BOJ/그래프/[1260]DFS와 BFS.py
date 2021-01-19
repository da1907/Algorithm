import sys

point, edge, V = map(int, input().split())
edge_arr = []
matrix = [[0] * (point + 1) for _ in range(point+1)]

for _ in range(edge):
    edge_arr = list(map(int, sys.stdin.readline().split()))
    matrix[edge_arr[0]][edge_arr[1]] = 1
    matrix[edge_arr[1]][edge_arr[0]] = 1

def dfs(current_node, row, foot_prints):
    foot_prints += [current_node]
    for search_node in range(len(row[current_node])):
        if row[current_node][search_node] and search_node not in foot_prints:
            foot_prints = dfs(search_node, row, foot_prints)
    return foot_prints

def bfs(start):
    queue = [start]
    foot_prints = [start]
    while queue:
        current_node = queue.pop(0)
        for search_node in range(len(matrix[current_node])):
            if matrix[current_node][search_node] and search_node not in foot_prints:
                foot_prints += [search_node]
                queue += [search_node]
    return foot_prints

print(*dfs(V, matrix, []))
print(*bfs(V))