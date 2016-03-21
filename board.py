

class Board(object):

    def __init__(self):
        self.reset_board()

    def reset_board(self):
        # Set all cells to '0'
        self.board = [[0]*9]*9
        
    def change_board(self, pattern):
        self.board = pattern

    def check_board(self):
        self.check_rows_for_duplicates()
        self.check_columns_for_duplicates()
        #self.check_grids_for_duplicates()
        
        #self.check_rows_for_completion()
        #self.check_columns_for_completion()
        #self.check_grids_for_completion()

    # Check for duplicates
    def check_rows_for_duplicates(self):
        found = False
        index = 0
        print "\nRows\n"
        for row in self.board:
            index += 1
            print row
            if len(row) != len(set(row)):
                found = True
                print "Duplicates in row %d!" % index
        if found == False:
            print "\nNo duplicates in any rows!"
            
    def check_columns_for_duplicates(self):
        found = False
        print "\nColumns\n"
        for col in range(9):
            column = []
            for row in range(9):
                column.append(self.board[row][col])
            print column
            if len(column) != len(set(column)):
                found = True
                print "\nDuplicates in column %d!\n" % (col+1)
        if found == False:
            print "\nNo duplicates in any columns!"

    def check_grids_for_duplicates(self):
        index = 0
        found = False
        for grid in self.grids:
            index += 1
            if len(grid) != len(set(grid)):
                found = True
                print "Duplicates in grid %d!" % index
        if found == False:
            print "No duplicates in any grids!"

    # Check for completion
    def check_rows_for_completion(self):
        for row in self.board:
            for cell in row:
                pass

    def check_columns_for_completion(self):
        pass

    def check_grids_for_completion(self):
        pass

    # Print
    def print_board(self):
        print "\n\tSudoku\n"
        row_counter = 0
        for row in self.board:
            row_counter += 1
            cell_counter = 0
            print '',
            for cell in row:
                cell_counter += 1
                print cell,
                if cell_counter == 3 or cell_counter == 6:
                    print '|',
            if row_counter == 3 or row_counter == 6:
                print '\n ------|-------|------',
            print
        print

def modify_board(choice):
    t = range(1, 10)

    # No dups in rows or cols
    if choice == 1:
        new_board = [t[0:] + t[0:0],
                     t[1:] + t[0:1],
                     t[2:] + t[0:2],
                     t[3:] + t[0:3],
                     t[4:] + t[0:4],
                     t[5:] + t[0:5],
                     t[6:] + t[0:6],
                     t[7:] + t[0:7],
                     t[8:] + t[0:8]]
    # No dups in rows
    elif choice == 2:
        new_board = [t]*9
    # No dups in cols
    elif choice == 3:
        new_board = []
        for i in range(1, 10):
            new_board.append([i]*9)
    # No dups in rows, cols, or grids
    elif choice == 4:
        new_board = [t[0:] + t[0:0],
                     t[3:] + t[0:3],
                     t[6:] + t[0:6],
                     t[1:] + t[0:1],
                     t[4:] + t[0:4],
                     t[7:] + t[0:7],
                     t[2:] + t[0:2],
                     t[5:] + t[0:5],
                     t[8:] + t[0:8]]
    return new_board

def main():
    board = Board()
    board.print_board()
    board.change_board(modify_board(1))
    board.print_board()
    board.change_board(modify_board(2))
    board.print_board()
    board.change_board(modify_board(3))
    board.print_board()
    board.change_board(modify_board(4))
    board.print_board()
    board.check_board()
    
if __name__ == "__main__":
    main()
