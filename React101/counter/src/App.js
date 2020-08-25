import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Counter from './Counter';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      name: "Mina"
    };
  }
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Welcome {this.state.name}</h2>
        </div>
        <Counter />
      </div>
    );
  }
}

export default App;
