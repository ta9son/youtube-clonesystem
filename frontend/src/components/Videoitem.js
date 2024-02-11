import React, {useContext} from 'react'
import {ApiContext} from "../context/ApiContext";
import { makeStyles } from '@material-ui/core/styles';
import { Card, CardMedia, CardContent, CardActionArea, Typography } from '@material-ui/core';


const useStyles = makeStyles((theme) => ({
  card: {
    position: "relative",
    display: "flex",
    marginBottom: 15,
  },
  cardcont: {
    padding: theme.spacing(1),
  },
}));

const Videoitem = ({video}) => {
    const classes = useStyles();
    const { setSelectedVideo } = useContext(ApiContext);
  return (
    <Card className={classes.card} onClick={() => setSelectedVideo(video)}>
      <CardActionArea>
        <CardMedia
          component="img"
          alt="thumnail"
          height="200"
          image={video.thum}
        />
        <CardContent className={classes.cardcont}>
          <Typography variant="h6"> {video.title} </Typography>
        </CardContent>
      </CardActionArea>
    </Card>
  )
}

export default Videoitem
