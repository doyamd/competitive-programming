#https://leetcode.com/problems/find-duplicate-file-in-system/description/
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        path_count=collections.defaultdict(list)
        duplicate_files=[]
        for files in paths:
            path=files.split() #spliting the root and the internal files
            root=path[0]
            for sub_path in (path[1:]):
                directory, content=sub_path.split('(') # to get the content of the file
                path_count[content].append(root + "/" + directory) # merging the root and the path
        for key, val in path_count.items():
            temp=[]
            if len(val)>1: # finding files repeated morethan onec
                for j in val:
                    temp.append(j)
                duplicate_files.append(temp)
        return(duplicate_files)
