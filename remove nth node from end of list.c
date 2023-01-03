#https://leetcode.com/problems/remove-nth-node-from-end-of-list/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    struct ListNode* curr = head;
    struct ListNode* prev = NULL;
    struct ListNode* cnt = head;
    int count = 0 ;
    while (cnt!=NULL) {
        count = count+1;
        cnt = cnt->next;
    }
    if ((count - n) == 0) {
        head = head->next;
        return head;
    }
    int ncnt = 0;
    while(curr!=NULL) {
        if (ncnt == (count - n)) {
            //printf("Inside if\n");
            prev->next = curr->next;
            curr = curr->next;
            ncnt = ncnt + 1;
        }
        else {
            prev = curr;
            curr = curr->next;
            //if(prev && curr)
            // printf("inside else prev: %d curr%d \n", prev->val, curr->val);
            ncnt = ncnt + 1;
        }
    }
    //printf("%d", count);
    return head;
    
}
