import React, { Component } from 'react';
import { Map, GoogleApiWrapper, InfoWindow, Marker } from 'google-maps-react';
import { Polygon } from "google-maps-react";
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';

/* ML predicted communities - TO DO: integrate to ES once ML model is scaled to predict across the globe */
import communities from './ml_community_predict.json';

const mapStyles = {
    width: '100%',
    height: '100%'
};

export class MapContainer extends Component {

    constructor(props) {
        super(props);

        /* TO DO:  Marker Code - To get more demographic information from communities */
        this.state = {
            stores: [{lat: 47.49855629475769, lng: -122.14184416996333},
                {latitude: 47.359423, longitude: -122.021071},
                {latitude: 47.2052192687988, longitude: -121.988426208496},
                {latitude: 47.6307081, longitude: -122.1434325},
                {latitude: 47.3084488, longitude: -122.2140121},
                {latitude: 47.5524695, longitude: -122.0425407}]
        }

    }
    /* Marker Code Display*/
    displayMarkers = () => {
        return this.state.stores.map((store, index) => {
            return <Marker key={index} id={index} position={{
                lat: store.latitude,
                lng: store.longitude
            }}
                           onClick={() => console.log("You clicked me!")}/>
        })
    }
    /* Display ML Predicted Community Polygons */
    displayCommunities = () => {
        var coords;
        var key = 1 ;
        var community_polygons = [];
        for ( var community in communities){
            key++;
            coords = communities[community]
            community_polygons.push(<Polygon
                key={key}
                paths={coords}
                strokeColor="#ffaa17"
                strokeOpacity={0.8}
                strokeWeight={2}
                fillColor="#ffa640"
                fillOpacity={0.35} />)
                console.log(coords)
        }
        return community_polygons;
    }

    render() {
        return (
            <div>
                <AppBar position="static" color="primary">
                    <Toolbar>
                        <Typography variant="h6">
                            Planet Captain
                        </Typography>
                    </Toolbar>
                </AppBar>
            <Map
                google={this.props.google}
                zoom={15}
                style={mapStyles}
                mapType={"satellite"}
                /* Initial App Zoomed in on ML predicted communities */
                initialCenter={{lat: 26.998618, lng: 81.554844}}>
                {this.displayCommunities()}
            </Map>
            </div>

        );
    }
}

export default GoogleApiWrapper({
    apiKey: 'AIzaSyANs8IkEudsPGEA1dicW7gLY8T7K6orJ3E'
})(MapContainer);