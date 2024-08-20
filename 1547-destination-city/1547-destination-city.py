class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # all_elements = set()
        # origin_elements = set()

        # for path in paths:
        #     all_elements.add(path[0])
        #     all_elements.add(path[1])
        #     origin_elements.add(path[0])
        
        # dest = (all_elements - origin_elements).pop()
        # return dest

        map = dict()
        for i in paths:
            map[i[0]] = i[1]
        for j in paths:
            if j[1] not in map:
                return j[1]
        return "" 