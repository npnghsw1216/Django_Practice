// TODO: #1 like 오름차순으로 정렬
// 출력포맷 : `[좋아요수] 곡명`
// Array의 sort 활용
// ref: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/sort

const { melon_data: song_array } = require("./melon_data");

const song = song_array.sort(
    (song_array1, song_array2) => {
        return -(song_array1.like - song_array2.like);
    }
);
console.log("----- like 오름차순으로 정렬 -----")

for (const song of song_array) {
    console.log(`[${song.like}]`, song.title);
}