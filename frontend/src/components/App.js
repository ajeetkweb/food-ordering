import React, {useEffect, useState} from "react";
import axios from 'axios'

function App() {

    const [restaurants, setRestaurants] = useState([]);

    return <div>{restaurants}</div>
}

export default App;
