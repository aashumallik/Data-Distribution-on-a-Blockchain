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

Takes the compressed and uncompressed file and trains the Neural Net to optimize the platform

# Hash (Encryption) 

https://github.com/ashumallik/Data-Distribution-in-a-Blockchain/blob/master/Hash.py

After optimizing the platform using the Neural Net the Data then goes through the Encryption module 

# Blockchain

https://github.com/ashumallik/Data-Distribution-in-a-Blockchain/blob/master/Blockchain.js

After Encrypting each individual module the hashed module then stores itself into a Blockchain

# Credit

This package-lock.json, package.json, Encryption.java, Decryption.java were adapted from the following article which uses JSON & Java: 

https://hackernoon.com/learn-blockchains-by-building-one-117428612f46?gi=89cd42f5e67b
https://www.veracode.com/blog/research/encryption-and-decryption-java-cryptography

