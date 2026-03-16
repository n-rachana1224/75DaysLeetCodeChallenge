class Solution(object):
    def groupAnagrams(self, strs):        
        res=defaultdict(list)
        for s in strs:
            key=''.join(sorted(s))
            res[key].append(s)
        return list(res.values())

