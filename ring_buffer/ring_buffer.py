class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity
    self.full = False

  def append(self, item):
    self.storage[self.current] = item
    self.current = (self.current + 1) % self.capacity

    if self.storage[self.capacity - 1] is not None:
      self.full = True


  def get(self):
    if self.full is False:
      return self.storage[:self.current]
    else:
      return self.storage

if __name__ == "__main__":
  ring_buffer = RingBuffer(5)
  print(ring_buffer.get())
  ring_buffer.append('a')
  ring_buffer.append('b')
  ring_buffer.append('c')
  print(ring_buffer.get())
  ring_buffer.append('d')
  ring_buffer.append('e')
  print(ring_buffer.get())
  ring_buffer.append('f')
  print(ring_buffer.get())