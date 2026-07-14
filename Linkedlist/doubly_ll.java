class Node{
    int data;
    Node next;
    Node back;

    Node(int data1, Node next1, Node back1){
        this.data = data1;
        this.next = next1;
        this.back = back1;
    }
    Node(int data1){
        this.data = data1;
        this.next = null;
        this.back = null;
    }

}


public class doubly_ll {
    public static Node convertarrtoDll(int[] arr){
        Node head = new Node(arr[0]);
        Node prev = head;

        for(int i = 1; i <arr.length; i++){
            Node temp = new Node (arr[i],null,prev);
            prev.next = temp;
            prev = temp;
        }
        return head;
    }
    //Insert element in DLL
    public static Node insertHead(Node head, int val){
        Node newhead = new Node(val,head, null);
        head.back = newhead;

        return newhead;
    }
    public static Node insertbeforetail(Node head, int val){
        if (head.next == null){
            return insertHead(head,val);
        }
        Node tail = head;
        while(tail.next != null){
            tail = tail.next;
        }
        Node prev = tail.back;
        Node newNode = new Node(val, tail,prev);
        prev.next = newNode;
        tail.back = newNode;

        return head;
    }
    //Insert before kth element
    public static Node insertbeforeK(Node head, int k, int val){
        if (k == 1){
            return insertHead(head, val);
        }
        int count = 0;
        Node temp = head;
        while(temp != null){
            count++;
            if(count == k){
                break;
            }
            temp = temp.next;
        }
        Node prev = temp.back;
        Node newNode= new Node(val,temp,prev);
        prev.next = newNode;
        temp.back = newNode;

        return head;
    }
    //Insert element before given Node
    public static void insertbeforeNode(Node node, int val){
        Node prev = node.back;
        Node newNode = new Node(val, node, prev);
        prev.next = newNode;
        node.back = newNode;
    }
    private static void print(Node head){
         Node temp = head;
        while(temp != null){
            System.out.print(temp.data+"<->");
            temp = temp.next;
        }
        System.out.println();
    }
    //Delete the head element
    private static Node deleteHead(Node head){
        if(head == null || head.next == null){
            return null;
        }
        Node prev = head;
        head = head.next;

        head.back = null;
        prev.next = null;

        return head;
    }
    //Delete the tail element
    private static Node deleteTail(Node head){
        if(head == null || head.next == null){
            return null;
        }
        Node tail = head;
        while(tail.next != null){
            tail=tail.next;
        }
        Node newtail = tail.back;
        newtail.next = null;
        tail.back = null;

        return head;
    }
    //Delete the kth element
    private static Node deleteKelement(Node head, int k){

        if(head == null){
            return null;
        }
        int count = 0;
        Node kNode = head;
        while(kNode != null){
            count++;
            if(count==k) break;
            kNode = kNode.next;
        }
        Node prev = kNode.back;
        Node front = kNode.next;

        if(prev == null && front == null){
            return null;
        }
        else if(prev == null){
            return deleteHead(head);
        }
        else if(front == null){
            return deleteTail(head);
        }
        prev.next = front;
        front.back = prev;

        kNode.next = null;
        kNode.back = null;
        return head;
    }
    //Delete the Node
    private static void deleteNode(Node temp){
        Node prev = temp.back;
        Node front = temp.next;

        if(front == null){
            prev.next = null;
            temp.back = null;
            return;
        }
        prev.next = front;
        front.back = prev;
        temp.back = temp.next = null;

    }
    //Reverse a DLL
    private static Node reverseDll(Node head){
        if (head == null || head.next == null){
            return head;
        }
        Node prev = null;
        Node current = head;
        while(current != null){
            prev = current.back;
            current.back = current.next;
            current.next = prev;
            current = current.back;
        }
        return prev.back;
    }
    public static void main(String[] args) {
        int[] arr = {2,5,7,1};
        Node head = convertarrtoDll(arr);
        // head = insertHead(head, 100);//Insert element before head
        // head = insertbeforetail(head, 50);//insert element before tail
        //  head = insertbeforeK(head, 4,20);
        // insertbeforeNode(head.next.next, 30);
        // head = deleteHead(head);//Delete the head
        // head = deleteTail(head);//Delete the tail
        // head = deleteKelement(head, 2);//Delete the kth element
        // deleteNode(head.next.next);//Delete the Node
        // head = reverseDll(head);//Reverse a linked list
        print(head);
        
    }
    
}
