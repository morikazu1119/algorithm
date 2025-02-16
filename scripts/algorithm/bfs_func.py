from collections import deque

def bfs(graph, start):
    """
    幅優先探索 (BFS)
    
    :param graph: 隣接リスト形式のグラフ（各ノードの隣接ノードが集合で保持されている）
    :param start: 探索開始ノード
    :return: 探索順序のリスト
    """
    visited = set()
    order = []
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            order.append(node)
            visited.add(node)
            queue.extend(sorted(graph[node] - visited))
    
    return order