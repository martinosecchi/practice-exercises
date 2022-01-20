
/**
 * Returns a boolean indicating whether or not it is possible to generate the `targetSum` using numbers
 * from the `numbers` array.
 * You may use an element of the array as many times as needed.
 * You may assume that all input numbers are non-negative.
 */
// O(n*m)
const canSumMemo = (targetSum, numbers, memo = {}) => {
    if (targetSum in memo) return memo[targetSum];
    if (targetSum === 0) return true;
    if (targetSum < 0) return false;
    for (number of numbers){
        const result = canSumMemo(targetSum - number, numbers, memo);
        if (result) {
            memo[targetSum] = true;
            return true;
        }
    }
    memo[targetSum] = false;
    return false;
}

// console.log(canSumMemo(5, [1, 2]) === true);
// console.log(canSumMemo(7, [5,3,4,7]) === true);
// console.log(canSumMemo(7, [2,4]) === false);


// O(n*m)
const canSumTab = (targetSum, numbers) => {
    const table = Array(targetSum + 1).fill(false);
    table[0] = true;   // canSum(0, [...]) -> true
    for (let i = 0; i < targetSum + 1; i++){
        if (table[i] === false) continue;
        for (num of numbers){
            const j = i + num;
            if (j <= targetSum) {
                table[j] = true;
            }
        }
    }
    return table[targetSum];
}

// console.log(canSumTab(5, [1, 2]) === true);
// console.log(canSumTab(7, [5,3,4,7]) === true);
// console.log(canSumTab(7, [2,4]) === false);


/**
 * Return an array containing any combination of elements that add up to exactly targetSum.
 * If there is no such combination, return null.
 * If there are multiple combinations, return any one of them.
 * You may use an element of the array as many times as needed.
 * You may assume that all input numbers are non-negative.
 */
const howSumMemo = (targetSum, numbers, memo = {}) => {
    if (targetSum in memo) return memo[targetSum];
    if (targetSum === 0) return [];
    if (targetSum < 0) return null;

    for (let number of numbers){
        const combination = howSumMemo(targetSum - number, numbers, memo);
        if (combination !== null) {
            memo[targetSum] = [number, ...combination];
            return memo[targetSum];
        }
    }
    memo[targetSum] = null;
    return null

}


// console.log(howSumMemo(5, [2, 1]));
// console.log(howSumMemo(7, [5,3,4,7]));
// console.log(howSumMemo(7, [2,4]));
// console.log(howSumMemo(10, [3, 2, 1]));
// console.log(howSumMemo(0, [1,2,3]));


const howSumTab = (targetSum, numbers) => {
    const table = Array(targetSum + 1).fill(null);
    table[0] = [];

    for (let i = 0; i < targetSum + 1; i++){
        if (table[i] === null) continue;
        for (number of numbers){
            const j = i + number;
            if (j <= targetSum){
                table[j] = [number, ...table[i]];
            }
        }
    }
    return table[targetSum];
}


// console.log(5, howSumTab(5, [2, 1]));
// console.log(7, howSumTab(7, [5, 3, 4, 7]));
// console.log(7, howSumTab(7, [2, 4]));
// console.log(10, howSumTab(10, [3, 2, 1]));
// console.log(0, howSumTab(0, [1, 2, 3]));


/**
 * Return an array containing the shortest combination of numbers that add up to exactly
 * the targetSum.
 * If there is a tie in the shortest combination, you may return any one of the shortest.
 * You may use an element of the array as many times as needed.
 */
const bestSumMemo = (targetSum, numbers, memo = {}) => {
    if (targetSum in memo) return memo[targetSum];
    if (targetSum == 0) return [];
    if (targetSum < 0) return null;

    let shortestCombination = null;
    for (const number of numbers) {
        const combination = bestSumMemo(targetSum - number, numbers, memo);
        if (combination !== null && (shortestCombination === null || combination.length + 1 < shortestCombination.length)){
            shortestCombination = [number, ...combination];
        }
    }
    memo[targetSum] = shortestCombination;
    return shortestCombination;
}

// console.log(bestSumMemo(7, [5, 3, 4, 7]));  // [7]
// console.log(bestSumMemo(8, [2, 3, 5]));     // [3, 5]
// console.log(bestSumMemo(9, [2, 4]));        // null
// console.log(bestSumMemo(0, [2, 4]));        // []


const bestSumTab = (targetSum, numbers) => {
    const table = Array(targetSum + 1).fill(null);
    table[0] = [];

    for (let i = 0; i < targetSum + 1; i++) {
        if (table[i] === null) continue;
        for (const number of numbers) {
            const j = i + number;
            if (j <= targetSum){
                if (table[j] === null || table[j].length > table[i].length + 1){
                    table[j] = [...table[i], number];
                }
            }
        }
        
    }

    return table[targetSum];
}

// console.log(bestSumTab(7, [5, 3, 4, 7]));  // [7]
// console.log(bestSumTab(8, [2, 3, 5]));     // [3, 5]
// console.log(bestSumTab(9, [2, 4]));        // null
// console.log(bestSumTab(0, [2, 4]));        // []
