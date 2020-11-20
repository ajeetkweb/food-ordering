import React, {useEffect, useState} from 'react';
import {makeStyles} from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import api from "../../api";
import {useOrder} from "../../context/OrderProvider";

const useStyles = makeStyles({
    table: {
        minWidth: 650,
    },
});

export default function BasicTable() {
    const classes = useStyles();
    const order = useOrder();
    const [orders, setOrders] = useState([]);

    useEffect(() => {
        (async function getOrders() {
            const result = await api.orders.getOrders();
            setOrders(result)
        })();
    }, []);


    return (
        <TableContainer component={Paper}>
            <Table className={classes.table} aria-label="simple table">
                <TableHead>
                    <TableRow>
                        <TableCell>Status</TableCell>
                        <TableCell align="right">Subtotal</TableCell>
                        <TableCell align="right">Status</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {orders.map((order) => (
                        <TableRow key={order.pk}>
                            <TableCell component="th" scope="row">
                                {order.status}
                            </TableCell>
                            <TableCell align="right">{order.subtotal}</TableCell>
                            <TableCell align="right">{order.status}</TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        </TableContainer>
    );
}