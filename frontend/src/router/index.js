import React from "react";
import {
  HashRouter as Router,
  Switch,
  Route,
} from "react-router-dom";

import Home from '../pages/Home'
import RestaurantDetailsPage from "../pages/RestaurantDetailsPage";


export default () => {
   return (
   <Router>
      <Switch>
         <Route exact path="/" component={Home} />
         <Route path={`/restaurant/:restaurantId`} component={RestaurantDetailsPage} />
      </Switch>
   </Router>
   )
}