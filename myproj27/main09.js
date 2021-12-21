// TODO: #9 좋아요수가 200,000이상인 곡들의 곡명 리스트를 만들어보세요.
// Array의 filter와 map 활용

const { melon_data: song_array } = require("./melon_data");

const song_20000 = song_array.filter(song1 => song1.like >= 200000);
const title_song_20000 = song_20000.map((song2) => ({ title: song2.title }))

let song_20000_list = [];
for (const obj of title_song_20000) {
    song_20000_list.push(obj.title)
}
console.log("----- 좋아요수가 200,000이상인 곡들의 곡명 리스트 -----")

console.log(song_20000_list);
