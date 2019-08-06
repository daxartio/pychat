import React from 'react';
import './Chat.css';

export default class Chat extends React.Component {
    constructor(props) {
        super(props);
        this.state = {

        };
    }

    render() {
        return (
            <div className='Chat'>{this.props.children}</div>
        );
    }
}