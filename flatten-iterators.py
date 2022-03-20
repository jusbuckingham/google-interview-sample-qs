import collections
class NoSuchElementException(Exception):
  pass
class InterleavingFlattener(object):
  def __init__(self, iterlist):
    self._queue = collections.deque()
    for iterator in iterlist:
      self._insert_in_queue(iterator)
  def _insert_in_queue(self, curr_iter)
    try:
      self._queue.append((next(curr_iter), curr_iter))
    except StopIteration:
      pass
  def next(self):
    if not self.has_next():
      raise NoSuchElementException
    value, iterator = self._queue.pop();
    self._insert_in_queue(iterator)
    return val
  def has_next(self):
    return len(self._queue) != 0