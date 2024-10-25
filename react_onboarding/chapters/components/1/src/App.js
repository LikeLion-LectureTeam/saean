import Hello from './components/Hello';
import HelloProps from './components/Helloprops';
import Time from './components/Time';


function App() {
  return (
			<HelloProps 
				name="jaehyun" 
				age={25} 
				someFunc={() => 'awesome!!!'} 
				someJSX={<img src="https://picsum.photos/id/237/200/300" />} 
				someArr={[1, 2, 3]} 
				someObj={{ one: 1 }} />
  );
}

export default App;