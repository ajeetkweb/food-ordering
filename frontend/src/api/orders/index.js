import axios from 'axios';

export const orders = {
    getOrders() {
        return axios.get("api/orders").then((res) => res.data);
    },

    getOrderInProgress() {
        return axios.get(`api/orders/in-progress`).then((res) => res.data);
    },

    createNewOrder(data) {
        return axios.post(`api/orders/create`, data).then((res) => res.data);
    }
}
