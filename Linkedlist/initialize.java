class Node{
    int data;
    Node next;

    Node(int data1, Node next1){
        this.data = data1;
        this.next = next1;
    }
    Node(int data1){
        this.data = data1;
        this.next = null;
    }
}
public class initialize{
    //Convert Array to linked list
    private static Node convertArrToLL(int[] arr){
        Node head = new Node (arr[0]);
        Node mover = head;
        for(int i = 1; i<arr.length;i++){
            Node temp = new Node(arr[i]);
            mover.next = temp;
            mover = temp;
        }
        return head;
    }
    //Length of linked list
    private static int lengthLL(Node head){
        int count = 0;
        Node temp = head;
        while(temp != null){
            temp = temp.next;
            count++;
        }
        return count;
    }

    //Check if the value is present the linked list or not
    private static int checkPresent(Node head, int val){
        Node temp = head;
        while(temp != null){
            if (temp.data == val){
                return 1;
            }
            temp = temp.next;
        }
        return 0;
    }
    //Insert element at the head
    public static  Node inserthead(Node head, int val){
        
            Node temp = new Node(val, head);
            return temp;
        
    }
    // Insert element at the tail
    public static Node inserttail(Node head, int val){
        if (head == null){
            return new Node(val);
        }
        Node temp = head;
        while (temp.next != null){
            temp = temp.next;
        }
        Node newNode = new Node(val);
        temp.next = newNode;
        return head;
    }
    //Insert element at the kth place
    public static Node insertK(Node head,int ele,int k){
        if(head == null){
            if(k==1){
                return new Node(ele);
            }else{
                return head;
            }
        }
        if(k==1){
            Node temp = new Node(ele,head);
            return temp;
        }
        int count = 0;
        Node temp = head;
        while(temp != null){
            count++;

            if(count == k-1){
                Node x = new Node(ele);
                x.next = temp.next;
                temp.next = x;
                break;
            }
            temp = temp.next;
        }
        return head;
    }
    //Insert element before given value
    public static Node insertVal(Node head, int ele, int val){
        if (head==null){
            return null;
        }
        if(head.data == val){
            return new Node(ele, head);
        }
        Node temp = head;
        while(temp.next != null){
            if(temp.next.data == val){
                Node x = new Node(ele);
                x.next = temp.next;
                temp.next = x;
                break;
            }
            temp = temp.next;
        }
        return head;
    }

    public static void main(String[] args){
        int[] arr = {2,5,7,1};
        Node head =  convertArrToLL(arr);

        // head = inserthead(head, 9);// Insert value at the head
        // head = inserttail(head, 10);//insert value at the end
        // head = insertK(head, 100,3);//Insert value at k place
        head = insertVal(head, 200, 7);//Insert element before given value
        //Traverse a linked list
        Node temp = head; // Don't temper your head , always create a temp variable for traversal
        while(temp != null){
            System.out.print(temp.data+"->");
            temp = temp.next;
        }
        // System.out.println(lengthLL(head));//Returns the length of linked list

        // System.out.println(checkPresent(head, 8));// If present return 1 else 0
        
        System.out.println(head);
    }
}