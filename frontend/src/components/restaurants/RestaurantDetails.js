import React, {useEffect, useState} from "react";
import api from "../../api";
import ArticleListItem from "../articles/ArticleListItem";


const RestaurantDetails = ({restaurantId}) => {

    const [restaurantDetails, setRestaurantDetails] = useState({
        articles: [],
    });

    useEffect(() => {
        (async function getRestaurantDetails(restaurantId) {
            const result = await api.restaurants.getRestaurant(restaurantId);
            setRestaurantDetails(result);
        })(restaurantId);
    }, [])

    return (
        <div>
            <div>{restaurantDetails.name}</div>
            <div className={"article-list"}>
                {restaurantDetails.articles.forEach(article => (<ArticleListItem {...article} key={article.pk}/>))}
            </div>
        </div>
    )
}

export default RestaurantDetails;