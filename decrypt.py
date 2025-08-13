import base64
import time
import json

def decrypt_assessment_data(file_path, key=None):
    from cryptography.fernet import Fernet
    
    if key is None:
        base_key = base64.b64decode(b'ZmRhdGFfZW5jcnlwdGlvbl9rZXlfZm9yX3NlY3VyaXR5X3Rlc3RfMjAyNA==').decode()
        key = base64.urlsafe_b64encode(base_key[:32].ljust(32, '0').encode())
    
    fernet = Fernet(key)
    
    with open(file_path, 'rb') as f:
        encrypted_data = f.read()
    
    decrypted_data = fernet.decrypt(encrypted_data)
    return json.loads(decrypted_data.decode())

if __name__ == "__main__":
    try:
        data = decrypt_assessment_data('.sys_c2VjdXJp.dat')
        print(json.dumps(data, indent=2))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        try:
            input("Press Enter to exit...")
        except Exception:
            # Fallback when no console is attached (e.g., pythonw/Explorer)
            time.sleep(10)