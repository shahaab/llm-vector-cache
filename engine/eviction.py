import time
from collections import OrderedDict


class LRUEvictionPolicy:
    def __init__(self):
        self.access_order = OrderedDict()

    def record_access(self, key: str):
        self.access_order.pop(key, None)
        self.access_order[key] = time.time()

    def evict(self) -> str:
        if self.access_order:
            key, _ = self.access_order.popitem(last=False)
            return key
        return None

    def remove(self, key: str):
        self.access_order.pop(key, None)
