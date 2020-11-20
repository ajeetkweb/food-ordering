import React, {useEffect, useState} from "react"
import RestaurantList from "../components/restaurants/RestaurantList"
import OrdersTable from "../components/orders/OrdersTable";
import {OrderProvider} from "../context/OrderProvider";
import api from "../api";
import MenuBar from "../components/layout/menu/MenuBar";

const Home = () => {
    const [restaurantList, setRestaurantList] = useState([]);

    useEffect(() => {
        (async function getRestaurants() {
            const result = await api.restaurants.getRestaurants();
            setRestaurantList(result)
        })();
    }, []);

    const searchRestaurants = async (event) => {
        const results = await api.restaurants.searchRestaurants(event.target.value);
        setRestaurantList(results);
    }


   return (
       <div>
           <OrderProvider>
               <MenuBar onSearch={searchRestaurants}/>
               <RestaurantList restaurantList={restaurantList} />
           </OrderProvider>
       </div>
   )
}

export default Home;