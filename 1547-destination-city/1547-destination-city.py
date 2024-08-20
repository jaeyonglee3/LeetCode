class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        all_elements = set()
        origin_elements = set()

        for path in paths:
            all_elements.add(path[0])
            all_elements.add(path[1])
            origin_elements.add(path[0])
        
        dest = (all_elements - origin_elements).pop()
        return dest
