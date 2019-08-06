import React from 'react';

export default class MessageBody extends React.Component {
    constructor(props) {
        super(props);
        this.state = {

        };
    }

    render() {
        return (
            <div className='MessageBody'>{this.props.children}</div>
        );
    }
}