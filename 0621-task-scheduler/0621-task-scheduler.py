class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # paraphrase
        # given an array of tasks, representetd by a letter from A-Z
        # an interval for a CPU can be: either IDLE or used to complete ONE task
        # tasks from the array can be completed in ANY order
        # constraint: we need a gap of at lease n intervals between 
        # any 2 intervals where we complete tasks of the same letter
        
        # we need at least len(tasks) intervals, since each interval can complete 1 task
        # we need at most len(tasks) + n * len(tasks) intervals

        # dry runs (examples)
        # Input: tasks = ["A","A","A","B","B","B"], n = 2
        # A > B > _ > A > B > _ > A > B

        # Input: tasks = ["A","A","A","A"], n = 2
        # A > _ > _ A > _ > _ > A > _ > _ > A

        # map of frequency of each task
        task_freq = {}
        for task in tasks:
            task_freq[task] = task_freq.get(task, 0) + 1
        
        # create a max heap
        # the heap contains the count of every single task
        # counts only, no need to know which task its associated to
        max_heap = [-count for count in task_freq.values()]
        heapq.heapify(max_heap)

        time = 0
        # contains pair of values (-count, idle_time), 
        # idle_time is the time its available to add back to the max heap
        # queue contains all the tasks that need to be completed
        q = collections.deque()

        while max_heap or q:
            # as long as heap or q is nonempty, that means we have more tasks to complete
            time += 1

            if max_heap:
                # plus 1 to decrement the count b/c we're using neg values in our heap
                count = heapq.heappop(max_heap) + 1

                if count != 0:
                    # add the count and the time at which it'll be available again
                    # which is just the current time PLUS the cooldown time n
                    q.append([count, time + n])
                
            if q and q[0][1] == time:
                # we can pop it from our queue
                heapq.heappush(max_heap, q.popleft()[0])
        
        return time