def solution(X, Y, D):
    distance = Y - X
        
    jumps = float(distance) / D
    
    jumps_int = int(jumps)
    
    if jumps > jumps_int:
        return jumps_int + 1
    
    return jumps_int