# 🚀 Learning-Python Portfolio

A structured collection of self-contained, dependency-free Python utilities designed to showcase progressive software development milestones—ranging from network integrations and JSON parsing to custom desktop interfaces and cryptographic storage logic.

---

## 📂 Repository Workspace Structure

The root repository is organized into isolated, modular directories to support cross-project scalability without environmental collision:

```text
Learning-Python/
├── .gitignore             # Global rule layer masking system/credential data
├── README.md              # Main engineering portfolio landing display
├── Currency_Converter/    # Live HTTP network data parsing module
└── RDP_Automator/         # Secure desktop automation interface utility
```

---

## 🛠️ Individual Project Milestones

### 1. 🖥️ Secure Multi-RDP Connection Manager (`/RDP_Automator/`)
A portable desktop application that simplifies and accelerates administrative Remote Desktop handshakes while heavily encrypting sensitive network credentials.

*   **Core Engineering Focus:** Object-Oriented `tkinter` desktop GUI layouts, portable rotational streaming bitwise ciphers, and native Windows subsystem processes (`subprocess`, `cmdkey`, `mstsc`).
*   **Key Technical Feats:**
    *   **Dynamic Inventory Pipeline:** Offers dynamic CRUD operations directly from the user interface, allowing users to smoothly add new profile targets or erase old ones with automated alphabetical dropdown sorting.
    *   **Zero-Leak Security Bounds:** Encrypts user credentials behind a flexible shared Master Passkey using custom ciphers, paired with a robust integrity verification check marker block.
    *   **VBS Silent Bootstrap Launcher:** Includes a `Launch_App.vbs` companion script to cleanly suppress background command prompt logs, launching the utility natively with a clean double-click shortcut.

### 2. 💱 Live Mid-Market Currency Utility (`/Currency Converter/`)
An interactive command-line currency converter that monitors real-time global exchange rates natively without downloading heavy external packages.

*   **Core Engineering Focus:** Standard network integrations, persistent error-handling loops, and structured JSON object mapping.
*   **Key Technical Feats:**
    *   **Vanilla Core Footprint:** Built entirely using native Python standard built-in networking modules (`urllib.request`, `json`), keeping code assembly completely lightweight.
    *   **Keyless API Streaming:** Leverages direct open-access HTTP requests to gather fast mid-market exchange evaluations instantly.
    *   **Input Exception Interceptors:** Employs persistent control validation loops (`while True` / `try-except`) to intercept invalid values or dead network requests gracefully.

---

## ⚙️ How to Review and Run Projects Locally

All programs contained in this repository adhere strictly to a **zero-dependency** design constraint. You only need a standard Python 3 interpreter environment installed—no `pip install` commands required.

1. Clone the project repository to your environment:
   ```bash
   git clone https://github.com
   cd Learning-Python
   ```
2. Navigate into your target module of choice and execute the root wrapper script:
   ```bash
   # Running the Currency utility
   python Currency_Converter/converter.py

   # Running the RDP Automation system
   python RDP_Automator/rdp_launcher.py
   ```
