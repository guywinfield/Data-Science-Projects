import numpy as np
np.set_printoptions(legacy='1.13')

def main():
    rows,columns = input().split(" ")
    row = int(rows)
    columns = int(columns)

    matrix = np.zeros((row,columns)).astype(int)


    index = -1
    for x in matrix:
        index += 1
        for _ in x:
            try:
                x[index] =1
            except IndexError:
                pass
    print(matrix)

if __name__ == "__main__":
    main()
