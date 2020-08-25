import React, { Component } from 'react';
import './counter.css';

class Counter extends React.Component {
    constructor (props) {
        super(props);
        this.state = {
            count: 0
        }
    }

    render () {
        return (
            <div>
                <button onClick={() => this.setState({ count: this.state.count + 1 })}>Click me!</button>
                <p>You clicked {this.state.count} times</p>
                <button onClick={() => this.setState({ count: 0})}>Reset to 0</button>

            </div>
        )
    }
}


export default Counter;