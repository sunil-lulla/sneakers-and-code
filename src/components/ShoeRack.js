import React from "react";
// import reactDOM from "react-dom";
import ShoeContainer from "./ShoeContainer";

class ShoeRack extends React.Component {
	constructor(props) {
		super(props);
		this.state = { shoe_data: [] };
		this.setupInitialState = this.setupInitialState.bind(this);
		this.renderShoe = this.renderShoe.bind(this);
	}
	setupInitialState(api_data) {
		this.setState({
			shoe_data: api_data
		});
	}

	renderShoe(elem_props, b) {
		return <ShoeContainer {...elem_props} />;
	}

	componentWillMount() {
		fetch("https://api.myjson.com/bins/11upkk")
			.then(data => data.json())
			.then(data => {
				this.setupInitialState(data);
			});
	}
	render() {
		console.log("rendered");
		return <div>{this.state.shoe_data.map(this.renderShoe)}</div>;
	}
}

export default ShoeRack;
