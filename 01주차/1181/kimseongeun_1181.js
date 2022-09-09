// const fs = require('fs');
// const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const input = [
    '13',
    'but',
    'i',
    'wont',
    'hesitate',
    'no',
    'more',
    'no',
    'more',
    'it',
    'cannot',
    'wait',
    'im',
    'yours'
];
const sorted = input.sort((a, b) => a.length - b.length || a.localeCompare(b));
const uniqueValues = new Set(sorted);
console.log(Array.from(uniqueValues).join('\n'));

/*
sort()로 단어의 길이만큼 정렬하고, 같은 길이의 단어가 있다면 localeCompare()를 이용해 정렬이 가능함.
그렇게 정렬된 배열을 new Set()에 됨

*** localeCompare : 브라우저 언어 설정 기반해 순서 비교
->str1이 str2 앞에 : -1 반환
->두 문자열 같으면 :  0 반환
->str2가 str1 앞에:   1 반환

*** Set : 이 배열에 어떤 숫자가 포함 되어 있는지 확인가능 has()로 / Array.from으로 Arr 배열 객체로 변환 가능
* */