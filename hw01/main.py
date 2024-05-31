import sys
from sparse_matrix import SparseMatrix

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <operation> <matrix1.txt> <matrix2.txt>")
        return
    
    operation = sys.argv[1]
    matrix1_path = sys.argv[2]
    matrix2_path = sys.argv[3]

    try:
        matrix1 = SparseMatrix(matrix1_path)
        matrix2 = SparseMatrix(matrix2_path)
    except FileNotFoundError:
        print(f"Error: File not found. Please check the file paths: {matrix1_path}, {matrix2_path}")
        return
    except ValueError as ve:
        print(f"Error: {ve}")
        return

    try:
        if operation == 'add':
            result = matrix1.add(matrix2)
        elif operation == 'subtract':
            result = matrix1.subtract(matrix2)
        elif operation == 'multiply':
            result = matrix1.multiply(matrix2)
        else:
            print("Invalid operation. Use add, subtract, or multiply.")
            return
    except ValueError as ve:
        print(f"Error: {ve}")
        return

    print(result)

if __name__ == "__main__":
    main()