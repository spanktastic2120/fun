

function getGrade(score) {
    let grade;
    // Write your code here
    25 < score && score <= 30 ? grade = 'A':
    20 < score && score <= 25 ? grade = 'B' :
    15 < score && score <= 20 ? grade = 'C':
    10 < score && score <= 15 ? grade = 'D':
    5 < score && score <= 10 ? grade = 'E':
    grade = 'F'
    return grade;
}

