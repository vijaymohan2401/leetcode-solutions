/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverse(ListNode head){
        ListNode temp=head;
        ListNode prev=null;
        ListNode front;
        while(temp!=null){
            front=temp.next;
            temp.next=prev;
            prev=temp;
            temp=front;
        }
        return prev;
    }
    public ListNode removeNodes(ListNode head) {
       head=reverse(head);
       ListNode temp1=head;
       int max=temp1.val;
       while(temp1!=null&&temp1.next!=null){
            if(temp1.next.val<max){
                temp1.next=temp1.next.next;
            }
            else{
                temp1=temp1.next;
                max=temp1.val;
            }
           
       }
        return reverse(head);
    }
}