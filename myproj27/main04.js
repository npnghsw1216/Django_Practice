// TODO: #4 좋아요수가 200,000 이상인 곡명만 출력하기
// Array의 filter 활용
// 출력포맷 : `[좋아요수] 곡명 가수명`

const { melon_data: song_array } = require("./melon_data");

const song_20000 = song_array.filter(song20000 => song20000.like >= 200000);

console.log("----- 좋아요가 200,000 이상인 곡 -----")

for (const song of song_20000) {
    console.log(`[${song.like}]`, song.title);
}