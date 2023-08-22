        
        l = 0
        r = len(A) - 1
        while True:
            i = (l+r)//2
            j = half - i - 2
            
            leftA = A[i] if i >= 0 else float
('-inf')
            rightA = A[i+1] if i < len(A) - 
1 else float('inf')
            leftB = B[j] if j >= 0 else float
('-inf')
            rightB = B[j+1] if j < len(B) - 
1 else float('inf')
            
            if leftA <= rightB and leftB <= 
rightA:
                if total % 2 == 0:
                    return (max(leftA,leftB) 
+ min(rightA,rightB))/2
                else:
                    return min(rightA,rightB)
            elif leftA > rightB:
                r = i-1
            else:
                l = i+1