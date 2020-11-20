import React from 'react';
import InputBase from "@material-ui/core/InputBase";

const SearchInput = ({onChange}) => {
    return (
        <div>
            <InputBase
                placeholder="Search…"
                onChange={onChange}
                inputProps={{'aria-label': 'search'}}
            />
        </div>
    )
}

export default SearchInput;