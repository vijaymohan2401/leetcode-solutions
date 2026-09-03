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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy=new ListNode(0);
        ListNode curr=dummy;
       
        ListNode temp3=l1;
        ListNode prev1=null;
        ListNode front1;
        while(temp3!=null){
            front1=temp3.next;
            temp3.next=prev1;
            prev1=temp3;
            temp3=front1;
        }
         ListNode temp4=l2;
        ListNode prev2=null;
        ListNode front2;
        while(temp4!=null){
            front2=temp4.next;
            temp4.next=prev2;
            prev2=temp4;
            temp4=front2;
        }
         ListNode temp1=prev1;
        ListNode temp2=prev2;
          int carry=0;
    while(temp1!=null||temp2!=null){
            int sum=carry;
            if(temp1!=null){
                sum=sum+temp1.val;
            }
            if(temp2!=null){
                sum=sum+temp2.val;
            }
            ListNode newnode=new ListNode(sum%10);
            carry=sum/10;
            curr.next=newnode;
            curr=curr.next;
            if(temp1!=null){
                temp1=temp1.next;

            }
            if(temp2!=null){
                temp2=temp2.next;
            }
    }
    if(carry!=0){
        ListNode node1=new ListNode(carry);
        curr.next=node1;
    }
     ListNode temp5=dummy.next;
        ListNode prev3=null;
        ListNode front3;
        while(temp5!=null){
            front3=temp5.next;
            temp5.next=prev3;
            prev3=temp5;
            temp5=front3;
        }
    return prev3;
}}