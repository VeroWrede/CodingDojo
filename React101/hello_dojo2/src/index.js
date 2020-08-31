import React from 'react';
import ReactDOM from 'react-dom';
// import App from './App';
import './index.css';

// ReactDOM.render(
//   <App />,
//   document.getElementById('root')
// );

const helloReact2 = React.createElement("div", null, 
  React.createElement("h1", null, "Hello Dojo 2"),
  React.createElement("h2", null, "Things to do"),
  React.createElement("ul", null, 
    React.createElement("li", null, "React 101"),
    React.createElement("li", null, "laundry"),
    React.createElement("li", null, "bath kittens"),
    React.createElement("li", null, "workout")
  )
);

ReactDOM.render(
  helloReact2,
  document.getElementById("root")
);
