def calc_score(frames):
   total_score = 0
   frame_list = frames.split()
   if frames == "X":
        return 10
   elif len(frames) == 2:
       return int(frames[0]) + int(frames[1])
   else: 
        for frame in frame_list:
            rolls_in_frame = list(frame)
            total_score += int(rolls_in_frame[0])
            total_score += int(rolls_in_frame[1])
        
        return total_score
   
calc_score("23 62")