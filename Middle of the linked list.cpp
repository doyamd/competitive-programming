/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* current;
        current=head;
        int count=0;
        while(current!=NULL){
            current=current->next;
             count++;
        }
        if(count%2==0) count=(count/2)+1;
        else count=(count+1)/2;
        current=head;
        while(count>1){
            current=current->next;
        count--;
        }
        return current;
    }
};
