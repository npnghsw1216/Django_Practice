const animal_names = [
    "cat",
    "dog",
    "fox",
    "monkey",
    "mouse",
    "panda",
    "frog",
    "snake",
    "wolf",
];

// string
// iconv-lite 등으로 한글 구현 하는 방법??
// iconv를 사용했지만 출력만되고 input이 되지않았다.

// 다른 문자를 입력했을 때 빈칸이 출력 되도록 if 문
const { question } = require("readline-sync");
const input_start = question("Press Any Key:");
if (input_start === "") {
    console.log(input_start);
}
else {
    console.log("");
};

// animal 리스트를 섞어주는 shuffleArray
function shuffleArray(animal_names) {
    animal_names.sort(() => Math.random() - 0.5);
};

random_animal = shuffleArray(animal_names);
// 타이핑 시작 시간 측정
const begin_time = new Date().getTime();
// 정확성 check를 위한 변수선언
let ok_counter = 0;
// 5번의 타이핑만 허락하도록 하는 for 문
// slicing
for (i = 0; i < 5; i++) {
    console.log(animal_names[i]);
    const { question } = require("readline-sync");
    const typing = question(">>>");
    console.log(typing);

    if (animal_names[i] === typing) {
        ok_counter += 1;
        console.log("정확합니다.");
    }
    else {
        console.log("오타가 있어요.");
    };
};
// for문이 끝났을 때의 시간 측정
const end_time = new Date().getTime();

// 타이핑 시간을 계산하는 time변수 선언후 계산식 입력
let time = Math.floor((end_time - begin_time) / 1000);

// 출력문
console.log("---------------------------------");
console.log(`총 ${ok_counter}번 성공하셨습니다.`);
console.log(`${time}초 걸리셨습니다.`);