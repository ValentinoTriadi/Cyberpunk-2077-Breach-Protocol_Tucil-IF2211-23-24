import random, os
import solve, time

class INFO:
    def __init__(self):
        self.reset()
        self.time_executed = 0

    def reset(self):
        self.buffer_size = 0
        self.matrix_col = 0
        self.matrix_row = 0
        self.number_of_sequences = 0
        self.sequences = []
        self.matrix = []

    def parse(self, file):
        with open(file, 'r') as f:
            # Read buffer size
            line = f.readline()
            self.buffer_size = int(line.rstrip())

            # Read matrix width and height
            line = f.readline()
            self.matrix_col, self.matrix_row = map(int, line.rstrip().split(' '))

            # Read Matrix
            for i in range(self.matrix_row):
                line = f.readline()
                self.matrix.append(list(line.rstrip().split(' ')))

            # Read number of sequences
            line = f.readline()
            self.number_of_sequences = int(line.rstrip())

            # Read sequences and scores
            for i in range(self.number_of_sequences):
                line = f.readline()
                sequence = line.rstrip().split(' ')
                line = f.readline()
                score = int(line.rstrip())
                self.sequences.append([sequence, score])
    
    def random(self, jumlah_token_unik, token, buffer_size, matrix_col, matrix_row, number_of_sequences, max_number_of_sequence):
        self.buffer_size = buffer_size
        self.matrix_col = matrix_col
        self.matrix_row = matrix_row
        self.number_of_sequences = number_of_sequences
        for i in range(matrix_row):
            self.matrix.append([random.choice(token) for j in range(matrix_col)])
        for i in range(number_of_sequences):
            sequence = [random.choice(token) for j in range(random.randint(2, max_number_of_sequence))]
            score = random.randint(1, 100)
            self.sequences.append([sequence, score])

    def randomGUI(self, buffer_size, sequence_count, max_sequence_length, matrix_width, matrix_height, token_count, token):
        unique_token = ["" for i in range(token_count)]
        token = token.strip().split(' ')
        for i in range(token_count):
            unique_token[i] = token[i]
        self.buffer_size = buffer_size
        self.matrix_col = matrix_width
        self.matrix_row = matrix_height
        self.number_of_sequences = sequence_count
        for i in range(matrix_height):
            self.matrix.append([random.choice(unique_token) for j in range(matrix_width)])
        for i in range(sequence_count):
            sequence = [random.choice(unique_token) for j in range(random.randint(2, max_sequence_length))]
            score = random.randint(1, 100)
            self.sequences.append([sequence, score])


    def print(self):
        os.system("cls || clear")
        print("buffer size: ",self.buffer_size)
        print("matrix width: ",self.matrix_col)
        print("matrix height: ",self.matrix_row)
        print("matrix: ")
        for i in self.matrix:
            for j in i:
                print(j, end=' ')
            print()

        print("number of sequences:",self.number_of_sequences)
        print("sequences: ")
        for i in self.sequences:
            print(f"Score: {i[1]:3d}", end='  →  ')
            for j in i[0]:
                print(j, end=' ')
            print()

    def solve(self):
        # ide nya cari kebawah kalo directionnya horizontal, kalo nemu gas turun kalo ga nemu lanjut ke baris sampingnya
        os.system("cls || clear")
        print("Solving the problem...")
        solveClass = solve.SOLVE(self.matrix, self.sequences, self.buffer_size)
        start = time.time()
        solveClass.start()
        end = time.time()
        self.time_executed = end-start
        # print(res)
        # print(sorted(res, key = lambda x: x[1], reverse=True))
        return (sorted(solveClass.result, key = lambda x: x[1], reverse=True)) 




        


        
