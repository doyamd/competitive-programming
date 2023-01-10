#https://leetcode.com/problems/subdomain-visit-count/description/
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dom_count=collections.defaultdict(int)
        
        for dom in cpdomains:
            count,domain=dom.split() #spliting the visits and the domain
            count=int(count)
            sub_domain=domain.split('.')
            #counting each sub domain
            for i in range(len(sub_domain)):
                sub='.'.join(sub_domain[i:])
                dom_count[sub]+=count
                # returning in string form
        return (f"{count} {domain}" for domain,count in dom_count.items())
