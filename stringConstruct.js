

/**
 * Returns a boolean indicating whether or not the target can be constructed 
 * by concatenating elements of the wordBank array.
 * You may reuse elements of wordBank as many times as needed.
 **/
const canConstruct = (target, wordBank, memo = {}) => {
    // complexity:
    // m: target.length
    // n: wordBank.length
    //
    // time: O(n^m)  (O(n^m * m) if we include replace complexity, though it doesn't change the big O notation)
    //       with memo: O(n*m^2)
    // space: m stack calls, each has a different m-sized target, -> O(m^2)
    //        with memo I add an object with at most m^2 keys -> O(m^2 + m^2) = O(m^2)

    // // actual construction way
    // const construct = (word, memo) => {
    //     if (word in memo) return memo[word];
    //     if (word === target) return true;
    //     if (word.length >= target.length){
    //         memo[word] = false;
    //         return false;
    //     }
    //     for (let s of wordBank){
    //         if (target.includes(s)){
    //             const created = construct(word + s, memo);
    //             if (created) {
    //                 memo[word] = true;
    //                 return true;
    //             }
    //         }
    //     }
    //     memo[word] = false;
    //     return false;
    // }
    // return construct("", memo);

    // // incorrect way, it creates new adjacencies when removing subsets from the middle
    // if (target === "") return true;
    // for (let word of wordBank){
    //     if (target.includes(word)){
    //         const created = canConstruct(target.replace(word, ""), wordBank);
    //         if (created) return true;
    //     }
    // }
    // return false;

    // // kinda hacky way, what if there are _ in the target??
    // if (target === "_".repeat(target.length)) return true;
    // for (let word of wordBank){
    //     if (target.includes(word)){
    //         const created = canConstruct(target.replace(word, "_".repeat(word.length)), wordBank);
    //         if (created) return true;
    //     }
    // }
    // return false;

    // prefix only way
    if (target in memo) return memo[target];
    if (target === "") return true;
    for (let word of wordBank){
        if (target.startsWith(word)){
            const created = canConstruct(target.replace(word, ""), wordBank, memo);
            if (created) {
                memo[target] = true;
                return true;
            }
        }
    }
    memo[target] = false;
    return false;
}

// console.log(canConstruct("abc", ["a", "b", "c"]));                              // true
// console.log(canConstruct("abcd", ["a", "c", "cd", "bc", "b"]));                 // true
// console.log(canConstruct("aaaa", ["a", "b"]));                                  // true
// console.log(canConstruct("ababa", ["aba", "ab"]));                              // true
// console.log(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]));        // true
// console.log(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]));        // false
// console.log(canConstruct("abcd", ["a", "bc", "cd"]));                           // false
// console.log(canConstruct("abcdefghilmnopqrstuvz", ["a", "ab", "bc", "cd", "c", "d", "e", "f", "g", "h", "i", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "z"]));               // true
// console.log(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]));   // false



/**
 * Returns the number of ways in which the target can be constructed 
 * by concatenating elements of the wordBank array.
 * You may reuse elements of wordBank as many times as needed.
 **/
 const countConstruct = (target, wordBank, memo = {}) => {
    // complexity:
    // m = target.length
    // n = wordBank.length
    // brute force: 
    //      time: O(n^m)
    //      space: O(m^2)
    // memo:
    //      time: O(n * m^2)
    //      space: O(m^2 + m^2)
    if (target in memo) return memo[target];
    if (target == "") return 1;
    let count = 0;
    for (let word of wordBank){
        if (target.startsWith(word)){
            count = count + countConstruct(target.replace(word, ""), wordBank, memo);
        }
    }
    memo[target] = count;
    return count;
}

// console.log(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]));   // 1
// console.log(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]));   // 2
// console.log(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]));  // 4
// console.log(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]));  // 0
// console.log(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]));   // 0



/**
 * Returns all the possible ways in which the target can be constructed 
 * by concatenating elements of the wordBank array.
 * You may reuse elements of wordBank as many times as needed.
 **/
const allConstruct = (target, wordBank, memo = {}) => {
    // complexity
    // time: O(n^m)
    // space: O(m) for call stack (n^m subarrays though)
    if (target in memo) return memo[target];
    if (target === "") return [[]];

    let allCombinations = [];
    for (let word of wordBank){
        if (target.startsWith(word)){
            const thisWordCombinations = allConstruct(target.replace(word, ""), wordBank, memo);
            allCombinations.push(...thisWordCombinations.map(comb => [word, ...comb]));
        }
    }
    memo[target] = allCombinations;
    return allCombinations;
}


console.log(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]));   // [["abc", "def"]]
console.log(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]));   // [["purp", "le"], ["p", "ur", "p", "le"]]
console.log(allConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]));  // 4 ways
console.log(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]));   // []
console.log(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]));  // []
console.log(allConstruct("", ["abc"]));   // [[]]
