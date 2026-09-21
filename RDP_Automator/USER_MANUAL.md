# 🖥️ Shared Multi-RDP Connection Manager

A lightweight, secure desktop utility designed to manage automated Remote Desktop (RDP) connections across multiple remote targets without requiring manual credential entry every session.

---

## 🔒 Security Information
All connection credentials (IP Addresses, Usernames, and Passwords) are scrambled using a robust mathematical encryption engine before being saved locally. 
* Your passwords are never stored in plain text.
* To view, update, or launch connections, you must possess the shared **Master Cryptographic Passkey**.

---

## 🚀 Step-by-Step Operation Guide

### Step 1: Extract the Project Folder
Before launching the application for the first time, make sure you extract the files:
1. Right-click the distributed `.zip` folder.
2. Select **Extract All...** and choose your preferred destination folder (e.g., your Desktop).
3. Open the newly extracted folder.

### Step 2: Launch the Application
Do not worry about opening command lines or terminal windows. 
* Simply locate the file named **`Launch_App.vbs`** and **double-click it**.
* The program will execute silently in the background and present the Passkey prompt.

### Step 3: Authenticate with the Master Passkey
1. When the window pops up asking for the **Shared Cryptographic Key**, type your designated passkey.
2. Click **OK**.
   * *Note: You have 3 attempts to input the key correctly. If the key is typed incorrectly, the program will deny access to protect the integrity of the data.*

### Step 4: Selecting a Target Profile
1. Use the **dropdown menu** at the top of the interface window to select your target node (Profiles are labeled alphabetically: **A, B, E, H, I, J, K, N, O, P, Q, R, S, T, U, V**).
2. Choosing a letter profile will instantly load any saved IP addresses and usernames associated with that machine.

### Step 5: Connecting to the Remote Desktop
1. Verify that the correct target profile letter is selected.
2. Click the green **Connect Now** button.
3. The program will securely stage your credentials into the Windows network subsystem and immediately launch the native Windows Remote Desktop client (`mstsc.exe`). You will log in completely automatically.

---

## 🛠️ Modifying or Adding New Profiles (For Administrators)
If connection parameters change or a new remote device needs configuration:
1. Select the target **Letter Profile** from the dropdown menu.
2. Overwrite or fill in the **IP Address**, **Username**, and **Password** text boxes with the new values.
3. Click the **Save This Profile** button. 
4. The system will encrypt the updated data immediately and update the local profile storage database safely.
