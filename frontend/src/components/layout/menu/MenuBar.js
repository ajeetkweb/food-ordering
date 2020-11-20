import React from 'react';
import SearchInput from "./SearchInput";
import OrderBadge from "./OrderBadge";
import Toolbar from "@material-ui/core/Toolbar";
import AppBar from "@material-ui/core/AppBar";
import AccountMenu from "./AccountMenu";
import Typography from "@material-ui/core/Typography";

const MenuBar = ({onSearch}) => {
    return (
        <div>
            <AppBar position="static">
                <Toolbar>
                    <Typography variant="h6" noWrap>
                        Usereats
                    </Typography>
                    <SearchInput onChange={onSearch}/>
                    <OrderBadge onClick={() => {
                    }}/>
                    <AccountMenu/>
                </Toolbar>
            </AppBar>
        </div>
    );
}

export default MenuBar;