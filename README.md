# Microcontroller Toolbox

A centralized repository for deploying, diagnosing, and managing microcontrollers across the local fleet. Managed natively from the **Guarda** server.

## 📂 Repository Structure

- **`micropython/`**: Core Python scripts optimized for microcontrollers (RP2040, ESP32).
  - `boot.py`: Initial hardware boot configuration and RAM optimization.
  - `flash_info.py`: Cross-platform diagnostic tool for architecture identification.
- **`shell-scripts/`**: Automation scripts running on Linux nodes.
  - `deploy-fleet.sh`: Main script for synchronizing updates across network-connected hardware.

## 🚀 How to Deploy Changes

To commit modifications and update the global repository on GitHub, execute the deployment script from your terminal:

```bash
~/bin/deploy-microcontroller-toolbox.sh
