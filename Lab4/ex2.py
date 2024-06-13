class Buffer:
    def __init__(self):
        self.buffer = []
        self.sum_buffer = []

    def add(self, *a):
        self.buffer.extend(a)
        while len(self.buffer) >= 5:
            part_sum = sum(self.buffer[:5])
            self.sum_buffer.append(part_sum)
            print(f"Sum of the next part: {part_sum}")
            self.buffer = self.buffer[5:]

    def get_current_part(self):
        return self.buffer.copy()


# Приклад використання
buf = Buffer()
buf.add(1, 3, 7, 1, 1)  # Поки що нічого не виведеться
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)  # Виведе: Sum of the next part: 12
                                         # Виведе: Sum of the next part: 5
                                         # Виведе: Sum of the next part: 5
buf.add(1, 1)  # Нічого не виведеться
print(buf.get_current_part()) 