import React from "react";
// import reactDOM from "react-dom";

class ShoeContainer extends React.Component {
	constructor(props) {
		super(props);
		this.state = {};
	}

	render() {
		return (
			<div className="product">
				<img
					className="product-lst-banner-container"
					src={this.props.images[0]}
				/>
				<div className="product-desc-container">
					<h5>{this.props.title}</h5>
					<div>
						<div className="rating-container">
							<span className="rating-star-container">
								{this.props.starRating}
								<i className="fa fa-star " />
							</span>
							<span className="rating-by-container">
								&nbsp; ({this.props.starRatingBy})
							</span>
						</div>
						<div className="price-container">
							<i className="fa fa-inr" />
							<span>{this.props.price}</span>
						</div>
					</div>
				</div>
			</div>
		);
	}
}

export default ShoeContainer;
