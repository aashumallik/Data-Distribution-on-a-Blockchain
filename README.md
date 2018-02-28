# Overview

Data splitting &amp; distribution using asynchronous programming into a Blockchain. Takes an input of a file, splits the file using the File-Splitter wriiten in java. After Splitting the file takes the individual file and passes through the compression engine (Compression.py). After Compressing each split file the File then passes through the Neural Net(Neural-Net.py) to optimize the platform. After the Neural Net is trained the data is then transferred into Blockchain (Blockchain.js).

# File Splitter

https://github.com/ashumallik/Data-Distribution-in-a-Blockchain/blob/master/File-Splitter.java

File Splits after reaching the threshold of 2000 lines

# Compression

https://github.com/ashumallik/Data-Distribution-in-a-Blockchain/blob/master/Compression.py

Compresses each individual file created by File Splitter

# Machine Learning (Neural Net) - Feature

https://github.com/ashumallik/Data-Distribution-in-a-Blockchain/blob/master/NeuralNet.py

Takes the compressed and uncompressed file and trains the Neural Net to optimize tthe platform

# Hash (Encryption) 

https://github.com/ashumallik/Data-Distribution-in-a-Blockchain/blob/master/Hash.py

After optimizing the platform using the Neural Net the Data then goes through the Encryption module 

# Blockchain

https://github.com/ashumallik/Data-Distribution-in-a-Blockchain/blob/master/Blockchain.js

After Encrypting each individual module the hashed module then stores itself into a Blockchain
