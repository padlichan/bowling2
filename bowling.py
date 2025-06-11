def calc_score(frames):
   if frames == "X":
        return 10
   elif len(frames) == 2:
       return int(frames[0]) + int(frames[1])
   else: 
        return 0