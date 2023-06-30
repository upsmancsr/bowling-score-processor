# You've been asked to write a calculator to sum an individual player's rolls
# and return their score for each frame. The method should accept an array of rolls.
# Possible values include zero through nine, a "/" indicating a spare, and an "X"
# indicating a strike. The return value should be an array of scores for the frames the
# player has bowled.

# The scoring method will be used to calculate a player's running score during
# the game, so it's important that the method works for games in progress. For example,
# [4, 5, "X", 8] should return [9, nil, nil], since the second and third frames can't be
# calculated yet. When the second roll of the third frame comes in, all three frames
# should be returned, e.g. [4, 5, "X", 8, 1] would return [9, 19, 9]. (Note that these are
# the scores for the frames, not the running score).

def calculate_scores(rolls):
    frames = []
    frame = []

    for roll in rolls:
        if roll == "X":  # Strike
            frame.append(10)
            frames.append(frame)
            frame = []
        elif roll == "/":  # Spare
            frame.append(10 - frame[0])
            frames.append(frame)
            frame = []
        else:  # Numeric roll
            frame.append(int(roll))
            if len(frame) == 2:
                frames.append(frame)
                frame = []

    if frame:  # Last frame is in progress
        frames.append(frame)

    scores = []
    for i, frame in enumerate(frames):
        if len(frame) == 1:  # Strike
            if i + 2 < len(frames):  # Two following frames exist
                scores.append(10 + frames[i+1][0] + frames[i+2][0])
            elif i + 1 < len(frames) and len(frames[i+1]) == 2:  # One following frame exists and is complete
                scores.append(10 + frames[i+1][0] + frames[i+1][1])
            else:  # Not enough rolls after the strike to calculate the score yet
                scores.append(None)
        elif frame[0] + frame[1] == 10:  # Spare
            if i+1 < len(frames) and len(frames[i+1]) > 0:  # Following frame exists and has at least one roll
                scores.append(10 + frames[i+1][0])
            else:  # Not enough rolls after the spare to calculate the score yet
                scores.append(None)
        else:  # Open frame
            scores.append(sum(frame))

    return scores



# If you want to run this file directly in terminal with `python calculator.py`
# here are some print statements testing various scenarios
if __name__ == "__main__":
    print(calculate_scores([4, 5, "X", 8, 1]))  # Expected output: [9, 19, 9]
    print(calculate_scores([4, 5, "X", 8]))  # Expected output: [9, None, None]
    print(calculate_scores(["X", "X", 8]))  # Expected output: [None, None, None]
    print(calculate_scores(["X", 4, "/", 1, 3, 5, "/", 5, 2]))

