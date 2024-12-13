class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        queue = []
        prereq_count = dict() # keep courses: prereq count
        prereqs = dict() # keep prereq : courses
        for course, prereq in prerequisites:
            if course not in prereq_count:
                prereq_count[course] = 0
            if prereq not in prereq_count:
                prereq_count[prereq] = 0
            prereq_count[course] += 1
            if course not in prereqs:
                prereqs[course] = []
            if prereq not in prereqs:
                prereqs[prereq] = []
            prereqs[prereq].append(course)
        for course, count in prereq_count.items():
            if count == 0:
                queue.append(course)
        while queue:
            current_course = queue.pop(0)
            dependents = prereqs[current_course]
            print(current_course)
            for dependent in dependents:
                prereq_count[dependent] -= 1
                if prereq_count[dependent] == 0:
                    print("adding", dependent, "to queue")
                    queue.append(dependent)
        return max(prereq_count.values()) == 0
        
        