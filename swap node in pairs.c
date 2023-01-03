#https://leetcode.com/problems/swap-nodes-in-pairs/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* swapPairs(struct ListNode* head){
    struct ListNode* temp = head;
    struct ListNode* curr = head;
    struct ListNode* prev = NULL;
    if (head == NULL)
        return head;
    if (head->next == NULL) {
        return head;
    }
    int t = 0;
    struct ListNode* fp = head;
    while (curr && fp && fp->next) {
        t = 0;
        printf("start c:%d\n", curr->val);
        if (fp != curr) {
          curr = fp;
          prev = curr;
          curr = curr->next;
          t = curr->val;
          curr->val = prev->val;
          prev->val = t;
          printf("if c:%d p:%d\n", curr->val, prev->val);
          fp = fp->next->next;
        }
        else {
        prev = curr;
        curr = curr->next;
        fp = fp->next->next;
        t = curr->val;
        curr->val = prev->val;
        prev->val = t;
        printf("else c:%d p:%d\n", curr->val, prev->val);
        }
    }
    return head;

}
