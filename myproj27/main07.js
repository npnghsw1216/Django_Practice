// TODO: #7 방탄소년단의 곡명 문자열로 구성된 배열을 구성해주세요.
// Array의 filter와 map 활용
// 출력포맷 : [곡명1, 곡명2, 곡명3]
const { melon_data: song_array } = require("./melon_data");

const bts_song = song_array.filter(song1 => song1.artist === "방탄소년단")
const title_bts_song = bts_song.map((song) => ({ title: song.title }))

let bts_list = [];
for (const obj of title_bts_song) {
    bts_list.push(obj.title)
}
console.log("----- 방탄소년단의 곡명 문자열로 구성된 배열 -----")

console.log(bts_list)
