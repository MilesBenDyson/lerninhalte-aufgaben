import json
import hashlib
import random
import string

pw = ['alexander', 'abms4088214', 'Abms409922!', 'r2j3rfu98ewdfr93429§)§(', '12345', 'ASJHDFH']

salzliste = string.punctuation + string.ascii_letters + string.digits
#zu Lehrzwecken:
pw_bytes = []

pw_hashes = []
salt_ok = []
for p in pw:
    salt = ""
    for i in range(16):
        salt += random.choice(salzliste)
    p_and_salt = p, salt
    salt_ok.append(p_and_salt)
    ps = p + salt
    b = ps.encode('utf-8')
    pw_bytes.append(b)
    h = hashlib.sha256(b)
    hexa = h.hexdigest()
    pw_hashes.append(hexa)

with open('hashes_list.json', 'w', encoding='utf-8') as f:
    json.dump(pw_hashes, f, ensure_ascii=False, indent=2)

#zu testzwecken:
print(salt_ok)