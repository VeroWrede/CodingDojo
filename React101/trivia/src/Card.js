import React, {Component} from 'react';
import './Card.css';

class Card extends React.Component {
    constructor (props) {
        super(props);
        this.state = {
            count: 0,
            isTurned: false,
            question: "what is this?",
            tip: "it turns into somehting that lives on land and in water"
        }
    }


    turnCard() {
        this.setState(state => ({
            isTurned: !state.isTurned}));
    }

    render () {
        return (
            <div>
                
                <button className="card" onClick={ () => this.turnCard() }>
                    <h1>{this.state.isTurned ? "Tip" : "Question"}</h1>
                    <h3>{this.state.isTurned ? this.state.tip : this.state.question}</h3>
                </button>
            </div>
        )
    }
}

export default Card;