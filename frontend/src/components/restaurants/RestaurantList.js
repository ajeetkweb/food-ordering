import React, {useEffect, useState} from "react";
import api from "../../api";

import RestaurantListItem from "./RestaurantListItem";

const RestaurantList = () => {
    const [restaurantList, setRestaurantList] = useState([]);

    useEffect(() => {
        (async function getRestaurants() {
            const result = await api.restaurants.getRestaurants();
            setRestaurantList(result)
        })();
    }, []);

    return (
        <div className={"restaurant-list"}>
            <ul>
                {restaurantList.map(restaurant => <RestaurantListItem key={restaurant.pk} {...restaurant} />)}
            </ul>
        </div>
    )
}

export default RestaurantList;