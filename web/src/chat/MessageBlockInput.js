import React from 'react';

export default class MessageBlockInput extends React.Component {
    constructor(props) {
        super(props);
        this.state = {

        };
    }

    render() {
        return (
            <div className='MessageBlockInput'>{this.props.children}</div>
        );
    }
}