from scripts.algorithm.gene_algo_func import genetic_algorithm

def test_genetic_algorithm():
    best_solution, best_fitness = genetic_algorithm(10, 8, 50)
    assert len(best_solution) == 8
    assert best_fitness == 8