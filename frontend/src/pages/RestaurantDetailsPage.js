import React from "react";
import { useParams } from "react-router-dom";

import RestaurantDetails from '../components/restaurants/RestaurantDetails';

const RestaurantDetailsPage = () => {

   const { restaurantId } = useParams();

   return (
      <div>
         <RestaurantDetails restaurantId={restaurantId} />
      </div>
   )
}

export default RestaurantDetailsPage;