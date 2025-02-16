def dfs(graph, start, visited=None, order=None) -> list:
    """
    深さ優先探索 (DFS)

    :param graph: 隣接リスト形式のグラフ（各ノードの隣接ノードが集合で保持されている）
    :param start: 探索開始ノード
    :param visited: 既に訪れたノードを記録する集合（再帰呼び出しで利用）
    :param order: 探索順序を記録するリスト（再帰呼び出しで利用）
    :return: 探索順序のリスト
    """
    if visited is None:
        visited = set()
    if order is None:
        order = []

    if start not in visited:
        order.append(start)
        visited.add(start)

        for neighbor in sorted(graph[start] - visited):
            dfs(graph, neighbor, visited, order)

    return order
