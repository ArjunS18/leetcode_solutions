//https://leetcode.com/problems/linked-list-cycle-ii/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *detectCycle(struct ListNode *head) {

    if(head == NULL || head->next == NULL) {
        return NULL;
    }
    int match = 0;
    struct ListNode* fp = head; 
    struct ListNode* sp = head;
    struct ListNode* temp = NULL;
    while (fp != NULL && fp -> next != NULL) {
        sp = sp -> next;
        fp = fp -> next -> next;
        //printf("s: %d, f: %d\n", sp->val, fp->val);
        if (sp == fp) {
            match = 1;
            break;
        }
    }
    if(!match) 
        return NULL;
    fp = head;
    while(fp != sp) {
        fp = fp -> next;
        sp = sp -> next;
        }
    return fp;
    
    
}
