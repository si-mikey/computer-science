''' API
 hm.put('a', 1)
 hm.get('a') // 1
 hm['b'] = 1
 hm['b'] // 1
 hm.remove('a')
 hm['a'] // KeyError
'''

class HashMap:
    def __init__(self):
        self.amount_of_buckets = 10
        self.size = 0


    def put(self, key, value):
        pass
    def get(self, key):
        pass
    def remove(self, key):
        pass
    def _hash(self, key):
        pass
    def _index_of_key(self, key):
        pass
    def __getitem__(self, key):
        pass
    def __setitem__(self, key, value):
        pass

hm = HashMap()
hm.put('a', 1)
hm.put('b', 2)
print(hm.__dict__)
