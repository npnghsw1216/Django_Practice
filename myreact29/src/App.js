// import Counter from "./Counter";
// import MelonTop100 from "./MelonTop100";

import MelonTop100 from "MelonTop100";
import MelonSearch from "./MelonSearch";
import {SmileOutlined} from '@ant-design/icons';


function App(){
  return(
    <div>
      <h1 style={{color:'lightgreen'}}><SmileOutlined />  React Practice  <SmileOutlined /></h1>
      <MelonSearch/>
      {/* <MelonTop100/>
      <Counter/>
      <Counter/>
      <Counter/> */}
    </div>
  );
}
  

export default App;

