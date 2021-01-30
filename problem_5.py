import hashlib
import datetime
import json

class Block:
    
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp  # Greenwich Mean Time
        self.data = data
        self.previous_hash = previous_hash
        self.now_hash = self.calc_hash()
        self.next = None
        
    def calc_hash(self):
        sha = hashlib.sha256()
        
    # join the block data to prepare encoding
        joined_data = {
            'timestamp'        : str(self.timestamp),\
            'data'             : self.data,\
            'previous_hash'    : self.previous_hash
        }
        json_text = json.dumps(joined_data, sort_keys=True)
        hash_str = json_text.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()
    
    def __repr__(self):
        return str(self.timestamp) + str(" | ") +        str(self.data) + str(" | ") + str(self.previous_hash) +        str(" | ") + str(self.now_hash)

class BlockChain(object):
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def appendBlock(self, data):
        if data is None or data =="":
            return
        elif self.head is None:
            self.head = Block(datetime.datetime.utcnow(), data, 0)
            self.tail = self.head
        else:
            self.tail.next = Block(datetime.datetime.utcnow(), data, self.tail.now_hash)
            self.tail = self.tail.next
        return
    
    def toList(self):
        out = []
        block = self.head
        while block:
            out.append([block])
            block = block.next
        return out

def main():
    # Test Case 1: Normal uses
    bl = BlockChain()
    data1 = "Data: First Blockchain block"
    data2 = "Data: Second Blockchain block"
    data3 = "Data: Third Blockchain block"
    bl.appendBlock(data1)
    bl.appendBlock(data2)
    bl.appendBlock(data3)
    print("|time | data | previous hash | hash|")
    for lists in bl.toList(): # Print block chain
         print(lists)
            
    # Test Case 2: No data has been passed
    bl1 = BlockChain()
    bl1.appendBlock("")
    bl1.appendBlock("")
    print(bl1.toList())  # empty block chain
    
    #Test Case 3: No data has been passed
    bl2 = BlockChain()
    bl2.appendBlock(None)
    bl2.appendBlock(None)
    print(bl2.toList())  # empty block chain
if __name__ == "__main__":
    main()