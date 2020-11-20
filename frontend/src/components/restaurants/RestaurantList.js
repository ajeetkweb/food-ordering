import React from "react";

import RestaurantListItem from "./RestaurantListItem";
import Container from "@material-ui/core/Container";
import Grid from "@material-ui/core/Grid";

const RestaurantList = ({restaurantList}) => {
    return (
        <Container maxWidth="md">
            <Grid container spacing={4}>
                {restaurantList.map(restaurant => <RestaurantListItem key={restaurant.pk} {...restaurant} />)}
            </Grid>
        </Container>
    )
}

export default RestaurantList;