let fs = require("fs");
let input = fs.readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");
input.shift();
let input=4;
for (let i = 0; i < input.length; i += 3) {
    let mission = input[i].split("");
    let arr = JSON.parse(input[i + 2]);

    let isError = false;
    let isChange = false;

    for (let j = 0; j < mission.length; j++) {
        if (mission[j] === "R") isChange = !isChange;
        else if (mission[j] === "D") {
            if (arr.length > 0) {
                if (isChange) arr.pop();
                else arr.shift();
            } else {
                isError = !isError;
                break;
            }
        }
    }
    if (isError) console.log("error");
    else {
        if (isChange) console.log(JSON.stringify(arr.reverse()));
        else console.log(JSON.stringify(arr));
    }
}