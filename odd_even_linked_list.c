/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

#include<math.h>
struct ListNode* oddEvenList(struct ListNode* head){
    if (head == NULL) {
        return head;
    }
    struct ListNode* odd = NULL;
    struct ListNode* even = NULL;
    struct ListNode* last = head;
    int count = 1;
    while(last->next != NULL) {
        last = last->next;
        count = count + 1;
    }
    if (count == 1 || count == 2) {
        return head;
    }
    if (head->next != NULL) {
        even = head->next;
    }
    odd = head;
    count = (int)(ceil(count/2));
    struct ListNode* ebk = even;
    while (count>0) {
        odd->next = even->next;
        odd = odd->next;
        even = even->next->next;
        ebk->next = NULL;
        last->next = ebk;
        last = last->next;
        ebk = even;
        count = count - 1;
    }
    return head;

}
