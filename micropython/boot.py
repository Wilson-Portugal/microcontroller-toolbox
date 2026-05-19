# boot.py
# Part of the Microcontroller Toolbox Fleet System
# Runs on system initialization

import sys
import gc

# 1. Optimize the system path
# This allows you to import tools from custom subdirectories if your project grows
if '/flash' not in sys.path:
    sys.path.append('/flash')

# 2. Run Garbage Collection early
# Ensures maximum available RAM before main application scripts execute
gc.collect()

print("[BOOT] Hardware initialized. Memory optimized.")