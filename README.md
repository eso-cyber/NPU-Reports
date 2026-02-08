![License](https://img.shields.io) ![Go](https://img.shields.io) ![Python](https://img.shields.io) ![NPU](https://img.shields.io)

# NPU-Reports 🧠🚀

**NPU-Reports** is an open-source repository dedicated to benchmarking, analyzing, and documenting **Neural Processing Units (NPU)**. This project provides tools for hardware data extraction and performance reports for AI models (LLMs) on modern architectures like Intel Core Ultra, Apple Silicon, and Qualcomm Snapdragon.

---

## 🛠️ Features
- 📊 **LLM Benchmarking**: Real-world inference tests on NPU (Phi-3, Llama 3.1, Gemma).
- 💻 **NPU-Pro Tool**: A **Go**-based utility for hardware monitoring and control.
- 🐧 **Linux Native**: Optimized for Ubuntu with specific support for **IPEX-LLM** and Intel drivers.
- 🛡️ **Cyber Analysis**: Insights into hardware behavior during intensive AI workloads.

---

## 🚀 Quick Start

### 1. Compile the Tool (Go)
Ensure you have [Go](https://go.dev) installed, then compile the main utility:

```bash
go build -o npu-pro main.go
./npu-pro --check

