class SparseMatrix:
    def __init__(self, file_path=None, num_rows=0, num_cols=0):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.elements = {}
        if file_path:
            self._load_from_file(file_path)

    def _load_from_file(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            self.num_rows = int(lines[0].split('=')[1].strip())
            self.num_cols = int(lines[1].split('=')[1].strip())
            for line in lines[2:]:
                if line.strip():
                    if line.startswith('(') and line.endswith(')'):
                        try:
                            row, col, value = map(int, line[1:-1].split(','))
                            self.elements[(row, col)] = value
                        except ValueError:
                            raise ValueError("Input file has wrong format")
                    else:
                        raise ValueError("Input file has wrong format")

    def get_element(self, row, col):
        return self.elements.get((row, col), 0)

    def set_element(self, row, col, value):
        if value != 0:
            self.elements[(row, col)] = value
        elif (row, col) in self.elements:
            del self.elements[(row, col)]

    def add(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrices dimensions do not match for addition")
        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)
        for (row, col), value in self.elements.items():
            result.set_element(row, col, value + other.get_element(row, col))
        for (row, col), value in other.elements.items():
            if (row, col) not in self.elements:
                result.set_element(row, col, value)
        return result

    def subtract(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrices dimensions do not match for subtraction")
        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)
        for (row, col), value in self.elements.items():
            result.set_element(row, col, value - other.get_element(row, col))
        for (row, col), value in other.elements.items():
            if (row, col) not in self.elements:
                result.set_element(row, col, -value)
        return result

    def multiply(self, other):
        if self.num_cols != other.num_rows:
            raise ValueError("Matrices dimensions do not match for multiplication")
        result = SparseMatrix(num_rows=self.num_rows, num_cols=other.num_cols)
        for (row, col), value in self.elements.items():
            for k in range(other.num_cols):
                if (col, k) in other.elements:
                    result.set_element(row, k, result.get_element(row, k) + value * other.get_element(col, k))
        return result

    def __str__(self):
        result = f"rows={self.num_rows}\ncols={self.num_cols}\n"
        for (row, col), value in sorted(self.elements.items()):
            result += f"({row}, {col}, {value})\n"
        return result