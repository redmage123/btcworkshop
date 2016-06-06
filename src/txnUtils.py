#!/usr/bin/env python
# Makes a transaction from the inputs
# outputs is a list of [redemptionSatoshis, outputScript]
def makeRawTransaction(outputTransactionHash, sourceIndex, scriptSig, outputs):
    def makeOutput(data):
        redemptionSatoshis, outputScript = data
        return (struct.pack("<Q", redemptionSatoshis).encode('hex') +
                '%02x' % len(outputScript.decode('hex')) + outputScript)
        formattedOutputs = ''.join(map(makeOutput, outputs))
    return ("01000000" + # 4 bytes version
            "01" + # varint for number of inputs
            outputTransactionHash.decode('hex')[::-1].encode('hex') + # reverse outputTransactionHash
            struct.pack('<L', sourceIndex).encode('hex') +
                        '%02x' % len(scriptSig.decode('hex')) + scriptSig +
                        "ffffffff" + # sequence
                        "%02x" % len(outputs) + # number of outputs
                        formattedOutputs +
                        "00000000" # lock
           )
