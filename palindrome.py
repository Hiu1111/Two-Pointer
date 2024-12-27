#Checks if the string is a palindrome using the two pointers method 
#Ex: "level" is a palindrome because backwards is also "level"

def palindrome(self, x):        
        left = 0 #Sets our first pointer at the start 
        right = len(x) - 1 #Sets our second, the ending pointer at the end 

        while left < right: #Set our condition to left < right since when we compare our value, left will increase and right will decrease meaning once we have compared the whole list this loop will end 
            if x[left] != x[right]: #First loop: Checks if the most left value matches the most right value, if it doesnt return false since its not a palindrome 
                return False
            left += 1 #First Loop: Left adds one [l, "e" , v , e , l], the value of quoted character is always compared to the one that is directly opposite from it, using this method we can check for palindrome 
            right -= 1 #First Loop: Right adds one [l, e, v , "e", l]

        return True #returns true since its a palindrome 

