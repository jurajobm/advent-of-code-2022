FILE_NAME = 'input.txt'


def load_moves(file_name:str) -> list[str]:
    # Take data from file
    with open(file_name, "r") as f:
        moves = f.readlines()
    return moves

def step_score(moves:list[str]) -> list[int]:
    # Take moves and calculate score for each step
    points = []

    for line in moves:
        if line[2] == 'X': #rock
            points += [1]
            if line[0] == 'A':
                points += [3]
            elif line[0] == 'C':
                points += [6]
        elif line[2] == 'Y': #paper
            points += [2]
            if line[0] == 'A':
                points += [6]
            elif line[0] == 'B':
                points += [3]
        elif line[2] == 'Z': # scissors
            points += [3]
            if line[0] == 'B':
                points += [6]
            elif line[0] == 'C':
                points += [3]
    return points

def final_score(points:list[int]):

    result = sum(points)
    return result
        

if __name__ == "__main__":
    opponent_moves = load_moves(FILE_NAME)
    print(final_score(step_score(opponent_moves)))

