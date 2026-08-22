class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))#sort to "a","e","t"
            res[sortedS].append(s)#joins sorteds and s 

        return list(res.values())#convert it to list from dictionary