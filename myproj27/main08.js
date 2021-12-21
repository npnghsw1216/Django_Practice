// TODO: #8 곡명에 "사랑"이 포함된 곡들의 곡명 배열을 구성해주세요.
// Array의 filter와 map 활용
// 출력포맷 : [곡명1, 곡명2, 곡명3]
const { melon_data: song_array } = require("./melon_data");

const love_song = song_array.filter(song1 => song1.title.includes("사랑"));
const title_love_song = love_song.map((song) => ({ title: song.title }));

let love_song_list = [];
for (const obj of title_love_song) {
    love_song_list.push(obj.title)
}
console.log("----- 곡명에 ", "'사랑'", "이 포함된 곡들의 곡명 배열 -----");

console.log(love_song_list);
