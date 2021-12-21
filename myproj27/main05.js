// TODO: #5 좋아요수가 200,000이상인 곡명에 대해서, 곡명 오름차순 정렬
// Array의 filter와 sort를 연계
// 출력포맷 : `[좋아요수] 곡명 가수명`

const { melon_data: song_array } = require("./melon_data");

const song_20000 = song_array.filter(song20000 => song20000.like >= 200000);

const song_sort = song_20000.sort(
    (song1, song2) => {
        if (song1.title < song2.title)
            return -1;
        else if (song1.title > song2.title)
            return 1;
        else
            return 0;
    }
);
console.log("----- 좋아요가 200,000 이상인 곡에 대해서 곡명 오름차순 정렬 -----")

for (const song of song_sort) {
    console.log(`[${song.like}]`, song.title);
}

// song.title < song2.title return -1
// song1.title < song2.title return
// song1.title > song2.title return 1