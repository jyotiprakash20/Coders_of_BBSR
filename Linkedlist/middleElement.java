import java.util.Scanner;

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

public class middleElement {

    public static Node middleele(Node head){
        Node slow = head;
        Node fast = head;
        while(fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }

    public static void printLL(Node head){
        while(head != null){
            System.out.print(head.data+"->");
            head = head.next;
        }
        System.out.println();
    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the number of nodes: ");
        int n = sc.nextInt();

        Node head = null, tail = null;
        System.out.println("Enter the Node values");
        for(int i = 0; i<n;i++){
            int value = sc.nextInt();
            Node newNode = new Node(value);

            if(head == null){
                head = newNode;
                tail = newNode;
            }else{
                tail.next = newNode;
                tail = newNode;
            }
        }

        System.out.print("Linked list:");
        printLL(head);

        Node mid = middleele(head);
        System.out.println("Middle element: "+mid.data);
        

        sc.close();

    }
}
