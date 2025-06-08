# data stream solution with queue: 145
# ms
# Beats
# 19.06%
class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        q = deque([])
        hashSet = set()
        time = 0
        for task in tasks:
            while q and q[0][0] <= time: # <-- clear the expired task type
                hashSet.remove(q.popleft()[1])
            if task in hashSet:
                while q[0][1] != task: # <-- clear the task type before the current task type
                    hashSet.remove(q.popleft()[1])
                hashSet.remove(task)
                time = q.popleft()[0] # <-- reassign the current time to meet the schedule

            # the task is done after this line -----------------------------------------

            time += 1
            q.append([time+space, task]) # <-- time allowed to do the same task type again
            hashSet.add(task)
        return time
