import React from 'react';
import './card.css';

const Card = (props) => {
    return (
        <div className="card">
            <img src="./images/cat.jpg" alt="cat" className="card-img-top"></img>
            <div className="card-body">
                <h1 className="card-title">{props.title}</h1>
                <p className="card-text">{props.description}</p>
            </div>
        </div>
    )
}

export default Card;

