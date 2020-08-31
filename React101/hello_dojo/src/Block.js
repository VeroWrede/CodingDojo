import React from "react";
import './Block.css'

const Title = (props) => {
    return <h1 style={{color:props.color, backgroundColor:props.background}}>{props.text}</h1>
}

const Block = () => {
    return (
        <div>
            <title text="white on blue" color="white" backgroundColor="blue" />
            <title text="blue on red" color="blue" backgroundColor="red" />
            <title text="orange on green" color="orange" backgroundColor="green" />
        </div>
    )
}