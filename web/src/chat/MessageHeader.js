import React from 'react';

export default class MessageHeader extends React.Component {
    constructor(props) {
        super(props);
        this.state = {

        };
    }

    render() {
        return (
            <div className='MessageHeader'>{this.props.children}</div>
        );
    }
}