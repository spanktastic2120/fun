

/*
 * Complete the reverseString function
 * Use console.log() to print to stdout.
 */
function reverseString(s) {
    let r
    try {
        r = s.split('').reverse().join('')
        console.log(r)
    }
    catch(e) {
        console.log(e.message)
        console.log(s)
    }
}

