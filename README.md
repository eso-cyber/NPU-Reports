# NPU-Reports

## 💡 Pillola Tecnica: SYCL & NPU Acceleration
Durante i test su architetture Intel (Meteor Lake), abbiamo confermato che il backend **SYCL** è essenziale per il riconoscimento della NPU. 
- **SYCL Device Detection**: Lo script `avvia_npu.sh` forza l'inizializzazione tramite `DEVICE=npu`.
- **IPEX-LLM**: Agisce come bridge tra le librerie OneAPI di Intel e l'interfaccia di Ollama, permettendo l'inferenza di modelli `gguf` direttamente sull'acceleratore neurale invece che sulla iGPU o CPU.
- **Porta 11434**: Se riscontri l'errore *address already in use*, assicurati di terminare i processi pendenti con `sudo pkill ollama`.

---
