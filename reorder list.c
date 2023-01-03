//https://leetcode.com/problems/reorder-list/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


void reorderList(struct ListNode* head){
    struct ListNode* fp = head;
    struct ListNode* sp = head;
    struct ListNode* split = NULL;
    while (fp != NULL && fp -> next != NULL) {
        fp = fp -> next -> next;
        split = sp;
        sp = sp -> next;
    }
    if (split)
        split->next = NULL;
    else
        return head;
    struct ListNode* mid = sp;
    struct ListNode* prev = NULL;
    struct ListNode* curr = mid;
    struct ListNode* temp = mid;
    while(temp != NULL) {
        temp = temp->next;
        curr->next = prev;
        prev = curr;
        mid = curr;
        curr = temp;
    }
    struct ListNode* final = head;
    fp = final;
    sp = mid;
    struct ListNode* newlist = NULL;
    while(final != NULL && mid != NULL) {
        final = final->next;
        fp->next = NULL;
        if (newlist == NULL) {
            newlist = fp;
            head = newlist;
        }
        else {
            newlist->next = fp;
            newlist = newlist->next;
        }
        fp = final;
        mid = mid -> next;
        sp->next = NULL;
        newlist->next = sp;
        sp = mid;
        newlist = newlist->next;
    }
    if(mid) {
        newlist->next = mid;
        newlist = newlist->next;
    }
    newlist->next = NULL;
    
    return newlist;
}
