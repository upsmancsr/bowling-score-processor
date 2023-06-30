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


if __name__ == "__main__":
    print(calculate_scores([4, 5, "X", 8, 1]))  # Expected output: [9, 19, 9]
    print(calculate_scores([4, 5, "X", 8]))  # Expected output: [9]

