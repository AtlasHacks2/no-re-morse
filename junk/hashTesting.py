import hashlib
string="pass"
encoded=string.encode()
result = hashlib.sha256(encoded)
print("String : ", end ="")
print(string)
print("Hash Value : ", end ="")
print(result)
print("Hexadecimal equivalent: ", result.hexdigest())
print(type(result.hexdigest()))
print("Digest Size : ", end ="")
print(result.digest_size)
print("Block Size : ", end ="")
print(result.block_size)