# AES Decryption — Python

Decrypts AES-encrypted data using **CBC mode** with PKCS7 padding.  
This is the decryption counterpart to the AES Encryption script.

---

## Demo (CyberChef)

| Field      | Value                                                              |
|------------|--------------------------------------------------------------------|
| Input      | `5c7b032ac3c808928b44d7e80076caf07966e382a2056e5890df68b2ecaf97d9` |
| Key        | `gomycodegomycode`                                                 |
| IV         | `4567890123456`                                                     |
| Mode       | CBC                                                                |
| **Output** | **`cybersecurity is powerful`**                                    |

---

## Requirements

```bash
pip install pycryptodome
```

## Usage

```python
from aes_decryption import aes_decrypt

result = aes_decrypt(
    ciphertext_hex="5c7b032ac3c808928b44d7e80076caf07966e382a2056e5890df68b2ecaf97d9",
    key="gomycodegomycode",
    iv="4567890123456"
)
print(result)  # cybersecurity is powerful
```

## Run directly

```bash
python aes_decryption.py
```

Expected output:
```
Ciphertext (hex) : 5c7b032ac3c808928b44d7e80076caf07966e382a2056e5890df68b2ecaf97d9
Decrypted text   : cybersecurity is powerful
```

## How it works

1. The hex ciphertext is converted to bytes
2. AES-CBC decryption is applied using the key and IV
3. PKCS7 padding is removed
4. The result is decoded as a UTF-8 string

## Related
- [AES Encryption](../aes_encryption/aes_encryption.py) — matching encryption script
