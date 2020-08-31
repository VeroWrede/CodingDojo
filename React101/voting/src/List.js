import React from 'react';
import Subject from './Subject';
import './list.css';

const List = () => {
    return (
        <div className="list">
            <Subject subject="Bacon" />
            <Subject subject="Chocolate" />
            <Subject subject="Steak" />
            <Subject subject="Cucumbers" />
        </div>
    )
}

export default List;