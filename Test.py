import Crypto.Hash.SHA256 as SHA256
hash = SHA256.new('ilijailja'.encode("utf-8"))
print(hash.hexdigest())