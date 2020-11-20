import React from 'react';
import IconButton from "@material-ui/core/IconButton";
import Badge from "@material-ui/core/Badge";
import AccountCircleIcon from '@material-ui/icons/AccountCircle';

const AccountBadge = ({onClick}) => {
    return (
        <IconButton aria-label="show 17 new notifications" color="inherit">
            <Badge badgeContent={null} color="secondary">
                <AccountCircleIcon onClick={onClick}/>
            </Badge>
        </IconButton>
    )
}


export default AccountBadge;