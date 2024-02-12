
class SOLVE:
    def __init__(self, matrix, sequences, buffer_size) -> None:
        self.buffer_size = buffer_size
        self.matrix = matrix
        self.matrix_row = len(matrix)
        self.matrix_col = len(matrix[0])
        self.sequences = sequences
        self.number_of_sequences = len(self.sequences)
        self.buffer = [() for i in range(self.buffer_size)]
        self.current_position = ()
        self.direction = False # True for horizontal, False for vertical
        self.token_to_search = [self.sequences[i][0][0] for i in range(self.number_of_sequences)]
        self.token_to_search_index = [0 for i in range(self.number_of_sequences)]
        self.acc_token = [[] for i in range(self.buffer_size)]
        self.curr_col = 0
        self.curr_row = 0
        self.result = []
        self.curr_score = 0

    def findAllToken(self):
        temp = []
        max_iterate = self.matrix_col if self.direction else self.matrix_row
        for i in range(max_iterate):
            token = self.matrix[self.curr_row][i] if self.direction else self.matrix[i][self.curr_col]
            if token in self.token_to_search:
                if self.direction:
                    if ((self.curr_row,i) not in self.buffer):
                        temp.append((self.curr_row, i))
                else:
                    if ((i,self.curr_col) not in self.buffer):
                        temp.append((i, self.curr_col))
        return temp
    
    def getCurrentBufferNumber(self):
        temp = 0
        while temp < self.buffer_size and self.buffer[temp] != ():
            temp += 1
        return temp
    
    def getCurrentTokenNumber(self):
        temp = self.buffer_size-1
        while temp >= 0 and self.acc_token[temp] != []:
            temp -= 1
        return temp
    
    def changeDirection(self):
        self.direction = not self.direction

    def getCurrentPositionToken(self):
        return self.matrix[self.curr_row][self.curr_col]

    def changeTokenToSearch(self):
        curr_token = self.getCurrentPositionToken()
        temp = []
        for i in range(self.number_of_sequences):
            if curr_token == self.token_to_search[i]:
                if (self.token_to_search_index[i] < len(self.sequences[i][0])-1):
                    self.token_to_search_index[i] += 1
                else:
                    self.curr_score += self.sequences[i][1]
                    temp.append(i)
                    self.result.append([self.copyList(self.buffer), self.curr_score])
            else:
                self.token_to_search_index[i] = 0
            self.token_to_search[i] = self.sequences[i][0][self.token_to_search_index[i]]
        for i in temp:
            self.token_to_search_index.pop(i)
            self.token_to_search.pop(i)
            self.sequences.pop(i)
            self.number_of_sequences -= 1
                
    def isDone(self):
        return self.getCurrentBufferNumber() >= self.buffer_size

    def copyList(self, arr):
        temp = []
        for i in arr:
            temp.append(i)
        return temp

    def findLast(self, arr):
        self.changeDirection()
        buff_number = self.buffer_size-1
        temp_score = self.curr_score
        for coor in arr:
            self.acc_token[buff_number].remove(coor)
            self.curr_score = temp_score
            self.buffer[buff_number] = coor
            self.curr_row = coor[0]
            self.curr_col = coor[1]
            self.changeTokenToSearch()
        self.buffer[buff_number] = ()

    def findNext(self, arr):
        self.changeDirection()
        dir = self.direction
        buff_number = self.getCurrentBufferNumber()
        temp_score = self.curr_score
        temp_token_to_search = self.copyList(self.token_to_search)
        temp_token_to_search_index = self.copyList(self.token_to_search_index)
        temp_sequence = self.copyList(self.sequences)
        temp_number_of_sequences = self.number_of_sequences
        for coor in arr:
            self.direction = dir
            self.acc_token[buff_number].remove(coor)
            self.token_to_search = self.copyList(temp_token_to_search)
            self.token_to_search_index = self.copyList(temp_token_to_search_index)
            self.number_of_sequences = temp_number_of_sequences
            self.sequences = self.copyList(temp_sequence)
            self.curr_score = temp_score
            self.buffer[buff_number] = coor
            self.curr_row = coor[0]
            self.curr_col = coor[1]
            self.changeTokenToSearch()
            temp = self.findAllToken() if not self.isDone() else []
            if temp != []:
                if (self.isDone()):
                    # self.result.append([self.buffer, self.curr_score]) if self.curr_score > 0 else None
                    self.findLast(self.copyList(temp))
                else:
                    self.acc_token[buff_number+1] = temp
                    self.findNext(self.copyList(temp))
        self.buffer[buff_number] = ()

    
    
    def start(self):
        for i in range(self.matrix_col):
            self.direction = False
            self.buffer[0] = (0, i)
            self.curr_score = 0
            self.curr_col = i
            self.curr_row = 0
            self.token_to_search = [self.sequences[i][0][0] for i in range(self.number_of_sequences)]
            self.token_to_search_index = [0 for i in range(self.number_of_sequences)]
            temp = self.findAllToken()
            if (temp != []):
                self.acc_token[1] = temp
                self.findNext(self.copyList(temp))
