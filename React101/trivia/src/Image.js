import React from 'react';
import Eggs from './IMG_2372.JPG';
import './Image.css';

const Image = () => {
    return (
        <div className="image">
            <img src={Eggs} alt="Eggs" />
        </div>
    )
}

export default Image;