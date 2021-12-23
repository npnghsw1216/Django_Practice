import { useState } from 'react';

function Counter() {
  const [value, setValue] = useState(10);
  const [color, setColor] = useState('red');

  const handleClick = () => {
    console.log(`clicked`);
    setValue(value + 1);
    setColor(value % 2 === 0 ? 'green' : 'red');
  };
  return (
    <div
      style={{
        backgroundColor: color,
        width: 100,
        height: 100,
        display: 'inline-block',
        margin: 5,
        borderRadius: 50,
        textAlign: 'center',
        userSelect: 'none',
        cursor: 'pointer',
      }}
      onClick={handleClick}
    >
      <span>{value}</span>
    </div>
  );
}

export default Counter;
