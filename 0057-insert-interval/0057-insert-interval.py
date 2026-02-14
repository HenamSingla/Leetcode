class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        a=newInterval[0]
        b=newInterval[1]
        placed=False
        for i in intervals:
            #[[1,3],[6,9]]
            #s=1,e=3; s=1,e=9
            #a=2,b=5
            s=i[0]
            e=i[1]
            if a>e:
                res.append([s,e])
            elif s>b:
                if not placed:
                    res.append([a,b])
                    placed=True
                res.append([s,e])
            else:
                a=min(s,a)
                b=max(e,b)
        if not placed:
            res.append([a,b])
        return res

'''
every new interval in the result should start with start_i
ascending order by start_i
newInterval check the start of it and check where it lies meaning which interval and compare the end of new Interval where it lies. 
wherever it lies, take the start_i and check the end of Newinterval and insert the new end being end_i or end of newInterval which ever one is higher. 
a,b= newInterval
initialise an empty list
loop through every list in the array
for every list in list, i will look at the start_i and a 
and check if greater than start_i and less than end_i
if a>start_i and a<end_i
and now lets check for b, check where it lies, if b<end_j tehn merge evrything and return [start_i, end_j]
if a,b doesnt lie in the inetrval then just append it to result

corner cases: what if b==start_i?
is newInterval always one?
is interval sorted?
'''



