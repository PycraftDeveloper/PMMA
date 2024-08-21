import numpy as _numpy

class Stack:
    def __init__(self, max_size=None):
        self.frames = []
        self.max_size = max_size
        self.has_changed = False

    def push(self, item):
        if not self.is_full():
            self.has_changed = True
            self.frames.append(item)

    def pop(self):
        if not self.is_empty():
            self.has_changed = True
            return self.frames.pop()

    def peek(self):
        if not self.is_empty():
            return self.frames[-1]

    def is_empty(self):
        return len(self.frames) == 0

    def is_full(self):
        if self.max_size is None:
            return False
        return len(self.frames) >= self.max_size

    def size(self):
        return len(self.frames)

    def clear(self):
        self.has_changed = True
        self.frames = []

    def changed(self):
        value = self.has_changed
        self.has_changed = False
        return value

class Queue:
    def __init__(self, max_size=None):
        self.frames = []
        self.max_size = max_size
        self.has_changed = False

    def enqueue(self, item):
        if not self.is_full():
            self.has_changed = True
            self.frames.append(item)

    def dequeue(self):
        if not self.is_empty():
            self.has_changed = True
            return self.frames[0]

    def peek(self):
        if not self.is_empty():
            return self.frames[0]

    def is_empty(self):
        return len(self.frames) == 0

    def is_full(self):
        if self.max_size is None:
            return False
        return len(self.frames) >= self.max_size

    def size(self):
        return len(self.frames)

    def clear(self):
        self.has_changed = True
        self.frames = []

    def changed(self):
        value = self.has_changed
        self.has_changed = False
        return value

class CircularQueue:
    def __init__(self, size):
        self.max_size = size
        self.frames = [0] * size
        self.front = -1
        self.rear = -1
        self.has_changed = False

    def clear(self):
        self.has_changed = True
        self.frames = [0] * self.max_size
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if self.is_empty():
            self.front = 0
            self.rear = 0
            self.frames[self.rear] = item
        else:
            self.has_changed = True
            self.rear = (self.rear + 1) % self.max_size
            if self.is_full():
                self.rear = (self.rear - 1 + self.max_size) % self.max_size
            else:
                self.frames[self.rear] = item

    def dequeue(self):
        if not self.is_empty():
            self.has_changed = True
            item = self.frames[self.front]
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front = (self.front + 1) % self.max_size

            return item

    def peek(self):
        if not self.is_empty():
            return self.frames[self.front]

    def size(self):
        if self.is_empty():
            return 0
        elif self.front <= self.rear:
            return self.rear - self.front + 1
        else:
            return self.max_size - self.front + self.rear + 1

    def is_empty(self):
        return self.front == -1 and self.rear == -1

    def is_full(self):
        rear = (self.rear + 1) % self.max_size
        return rear == self.front

    def changed(self):
        value = self.has_changed
        self.has_changed = False
        return value

class PriorityQueue:
    """higher value, higher priority"""
    def __init__(self):
        # Initialize an empty list to store the heap as an array of tuples (priority, value)
        self.heap = _numpy.array([], dtype=[('priority', _numpy.float64), ('value', object)])
        self.has_changed = False

    def enqueue(self, value, priority):
        """Insert a new value with the given priority into the priority queue."""
        # Append the new (priority, value) tuple to the heap
        new_item = _numpy.array([(priority, value)], dtype=self.heap.dtype)
        self.heap = _numpy.append(self.heap, new_item)
        # Perform up-heap bubbling to maintain the max-heap property based on priority
        self._sift_up(len(self.heap) - 1)
        self.has_changed = True

    def dequeue(self):
        """Remove and return the value with the highest priority from the queue."""
        if len(self.heap) != 0:
            self.has_changed = True
            # The root of the heap (index 0) has the maximum priority
            max_value = self.heap[0]['value']

            # Move the last element to the root and then heapify down
            self.heap[0] = self.heap[-1]
            self.heap = _numpy.delete(self.heap, -1)

            # Perform down-heap bubbling to maintain the max-heap property
            self._sift_down(0)

            return max_value

    def peek_next_priority(self):
        """Return the highest priority value without removing it from the queue."""
        if len(self.heap) != 0:
            return self.heap[0]['priority']

    def peek(self):
        """Return the value with the highest priority without removing it from the queue."""
        if len(self.heap) != 0:
            return self.heap[0]['value']

    def _sift_up(self, index):
        """Move the element at the given index up to its proper position based on priority."""
        parent = (index - 1) // 2
        if index > 0 and self.heap[index]['priority'] > self.heap[parent]['priority']:
            self.heap[[index, parent]] = self.heap[[parent, index]]
            self._sift_up(parent)

    def _sift_down(self, index):
        """Move the element at the given index down to its proper position based on priority."""
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left]['priority'] > self.heap[largest]['priority']:
            largest = left
        if right < len(self.heap) and self.heap[right]['priority'] > self.heap[largest]['priority']:
            largest = right

        if largest != index:
            self.heap[[index, largest]] = self.heap[[largest, index]]
            self._sift_down(largest)

    def is_empty(self):
        """Return True if the queue is empty, False otherwise."""
        return len(self.heap) == 0

    def size(self):
        """Return the number of elements in the queue."""
        return len(self.heap)

    def clear(self):
        """Remove all elements from the queue."""
        self.heap = _numpy.array([], dtype=self.heap.dtype)
        self.has_changed = True

    def changed(self):
        value = self.has_changed
        self.has_changed = False
        return value

class InvertedPriorityQueue:
    """lower value, higher priority"""
    def __init__(self):
        # Initialize an empty list to store the heap as an array of tuples (priority, value)
        self.heap = _numpy.array([], dtype=[('priority', _numpy.float64), ('value', object)])
        self.has_changed = False

    def enqueue(self, value, priority):
        """Insert a new value with the given priority into the priority queue."""
        # Append the new (priority, value) tuple to the heap
        new_item = _numpy.array([(priority, value)], dtype=self.heap.dtype)
        self.heap = _numpy.append(self.heap, new_item)
        # Perform up-heap bubbling to maintain the min-heap property based on priority
        self._sift_up(len(self.heap) - 1)
        self.has_changed = True

    def dequeue(self):
        """Remove and return the value with the highest priority (lowest priority value) from the queue."""
        if len(self.heap) != 0:
            self.has_changed = True
            # The root of the heap (index 0) has the minimum priority
            min_value = self.heap[0]['value']

            # Move the last element to the root and then heapify down
            self.heap[0] = self.heap[-1]
            self.heap = _numpy.delete(self.heap, -1)

            # Perform down-heap bubbling to maintain the min-heap property
            self._sift_down(0)

            return min_value

    def peek_next_priority(self):
        """Return the lowest priority value (highest priority) without removing it from the queue."""
        if len(self.heap) != 0:
            return self.heap[0]['priority']

    def peek(self):
        """Return the value with the highest priority (lowest priority value) without removing it from the queue."""
        if len(self.heap) != 0:
            return self.heap[0]['value']

    def _sift_up(self, index):
        """Move the element at the given index up to its proper position based on priority."""
        parent = (index - 1) // 2
        if index > 0 and self.heap[index]['priority'] < self.heap[parent]['priority']:
            self.heap[[index, parent]] = self.heap[[parent, index]]
            self._sift_up(parent)

    def _sift_down(self, index):
        """Move the element at the given index down to its proper position based on priority."""
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left]['priority'] < self.heap[smallest]['priority']:
            smallest = left
        if right < len(self.heap) and self.heap[right]['priority'] < self.heap[smallest]['priority']:
            smallest = right

        if smallest != index:
            self.heap[[index, smallest]] = self.heap[[smallest, index]]
            self._sift_down(smallest)

    def is_empty(self):
        """Return True if the queue is empty, False otherwise."""
        return len(self.heap) == 0

    def size(self):
        """Return the number of elements in the queue."""
        return len(self.heap)

    def clear(self):
        """Remove all elements from the queue."""
        self.heap = _numpy.array([], dtype=self.heap.dtype)
        self.has_changed = True

    def changed(self):
        value = self.has_changed
        self.has_changed = False
        return value

class PriorityList:
    """higher value, higher priority"""
    def __init__(self):
        # Initialize an empty list to store the heap as an array of tuples (priority, value)
        self.heap = _numpy.array([], dtype=[('priority', _numpy.float64), ('value', object)])
        self.has_changed = False

    def enqueue(self, value, priority):
        """Insert a new value with the given priority into the priority queue."""
        # Append the new (priority, value) tuple to the heap
        new_item = _numpy.array([(priority, value)], dtype=self.heap.dtype)
        self.heap = _numpy.append(self.heap, new_item)
        # Perform up-heap bubbling to maintain the max-heap property based on priority
        self._sift_up(len(self.heap) - 1)
        self.has_changed = True

    def dequeue(self):
        """Remove and return the value with the highest priority from the queue."""
        values = []
        priority = self.peek_next_priority()
        while not self.is_empty() and self.peek_next_priority() == priority:
            # The root of the heap (index 0) has the maximum priority
            max_value = self.heap[0]['value']

            # Move the last element to the root and then heapify down
            self.heap[0] = self.heap[-1]
            self.heap = _numpy.delete(self.heap, -1)

            # Perform down-heap bubbling to maintain the max-heap property
            self._sift_down(0)

            values.append(max_value)
            self.has_changed = True
        return values

    def peek_next_priority(self):
        """Return the highest priority value without removing it from the queue."""
        if len(self.heap) != 0:
            return self.heap[0]['priority']

    def peek(self):
        """Return the value with the highest priority without removing it from the queue."""
        if len(self.heap) != 0:
            return self.heap[0]['value']

    def _sift_up(self, index):
        """Move the element at the given index up to its proper position based on priority."""
        parent = (index - 1) // 2
        if index > 0 and self.heap[index]['priority'] > self.heap[parent]['priority']:
            self.heap[[index, parent]] = self.heap[[parent, index]]
            self._sift_up(parent)

    def _sift_down(self, index):
        """Move the element at the given index down to its proper position based on priority."""
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left]['priority'] > self.heap[largest]['priority']:
            largest = left
        if right < len(self.heap) and self.heap[right]['priority'] > self.heap[largest]['priority']:
            largest = right

        if largest != index:
            self.heap[[index, largest]] = self.heap[[largest, index]]
            self._sift_down(largest)

    def is_empty(self):
        """Return True if the queue is empty, False otherwise."""
        return len(self.heap) == 0

    def size(self):
        """Return the number of elements in the queue."""
        return len(self.heap)

    def clear(self):
        """Remove all elements from the queue."""
        self.heap = _numpy.array([], dtype=self.heap.dtype)
        self.has_changed = True

    def changed(self):
        value = self.has_changed
        self.has_changed = False
        return value

class InvertedPriorityList:
    """lower value, higher priority"""
    def __init__(self):
        # Initialize an empty list to store the heap as an array of tuples (priority, value)
        self.heap = _numpy.array([], dtype=[('priority', _numpy.float64), ('value', object)])
        self.has_changed = False

    def enqueue(self, value, priority):
        """Insert a new value with the given priority into the priority queue."""
        # Append the new (priority, value) tuple to the heap
        new_item = _numpy.array([(priority, value)], dtype=self.heap.dtype)
        self.heap = _numpy.append(self.heap, new_item)
        # Perform up-heap bubbling to maintain the min-heap property based on priority
        self._sift_up(len(self.heap) - 1)
        self.has_changed = True

    def dequeue(self):
        """Remove and return the value with the highest priority (lowest priority value) from the queue."""
        values = []
        priority = self.peek_next_priority()
        while not self.is_empty() and self.peek_next_priority() == priority:
            # The root of the heap (index 0) has the minimum priority
            min_value = self.heap[0]['value']

            # Move the last element to the root and then heapify down
            self.heap[0] = self.heap[-1]
            self.heap = _numpy.delete(self.heap, -1)

            # Perform down-heap bubbling to maintain the min-heap property
            self._sift_down(0)

            values.append(min_value)
            self.has_changed = True

        return values

    def peek_next_priority(self):
        """Return the lowest priority value (highest priority) without removing it from the queue."""
        if len(self.heap) != 0:
            return self.heap[0]['priority']

    def peek(self):
        """Return the value with the highest priority (lowest priority value) without removing it from the queue."""
        if len(self.heap) != 0:
            return self.heap[0]['value']

    def _sift_up(self, index):
        """Move the element at the given index up to its proper position based on priority."""
        parent = (index - 1) // 2
        if index > 0 and self.heap[index]['priority'] < self.heap[parent]['priority']:
            self.heap[[index, parent]] = self.heap[[parent, index]]
            self._sift_up(parent)

    def _sift_down(self, index):
        """Move the element at the given index down to its proper position based on priority."""
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left]['priority'] < self.heap[smallest]['priority']:
            smallest = left
        if right < len(self.heap) and self.heap[right]['priority'] < self.heap[smallest]['priority']:
            smallest = right

        if smallest != index:
            self.heap[[index, smallest]] = self.heap[[smallest, index]]
            self._sift_down(smallest)

    def is_empty(self):
        """Return True if the queue is empty, False otherwise."""
        return len(self.heap) == 0

    def size(self):
        """Return the number of elements in the queue."""
        return len(self.heap)

    def clear(self):
        """Remove all elements from the queue."""
        self.heap = _numpy.array([], dtype=self.heap.dtype)
        self.has_changed = True

    def changed(self):
        value = self.has_changed
        self.has_changed = False
        return value