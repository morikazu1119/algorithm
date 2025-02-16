import random


# 適応度関数
def fitness(individual):
    return sum(individual)


# 初期集団の生成
def generate_population(size, length):
    return [[random.randint(0, 1) for _ in range(length)] for _ in range(size)]


# 選択（トーナメント方式）
def selection(population):
    return max(random.sample(population, 2), key=fitness)


# 交叉（一点交叉）
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]


# 突然変異
def mutate(individual, mutation_rate=0.01):
    return [
        gene if random.random() > mutation_rate else 1 - gene for gene in individual
    ]


# 遺伝的アルゴリズム
def genetic_algorithm(pop_size, gene_length, generations):
    population = generate_population(pop_size, gene_length)

    for _ in range(generations):
        new_population = []
        for _ in range(pop_size // 2):
            parent1 = selection(population)
            parent2 = selection(population)
            offspring1, offspring2 = crossover(parent1, parent2)
            new_population.extend([mutate(offspring1), mutate(offspring2)])
        population = new_population

    best = max(population, key=fitness)
    return best, fitness(best)
