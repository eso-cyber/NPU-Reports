# Intel NPU Setup Guide (Ubuntu 24.04+)

To enable the NPU on Intel Meteor Lake architectures, follow these steps:

## 1. System Requirements
- Hardware: Intel Core Ultra (Meteor Lake) or newer.
- Kernel: Linux 6.8+ (6.11 recommended).

## 2. Install Compute Runtime (Level Zero)
The NPU communicates via the Level Zero interface.

```bash
sudo apt update
sudo apt install intel-opencl-icd intel-level-zero-gpu level-zero level-zero-dev
