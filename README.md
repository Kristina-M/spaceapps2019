# spaceapps2019 - team planet captain
We love the earth it is our planet!
We love the earth it is our home!

### Challenge: [From Curious Minds Come Helping Hands](https://2019.spaceappschallenge.org/challenges/living-our-world/curious-minds-come-helping-hands/details)

This repo contains the following:
- space-apps contains the react app which display the ML classified communities
- data-pull includes python scripts for pulling external data sources into elastic search and data prepocessing scripts
- MLDataset - labelled community dataset from communities in Uttar Pradesh (Labelled during hackathon - used to augment object detection model weights)
- mask_RCNN - Augmented code from base repo by matterpot - https://github.com/matterport/Mask_RCNN


## Helping Hands

Our app is currently being hosted on google cloud. 

[Kibana Front End (Main Application)](http://35.197.176.167:5601/app/kibana#/dashboard/35274380-f24d-11e9-b8e1-8d0d8149bbc2)

[React App Front End ( ML result visulization )](http://35.197.176.167:3000)


## Tech Stack
![Alt text](stack.png?raw=true "Tech Stack")


## ML Predictions
![Predictions not found](CommunitiesIdentified.png?raw=true "Highlighted communities identified by MaskRCNN")
 ML network weights can be found [here](https://drive.google.com/file/d/1QeQUpRH8wHO0f36oKcKAVHXi9s-DIqHb/view?usp=sharing)

