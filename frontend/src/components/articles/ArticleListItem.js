import React, {useState, useEffect} from "react";
import Grid from "@material-ui/core/Grid";
import Card from "@material-ui/core/Card";
import CardMedia from "@material-ui/core/CardMedia";
import CardContent from "@material-ui/core/CardContent";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";
import CardActions from "@material-ui/core/CardActions";
import TextField from "@material-ui/core/TextField";

const ArticleListItem = ({pk, name, description, price}) => {
    const [articlePk, setArticlePk] = useState(null);
    const [quantity, setQuantity] = useState(1);

    const handleQuantityChange = (event) => {
        setQuantity(event.target.value);
    }

    const handleAddToOrder = () => {
        console.log(articlePk, quantity)
    }

    useEffect(() => {
        setArticlePk(pk);
    }, [])

    return (
        <Grid item key={pk} xs={12} sm={6} md={4}>
            <Card>
                <CardMedia
                    image={""}
                    title={name}
                />
                <CardContent>
                    <Typography gutterBottom variant="h5" component="h2">
                        {name}
                    </Typography>
                    <Typography>
                        {description}
                    </Typography>
                    <Typography>
                        {price}
                    </Typography>
                </CardContent>
                <CardActions>
                    <Button size="small" color="primary" onClick={handleAddToOrder}>
                        Add to order
                    </Button>
                    <TextField
                        id="standard-number"
                        label="Number"
                        type="number"
                        onChange={handleQuantityChange}
                        InputLabelProps={{
                            shrink: true,
                        }}
                    />
                </CardActions>
            </Card>
        </Grid>
    )
}

export default ArticleListItem;
