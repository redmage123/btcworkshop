import hashlib
import ecdsa
import utils

# This method takes a hexadecimal SHA-256 generated key and 
# uses the Bitcoin Base58 Check algorithm to return a WIF
# bitcoin address.

def privateKeyToWif(key_hex):    
    return utils.base58CheckEncode(0x80, key_hex.decode('hex'))
        
# This method decodes a string 
def privateKeyToPublicKey(s):
    sk = ecdsa.SigningKey.from_string(s.decode('hex'), curve=ecdsa.SECP256k1)
    vk = sk.verifying_key
    return ('\04' + sk.verifying_key.to_string()).encode('hex')
                    
def pubKeyToAddr(s):
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(hashlib.sha256(s.decode('hex')).digest())
    return utils.base58CheckEncode(0, ripemd160.digest())

def keyToAddr(s):
    return pubKeyToAddr(privateKeyToPublicKey(s))

 # Warning: this random function is not cryptographically strong and is just for example
private_key = ''.join(['%x' % random.randrange(16) for x in range(0, 64)])
                      print keyUtils.privateKeyToWif(private_key)
                      print keyUtils.keyToAddr(private_key)

def makeSignedTransaction(privateKey, outputTransactionHash, sourceIndex, scriptPubKey, outputs):

    myTxn_forSig = (makeRawTransaction(outputTransactionHash, sourceIndex, scriptPubKey, outputs)
                     + "01000000") # hash code

    s256 = hashlib.sha256(hashlib.sha256(myTxn_forSig.decode('hex')).digest()).digest()
    sk = ecdsa.SigningKey.from_string(privateKey.decode('hex'), curve=ecdsa.SECP256k1)
    sig = sk.sign_digest(s256, sigencode=ecdsa.util.sigencode_der) + '\01' # 01 is hashtype
    pubKey = keyUtils.privateKeyToPublicKey(privateKey)
    scriptSig = utils.varstr(sig).encode('hex') + utils.varstr(pubKey.decode('hex')).encode('hex')
    signed_txn = makeRawTransaction(outputTransactionHash, sourceIndex, scriptSig, outputs)
    verifyTxnSignature(signed_txn)
    return signed_txn

# Makes a transaction from the inputs
# outputs is a list of [redemptionSatoshis, outputScript]
def makeRawTransaction(outputTransactionHash, sourceIndex, scriptSig, outputs):
    def makeOutput(data):
       redemptionSatoshis, outputScript = data
       return (struct.pack("<Q", redemptionSatoshis).encode('hex') +
                           '%02x' % len(outputScript.decode('hex')) + outputScript)
    formattedOutputs = ''.join(map(makeOutput, outputs))

    return ("01000000" + # 4 bytes version "01" + # varint for number of inputs outputTransactionHash.decode('hex')[::-1].encode('hex') +
            # reverse outputTransactionHash struct.pack('<L', sourceIndex).encode('hex') +
            '%02x' % len(scriptSig.decode('hex')) + scriptSig + "ffffffff" +
            # sequence "%02x" % len(outputs) + # number of outputs formattedOutputs +
            "00000000" # lockTime)
