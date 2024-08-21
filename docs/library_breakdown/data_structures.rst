Stack (``pmma.Stack``)
======================

Not Yet Written

Create
------

.. py:method:: pmma.Stack() -> pmma.Stack

   Not Yet Written

Methods
-------

.. py:method:: Stack.push() -> None

   Not Yet Written

.. py:method:: Stack.pop() -> None

   Not Yet Written

.. py:method:: Stack.peek() -> None

   Not Yet Written

.. py:method:: Stack.is_empty() -> None

   Not Yet Written

.. py:method:: Stack.is_full() -> None

   Not Yet Written

.. py:method:: Stack.size() -> None

   Not Yet Written

.. py:method:: Stack.clear() -> None

   Not Yet Written

.. py:method:: Stack.changed() -> None

   Not Yet Written

Queue (``pmma.Queue``)
======================

Not Yet Written

Create
------

.. py:method:: pmma.Queue() -> pmma.Queue

   Not Yet Written

Methods
-------

.. py:method:: Queue.enqueue() -> None

   Not Yet Written

.. py:method:: Queue.dequeue() -> None

   Not Yet Written

.. py:method:: Queue.peek() -> None

   Not Yet Written

.. py:method:: Queue.is_empty() -> None

   Not Yet Written

.. py:method:: Queue.is_full() -> None

   Not Yet Written

.. py:method:: Queue.size() -> None

   Not Yet Written

.. py:method:: Queue.clear() -> None

   Not Yet Written

.. py:method:: Queue.changed() -> None

   Not Yet Written

Circular Queue (``pmma.CircularQueue``)
=======================================

Not Yet Written

Create
------

.. py:method:: pmma.CircularQueue() -> pmma.CircularQueue

   Not Yet Written

Methods
-------

.. py:method:: CircularQueue.clear() -> None

   Not Yet Written

.. py:method:: CircularQueue.enqueue() -> None

   Not Yet Written

.. py:method:: CircularQueue.dequeue() -> None

   Not Yet Written

.. py:method:: CircularQueue.peek() -> None

   Not Yet Written

.. py:method:: CircularQueue.size() -> None

   Not Yet Written

.. py:method:: CircularQueue.is_empty() -> None

   Not Yet Written

.. py:method:: CircularQueue.is_full() -> None

   Not Yet Written

.. py:method:: CircularQueue.changed() -> None

   Not Yet Written

Priority Queue (``pmma.PriorityQueue``)
=======================================

higher value, higher priority
def __init__(self):
# Initialize an empty list to store the heap as an array of tuples (priority, value)
self.heap = _numpy.array([], dtype=[('priority', _numpy.float64), ('value', object)])
self.has_changed = False

def enqueue(self, value, priority):
Insert a new value with the given priority into the priority queue.

Create
------

.. py:method:: pmma.PriorityQueue() -> pmma.PriorityQueue

   Not Yet Written

Methods
-------

.. py:method:: PriorityQueue.enqueue() -> None

 sert a new value with the given priority into the priority queue.
    # Append the new (priority, value) tuple to the heap
    new_item = _numpy.array([(priority, value)], dtype=self.heap.dtype)
    self.heap = _numpy.append(self.heap, new_item)
    # Perform up-heap bubbling to maintain the max-heap property based on priority
    self._sift_up(len(self.heap) - 1)
    self.has_changed = True
    
    def dequeue(self):
    Remove and return the value with the highest priority from the queue.

.. py:method:: PriorityQueue.dequeue() -> None

 move and return the value with the highest priority from the queue.
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
    Return the highest priority value without removing it from the queue.

.. py:method:: PriorityQueue.peek_next_priority() -> None

 turn the highest priority value without removing it from the queue.
    if len(self.heap) != 0:
    return self.heap[0]['priority']
    
    def peek(self):
    Return the value with the highest priority without removing it from the queue.

.. py:method:: PriorityQueue.peek() -> None

 turn the value with the highest priority without removing it from the queue.
    if len(self.heap) != 0:
    return self.heap[0]['value']
    
    def _sift_up(self, index):
    Move the element at the given index up to its proper position based on priority.

.. py:method:: PriorityQueue._sift_up() -> None

 ve the element at the given index up to its proper position based on priority.
    parent = (index - 1) // 2
    if index > 0 and self.heap[index]['priority'] > self.heap[parent]['priority']:
    self.heap[[index, parent]] = self.heap[[parent, index]]
    self._sift_up(parent)
    
    def _sift_down(self, index):
    Move the element at the given index down to its proper position based on priority.

.. py:method:: PriorityQueue._sift_down() -> None

 ve the element at the given index down to its proper position based on priority.
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
    Return True if the queue is empty, False otherwise.

.. py:method:: PriorityQueue.is_empty() -> None

 turn True if the queue is empty, False otherwise.
    return len(self.heap) == 0
    
    def size(self):
    Return the number of elements in the queue.

.. py:method:: PriorityQueue.size() -> None

 turn the number of elements in the queue.
    return len(self.heap)
    
    def clear(self):
    Remove all elements from the queue.

.. py:method:: PriorityQueue.clear() -> None

 move all elements from the queue.
    self.heap = _numpy.array([], dtype=self.heap.dtype)
    self.has_changed = True
    
    def changed(self):
    value = self.has_changed
    self.has_changed = False
    return value
    
    class InvertedPriorityQueue:
    lower value, higher priority

.. py:method:: PriorityQueue.changed() -> None

   Not Yet Written

Inverted Priority Queue (``pmma.InvertedPriorityQueue``)
========================================================

lower value, higher priority
def __init__(self):
# Initialize an empty list to store the heap as an array of tuples (priority, value)
self.heap = _numpy.array([], dtype=[('priority', _numpy.float64), ('value', object)])
self.has_changed = False

def enqueue(self, value, priority):
Insert a new value with the given priority into the priority queue.

Create
------

.. py:method:: pmma.InvertedPriorityQueue() -> pmma.InvertedPriorityQueue

   Not Yet Written

Methods
-------

.. py:method:: InvertedPriorityQueue.enqueue() -> None

 sert a new value with the given priority into the priority queue.
    # Append the new (priority, value) tuple to the heap
    new_item = _numpy.array([(priority, value)], dtype=self.heap.dtype)
    self.heap = _numpy.append(self.heap, new_item)
    # Perform up-heap bubbling to maintain the min-heap property based on priority
    self._sift_up(len(self.heap) - 1)
    self.has_changed = True
    
    def dequeue(self):
    Remove and return the value with the highest priority (lowest priority value) from the queue.

.. py:method:: InvertedPriorityQueue.dequeue() -> None

 move and return the value with the highest priority (lowest priority value) from the queue.
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
    Return the lowest priority value (highest priority) without removing it from the queue.

.. py:method:: InvertedPriorityQueue.peek_next_priority() -> None

 turn the lowest priority value (highest priority) without removing it from the queue.
    if len(self.heap) != 0:
    return self.heap[0]['priority']
    
    def peek(self):
    Return the value with the highest priority (lowest priority value) without removing it from the queue.

.. py:method:: InvertedPriorityQueue.peek() -> None

 turn the value with the highest priority (lowest priority value) without removing it from the queue.
    if len(self.heap) != 0:
    return self.heap[0]['value']
    
    def _sift_up(self, index):
    Move the element at the given index up to its proper position based on priority.

.. py:method:: InvertedPriorityQueue._sift_up() -> None

 ve the element at the given index up to its proper position based on priority.
    parent = (index - 1) // 2
    if index > 0 and self.heap[index]['priority'] < self.heap[parent]['priority']:
    self.heap[[index, parent]] = self.heap[[parent, index]]
    self._sift_up(parent)
    
    def _sift_down(self, index):
    Move the element at the given index down to its proper position based on priority.

.. py:method:: InvertedPriorityQueue._sift_down() -> None

 ve the element at the given index down to its proper position based on priority.
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
    Return True if the queue is empty, False otherwise.

.. py:method:: InvertedPriorityQueue.is_empty() -> None

 turn True if the queue is empty, False otherwise.
    return len(self.heap) == 0
    
    def size(self):
    Return the number of elements in the queue.

.. py:method:: InvertedPriorityQueue.size() -> None

 turn the number of elements in the queue.
    return len(self.heap)
    
    def clear(self):
    Remove all elements from the queue.

.. py:method:: InvertedPriorityQueue.clear() -> None

 move all elements from the queue.
    self.heap = _numpy.array([], dtype=self.heap.dtype)
    self.has_changed = True
    
    def changed(self):
    value = self.has_changed
    self.has_changed = False
    return value
    
    class PriorityList:
    higher value, higher priority

.. py:method:: InvertedPriorityQueue.changed() -> None

   Not Yet Written

Priority List (``pmma.PriorityList``)
=====================================

higher value, higher priority
def __init__(self):
# Initialize an empty list to store the heap as an array of tuples (priority, value)
self.heap = _numpy.array([], dtype=[('priority', _numpy.float64), ('value', object)])
self.has_changed = False

def add(self, value, priority):
Insert a new value with the given priority into the priority queue.

Create
------

.. py:method:: pmma.PriorityList() -> pmma.PriorityList

   Not Yet Written

Methods
-------

.. py:method:: PriorityList.add() -> None

 sert a new value with the given priority into the priority queue.
    # Append the new (priority, value) tuple to the heap
    new_item = _numpy.array([(priority, value)], dtype=self.heap.dtype)
    self.heap = _numpy.append(self.heap, new_item)
    # Perform up-heap bubbling to maintain the max-heap property based on priority
    self._sift_up(len(self.heap) - 1)
    self.has_changed = True
    
    def remove_item(self, item):
    Remove a specific item from the queue.

.. py:method:: PriorityList.remove_item() -> None

 move a specific item from the queue.
    for i in range(len(self.heap)):
    if self.heap[i]['value'] == item:
    self.heap = _numpy.delete(self.heap, i)
    self.has_changed = True
    break
    
    def remove_highest_priority(self):
    Remove and return the value with the highest priority from the queue.

.. py:method:: PriorityList.remove_highest_priority() -> None

 move and return the value with the highest priority from the queue.
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
    
    def update_priority(self, value, new_priority):
    Update the priority of a value in the queue.

.. py:method:: PriorityList.update_priority() -> None

 date the priority of a value in the queue.
    for i in range(len(self.heap)):
    if self.heap[i]['value'] == value:
    self.heap[i]['priority'] = new_priority
    self._sift_up(i)
    self._sift_down(i)
    self.has_changed = True
    break
    
    def peek_next_priority(self):
    Return the highest priority value without removing it from the queue.

.. py:method:: PriorityList.peek_next_priority() -> None

 turn the highest priority value without removing it from the queue.
    if len(self.heap) != 0:
    return self.heap[0]['priority']
    
    def peek(self):
    Return the value with the highest priority without removing it from the queue.

.. py:method:: PriorityList.peek() -> None

 turn the value with the highest priority without removing it from the queue.
    if len(self.heap) != 0:
    return self.heap[0]['value']
    
    def _sift_up(self, index):
    Move the element at the given index up to its proper position based on priority.

.. py:method:: PriorityList._sift_up() -> None

 ve the element at the given index up to its proper position based on priority.
    parent = (index - 1) // 2
    if index > 0 and self.heap[index]['priority'] > self.heap[parent]['priority']:
    self.heap[[index, parent]] = self.heap[[parent, index]]
    self._sift_up(parent)
    
    def _sift_down(self, index):
    Move the element at the given index down to its proper position based on priority.

.. py:method:: PriorityList._sift_down() -> None

 ve the element at the given index down to its proper position based on priority.
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
    Return True if the queue is empty, False otherwise.

.. py:method:: PriorityList.is_empty() -> None

 turn True if the queue is empty, False otherwise.
    return len(self.heap) == 0
    
    def size(self):
    Return the number of elements in the queue.

.. py:method:: PriorityList.size() -> None

 turn the number of elements in the queue.
    return len(self.heap)
    
    def clear(self):
    Remove all elements from the queue.

.. py:method:: PriorityList.clear() -> None

 move all elements from the queue.
    self.heap = _numpy.array([], dtype=self.heap.dtype)
    self.has_changed = True
    
    def changed(self):
    value = self.has_changed
    self.has_changed = False
    return value
    
    class InvertedPriorityList:
    lower value, higher priority

.. py:method:: PriorityList.changed() -> None

   Not Yet Written

Inverted Priority List (``pmma.InvertedPriorityList``)
======================================================

lower value, higher priority
def __init__(self):
# Initialize an empty list to store the heap as an array of tuples (priority, value)
self.heap = _numpy.array([], dtype=[('priority', _numpy.float64), ('value', object)])
self.has_changed = False

def add(self, value, priority):
Insert a new value with the given priority into the priority queue.

Create
------

.. py:method:: pmma.InvertedPriorityList() -> pmma.InvertedPriorityList

   Not Yet Written

Methods
-------

.. py:method:: InvertedPriorityList.add() -> None

 sert a new value with the given priority into the priority queue.
    # Append the new (priority, value) tuple to the heap
    new_item = _numpy.array([(priority, value)], dtype=self.heap.dtype)
    self.heap = _numpy.append(self.heap, new_item)
    # Perform up-heap bubbling to maintain the min-heap property based on priority
    self._sift_up(len(self.heap) - 1)
    self.has_changed = True
    
    def remove_highest_priority(self):
    Remove and return the value with the highest priority (lowest priority value) from the queue.

.. py:method:: InvertedPriorityList.remove_highest_priority() -> None

 move and return the value with the highest priority (lowest priority value) from the queue.
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
    
    def update_priority(self, value, new_priority):
    Update the priority of a value in the queue.

.. py:method:: InvertedPriorityList.update_priority() -> None

 date the priority of a value in the queue.
    for i in range(len(self.heap)):
    if self.heap[i]['value'] == value:
    self.heap[i]['priority'] = new_priority
    self._sift_up(i)
    self._sift_down(i)
    self.has_changed = True
    break
    
    def remove_item(self, item):
    Remove a specific item from the queue.

.. py:method:: InvertedPriorityList.remove_item() -> None

 move a specific item from the queue.
    for i in range(len(self.heap)):
    if self.heap[i]['value'] == item:
    self.heap = _numpy.delete(self.heap, i)
    self.has_changed = True
    break
    
    def peek_next_priority(self):
    Return the lowest priority value (highest priority) without removing it from the queue.

.. py:method:: InvertedPriorityList.peek_next_priority() -> None

 turn the lowest priority value (highest priority) without removing it from the queue.
    if len(self.heap) != 0:
    return self.heap[0]['priority']
    
    def peek(self):
    Return the value with the highest priority (lowest priority value) without removing it from the queue.

.. py:method:: InvertedPriorityList.peek() -> None

 turn the value with the highest priority (lowest priority value) without removing it from the queue.
    if len(self.heap) != 0:
    return self.heap[0]['value']
    
    def _sift_up(self, index):
    Move the element at the given index up to its proper position based on priority.

.. py:method:: InvertedPriorityList._sift_up() -> None

 ve the element at the given index up to its proper position based on priority.
    parent = (index - 1) // 2
    if index > 0 and self.heap[index]['priority'] < self.heap[parent]['priority']:
    self.heap[[index, parent]] = self.heap[[parent, index]]
    self._sift_up(parent)
    
    def _sift_down(self, index):
    Move the element at the given index down to its proper position based on priority.

.. py:method:: InvertedPriorityList._sift_down() -> None

 ve the element at the given index down to its proper position based on priority.
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
    Return True if the queue is empty, False otherwise.

.. py:method:: InvertedPriorityList.is_empty() -> None

 turn True if the queue is empty, False otherwise.
    return len(self.heap) == 0
    
    def size(self):
    Return the number of elements in the queue.

.. py:method:: InvertedPriorityList.size() -> None

 turn the number of elements in the queue.
    return len(self.heap)
    
    def clear(self):
    Remove all elements from the queue.

.. py:method:: InvertedPriorityList.clear() -> None

 move all elements from the queue.
    self.heap = _numpy.array([], dtype=self.heap.dtype)
    self.has_changed = True
    
    def changed(self):
    value = self.has_changed
    self.has_changed = False
    return value

.. py:method:: InvertedPriorityList.changed() -> None

   Not Yet Written

