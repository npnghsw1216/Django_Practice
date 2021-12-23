import { Input } from 'antd';
import { useState } from 'react';
import { List, Avatar } from 'antd';

import Axios from 'axios';
import jsonpAdapter from 'axios-jsonp';
import { CustomerServiceOutlined } from '@ant-design/icons';
import { SearchOutlined } from '@ant-design/icons';

function MelonSearch() {
  const [query, setQeury] = useState('');
  const [songList, setSongList] = useState([]);

  const handleChange = (e) => {
    const {
      target: { value },
    } = e;
    console.group('handleChange');
    console.log(value);
    console.groupEnd();
    setQeury(value);
  };
  const handlePressEnter = (e) => {
    console.group('handlePressEnter');
    console.log(`검색어 ${query}로 검색합니다.`);
    console.groupEnd();

    const url = 'https://www.melon.com/search/keyword/index.json';

    Axios({
      url: url,
      adapter: jsonpAdapter,
      callbackParamName: 'jscallback',
      params: {
        query: query,
      },
    })
      // .then이 결과값을 받음(오후 4시20분 경)
      .then((response) => {
        const {
          data: { SONGCONTENTS: searchedsongList },
        } = response;
        console.group('멜론 검색결과');
        console.log(response);
        console.log(searchedsongList);
        console.groupEnd();

        setSongList(searchedsongList);
      })
      // error가 발생하면 .catch를 호출
      .catch((error) => {
        console.group('멜론 검색 에러');
        console.error(error);
        console.groupEnd();
      });
  };

  const data = [
    {
      title: '',
    },
  ];

  return (
    <div style={{ width: 300, margin: '0 auto', color: 'lightgreen' }}>
      <h2 style={{ color: 'lightgreen' }}>
        <CustomerServiceOutlined /> 멜론 검색
      </h2>
      <SearchOutlined /> 검색어 : {query}
      <Input
        placeholder="검색어를 입력해주세요."
        onChange={handleChange}
        onPressEnter={handlePressEnter}
      />
      {songList.map((song) => {
        return (
          <List
            itemLayout="horizontal"
            dataSource={data}
            renderItem={(songList) => (
              <List.Item>
                <List.Item.Meta
                  avatar={<Avatar src={song.ALBUMIMG} />}
                  title={song.SONGNAME}
                  description={song.ARTISTNAME}
                />
              </List.Item>
            )}
          />
        );
      })}
    </div>
  );
}

export default MelonSearch;
