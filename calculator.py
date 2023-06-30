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
    scores = []
    current_frame = []

    for roll in rolls:
        if roll == "X":
            current_frame.append(10)
        elif roll == "/":
            current_frame.append(10 - sum(current_frame))
        else:
            current_frame.append(roll)
            
        if sum(current_frame) >= 10 or len(current_frame) == 2:
            frames.append(current_frame)
            current_frame = []

    for i, frame in enumerate(frames):
        frame_score = sum(frame)
        if 10 in frame and i + 1 < len(frames):  # strike or spare
            frame_score += sum(frames[i + 1][:2 if len(frame) == 1 else 1])
        scores.append(frame_score)
        
    return scores[:10]  # Only return scores for the first 10 frames


# If you want to run this file directly in terminal with `python calculator.py`
# here are some print statements testing various scenarios
if __name__ == "__main__":
    print(calculate_scores([4, 5, "X", 8, 1]))  # Expected output: [9, 19, 9]
    print(calculate_scores([4, 5, "X", 8]))  # Expected output: [9]
    print(calculate_scores(["X", "X", 8]))  # Expected output: [20, 10]

