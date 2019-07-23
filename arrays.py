class Array:
    def __init__(self, capacity=10):
        self._capacity = capacity
        self._length = 0
        self._array = self._make_array(capacity)

    def _make_array(self, capacity):
        self._capacity = capacity
        return [None] * capacity

    def append(self, ele):
        if self._capacity == self._length:
            tmp_array = self._make_array(2 * self._capacity)
            for idx in range(self._length):
                tmp_array[idx] = self._array[idx]
            self._array = tmp_array
        self._array[self._length] = ele
        self._length += 1
