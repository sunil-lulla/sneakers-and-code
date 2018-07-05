import React from "react";
// import reactDOM from "react-dom";

class App extends React.Component {
	constructor(props) {
		super(props);
		this.state = { shoe_data: [] };
		this.setupInitialState = this.setupInitialState.bind(this);
	}

	setupInitialState = api_data => {
		this.setState({
			shoe_data: api_data
		});
	};

	componentWillMount() {
		fetch("https://api.myjson.com/bins/11upkk").then(data => {
			this.setupInitialState(data);
		});
	}
	render() {
		return (
			<div>
				My parent product {this.state.productName} container which will hold all
				the products
			</div>
		);
	}
}

export default App;
