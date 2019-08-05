
function getMaxLessThanK(n, k){
    return ((k | (k - 1)) > n) ? (k - 2) : (k - 1);
}
