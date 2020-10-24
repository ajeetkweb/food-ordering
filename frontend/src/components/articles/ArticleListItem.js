import React from "react";


const ArticleListItem = ({ name, description, price}) => {
    return (
        <div className={"article-list-item"}>
            <div className={"article-list-item-name"}>{name}</div>
            <div className={"article-list-item-description"}>{description}</div>
            <div className={"article-list-item-price"}>{price}</div>
        </div>
    )
}


export default ArticleListItem;