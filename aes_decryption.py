from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import binascii

def aes_decrypt(ciphertext_hex, key, iv, mode=AES.MODE_CBC):
    """
    AES Decryption (CBC Mode)

    Parameters:
        ciphertext_hex (str): Hex-encoded ciphertext
        key (str): Decryption key (UTF-8 string)
        iv  (str): Initialization vector (UTF-8 string)
        mode: AES mode (default: AES.MODE_CBC)

    Returns:
        str: Decrypted plaintext
    """
    key_bytes = key.encode('utf-8')
    iv_bytes  = iv.encode('utf-8')
    ciphertext = binascii.unhexlify(ciphertext_hex)

    cipher    = AES.new(key_bytes, mode, iv_bytes)
    decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted.decode('utf-8')


if __name__ == "__main__":
    # -------------------------------------------------------
    # Settings (matching CyberChef screenshot)
    # -------------------------------------------------------
    KEY            = "gomycodegomycode"   # 16-byte UTF-8 key  (AES-128)
    IV             = "4567890123456"      # IV from CyberChef  (UTF-8)
    CIPHERTEXT_HEX = "5c7b032ac3c808928b44d7e80076caf07966e382a2056e5890df68b2ecaf97d9"

    plaintext = aes_decrypt(CIPHERTEXT_HEX, KEY, IV)
    print(f"Ciphertext (hex) : {CIPHERTEXT_HEX}")
    print(f"Decrypted text   : {plaintext}")
