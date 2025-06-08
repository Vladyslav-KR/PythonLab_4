class Buffer:
    def __init__(self):
        self._buffer = []

    def add(self, *a):
        self._buffer.extend(a)
        while len(self._buffer) >= 5:
            part = self._buffer[:5]
            print(f"Сума п’ятірки {part} = {sum(part)}")
            self._buffer = self._buffer[5:]

    def get_current_part(self):
        return self._buffer


if __name__ == "__main__":
    buf = Buffer()
    buf.add(1, 2, 3)
    print("Залишок у буфері:", buf.get_current_part())

    buf.add(4, 5, 6)
    print("Залишок у буфері:", buf.get_current_part())

    buf.add(7, 8, 9, 10, 11)
    print("Залишок у буфері:", buf.get_current_part())

