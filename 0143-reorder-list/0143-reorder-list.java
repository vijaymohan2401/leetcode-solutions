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
    public void reorderList(ListNode head) {
        if(head==null||head.next==null){
            return;
        }
            ListNode slow=head;
            ListNode fast=head;
            while(fast.next!=null&&fast.next.next!=null){
                slow=slow.next;
                fast=fast.next.next;
            }    
            ListNode temp=slow.next;
            slow.next=null;
            ListNode prev=null;
            ListNode front;
            while(temp!=null){
                front=temp.next;
                temp.next=prev;
                prev=temp;
                temp=front;
            }
            ListNode first=head;
            ListNode second=prev;
            while(second!=null){
                ListNode first1=first.next;
                ListNode second1=second.next;
                first.next=second;
                second.next=first1;
                first=first1;
                second=second1;
            }
    }
}