import React, {useContext} from 'react'
import {ApiContext} from "../context/ApiContext";
import { Grid } from '@material-ui/core';
import VideoItem from './Videoitem';

const VideoList = () => {
    const {videos} = useContext(ApiContext);
    const listOfVideos = videos.map((video) => (
        <VideoItem video={video} key={video.id} />
    ));
    return (
        <Grid container spacing={5}>
            <div className="video-list">{listOfVideos}</div>
        </Grid>
    )
}

export default VideoList
