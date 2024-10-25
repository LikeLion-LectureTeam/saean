import Resume from "./components/Resume";
import { ColorText } from "./components/ColorText";

function App() {
  return (
    <div>
      <Resume hello="안녕하세요" name="개리" hobby="게임" food="고기" color="blue" />
      <ColorText color="skyblue" />
    </div>
  );
}

export default App;

