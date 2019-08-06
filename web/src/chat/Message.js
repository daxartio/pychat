import React from 'react';

export default class Message extends React.Component {
    constructor(props) {
        super(props);
        this.state = {

        };
    }

    render() {
        return (
            <div className='Message'>{this.props.children}</div>
        );
    }
}