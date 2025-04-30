class ArrayIntersection:
    def __init__(self, array1: list, array2: list):
        self.array1 = array1
        self.array2 = array2
        self.common_elements = []

    def find_common_elements(self):
        i, j = 0, 0
        while i < len(self.array1) and j < len(self.array2):
            if self.array1[i] == self.array2[j]:
                if not self.common_elements or self.common_elements[-1] != self.array1[i]:
                    self.common_elements.append(self.array1[i])
                i += 1
                j += 1
            elif self.array1[i] < self.array2[j]:
                i += 1
            else:
                j += 1

    def get_common_elements(self):
        return self.common_elements


if __name__ == "__main__":
    array1 = [1, 3, 4, 6, 7, 8, 9]
    array2 = [3, 4, 5, 6, 8, 10]

    intersect = ArrayIntersection(array1, array2)
    intersect.find_common_elements()
    print("Common elements:", intersect.get_common_elements())
