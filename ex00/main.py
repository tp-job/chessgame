from checkmate import checkmate

# board
def main():
# 1
    board = """\
....
.K..
..Q.
....\
"""
    checkmate(board)

# 2
    board = """\
........
...Q....
...P....
...K....
........
........
........
.......R
\
"""
    checkmate(board)

if __name__ == "__main__":
    main()