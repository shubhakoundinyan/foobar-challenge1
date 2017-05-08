#!/ usr/bin/python

#   This algorithm works on PATTERN RECOGNITION

#   i -> Length at current iteration
#   start1, end--> start and end of the current row/array

#   If length = 1 -> checksum ^=end
#   If start1 = even, i%2 = 0 -> checksum ^=1
#   If start1 = even, i%4 = 0 -> checksum ^=0

#   If start1 = odd, i=3 -> checksum ^= start 1-1
#                (i-3)%4 = 0 -> checksum ^= start 1-1
#                (i-3)%2 = 0 -> checksum ^= start1

#   If start1 = even, i<3 -> checksum ^= start1^end
#               (i-1) = 3 -> checksum ^= (start1-1)^end
#               (i-1-3)%4 = 0 -> checksum ^= (start1-1)^end
#               (i-1-3)%2==0 --> checksum ^= (start1)^end

def answer(start, length):

    result = 0
    count = 0
    end = start
    for i in xrange(length, 0, -1):
        count = count+1
        start1 = start + (count-1)*length
        end = end +(length -1)
        
        if i==1:
            result ^=end
        
        elif start1%2==0 and i%2==0:
            if i%4==0:
                result ^=0
            elif i%2==0:
                result ^=1
                
        elif start1%2==0 and i%2!=0:
            if (i-1)%4==0:
                result ^=end
            elif (i-1)%2==0:
                result ^=end^1
                
        elif start1%2!=0 and i%2!=0:
            if i==3:
                result ^=start1-1
            elif (i-3)%4==0:
                result ^=start1-1
            elif (i-3)%2==0:
                result ^=start1
                
        elif start1%2!=0 and i%2==0:
            if i<3:
                result ^=(start1)^end
            elif (i-1)==3:
                result ^=(start1-1)^end
            elif (i-1-3)%4==0:
                result ^=(start1-1)^end
            elif (i-1-3)%2==0:
                result ^=(start1)^end
                
    return int(result)        