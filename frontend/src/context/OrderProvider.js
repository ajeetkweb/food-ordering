import React, {useState, useContext, createContext, useEffect} from "react";
import api from "../api";

const orderContextDefaultValues = {
    order: {
        pk: null,
        status: null,
        articles: [],
    },
    setOrderState: (order) => {},
    clearOrder: () => {},
}

const OrderContext = createContext(orderContextDefaultValues);

const OrderProvider = (props) => {
    const [order, setOrderState] = useState({});

    useEffect(() => {
        (async function getOrderInProgress() {
            const result = await api.orders.getOrderInProgress();
            setOrder(result);
        })();
    }, []);

    const setOrder = (order) => {
        setOrderState({...order})
    }

    const clearOrder = () => {
        setOrderState({});
    }


    return <OrderContext.Provider value={{order, clearOrder, setOrder}} {...props} />
}

const useOrder = () => useContext(OrderContext);


export {OrderProvider, useOrder}