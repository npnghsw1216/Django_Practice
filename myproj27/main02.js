// TOOD: #2 방탄소년단의 곡명만 출력
// 출력포맷 : `가수명 곡명 좋아요수`
// Array의 filter 활용
// ref: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/filter
const { melon_data: song_array } = require("./melon_data");


const song_bts = song_array.filter(bts => bts.artist === "방탄소년단");

console.log("----- 방탄소년단의 곡명만 출력 -----")

for (const song of song_bts) {
    console.log(song.artist, song.title, song.like)
}

