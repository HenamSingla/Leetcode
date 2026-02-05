class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start=sorted([i[0] for i in intervals])
        end=sorted([i[1] for i in intervals])
        print(start)
        print(end)

        count=0
        res=0
        s,e=0,0
        while s<len(intervals):
            if start[s]<end[e]:
                s+=1
                count+=1
            else:
                e+=1
                count-=1
            res=max(res,count)
        return res

        # rooms=0
        # track={}
        # for i in intervals:
        #     if not track:
        #         track[tuple(i)] = 1
        #         print(track)
        #     if i[1]<i+1[0]:
        #         track[tuple(i)] += 1
        #     else:
        #         track[tuple(i)] = 1
        #     print(track)
            # for j in intervals:
            #     if i[1]<j[0] and i!=j:
            #       rooms+=1
            #       print(i)
            #       print(f'This is {j}')
            #     if i[1]>i[0]:
            #         rooms+=1
                    
        # return rooms  
            
