import os

def main():
    os.system("cls || clear")
    print("Welcome to Cyberpunk 2077 Breach Protocol Solver!")
    print("Please select the menu above to start the program.")
    print("1. Solve Breach Protocol from file")
    print("2. Solve Breach Protocol from input")
    print("3. Exit")
    while (True):
        try:
            choice = int(input("Enter your choice: "))
            if (1 <= choice <= 3):
                break
        except:
            print("Invalid input. Please enter a number (1-3).")
            exit()
    return choice
        
def solveFromFile():
    os.system("cls || clear")
    # file_name = "input/" + input("Enter file name: ")
    file_name = "src/input/input.txt"
    print("Opening file", file_name)
    # print(os.getcwd())
    # time.sleep(2)
    if (os.path.isfile(file_name)):
        return file_name
    
    print("File not found. Returning to main menu.")

# def solveFromFileGUI():


def solveFromInput():
    print("Enter the input below:")
    jumlah_token_unik = int(input("Jumlah token unik: "))
    token = []
    for i in range(jumlah_token_unik):
        token.append(input(f"Masukkan token unik ke-{i+1}: "))
    buffer_size = int(input("Buffer size: "))
    matrix_col, matrix_row = map(int, input("Matrix row and column (r c): ").split(' '))
    number_of_sequences = int(input("Number of sequences: "))
    max_number_of_sequence = int(input("Max number of sequence: "))
    return jumlah_token_unik, token, buffer_size, matrix_col, matrix_row, number_of_sequences, max_number_of_sequence

def getLength(l):
    for i in range(len(l)):
        if l[i]  == ():
            return i
    return len(l)

def printSingle(arr, score, matrix):
    for i in range(getLength(arr)):
        if (i != 0):
            print(" → ", end="")
        print(matrix[arr[i][0]][arr[i][1]], end="")
    print(f"\t\tscore: {score}")

def printAll(arr, matrix):
    max = arr[0][1]
    for i in arr:
        if (i[1] < max):
            break
        for j in range(getLength(i[0])):
            if (j != 0):
                print(" → ", end="")
            print(matrix[i[0][j][0]][i[0][j][1]], end="")
        print(f"\t\tscore: {i[1]}")
        print("Koor → ", end="")
        for j in range(getLength(i[0])):
            if (j != 0):
                print(" → ", end="")
            print(i[0][j], end="")
        print()

def printResult(arr, matrix, time):
    os.system("cls || clear")
    print("Executed in", time, "s")
    print("Result:")
    if (len(arr) == 0):
        print("No solutions found!")
        return
    printSingle(arr[0][0], arr[0][1], matrix)
    opt = ""
    while True:
        opt = input("show all the solution? (Y/N)")
        if (opt != "Y" and opt != "y" and opt != "N" and opt != "n"):
            print("Invalid input!")
        else:
            break
    if (opt == "y" or opt == "Y"):
        printAll(arr, matrix)
        
    