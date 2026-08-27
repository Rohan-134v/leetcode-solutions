from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        
        # Maps key -> value
        self.key_val = {}
        
        # Maps key -> frequency
        self.key_freq = {}
        
        # Maps frequency -> OrderedDict of keys. 
        # OrderedDict maintains the exact order keys were used (LRU at the start).
        self.freq_keys = defaultdict(OrderedDict)

    def _update_freq(self, key: int) -> None:
        """Helper method to increase the frequency of a given key."""
        freq = self.key_freq[key]
        
        # Remove the key from its current frequency bucket
        del self.freq_keys[freq][key]
        
        # If this frequency bucket is now empty AND it was our minimum frequency,
        # we must increment our global minimum frequency.
        if not self.freq_keys[freq] and self.min_freq == freq:
            self.min_freq += 1
            
        # Update the key's frequency and add it to the new frequency bucket
        self.key_freq[key] = freq + 1
        self.freq_keys[freq + 1][key] = None # We only care about the keys in this dict

    def get(self, key: int) -> int:
        if key not in self.key_val:
            return -1
            
        # If it exists, update its frequency and return the value
        self._update_freq(key)
        return self.key_val[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
            
        if key in self.key_val:
            # Update the existing value and bump its frequency
            self.key_val[key] = value
            self._update_freq(key)
        else:
            # If we are at capacity, we must evict the LFU / LRU key
            if len(self.key_val) == self.capacity:
                # popitem(last=False) removes and returns the first inserted item (the LRU element)
                evict_key, _ = self.freq_keys[self.min_freq].popitem(last=False)
                del self.key_val[evict_key]
                del self.key_freq[evict_key]
                
            # Insert the new key-value pair with a starting frequency of 1
            self.key_val[key] = value
            self.key_freq[key] = 1
            self.min_freq = 1
            self.freq_keys[1][key] = None