class Node {
    constructor(value, left = null, right = null){
        this.value = value;
        this.left = left;
        this.right = right;
    }
}

const newTree = () => {
    const [one, two, three, four, five, six] = [
        new Node(1),
        new Node(2), new Node(3),
        new Node(4), new Node(5), new Node(6),
    ]
    one.left = two;
    one.right = three;
    two.left = four;
    two.right = five;
    three.left = six;
    return one;
}

const equals = (list1, list2) => {
    return JSON.stringify(list1) == JSON.stringify(list2)
}


const depthFirstValues = (root) => {
    if (root == null) return [];
    return [
        root.value, 
        ...depthFirstValues(root.left), 
        ...depthFirstValues(root.right)
    ]
}

console.log(equals(depthFirstValues(newTree()), [1, 2, 4, 5, 3, 6]))


const breadthFirstValues = (root) => {
    const queue = [root];
    const values = [];
    while (queue.length > 0) {
        const current = queue.shift();
        if (current == null) continue;
        values.push(current.value);
        queue.push(current.left);
        queue.push(current.right);
    }
    return values
}

console.log(equals(breadthFirstValues(newTree()), [1, 2, 3, 4, 5, 6]))


const maxRootToLEafPath = (root, pathSum = 0) => {
    if (root == null) return pathSum;
    return Math.max(
        maxRootToLEafPath(root.left, pathSum + root.value), 
        maxRootToLEafPath(root.right, pathSum + root.value), 
    )
}

console.log(maxRootToLEafPath(newTree()) == 10)
