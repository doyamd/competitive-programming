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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode*current1=list2;
        ListNode*current2=list1;
        ListNode*dummyNode=new ListNode(-1);
        ListNode*ptr=dummyNode;
         
      
             while(current1!=NULL && current2!=NULL){
            if(current2->val<current1->val){
                ptr->next=current2;
                current2=current2->next;
                ptr=ptr->next;
            }
            else{
                ptr->next=current1;
                current1=current1->next;
                ptr=ptr->next;
            }
        }
        if(current1!=NULL) ptr->next=current1;
        if(current2!=NULL) ptr->next=current2;
        
        
        
        return dummyNode->next;
    }
};
