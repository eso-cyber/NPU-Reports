import requests
import time
import json
import csv
from datetime import datetime

# Configurazione
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.1:latest"
PROMPT = "Spiega brevemente cos'è una NPU in ambito AI."
OUTPUT_FILE = "benchmarks/results.csv"

def run_benchmark():
    payload = {
        "model": MODEL,
        "prompt": PROMPT,
        "stream": False
    }
    
    print(f"🚀 Avvio benchmark per il modello: {MODEL}...")
    start_time = time.time()
    
    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        end_time = time.time()
        
        data = response.json()
        duration = end_time - start_time
        
        # Ollama fornisce le statistiche in nanosecondi, le convertiamo
        total_duration = data.get("total_duration", 0) / 1e9
        eval_count = data.get("eval_count", 0) # Numero di token generati
        tokens_per_sec = eval_count / total_duration if total_duration > 0 else 0
        
        print(f"✅ Completato in {total_duration:.2f}s")
        print(f"📊 Performance: {tokens_per_sec:.2f} t/s")

        # Salvataggio dati
        with open(OUTPUT_FILE, mode='a', newline='') as f:
            writer = csv.writer(f)
            # Header se il file è nuovo
            if f.tell() == 0:
                writer.writerow(["Timestamp", "Model", "Tokens", "Duration(s)", "Tokens/s"])
            writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M"), MODEL, eval_count, round(total_duration, 2), round(tokens_per_sec, 2)])
            
    except Exception as e:
        print(f"❌ Errore durante il benchmark: {e}")

if __name__ == "__main__":
    run_benchmark()
