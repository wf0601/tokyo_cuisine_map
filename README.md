# Tokyo Cuisine Map

As a Food Hunter used to be living in Tokyo, I collected information about restaurants in Tokyo including all genres. The original data can be found in the following repository [Japan Foodie Library](https://github.com/wf0601/japan_foodie_library). The restaurant data is updated every half year. 

This project can serve as your personal pocket guide to explore great food in Tokyo. You can mark the places you have visited, save your comments and reviews, and get your daily recommendations or use it as a search engine. 


You can simply build from source using docker. 

To build the image:

`docker build -t tokyo_cuisine .`

Run with either clicking the run button in Docker or using the command below.

`docker run -d -p 5004:5004 --name my_tokyo_cuisine tokyo_cuisine`

Feel free to modify settings in the config e.g. `./config/cuisines.yaml`, you can add/remove genres to tailor your own version of maps.

## Landing Page
![landing_page](md_pics/p3.png)

## Map Page

You can tick on 'Visited' to mark the restaurants you have already been to. 

![example1](md_pics/p2.png)

You can also add your own reviews or remarks of the restaurants, it will be saved automatically in the backend. 

<img src="md_pics/p1.png" alt="example2" style="width:50%; height:auto;">
