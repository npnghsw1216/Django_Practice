// 바뀌지 않는 데이터
// 전역 변수 : 바뀌지 않는 데이터

import { useState } from 'react';
import { Button as BootstrapButton } from 'react-bootstrap';
import { Button as AntButton } from 'antd';
import Axios from 'axios';
import initialSongList from './data/melon_data.json';
import './MelonTop100.css';
import { FireTwoTone } from '@ant-design/icons';

function MelonTop100() {
  const [songList, setSongList] = useState([]);

  const handleClick1 = () => {
    setSongList(initialSongList);
  };

  const handleClick2 = () => {
    const url = 'https://antigravity-daejeon-2021.herokuapp.com/api/melon/';
    Axios.get(url)
      .then((response) => {
        const { data } = response;
        setSongList(data);
        // console.log('응답을 받았습니다.');
        // console.log(response);
      })
      .catch((error) => {
        console.error(error);
      });
  };

  const handleClick3 = () => {
    setSongList([]);
  };

  return (
    <div>
      <h2>
        <FireTwoTone />
        멜론 top 100
        <FireTwoTone />
      </h2>
      <BootstrapButton variant="success" onClick={handleClick1}>
        파일 로딩
      </BootstrapButton>

      <AntButton type="primary" onClick={handleClick2}>
        서버 로딩
      </AntButton>

      <AntButton type="dashed" onClick={handleClick3}>
        클리어
      </AntButton>

      <ul className="songList">
        {songList.map((song) => {
          return (
            <li key={song.song_no}>
              [{song.rank}] {song.title} by {song.artist} likes : {song.like}
            </li>
          );
        })}
      </ul>
    </div>
  );
}

export default MelonTop100;
