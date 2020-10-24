import React from "react";
import { Link }from "react-router-dom";

const RestaurantListItem = ({pk, name, logo}) => {

    return (
        <div className={"restaurant-list-item"}>
            <li>
                <Link to={`/restaurant/${pk}`}>{name}</Link>
            </li>
        </div>
    )
}

export default RestaurantListItem;