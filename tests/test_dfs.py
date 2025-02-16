from scripts.algorithm.dfs_func import dfs


def test_dfs():
    graph = {
        "A": {"B", "C"},
        "B": {"A", "D", "E"},
        "C": {"A", "F"},
        "D": {"B"},
        "E": {"B", "F"},
        "F": {"C", "E"},
    }
    result = dfs(graph, "A")
    assert result == ["A", "B", "D", "E", "F", "C"]
