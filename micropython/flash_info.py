# flash_info.py
# A cross-platform diagnostic tool for RP2040 and ESP32
# Collaborative update - 2026

from binascii import hexlify
from machine import freq, Pin, unique_id
from math import ceil
import sys
import uos

def get_clock_speed() -> int:
    return ceil(freq() / 1_000_000)

# 1. Gather Platform Information
sys_info = uos.uname()
sys_platform = sys.platform  # e.g., 'rp2' or 'esp32'
machine_type = sys_info[4].strip()
os_version = sys.version.split(';')[1].strip()

# 2. Universal Serial Number Extraction
# This works on both bytes objects by converting them cleanly to a hex string
serial_no = hexlify(unique_id()).decode('utf-8')

# 3. Universal Storage Calculation
try:
    f_bsize, f_frsize, f_blocks, f_bfree, *rest = uos.statvfs('/')
    total_storage = f_bsize * f_blocks
    free_storage = f_bsize * f_bfree
    storage_msg = f"Total Storage: {total_storage:,} bytes\nFree Storage:  {free_storage:,} bytes"
except Exception:
    storage_msg = "Storage Info: Unable to read filesystem"

# 4. Dynamic LED Assignment
led = None
is_neopixel = False

if sys_platform == 'rp2':
    if 'Pico W' in machine_type:
        led = Pin("LED", Pin.OUT)
    else:
        led = Pin(25, Pin.OUT)  # Standard Pico and WeAct RP2040
elif sys_platform == 'esp32':
    # Standard ESP32 dev boards usually use Pin 2 for the blue LED
    # Note: If your specific ESP32 uses a NeoPixel, this won't light up, 
    # but it won't crash the script either.
    led = Pin(2, Pin.OUT)

# 5. Output Data
print('=' * 40)
print('Microcontroller Diagnostic Utility')
print('=' * 40)
print(f'Platform:       {sys_platform.upper()}')
print(f'Machine:        {machine_type}')
print(f'Firmware:       {os_version}')
print(f'Clock Speed:    {get_clock_speed()} MHz')
print(f'Serial Number:  {serial_no}')
print(storage_msg)
print('=' * 40)

# 6. Safe Execution of the Blink Test
if led is not None:
    try:
        led.value(0)
        for _ in range(10):
            led.toggle()
            import time
            time.sleep(0.5)
        led.value(0)
    except Exception as e:
        print(f"LED blink failed: {e}")
else:
    print("No standard LED configured for this target architecture.")