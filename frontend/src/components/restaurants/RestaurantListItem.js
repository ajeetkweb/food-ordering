import React from "react";
import {Link} from "react-router-dom";
import Grid from "@material-ui/core/Grid";
import Card from "@material-ui/core/Card";
import CardMedia from "@material-ui/core/CardMedia";
import CardContent from "@material-ui/core/CardContent";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";
import CardActions from "@material-ui/core/CardActions";

const RestaurantListItem = ({pk, name, logo}) => {

    return (
        <Grid item key={pk} xs={12} sm={6} md={4}>
            <Card>
                <CardMedia
                    // className={classes.cardMedia}
                    image={logo}
                    title={name}
                />
                <CardContent>
                    <Typography gutterBottom variant="h5" component="h2">
                        {name}
                    </Typography>
                    <Typography>
                        This is a media card. You can use this section to describe the content.
                    </Typography>
                </CardContent>
                <CardActions>
                    <Link to={`/restaurant/${pk}`}>
                        <Button size="small" color="primary">
                            View
                        </Button>
                    </Link>
                </CardActions>
            </Card>
        </Grid>
    )
}

export default RestaurantListItem;