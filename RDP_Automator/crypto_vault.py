import base64

def derive_key(master_key, length=32):
    """Generates a consistent byte key from a master password string."""
    # Simple deterministic hash padding to avoid external dependencies
    key = bytearray(master_key.encode('utf-8'))
    while len(key) < length:
        key.extend(str(len(key)).encode('utf-8'))
    return bytes(key[:length])

def encrypt_password(plain_password, master_key):
    """Encrypts text using a portable bitwise XOR rotation algorithm."""
    if not plain_password or not master_key:
        return ""
    try:
        key = derive_key(master_key)
        plain_bytes = plain_password.encode('utf-8')
        encrypted_bytes = bytearray()
        
        # Rotational XOR streaming cipher
        for i, byte in enumerate(plain_bytes):
            key_byte = key[i % len(key)]
            encrypted_bytes.append(byte ^ key_byte)
            
        return base64.b64encode(encrypted_bytes).decode('utf-8')
    except Exception as e:
        print(f"Portable encryption failed: {e}")
        return ""

def decrypt_password(encrypted_base64, master_key):
    """Decrypts text back using the exact same master key validation context."""
    if not encrypted_base64 or not master_key:
        return ""
    try:
        key = derive_key(master_key)
        encrypted_bytes = base64.b64decode(encrypted_base64)
        decrypted_bytes = bytearray()
        
        for i, byte in enumerate(encrypted_bytes):
            key_byte = key[i % len(key)]
            decrypted_bytes.append(byte ^ key_byte)
            
        return decrypted_bytes.decode('utf-8')
    except Exception as e:
        print(f"Portable decryption failed: {e}")
        return ""
