
class Node {
    constructor(value, next = null){
        this.value = value;
        this.next = next;
    }
}

const listToString = (head) => {
    if (head == null) return ""
    return head.value.toString() + listToString(head.next)
}


const newList = () => {
    d = new Node("D")
    c = new Node("C", d)
    b = new Node("B", c)
    a = new Node("A", b)
    return a
}

console.log(listToString(newList()) == "ABCD")


const reverse = (head, prev = null) => {
    if (head == null) return prev;
    const next = head.next;
    head.next = prev;
    return reverse(next, head);
}

const reversed = reverse(newList())
console.log(listToString(reversed) == "DCBA")


const zipperList = (head1, head2) => {
    if (head1 == null) return head2;
    if (head2 == null) return head1;
    const next1 = head1.next;
    const next2 = head2.next;
    head1.next = head2;
    head2.next = zipperList(next1, next2)
    return head1
}

const list1 = newList();            // A B C D
const list2 = reverse(newList());   // D C B A
console.log(listToString(zipperList(list1, list2)) == "ADBCCBDA")

console.log(listToString(zipperList(newList(), new Node("Z"))) == "AZBCD")
console.log(listToString(zipperList(new Node("Z"), newList())) == "ZABCD")

