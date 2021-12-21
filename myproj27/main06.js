// TODO: #6 "곡명 / 단어수" 배열을 구성해주세요.
// Array의 map 활용
// 100줄에서 한 줄 출력의 예: `Dynamite / 1`

const { melon_data: song_array } = require("./melon_data");

const song_title_word = song_array.map(
    (song1) => ({ title: song1.title, words: song1.title.split(' ') })
);

for (const song of song_title_word) {
    console.log(`'${song.title}/${song.words.length}'`)
}

