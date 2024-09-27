Stack (``pmma.Stack``)
======================

Not Yet Written

Create
------

.. py:method:: pmma.Stack() -> pmma.Stack

   Not Yet Written

Methods
-------

.. py:method:: Stack.quit() -> None

   Not Yet Written

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

.. py:method:: Queue.quit() -> None

   Not Yet Written

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

.. py:method:: CircularQueue.quit() -> None

   Not Yet Written

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

Create
------

.. py:method:: pmma.PriorityQueue() -> pmma.PriorityQueue

   Not Yet Written

Methods
-------

.. py:method:: PriorityQueue.quit() -> None

   Not Yet Written

.. py:method:: PriorityQueue.enqueue() -> None

    Insert a new value with the given priority into the priority queue.
    

.. py:method:: PriorityQueue.dequeue() -> None

    Remove and return the value with the highest priority from the queue.
    

.. py:method:: PriorityQueue.peek_next_priority() -> None

    Return the highest priority value without removing it from the queue.
    

.. py:method:: PriorityQueue.peek() -> None

    Return the value with the highest priority without removing it from the queue.
    

.. py:method:: PriorityQueue.is_empty() -> None

    Return True if the queue is empty, False otherwise.
    

.. py:method:: PriorityQueue.size() -> None

    Return the number of elements in the queue.
    

.. py:method:: PriorityQueue.clear() -> None

    Remove all elements from the queue.
    

.. py:method:: PriorityQueue.changed() -> None

   Not Yet Written

Inverted Priority Queue (``pmma.InvertedPriorityQueue``)
========================================================

lower value, higher priority.

Create
------

.. py:method:: pmma.InvertedPriorityQueue() -> pmma.InvertedPriorityQueue

   Not Yet Written

Methods
-------

.. py:method:: InvertedPriorityQueue.quit() -> None

   Not Yet Written

.. py:method:: InvertedPriorityQueue.enqueue() -> None

    Insert a new value with the given priority into the priority queue.
    

.. py:method:: InvertedPriorityQueue.dequeue() -> None

    Remove and return the value with the highest priority (lowest priority value) from the queue.
    

.. py:method:: InvertedPriorityQueue.peek_next_priority() -> None

    Return the lowest priority value (highest priority) without removing it from the queue.
    

.. py:method:: InvertedPriorityQueue.peek() -> None

    Return the value with the highest priority (lowest priority value) without removing it from the queue.
    

.. py:method:: InvertedPriorityQueue.is_empty() -> None

    Return True if the queue is empty, False otherwise.
    

.. py:method:: InvertedPriorityQueue.size() -> None

    Return the number of elements in the queue.
    

.. py:method:: InvertedPriorityQueue.clear() -> None

    Remove all elements from the queue.
    

.. py:method:: InvertedPriorityQueue.changed() -> None

   Not Yet Written

Priority List (``pmma.PriorityList``)
=====================================

higher value, higher priority

Create
------

.. py:method:: pmma.PriorityList() -> pmma.PriorityList

   Not Yet Written

Methods
-------

.. py:method:: PriorityList.quit() -> None

   Not Yet Written

.. py:method:: PriorityList.add() -> None

    Insert a new value with the given priority into the priority queue.
    

.. py:method:: PriorityList.remove_item() -> None

    Remove a specific item from the queue.
    

.. py:method:: PriorityList.remove_highest_priority() -> None

    Remove and return the value with the highest priority from the queue.
    

.. py:method:: PriorityList.update_priority() -> None

    Update the priority of a value in the queue.
    

.. py:method:: PriorityList.peek_next_priority() -> None

    Return the highest priority value without removing it from the queue.
    

.. py:method:: PriorityList.peek() -> None

    Return the value with the highest priority without removing it from the queue.
    

.. py:method:: PriorityList.is_empty() -> None

    Return True if the queue is empty, False otherwise.
    

.. py:method:: PriorityList.size() -> None

    Return the number of elements in the queue.
    

.. py:method:: PriorityList.clear() -> None

    Remove all elements from the queue.
    

.. py:method:: PriorityList.changed() -> None

   Not Yet Written

Inverted Priority List (``pmma.InvertedPriorityList``)
======================================================

lower value, higher priority

Create
------

.. py:method:: pmma.InvertedPriorityList() -> pmma.InvertedPriorityList

   Not Yet Written

Methods
-------

.. py:method:: InvertedPriorityList.quit() -> None

   Not Yet Written

.. py:method:: InvertedPriorityList.add() -> None

    Insert a new value with the given priority into the priority queue.
    

.. py:method:: InvertedPriorityList.remove_highest_priority() -> None

    Remove and return the value with the highest priority (lowest priority value) from the queue.
    

.. py:method:: InvertedPriorityList.update_priority() -> None

    Update the priority of a value in the queue.
    

.. py:method:: InvertedPriorityList.remove_item() -> None

    Remove a specific item from the queue.
    

.. py:method:: InvertedPriorityList.peek_next_priority() -> None

    Return the lowest priority value (highest priority) without removing it from the queue.
    

.. py:method:: InvertedPriorityList.peek() -> None

    Return the value with the highest priority (lowest priority value) without removing it from the queue.
    

.. py:method:: InvertedPriorityList.is_empty() -> None

    Return True if the queue is empty, False otherwise.
    

.. py:method:: InvertedPriorityList.size() -> None

    Return the number of elements in the queue.
    

.. py:method:: InvertedPriorityList.clear() -> None

    Remove all elements from the queue.
    

.. py:method:: InvertedPriorityList.changed() -> None

   Not Yet Written

