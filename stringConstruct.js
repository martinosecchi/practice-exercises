

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
// console.log(canConstruct("ababa", ["aba", "ab"]));                              // true
// console.log(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]));        // true
// console.log(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]));        // false
// console.log(canConstruct("abcd", ["a", "bc", "cd"]));                           // false
// console.log(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]));   // false


const canConstructTab = (target, wordBank) => {
    const m = target.length + 1
    const table = Array(m).fill(false);
    table[0] = true;
    // "" t a r g e t
    //  t f f f f f f     t: true, f: false

    for (let i = 0; i < m; i++) {
        if (table[i] === false) continue;
        for (const word of wordBank) {
            if (target.substring(i).startsWith(word)){
                table[word.length + i] = true;
            }
        }
    }
    return table[m-1];
}

// console.log(canConstructTab("abc", ["a", "b", "c"]) === true);                              // true
// console.log(canConstructTab("abcd", ["a", "c", "cd", "bc", "b"]) === true);                 // true
// console.log(canConstructTab("ababa", ["aba", "ab"])) === true;                              // true
// console.log(canConstructTab("abcdef", ["ab", "abc", "cd", "def", "abcd"]) === true);        // true
// console.log(canConstructTab("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]) === false);        // false
// console.log(canConstructTab("abcd", ["a", "bc", "cd"]) === false);                           // false
// console.log(canConstructTab("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]) === false);   // false



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


const countConstructTab = (target, wordBank) => {
    const m = target.length + 1;
    const table = Array(m).fill(0);
    table[0] = 1;
    // "" t a r g e t
    //  1 0 0 0 0 0 0 

    for (let i = 0; i < m; i++) {
        if (table[i] === 0) continue;
        for (const word of wordBank) {
            if (target.substring(i).startsWith(word) && word.length + i < m){
                table[word.length + i] += table[i];
            }
        }
    }
    return table[m - 1];
}


// console.log(countConstructTab("abcdef", ["ab", "abc", "cd", "def", "abcd"]) === 1);   // 1
// console.log(countConstructTab("purple", ["purp", "p", "ur", "le", "purpl"]) === 2);   // 2
// console.log(countConstructTab("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]) === 4);  // 4
// console.log(countConstructTab("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]) === 0);  // 0
// console.log(countConstructTab("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]) === 0);   // 0



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


// console.log(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]));   // [["abc", "def"]]
// console.log(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]));   // [["purp", "le"], ["p", "ur", "p", "le"]]
// console.log(allConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]));  // 4 ways
// console.log(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]));   // []
// console.log(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]));  // []
// console.log(allConstruct("", ["abc"]));   // [[]]


const allConstructTab = (target, wordBank) => {
    const m = target.length + 1;
    const table = Array(m).fill().map(() => []);
    table[0] = [[]];

    for (let i = 0; i < m; i++) {
        if (table[i].length === 0) continue;
        for (word of wordBank) {
            if (target.substring(i).startsWith(word) && i + word.length < m){
                table[i + word.length].push(...table[i].map(comb => [...comb, word]));
            }
        }
    }
    return table[m-1];
}


// console.log(allConstructTab("abcdef", ["ab", "abc", "cd", "def", "abcd"]));   // [["abc", "def"]]
// console.log(allConstructTab("purple", ["purp", "p", "ur", "le", "purpl"]));   // [["purp", "le"], ["p", "ur", "p", "le"]]
// console.log(allConstructTab("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]));  // 4 ways
// console.log(allConstructTab("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]));   // []
// console.log(allConstructTab("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]));  // []
// console.log(allConstructTab("", ["abc"]));   // [[]]
