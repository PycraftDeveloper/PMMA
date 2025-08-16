Stack (``pmma.Stack``)
======================

🟩 **R** -

Create
------

.. py:method:: pmma.Stack() -> pmma.Stack

    🟩 **R** -
    

Methods
-------

.. py:method:: Stack.quit() -> None

    🟩 **R** -
    

.. py:method:: Stack.push() -> None

    🟩 **R** -
    

.. py:method:: Stack.pop() -> None

    🟩 **R** -
    

.. py:method:: Stack.peek() -> None

    🟩 **R** -
    

.. py:method:: Stack.is_empty() -> None

    🟩 **R** -
    

.. py:method:: Stack.is_full() -> None

    🟩 **R** -
    

.. py:method:: Stack.size() -> None

    🟩 **R** -
    

.. py:method:: Stack.clear() -> None

    🟩 **R** -
    

.. py:method:: Stack.changed() -> None

    🟩 **R** -
    

Queue (``pmma.Queue``)
======================

🟩 **R** -

Create
------

.. py:method:: pmma.Queue() -> pmma.Queue

    🟩 **R** -
    

Methods
-------

.. py:method:: Queue.quit() -> None

    🟩 **R** -
    

.. py:method:: Queue.enqueue() -> None

    🟩 **R** -
    

.. py:method:: Queue.dequeue() -> None

    🟩 **R** -
    

.. py:method:: Queue.peek() -> None

    🟩 **R** -
    

.. py:method:: Queue.is_empty() -> None

    🟩 **R** -
    

.. py:method:: Queue.is_full() -> None

    🟩 **R** -
    

.. py:method:: Queue.size() -> None

    🟩 **R** -
    

.. py:method:: Queue.clear() -> None

    🟩 **R** -
    

.. py:method:: Queue.changed() -> None

    🟩 **R** -
    

Circular Queue (``pmma.CircularQueue``)
=======================================

🟩 **R** -

Create
------

.. py:method:: pmma.CircularQueue() -> pmma.CircularQueue

    🟩 **R** -
    

Methods
-------

.. py:method:: CircularQueue.quit() -> None

    🟩 **R** -
    

.. py:method:: CircularQueue.clear() -> None

    🟩 **R** -
    

.. py:method:: CircularQueue.enqueue() -> None

    🟩 **R** -
    

.. py:method:: CircularQueue.dequeue() -> None

    🟩 **R** -
    

.. py:method:: CircularQueue.peek() -> None

    🟩 **R** -
    

.. py:method:: CircularQueue.size() -> None

    🟩 **R** -
    

.. py:method:: CircularQueue.is_empty() -> None

    🟩 **R** -
    

.. py:method:: CircularQueue.is_full() -> None

    🟩 **R** -
    

.. py:method:: CircularQueue.changed() -> None

    🟩 **R** -
    

Priority Queue (``pmma.PriorityQueue``)
=======================================

🟩 **R** - higher value, higher priority

Create
------

.. py:method:: pmma.PriorityQueue() -> pmma.PriorityQueue

    🟩 **R** -
    

Methods
-------

.. py:method:: PriorityQueue.quit() -> None

    🟩 **R** -
    

.. py:method:: PriorityQueue.enqueue() -> None

    🟩 **R** - Insert a new value with the given priority into the priority queue.
    

.. py:method:: PriorityQueue.dequeue() -> None

    🟩 **R** - Remove and return the value with the highest priority from the queue.
    

.. py:method:: PriorityQueue.peek_next_priority() -> None

    🟩 **R** - Return the highest priority value without removing it from the queue.
    

.. py:method:: PriorityQueue.peek() -> None

    🟩 **R** - Return the value with the highest priority without removing it from the queue.
    

.. py:method:: PriorityQueue.is_empty() -> None

    🟩 **R** - Return True if the queue is empty, False otherwise.
    

.. py:method:: PriorityQueue.size() -> None

    🟩 **R** - Return the number of elements in the queue.
    

.. py:method:: PriorityQueue.clear() -> None

    🟩 **R** - Remove all elements from the queue.
    

.. py:method:: PriorityQueue.changed() -> None

    🟩 **R** -
    

Inverted Priority Queue (``pmma.InvertedPriorityQueue``)
========================================================

🟩 **R** - lower value, higher priority.

Create
------

.. py:method:: pmma.InvertedPriorityQueue() -> pmma.InvertedPriorityQueue

    🟩 **R** -
    

Methods
-------

.. py:method:: InvertedPriorityQueue.quit() -> None

    🟩 **R** -
    

.. py:method:: InvertedPriorityQueue.enqueue() -> None

    🟩 **R** - Insert a new value with the given priority into the priority queue.
    

.. py:method:: InvertedPriorityQueue.dequeue() -> None

    🟩 **R** - Remove and return the value with the highest priority (lowest priority value) from the queue.
    

.. py:method:: InvertedPriorityQueue.peek_next_priority() -> None

    🟩 **R** - Return the lowest priority value (highest priority) without removing it from the queue.
    

.. py:method:: InvertedPriorityQueue.peek() -> None

    🟩 **R** - Return the value with the highest priority (lowest priority value) without removing it from the queue.
    

.. py:method:: InvertedPriorityQueue.is_empty() -> None

    🟩 **R** - Return True if the queue is empty, False otherwise.
    

.. py:method:: InvertedPriorityQueue.size() -> None

    🟩 **R** - Return the number of elements in the queue.
    

.. py:method:: InvertedPriorityQueue.clear() -> None

    🟩 **R** - Remove all elements from the queue.
    

.. py:method:: InvertedPriorityQueue.changed() -> None

    🟩 **R** -
    

Priority List (``pmma.PriorityList``)
=====================================

🟩 **R** - higher value, higher priority

Create
------

.. py:method:: pmma.PriorityList() -> pmma.PriorityList

    🟩 **R** -
    

Methods
-------

.. py:method:: PriorityList.quit() -> None

    🟩 **R** -
    

.. py:method:: PriorityList.add() -> None

    🟩 **R** - Insert a new value with the given priority into the priority queue.
    

.. py:method:: PriorityList.remove_item() -> None

    🟩 **R** - Remove a specific item from the queue.
    

.. py:method:: PriorityList.remove_highest_priority() -> None

    🟩 **R** - Remove and return the value with the highest priority from the queue.
    

.. py:method:: PriorityList.update_priority() -> None

    🟩 **R** - Update the priority of a value in the queue.
    

.. py:method:: PriorityList.peek_next_priority() -> None

    🟩 **R** - Return the highest priority value without removing it from the queue.
    

.. py:method:: PriorityList.peek() -> None

    🟩 **R** - Return the value with the highest priority without removing it from the queue.
    

.. py:method:: PriorityList.is_empty() -> None

    🟩 **R** - Return True if the queue is empty, False otherwise.
    

.. py:method:: PriorityList.size() -> None

    🟩 **R** - Return the number of elements in the queue.
    

.. py:method:: PriorityList.clear() -> None

    🟩 **R** - Remove all elements from the queue.
    

.. py:method:: PriorityList.changed() -> None

    🟩 **R** -
    

Inverted Priority List (``pmma.InvertedPriorityList``)
======================================================

🟩 **R** - Lower value, higher priority

Create
------

.. py:method:: pmma.InvertedPriorityList() -> pmma.InvertedPriorityList

    🟩 **R** -
    

Methods
-------

.. py:method:: InvertedPriorityList.quit() -> None

    🟩 **R** -
    

.. py:method:: InvertedPriorityList.add() -> None

    🟩 **R** - Insert a new value with the given priority into the priority queue.
    

.. py:method:: InvertedPriorityList.remove_highest_priority() -> None

    🟩 **R** - Remove and return the value with the highest priority (lowest priority value) from the queue.
    

.. py:method:: InvertedPriorityList.update_priority() -> None

    🟩 **R** - Update the priority of a value in the queue.
    

.. py:method:: InvertedPriorityList.remove_item() -> None

    🟩 **R** - Remove a specific item from the queue.
    

.. py:method:: InvertedPriorityList.peek_next_priority() -> None

    🟩 **R** - Return the lowest priority value (highest priority) without removing it from the queue.
    

.. py:method:: InvertedPriorityList.peek() -> None

    🟩 **R** - Return the value with the highest priority (lowest priority value) without removing it from the queue.
    

.. py:method:: InvertedPriorityList.is_empty() -> None

    🟩 **R** - Return True if the queue is empty, False otherwise.
    

.. py:method:: InvertedPriorityList.size() -> None

    🟩 **R** - Return the number of elements in the queue.
    

.. py:method:: InvertedPriorityList.clear() -> None

    🟩 **R** - Remove all elements from the queue.
    

.. py:method:: InvertedPriorityList.changed() -> None

    🟩 **R** -
    

