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

const { question } = require("readline-sync");
const string = question("ready to enter? : ");

const shuffled_name = animal_names
    .map(a => ([Math.random(), a]))
    .sort((a, b) => a[0] - b[0])
    .map(a => a[1]);

const begin_time = Math.floor(new Date() / 1000);

let ok_counter = 0;

for (i = 0; i < 5; i++) {
    console.log(shuffled_name[i]);
    const { question } = require("readline-sync");
    const name = question(">>> ")
    if (name == shuffled_name[i]) {
        ok_counter += 1
        console.log("정확합니다.")
    }
    else {
        console.log("오타가 있어요.")
    }
}
const end_time = Math.floor(new Date() / 1000);

console.log(`${ok_counter}번 성공하셨습니다.`);
console.log(`총${end_time - begin_time}초가 걸리셨어요.`)
