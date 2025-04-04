from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.module_utils import ModuleManager as _ModuleManager

class Stack:
    """
    🟩 **R** -
    """
    def __init__(self, max_size=None):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._frames = []
        self._max_size = max_size
        self._has_changed = False

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def push(self, item):
        """
        🟩 **R** -
        """
        if not self.is_full():
            self._has_changed = True
            self._frames.append(item)

    def pop(self):
        """
        🟩 **R** -
        """
        if not self.is_empty():
            self.has_changed = True
            return self._frames.pop()

    def peek(self):
        """
        🟩 **R** -
        """
        if not self.is_empty():
            return self._frames[-1]

    def is_empty(self):
        """
        🟩 **R** -
        """
        return len(self._frames) == 0

    def is_full(self):
        """
        🟩 **R** -
        """
        if self._max_size is None:
            return False
        return len(self._frames) >= self._max_size

    def size(self):
        """
        🟩 **R** -
        """
        return len(self._frames)

    def clear(self):
        """
        🟩 **R** -
        """
        self._has_changed = True
        self._frames = []

    def changed(self):
        """
        🟩 **R** -
        """
        value = self._has_changed
        self._has_changed = False
        return value

class Queue:
    """
    🟩 **R** -
    """
    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self, max_size=None):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._frames = []
        self._max_size = max_size
        self.has_changed = False

    def enqueue(self, item):
        """
        🟩 **R** -
        """
        if not self.is_full():
            self._has_changed = True
            self._frames.append(item)

    def dequeue(self):
        """
        🟩 **R** -
        """
        if not self.is_empty():
            self._has_changed = True
            return self._frames[0]

    def peek(self):
        """
        🟩 **R** -
        """
        if not self.is_empty():
            return self._frames[0]

    def is_empty(self):
        """
        🟩 **R** -
        """
        return len(self._frames) == 0

    def is_full(self):
        """
        🟩 **R** -
        """
        if self._max_size is None:
            return False
        return len(self._frames) >= self._max_size

    def size(self):
        """
        🟩 **R** -
        """
        return len(self._frames)

    def clear(self):
        """
        🟩 **R** -
        """
        self._has_changed = True
        self._frames = []

    def changed(self):
        """
        🟩 **R** -
        """
        value = self._has_changed
        self._has_changed = False
        return value

class CircularQueue:
    """
    🟩 **R** -
    """
    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self, size):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._max_size = size
        self._frames = [0] * size
        self._front = -1
        self._rear = -1
        self._has_changed = False

    def clear(self):
        """
        🟩 **R** -
        """
        self._has_changed = True
        self._frames = [0] * self._max_size
        self._front = -1
        self._rear = -1

    def enqueue(self, item):
        """
        🟩 **R** -
        """
        if self.is_empty():
            self._front = 0
            self._rear = 0
            self._frames[self._rear] = item
        else:
            self._has_changed = True
            self._rear = (self._rear + 1) % self._max_size
            if self.is_full():
                self._rear = (self._rear - 1 + self._max_size) % self._max_size
            else:
                self._frames[self._rear] = item

    def dequeue(self):
        """
        🟩 **R** -
        """
        if not self.is_empty():
            self._has_changed = True
            item = self._frames[self._front]
            if self._front == self._rear:
                self._front = -1
                self._rear = -1
            else:
                self._front = (self._front + 1) % self._max_size

            return item

    def peek(self):
        """
        🟩 **R** -
        """
        if not self.is_empty():
            return self._frames[self._front]

    def size(self):
        """
        🟩 **R** -
        """
        if self.is_empty():
            return 0
        elif self._front <= self._rear:
            return self._rear - self._front + 1
        else:
            return self._max_size - self._front + self._rear + 1

    def is_empty(self):
        """
        🟩 **R** -
        """
        return self._front == -1 and self._rear == -1

    def is_full(self):
        """
        🟩 **R** -
        """
        rear = (self._rear + 1) % self._max_size
        return rear == self._front

    def changed(self):
        """
        🟩 **R** -
        """
        value = self._has_changed
        self._has_changed = False
        return value

class PriorityQueue:
    """
    🟩 **R** - higher value, higher priority
    """
    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._numpy__module = _ModuleManager.import_module("numpy")

        # Initialize an empty list to store the heap as an array of tuples (priority, value)
        self._heap = self._numpy__module.array([], dtype=[('priority', self._numpy__module.float64), ('value', object)])
        self._has_changed = False

    def enqueue(self, value, priority):
        """
        🟩 **R** - Insert a new value with the given priority into the priority queue.
        """
        # Append the new (priority, value) tuple to the heap
        new_item = self._numpy__module.array([(priority, value)], dtype=self._heap.dtype)
        self._heap = self._numpy__module.append(self._heap, new_item)
        # Perform up-heap bubbling to maintain the max-heap property based on priority
        self._sift_up(len(self._heap) - 1)
        self._has_changed = True

    def dequeue(self):
        """
        🟩 **R** - Remove and return the value with the highest priority from the queue.
        """
        if len(self._heap) != 0:
            self._has_changed = True
            # The root of the heap (index 0) has the maximum priority
            max_value = self._heap[0]['value']

            # Move the last element to the root and then heapify down
            self._heap[0] = self._heap[-1]
            self._heap = self._numpy__module.delete(self._heap, -1)

            # Perform down-heap bubbling to maintain the max-heap property
            self._sift_down(0)

            return max_value

    def peek_next_priority(self):
        """
        🟩 **R** - Return the highest priority value without removing it from the queue.
        """
        if len(self._heap) != 0:
            return self._heap[0]['priority']

    def peek(self):
        """
        🟩 **R** - Return the value with the highest priority without removing it from the queue.
        """
        if len(self._heap) != 0:
            return self._heap[0]['value']

    def _sift_up(self, index):
        """
        🟩 **R** - Move the element at the given index up to its proper position based on priority.
        """
        parent = (index - 1) // 2
        if index > 0 and self._heap[index]['priority'] > self._heap[parent]['priority']:
            self._heap[[index, parent]] = self._heap[[parent, index]]
            self._sift_up(parent)

    def _sift_down(self, index):
        """
        🟩 **R** - Move the element at the given index down to its proper position based on priority.
        """
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self._heap) and self._heap[left]['priority'] > self._heap[largest]['priority']:
            largest = left
        if right < len(self._heap) and self._heap[right]['priority'] > self._heap[largest]['priority']:
            largest = right

        if largest != index:
            self._heap[[index, largest]] = self._heap[[largest, index]]
            self._sift_down(largest)

    def is_empty(self):
        """
        🟩 **R** - Return True if the queue is empty, False otherwise.
        """
        return len(self._heap) == 0

    def size(self):
        """
        🟩 **R** - Return the number of elements in the queue.
        """
        return len(self._heap)

    def clear(self):
        """
        🟩 **R** - Remove all elements from the queue.
        """
        self._heap = self._numpy__module.array([], dtype=self._heap.dtype)
        self._has_changed = True

    def changed(self):
        """
        🟩 **R** -
        """
        value = self._has_changed
        self._has_changed = False
        return value

class InvertedPriorityQueue:
    """
    🟩 **R** - lower value, higher priority.
    """
    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._numpy__module = _ModuleManager.import_module("numpy")

        # Initialize an empty list to store the heap as an array of tuples (priority, value)
        self._heap = self._numpy__module.array([], dtype=[('priority', self._numpy__module.float64), ('value', object)])
        self._has_changed = False

    def enqueue(self, value, priority):
        """
        🟩 **R** - Insert a new value with the given priority into the priority queue.
        """
        # Append the new (priority, value) tuple to the heap
        new_item = self._numpy__module.array([(priority, value)], dtype=self._heap.dtype)
        self._heap = self._numpy__module.append(self._heap, new_item)
        # Perform up-heap bubbling to maintain the min-heap property based on priority
        self._sift_up(len(self._heap) - 1)
        self._has_changed = True

    def dequeue(self):
        """
        🟩 **R** - Remove and return the value with the highest priority (lowest priority value) from the queue.
        """
        if len(self._heap) != 0:
            self._has_changed = True
            # The root of the heap (index 0) has the minimum priority
            min_value = self._heap[0]['value']

            # Move the last element to the root and then heapify down
            self._heap[0] = self._heap[-1]
            self._heap = self._numpy__module.delete(self._heap, -1)

            # Perform down-heap bubbling to maintain the min-heap property
            self._sift_down(0)

            return min_value

    def peek_next_priority(self):
        """
        🟩 **R** - Return the lowest priority value (highest priority) without removing it from the queue.
        """
        if len(self._heap) != 0:
            return self._heap[0]['priority']

    def peek(self):
        """
        🟩 **R** - Return the value with the highest priority (lowest priority value) without removing it from the queue.
        """
        if len(self._heap) != 0:
            return self._heap[0]['value']

    def _sift_up(self, index):
        """
        🟩 **R** - Move the element at the given index up to its proper position based on priority.
        """
        parent = (index - 1) // 2
        if index > 0 and self._heap[index]['priority'] < self._heap[parent]['priority']:
            self._heap[[index, parent]] = self._heap[[parent, index]]
            self._sift_up(parent)

    def _sift_down(self, index):
        """
        🟩 **R** - Move the element at the given index down to its proper position based on priority.
        """
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self._heap) and self._heap[left]['priority'] < self._heap[smallest]['priority']:
            smallest = left
        if right < len(self._heap) and self._heap[right]['priority'] < self._heap[smallest]['priority']:
            smallest = right

        if smallest != index:
            self._heap[[index, smallest]] = self._heap[[smallest, index]]
            self._sift_down(smallest)

    def is_empty(self):
        """
        🟩 **R** - Return True if the queue is empty, False otherwise.
        """
        return len(self._heap) == 0

    def size(self):
        """
        🟩 **R** - Return the number of elements in the queue.
        """
        return len(self._heap)

    def clear(self):
        """
        🟩 **R** - Remove all elements from the queue.
        """
        self._heap = self._numpy__module.array([], dtype=self._heap.dtype)
        self._has_changed = True

    def changed(self):
        """
        🟩 **R** -
        """
        value = self._has_changed
        self._has_changed = False
        return value

class PriorityList:
    """
    🟩 **R** - higher value, higher priority
    """
    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._numpy__module = _ModuleManager.import_module("numpy")

        # Initialize an empty list to store the heap as an array of tuples (priority, value)
        self._heap = self._numpy__module.array([], dtype=[('priority', self._numpy__module.float64), ('value', object)])
        self._has_changed = False

    def add(self, value, priority):
        """
        🟩 **R** - Insert a new value with the given priority into the priority queue.
        """
        # Append the new (priority, value) tuple to the heap
        new_item = self._numpy__module.array([(priority, value)], dtype=self._heap.dtype)
        self._heap = self._numpy__module.append(self._heap, new_item)
        # Perform up-heap bubbling to maintain the max-heap property based on priority
        self._sift_up(len(self._heap) - 1)
        self._has_changed = True

    def remove_item(self, item):
        """
        🟩 **R** - Remove a specific item from the queue.
        """
        for i in range(len(self._heap)):
            if self._heap[i]['value'] == item:
                self._heap = self._numpy__module.delete(self._heap, i)
                self._has_changed = True
                break

    def remove_highest_priority(self):
        """
        🟩 **R** - Remove and return the value with the highest priority from the queue.
        """
        values = []
        priority = self.peek_next_priority()
        while not self.is_empty() and self.peek_next_priority() == priority:
            # The root of the heap (index 0) has the maximum priority
            max_value = self._heap[0]['value']

            # Move the last element to the root and then heapify down
            self._heap[0] = self._heap[-1]
            self._heap = self._numpy__module.delete(self._heap, -1)

            # Perform down-heap bubbling to maintain the max-heap property
            self._sift_down(0)

            values.append(max_value)
            self._has_changed = True
        return values

    def update_priority(self, value, new_priority):
        """
        🟩 **R** - Update the priority of a value in the queue.
        """
        for i in range(len(self._heap)):
            if self._heap[i]['value'] == value:
                self._heap[i]['priority'] = new_priority
                self._sift_up(i)
                self._sift_down(i)
                self._has_changed = True
                break

    def peek_next_priority(self):
        """
        🟩 **R** - Return the highest priority value without removing it from the queue.
        """
        if len(self._heap) != 0:
            return self._heap[0]['priority']

    def peek(self):
        """
        🟩 **R** - Return the value with the highest priority without removing it from the queue.
        """
        if len(self._heap) != 0:
            return self._heap[0]['value']

    def _sift_up(self, index):
        """
        🟩 **R** - Move the element at the given index up to its proper position based on priority.
        """
        parent = (index - 1) // 2
        if index > 0 and self._heap[index]['priority'] > self._heap[parent]['priority']:
            self._heap[[index, parent]] = self._heap[[parent, index]]
            self._sift_up(parent)

    def _sift_down(self, index):
        """
        🟩 **R** - Move the element at the given index down to its proper position based on priority.
        """
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self._heap) and self._heap[left]['priority'] > self._heap[largest]['priority']:
            largest = left
        if right < len(self._heap) and self._heap[right]['priority'] > self._heap[largest]['priority']:
            largest = right

        if largest != index:
            self._heap[[index, largest]] = self._heap[[largest, index]]
            self._sift_down(largest)

    def is_empty(self):
        """
        🟩 **R** - Return True if the queue is empty, False otherwise.
        """
        return len(self._heap) == 0

    def size(self):
        """
        🟩 **R** - Return the number of elements in the queue.
        """
        return len(self._heap)

    def clear(self):
        """
        🟩 **R** - Remove all elements from the queue.
        """
        self._heap = self._numpy__module.array([], dtype=self._heap.dtype)
        self._has_changed = True

    def changed(self):
        """
        🟩 **R** -
        """
        value = self._has_changed
        self._has_changed = False
        return value

class InvertedPriorityList:
    """
    🟩 **R** - Lower value, higher priority
    """
    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._numpy__module = _ModuleManager.import_module("numpy")

        # Initialize an empty list to store the heap as an array of tuples (priority, value)
        self._heap = self._numpy__module.array([], dtype=[('priority', self._numpy__module.float64), ('value', object)])
        self._has_changed = False

    def add(self, value, priority):
        """
        🟩 **R** - Insert a new value with the given priority into the priority queue.
        """
        # Append the new (priority, value) tuple to the heap
        new_item = self._numpy__module.array([(priority, value)], dtype=self._heap.dtype)
        self._heap = self._numpy__module.append(self._heap, new_item)
        # Perform up-heap bubbling to maintain the min-heap property based on priority
        self._sift_up(len(self._heap) - 1)
        self._has_changed = True

    def remove_highest_priority(self):
        """
        🟩 **R** - Remove and return the value with the highest priority (lowest priority value) from the queue.
        """
        values = []
        priority = self.peek_next_priority()
        while not self.is_empty() and self.peek_next_priority() == priority:
            # The root of the heap (index 0) has the minimum priority
            min_value = self._heap[0]['value']

            # Move the last element to the root and then heapify down
            self._heap[0] = self._heap[-1]
            self._heap = self._numpy__module.delete(self._heap, -1)

            # Perform down-heap bubbling to maintain the min-heap property
            self._sift_down(0)

            values.append(min_value)
            self._has_changed = True

        return values

    def update_priority(self, value, new_priority):
        """
        🟩 **R** - Update the priority of a value in the queue.
        """
        for i in range(len(self._heap)):
            if self._heap[i]['value'] == value:
                self._heap[i]['priority'] = new_priority
                self._sift_up(i)
                self._sift_down(i)
                self._has_changed = True
                break

    def remove_item(self, item):
        """
        🟩 **R** - Remove a specific item from the queue.
        """
        for i in range(len(self._heap)):
            if self._heap[i]['value'] == item:
                self._heap = self._numpy__module.delete(self._heap, i)
                self._has_changed = True
                break

    def peek_next_priority(self):
        """
        🟩 **R** - Return the lowest priority value (highest priority) without removing it from the queue.
        """
        if len(self._heap) != 0:
            return self._heap[0]['priority']

    def peek(self):
        """
        🟩 **R** - Return the value with the highest priority (lowest priority value) without removing it from the queue.
        """
        if len(self._heap) != 0:
            return self._heap[0]['value']

    def _sift_up(self, index):
        """
        🟩 **R** - Move the element at the given index up to its proper position based on priority.
        """
        parent = (index - 1) // 2
        if index > 0 and self._heap[index]['priority'] < self._heap[parent]['priority']:
            self._heap[[index, parent]] = self._heap[[parent, index]]
            self._sift_up(parent)

    def _sift_down(self, index):
        """
        🟩 **R** - Move the element at the given index down to its proper position based on priority.
        """
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self._heap) and self._heap[left]['priority'] < self._heap[smallest]['priority']:
            smallest = left
        if right < len(self._heap) and self._heap[right]['priority'] < self._heap[smallest]['priority']:
            smallest = right

        if smallest != index:
            self._heap[[index, smallest]] = self._heap[[smallest, index]]
            self._sift_down(smallest)

    def is_empty(self):
        """
        🟩 **R** - Return True if the queue is empty, False otherwise.
        """
        return len(self._heap) == 0

    def size(self):
        """
        🟩 **R** - Return the number of elements in the queue.
        """
        return len(self._heap)

    def clear(self):
        """
        🟩 **R** - Remove all elements from the queue.
        """
        self._heap = self._numpy__module.array([], dtype=self._heap.dtype)
        self._has_changed = True

    def changed(self):
        """
        🟩 **R** -
        """
        value = self._has_changed
        self._has_changed = False
        return value