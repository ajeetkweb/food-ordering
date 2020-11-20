import React from "react";
import IconButton from "@material-ui/core/IconButton";
import Badge from "@material-ui/core/Badge";
import FastfoodIcon from '@material-ui/icons/Fastfood';
import {useOrder} from "../../../context/OrderProvider";

const OrderBadge = ({onClick}) => {

    const { order } = useOrder();

    const badgeContent = () => {
        return order.status === 0 ? "1": null
    }

    return (
        <IconButton aria-label="show 17 new notifications" color="inherit">
            <Badge badgeContent={badgeContent()} color="secondary">
                <FastfoodIcon onClick={onClick}/>
            </Badge>
        </IconButton>
    )
}

export default OrderBadge;