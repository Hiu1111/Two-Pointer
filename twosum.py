#Two Sum(Input is sorted)
#Two Pointer Method 

def twosum(self, numbers, target):
    l = 0 #sets first pointer to 0 
    r = len(numbers) - 1 #sets second pointer to the end 

    while l < r: 
        s = numbers[l] + numbers[r] #gets the sum to use to find the target
        if s == target: #if its equal to the target it returns the index of the numbers
            return [l+1, r+1]
        elif s < target: #if its less than the target we move the left pointer one to right 
            l += 1 
        else:
            r -= 1 #if its more tha the target we move the right pointer to the left, we adjust both these pointers until our target is reached 
        

    return [] #target not found return nothing 