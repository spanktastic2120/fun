

/*
 * Determine the original side lengths and return an array:
 * - The first element is the length of the shorter side
 * - The second element is the length of the longer side
 * 
 * Parameter(s):
 * literals: The tagged template literal's array of strings.
 * expressions: The tagged template literal's array of expression values (i.e., [area, perimeter]).
 */
function sides(literals, ...expressions) {
    let a = expressions[0];
    let p = expressions[1];
    let s1 = ((p + (p ** 2 - (16 * a)) ** 0.5) / 4);
    let s2 = ((p - (p ** 2 - (16 * a)) ** 0.5) / 4);
    [s1, s2] = [s1, s2].sort();
    return [s1, s2];
}

