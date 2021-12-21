// TODO: #10 방탄소년단의 좋아요의 총 합은?
// Array의 filter와 reduce를 활용해주세요.
// ref: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce

const { melon_data: song_array } = require("./melon_data");

const reducer = (previousValue, currentValue) => previousValue + currentValue;

const bts_song = song_array.filter(song1 => song1.artist === "방탄소년단")

const like_list = bts_song.map(function (song) {
    return song.like
})

console.log(like_list.reduce(reducer));