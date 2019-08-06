import React from 'react';

export default class Messages extends React.Component {
    constructor(props) {
        super(props);
        this.state = {

        };
        this.myRef = React.createRef();
    }

    scrollBottom() {
        const node = this.myRef.current;
        setTimeout(() => {
            node.scrollTop = node.scrollHeight;
        }, 100)
    }

    render() {
        return (
            <div ref={this.myRef} className='Messages'>{this.props.children}</div>
        );
    }
}