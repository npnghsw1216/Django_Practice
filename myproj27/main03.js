// TODO: #3 좋아요수 top10을 출력
// Array의 sort 활용
// 출력포맷 : `[좋아요수] 곡명 가수명`

const { melon_data: song_array } = require("./melon_data");

const top10 = song_array.sort(
    (top10_1, top10_2) => {
        return -(top10_1.like - top10_2.like);
    }
);

const like_top10 = top10.slice(0, 9);

console.log("----- 좋아요수 top10 -----")

for (const song of like_top10) {
    console.log(`[${song.like}]`, song.title, song.artist);
}
