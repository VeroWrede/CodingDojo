import React from 'react';

const Box = (props) => {
    return (
        <div style={{ background: props.background }}>
            <h1 className="box" style={{ color: props.color }}>{props.text} </h1>
        </div>
    )
}

const Grid = () => {
    return (
        <div style={{ display: "flex" }}>
            <Box text="white on blue" background="blue" color="white" /> ,
            <Box text="blue on red" background="red" color="blue" />,
            <Box text="red on black" background="black" color="red" />
        </div>
    )
}

export default Grid;