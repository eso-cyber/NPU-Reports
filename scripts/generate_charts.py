import pandas as pd
import matplotlib.pyplot as plt
import os

csv_file = "benchmarks/results.csv"
if not os.path.exists(csv_file):
    print("CSV not found, creating a dummy plot...")
    # Crea un grafico vuoto di sicurezza se il CSV non c'è ancora su GitHub
    plt.figure()
    plt.title("No Data Available Yet")
else:
    df = pd.read_csv(csv_file)
    plt.figure(figsize=(10, 6))
    plt.bar(df['Model'], df['t/s'], color='skyblue')
    plt.ylabel('Tokens per Second')
    plt.title('NPU Performance Comparison')

os.makedirs("assets", exist_ok=True)
plt.savefig("assets/benchmark_chart.png")
print("✅ Chart saved to assets/benchmark_chart.png")
