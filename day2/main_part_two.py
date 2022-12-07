FILE_NAME = 'input.txt'

def load_moves(file_name:str) -> list[str]:
    # Take data from file
    file = open(file_name, "r")
    moves = file.readlines()
    return moves

def step_score(moves:list[str]) -> list[int]:
    # Take moves and calculate score for each step
    points = [] 

    for line in moves:
        if line[0] == 'A': #rock
            if line[2] == 'Y':
                points += [4] # 3 for draw, 1 for rock
            elif line[2] == 'Z':
                points += [8] # 6 for win, 2 for paper
            else:
                points += [3]
        elif line[0] == 'B': #paper
            if line[2] == 'Y':
                points += [5] # 3 for draw, 2 for paper
            elif line[2] == 'Z':
                points += [9] # 6 for win, 3 for scissors
            else:
                points += [1]
        elif line[0] == 'C': # scissors
            if line[2] == 'Y':
                points += [6] # 3 for draw, 3 for scissors
            elif line[2] == 'Z':
                points += [7] # 6 for win, 1 for rock
            else:
                points += [2]
    return points

def final_score(points:list[int]) -> int:

    result = sum(points)
    return result
        
if __name__ == "__main__":
    opponent_moves = load_moves(FILE_NAME)
    print(final_score(step_score(opponent_moves)))

