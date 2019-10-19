import React, { Component } from 'react';
import { Map, GoogleApiWrapper, InfoWindow, Marker } from 'google-maps-react';
import { Polygon } from "google-maps-react";

const mapStyles = {
    width: '100%',
    height: '100%'
};

const communities = {
    CommunityC: [
        {lat: 28.774, lng: -83.190},
        {lat: 21.466, lng: -69.118},
        {lat: 35.321, lng: -67.757},
        {lat: 28.774, lng: -83.190}
    ],
    CommunityA: [
        {lat: 25.774, lng: -80.190},
        {lat: 18.466, lng: -66.118},
        {lat: 32.321, lng: -64.757},
        {lat: 25.774, lng: -80.190}
    ],
    CommunityB: [
        {lat: 31.774, lng: -83.190},
        {lat: 24.466, lng: -69.118},
        {lat: 38.321, lng: -67.757},
        {lat: 31.774, lng: -83.190}
    ]
}

export class MapContainer extends Component {

    constructor(props) {
        super(props);

        this.state = {
            stores: [{lat: 47.49855629475769, lng: -122.14184416996333},
                {latitude: 47.359423, longitude: -122.021071},
                {latitude: 47.2052192687988, longitude: -121.988426208496},
                {latitude: 47.6307081, longitude: -122.1434325},
                {latitude: 47.3084488, longitude: -122.2140121},
                {latitude: 47.5524695, longitude: -122.0425407}]
        }
    }

    displayMarkers = () => {
        return this.state.stores.map((store, index) => {
            return <Marker key={index} id={index} position={{
                lat: store.latitude,
                lng: store.longitude
            }}
                           onClick={() => console.log("You clicked me!")}/>
        })
    }

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
            <Map
                google={this.props.google}
                zoom={8}
                style={mapStyles}
                mapType={"satellite"}
                initialCenter={{lat: 26.8, lng: 80.9 }}>
                {this.displayCommunities()}
                <Marker
                    position={{ lat: -34.397, lng: 150.644 }}
                />
            </Map>

        );
    }
}


export default GoogleApiWrapper({
    apiKey: 'AIzaSyANs8IkEudsPGEA1dicW7gLY8T7K6orJ3E'
})(MapContainer);