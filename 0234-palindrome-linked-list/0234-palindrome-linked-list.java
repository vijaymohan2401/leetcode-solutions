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
    public boolean isPalindrome(ListNode head) {
        ListNode slow=head;
        ListNode fast=head.next;
        while(fast!=null&&fast.next!=null){
            slow=slow.next;
            fast=fast.next.next;
        }
        ListNode second=slow.next;
        slow.next=null;
        ListNode temp=second;
        ListNode prev=null;
        ListNode front;
        while(temp!=null){
            front=temp.next;
            temp.next=prev;
            prev=temp;
            temp=front;
        }
        ListNode t1=head;
        ListNode t2=prev;
        while(t1!=null&&t2!=null){
        if(t1.val==t2.val){
            t1=t1.next;
            t2=t2.next;
     
        }
        else {
            return false;
        }
       
        }
        return true;
        }}