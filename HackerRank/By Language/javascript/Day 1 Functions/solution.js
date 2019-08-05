
/*
 * Create the function factorial here
 */
function factorial(f) {
    let result = 1
    while (f >= 1) {
        result = result * f
        f = f -1
    }
    return result
}
