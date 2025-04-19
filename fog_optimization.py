# 🌫️ Fog Computing Task Allocation Optimization using Genetic Algorithm
# Author: Zülal Özyazıcıoğlu

import random

# Örnek veriler: görevler ve fog düğümleri
NUM_TASKS = 10
NUM_NODES = 4

# Rastgele görevlerin kaynak gereksinimi (CPU) ve düğüm kapasiteleri
task_requirements = [random.randint(1, 5) for _ in range(NUM_TASKS)]
node_capacities = [10, 12, 15, 8]
latency_matrix = [[random.randint(1, 10) for _ in range(NUM_NODES)] for _ in range(NUM_TASKS)]

# GA parametreleri
POP_SIZE = 30
NUM_GENERATIONS = 100
MUTATION_RATE = 0.1

# Birey: görev -> node eşleşmesi
def create_individual():
    return [random.randint(0, NUM_NODES - 1) for _ in range(NUM_TASKS)]

def create_population():
    return [create_individual() for _ in range(POP_SIZE)]

# Fitness: toplam gecikme + kapasite aşımlarına ceza
def fitness(individual):
    total_latency = 0
    node_usage = [0] * NUM_NODES
    penalty = 0

    for task_id, node_id in enumerate(individual):
        total_latency += latency_matrix[task_id][node_id]
        node_usage[node_id] += task_requirements[task_id]

    for i in range(NUM_NODES):
        if node_usage[i] > node_capacities[i]:
            penalty += (node_usage[i] - node_capacities[i]) * 5

    return 1 / (total_latency + penalty + 1)

def selection(population):
    return sorted(population, key=fitness, reverse=True)[:2]

def crossover(parent1, parent2):
    cut = len(parent1) // 2
    return parent1[:cut] + parent2[cut:]

def mutate(individual):
    if random.random() < MUTATION_RATE:
        index = random.randint(0, NUM_TASKS - 1)
        individual[index] = random.randint(0, NUM_NODES - 1)
    return individual

def evolve(population):
    new_pop = []
    for _ in range(POP_SIZE):
        p1, p2 = selection(population)
        child = crossover(p1, p2)
        child = mutate(child)
        new_pop.append(child)
    return new_pop

# Çalıştır
population = create_population()
for gen in range(NUM_GENERATIONS):
    population = evolve(population)
    best = max(population, key=fitness)
    if gen % 10 == 0:
        print(f"Gen {gen}, en iyi skor: {fitness(best):.4f}")

print("\nEn iyi çözüm:", best)