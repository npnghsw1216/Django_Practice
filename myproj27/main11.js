// TODO: #11 멜론 top100 리스트에 랭크된 가수는 총 몇 팀인가요?
// Set와 속성 .size를 활용
// ref: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Set

const { melon_data: song_array } = require("./melon_data");

const singer = song_array.map(function (song) {
    return song.artist
})

const mySet = new Set(singer);

console.log(mySet.size);


// const real_top100_artist = [];

// const top100_artist = song_array.map(song => song.artist);


// for (const artist of top100_artist) {
//     if (real_top100_artist.includes(artist)) {
//     } else {
//         real_top100_artist.push(artist)
//     }
// }

// const count_artist = real_top100_artist.length;
// console.log(count_artist);