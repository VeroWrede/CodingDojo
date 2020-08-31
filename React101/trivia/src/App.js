import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Image from './Image';
import Card from './Card';

class App extends React.Component {
  render() {
    return (
      <div className="App">
        <Image />
        <Card />
      </div>
    );
  }
}

export default App;
