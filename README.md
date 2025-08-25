# 🐍 MicroPython IntelliSense Stubs for TI‑84 Plus CE Python Edition

## 📖 Overview
This project provides a **complete set of MicroPython `.py` stub files** for use in editors like **VS Code** to enable:
- **Full IntelliSense** (autocompletion, hover docs, signature help)
- **Accurate linting** for TI‑84 Plus CE Python Edition’s built‑in modules
- **General MicroPython API coverage** for portable code
- **Optional safe emulation** of core functions so code can run on PC without hardware

It combines:
- **TI‑84‑specific modules** (`ti_system`, `ti_hub`, `ti_draw`, etc.)
- **General MicroPython modules** (`machine`, `utime`, `uos`, `network`, etc.)
- **Underused/advanced modules** (`ure`, `ujson`, `uasyncio`, `uzlib`, etc.)
- **Pyboard/STM32 modules** (`pyb`, `stm`) for cross‑port compatibility

---

## ✨ Features
- 📦 **Stubbed APIs** for *most* MicroPython modules
- 🖥 **PC‑safe emulation** for common functions (e.g., `utime.sleep`, `uos.listdir`)
- 🛠 **Accurate signatures** matching MicroPython docs
- 📚 **Docstrings** with TI‑84 quirks and notes
- 🔍 **Import‑aware linting** when paired with VS Code + Pylance
- 🔄 **Cross‑port development** — write once, run on TI‑84 or other MicroPython boards

---

## 📂 Included Modules

### TI‑84 Plus CE Python Edition
- `ti_system`
- `ti_hub`
- `ti_draw`
- `ti_plotlib`
- `ti_rover`
- `ti_sensor`

### General MicroPython Core
- `machine`
- `utime` / `time`
- `uos`
- `network`
- `random`
- `micropython`
- `gc`
- `sys`
- `errno`
- `select`
- `struct` / `ustruct`
- `binascii`
- `hashlib`
- `io` / `uio`

### Underused / Advanced
- `ure`
- `ujson`
- `uasyncio`
- `uzlib`
- `uheapq`
- `utimeq`
- `ubluetooth`
- `framebuf`
- `onewire`
- `ds18x20`

### Pyboard / STM32 Specific
- `pyb`
- `stm` (pre‑populated with STM32F405 register constants)

---

## 🚀 Getting Started

### 1. Clone or Download
```bash
git clone https://github.com/killercraft-thecoder/vscode-micropython-intellisense/