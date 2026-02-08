#!/bin/bash
# Launcher per Intel NPU via IPEX-LLM
export DEVICE=npu
export OLLAMA_NUM_GPU=1
export IPEX_LLM_NPU_DISABLE_ASYNC_QUEUE=1

# Definisco il percorso di Ollama (punto alla tua cartella Downloads)
OLLAMA_PATH="$HOME/Downloads/ollama-ipex-llm-2.2.0-ubuntu/ollama"

echo "Pulisco processi Ollama..."
sudo snap stop ollama 2>/dev/null

echo "Avvio Ollama su NPU..."
# Avvio usando il percorso assoluto
$OLLAMA_PATH serve & 
sleep 5
$OLLAMA_PATH run phi3 "Hardware check: NPU active?"
