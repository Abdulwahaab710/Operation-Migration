# Operation-Migration

## TL;DR
Operation Migration is an Android App geared towards bringing birdwatchers and scientists together to build a database of bird sightings using machine learning and pictures submitted by citizen scientists.

## Project Overview:

As part of understanding human impact on the environment, scientists are very interested in tracking and analyzing a variety of species, including birds. 

Until recently scientist would have to manually tag birds to track their migrations. With the communication boom that came with the internet and smartphones scientists can now leverage an already existing community of dedicated birdwatchers to track birds with far greater efficiency. For example, the Cornell Lab of Ornithology allows users to submit bird sightings as a means to increase the data available for scientists [1]. Our application expands on these ideas by creating a simple android application that facilitates data collection. 

Birdwatchers love to capture pictures of birds in their natural habitats, trekking through sunshine or rain. With this application, birdwatchers are able to take pictures of birds they spot, and upload them directly to a server along with the GPS location. Our server uses machine learning algorithms to identify the species of bird, and creates a record of that bird in the database. This greatly enhances the user experience, because the user does not need to be able to recognize the bird to expand the database. Users can then view, on google maps, pictures of birds taken by other people. Ultimately, as the dataset grows, the app would allow scientists to analyse migration patterns.

Our application uses the open source TensorFlow software to identify birds. This software uses machine learning to analyze patterns in the images and train itself to identify birds. Starting from a default dataset that comes with TensorFlow, we were able to train the algorithm using a subset of the Caltech-UCSD Birds 200 dataset [2] to improve the accuracy of bird identification. With further training, the system should be able to identify a wider variety of birds with a greater accuracy. Currently the server returns the bird with the highest percent match to the user, along with the next two closest matches. 

Our current implementation uses rudimentary search algorithms to allow users to search the database. For example, searching with the letter “a” will give all birds whose species name begins with the letter “a”. Over time, the search parameters could be expanded to conduct searches over specific areas and time periods. This will enhance the ability for scientists to analyze the data.
