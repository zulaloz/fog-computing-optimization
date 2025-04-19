# 🌫️ Fog Computing Task Allocation Optimization using Genetic Algorithm

This project demonstrates the use of a genetic algorithm to optimize task allocation in a fog computing environment.

## ⚙️ Features

- Simulates task-to-node allocation with random CPU requirements and network latencies
- Evaluates population fitness based on total latency and node capacity violations
- Uses selection, crossover, and mutation to evolve better solutions

## 📈 Optimization Goals

- Minimize total latency across all task allocations
- Prevent overloading fog nodes beyond their resource capacities
- Balance computational load across available nodes

## 🛠️ Technologies

- Python 3
- Standard libraries (no external dependencies)

## 🚀 How to Run

```bash
python fog_optimization.py
```

## 👩‍💻 Author

Zülal Özyazıcıoğlu  
KTÜ – Computer Engineering  


---

## 📊 Sample Output

```
Gen 0, en iyi skor: 0.0153
Gen 10, en iyi skor: 0.0254
Gen 20, en iyi skor: 0.0340
Gen 30, en iyi skor: 0.0450
Gen 40, en iyi skor: 0.0532
Gen 50, en iyi skor: 0.0621
Gen 60, en iyi skor: 0.0710
Gen 70, en iyi skor: 0.0804
Gen 80, en iyi skor: 0.0881
Gen 90, en iyi skor: 0.0945
Gen 100, en iyi skor: 0.0992

En iyi çözüm: [2, 0, 3, 1, 0, 2, 1, 3, 2, 0]
```

---

## 🖼️ Fitness Trend

![Fitness Trend](images/fitness_over_generations.png)