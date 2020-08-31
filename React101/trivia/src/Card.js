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
        this.TurnCard = this.TurnCard.bind(this);
    }


    TurnCard() {
        this.setState(state => ({
            isTurned: !state.isTurned}));
    }

    render () {
        return (
            <div>
                <button onClick={() => this.setState({ count: this.state.count + 1 })}>Click me!</button>
                <p>{this.state.count}</p>
                
                <button className="card" onClick={ () => this.turnCard() }>DOOOP
                </button>
                    <h1>{this.state.isTurned ? "Tip" : "Question"}</h1>
                    <h3>{this.state.isTurned ? this.state.tip : this.state.question}</h3>
            </div>
        )
    }
}

export default Card;