import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />

        <p>
          Paragraph
        </p>

        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>

        <label>
            Source link:
            <input type="text" name="src-link" />
          </label>
        <input type="src-submit" value="Submit" />

        <label>
            Destination link:
            <input type="text" name="dst-link" />
          </label>
        <input type="dst-submit" value="Submit" />

      </header>
    </div>
  );
}

export default App;
