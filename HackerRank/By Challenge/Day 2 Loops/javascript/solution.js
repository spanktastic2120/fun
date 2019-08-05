

/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    let vowels = ''
    let consonants = ''
    for (let l of s) {
        if ('aeiou'.includes(l)){
            vowels = vowels + l + '\n'
        }
        else {
            consonants = consonants + l + '\n'
        }
    }
    console.log(vowels + consonants)
}

