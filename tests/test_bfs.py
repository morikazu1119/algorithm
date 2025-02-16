from scripts.algorithm.bfs_func import bfs

def test_bfs():
    graph = {
        'A': {'B', 'C'},
        'B': {'A', 'D', 'E'},
        'C': {'A', 'F'},
        'D': {'B'},
        'E': {'B', 'F'},
        'F': {'C', 'E'}
    }
    result = sorted(bfs(graph, 'A'))
    assert result == ['A', 'B', 'C', 'D', 'E', 'F']