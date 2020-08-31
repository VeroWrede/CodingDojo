import React from 'react';
import './subject.css';

const Subject = (props) => {
    return (
        <div className='subject'>
            <h1 className='vote-count'> XX </h1>
            <h1> {props.subject} </h1>
            <button> + </button>
        </div>
    )
}

export default Subject;