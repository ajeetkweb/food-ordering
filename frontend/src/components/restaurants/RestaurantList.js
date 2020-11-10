import React, {useEffect, useState} from "react";
import api from "../../api";

import RestaurantListItem from "./RestaurantListItem";
import Container from "@material-ui/core/Container";
import Grid from "@material-ui/core/Grid";

const RestaurantList = () => {
    const [restaurantList, setRestaurantList] = useState([]);

    useEffect(() => {
        (async function getRestaurants() {
            const result = await api.restaurants.getRestaurants();
            setRestaurantList(result)
        })();
    }, []);

    return (
        <Container maxWidth="md">
            <Grid container spacing={4}>
                {restaurantList.map(restaurant => <RestaurantListItem key={restaurant.pk} {...restaurant} />)}
            </Grid>
        </Container>
    )
}

export default RestaurantList;