import React, {useContext, useRef} from 'react'
import {ApiContext} from "../context/ApiContext";
import { makeStyles } from '@material-ui/core/styles';
import { Grid, Card, CardMedia, CardContent, CardActionArea, Typography, Container, Fab } from '@material-ui/core';
import DeleteIcon from '@material-ui/icons/Delete';
import ReactPlayer from 'react-player';

import {AiFillLike, AiFillDislike} from 'react-icons/ai';
import {IoLogoYoutube} from 'react-icons/io';

const useStyles = makeStyles((theme) => ({
    title: {
      paddingLeft: theme.spacing(2),
    },
    delete: {
      margin: theme.spacing(2),
    },
    like: {
      paddingTop: theme.spacing(3),
    },
  }));

const VideoDetail = () => {
    const classes = useStyles();
    const player = useRef(null);
    const {
      selectedVideo,
      deleteVideo,
      incrementLike,
      incrementDislike,
    } = useContext(ApiContext);

    if (!selectedVideo)
        return (
            <div className="container">
                <button className="wait">
                <IoLogoYoutube />
                </button>
            </div>
        );
    
    return (
        <>
            <div className="wrapper">
                <ReactPlayer
                className="player"
                url={selectedVideo.video}
                ref={player}
                width="100%"
                height="100%"
                playing
                controls
                disablePictureInPicture
                config={{
                    file: {
                    attributes: {
                        controlsList: "nodownload",
                        disablePictureInPicture: true,
                    },
                    },
                }}
                />
            </div>
            <Grid container alignItems="center">
                <Grid item xs={10}>
                    <Typography className={classes.title} variant="h6">
                        {selectedVideo.title}
                    </Typography>
                </Grid>

                <Grid item xs={1}>
                    <button className="like" onClick={() => incrementLike()}>
                        <AiFillLike />
                        <Typography>{selectedVideo.like}</Typography>
                    </button>
                </Grid>
                <Grid item xs={1}>
                    <button className="like" onClick={() => incrementDislike()}>
                        <AiFillDislike />
                        <Typography>{selectedVideo.dislike}</Typography>
                    </button>
                </Grid>
            </Grid>
            <Fab
                className={classes.delete}
                color="primary"
                aria-label="delete"
                onClick={() => deleteVideo()}
            >
                <DeleteIcon />
            </Fab>
        </>
    )
}

export default VideoDetail
