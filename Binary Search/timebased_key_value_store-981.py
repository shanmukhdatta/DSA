## comment is the problem statement of the leetcode 981 completely in python
## leetcode 981. Time Based Key-Value Store
## Design a key-value store with set and get methods. The set method accepts a key, a value, and a timestamp. The get method accepts a key and a timestamp and returns the value associated with that key with the largest timestamp less than or equal to the given timestamp. If there is no such value, return an empty string.

from _typeshed import importlib
class solution:
    def __init__(self):
        self.store = {}
    def set(self, key : str, value: str , timestamp : int):
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp,value))
        
    def get(self, key : str, timestamp : int)-> str:
        res = ""
        time_value = self.store.get(key,[]) ## stores all values , timestapms are stored in sorted order
        l,r = 0, len(time_value)-1

        while l<=r:
            m = (l+r)//2 ##
            if time_value[m][0] == timestamp: ## if mid time is equal to timestamp
                return time_value[m][1]
            elif time_value[m][0] < timestamp: ## if mid time is less than timestamp
                res = time_value[m][1]
                l = m+1
            else: ## if mid time is greater than timestamp
                r = m-1
        return res

