from bitcoin import *

#Generate private key
my_private_key = random_key()
#display private key
print("Private Key: %sn" % my_private_key)
#add spaces
print("    ")

#Generate public key
my_public_key = privtopub(my_private_key)
#display pubilc key
print("Public Key: %sn" % my_public_key)
#add spaces
print("    ")

#Create a bitcoin address
my_bitcoin_address = pubtoaddr(my_public_key)
print("Bitcoin Address: %sn" % my_bitcoin_address)