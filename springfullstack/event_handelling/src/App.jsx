import { useState } from "react";
import './App.css'

function App() {

  const [text, setText] = useState("");
  const [x, setX] = useState(0);
  const [y, setY] = useState(0);

  // Alert button
  function showAlert() {
    alert("Button clicked");
  }

  // Input change
  function handleChange(e) {
    setText(e.target.value);
  }

  // Form submit
  function handleSubmit(e) {
    e.preventDefault();
    alert("Form submitted");
  }

  // Mouse position
  function handleMouseMove(e) {
    setX(e.clientX);
    setY(e.clientY);
  }

  // Console log
  function logMessage() {
    console.log("Button clicked");
  }

  return (
    <div onMouseMove={handleMouseMove}>

      <h3>1. Alert Button</h3>
      <button onClick={showAlert}>Click Me</button>

      <h3>2. Input onChange</h3>
      <input type="text" onChange={handleChange} />
      <p>Input value: {text}</p>

      <h3>3. Form Submit</h3>
      <form onSubmit={handleSubmit}>
        <input type="text" />
        <button type="submit">Submit</button>
      </form>

      <h3>4. Mouse Position</h3>
      <p>X: {x} Y: {y}</p>

      <h3>5. Console Log Button</h3>
      <button onClick={logMessage}>Console Button</button>

    </div>
  );
}

export default App;