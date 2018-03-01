# Overview

Data splitting &amp; distribution using asynchronous programming into a Blockchain. The Platform takes an input of a file from a user and splits the file using the File-Splitter written in java. The platform then passes all of the individual files through a compression engine written in python (Compression.py). After Compressing each file the platform then passes the files through an Artificial Neural Net(Neural-Net.py) to train the platform by analyzing patterns in the user given dataset . After the Neural Net is trained the files are then transferred into a Blockchain (Blockchain.js).

# File Splitter

https://github.com/ashumallik/Data-Distribution-in-a-Blockchain/blob/master/File-Splitter.java

File Splits after reaching the threshold of 2000 lines

# Lossless Compression 

https://github.com/ashumallik/Data-Distribution-in-a-Blockchain/blob/master/Compression.py

Compresses each individual file created by File Splitter

# Machine Learning (Artificial Neural Network) - Feature

https://github.com/ashumallik/Data-Distribution-in-a-Blockchain/blob/master/NeuralNet.py

Our Neural Netwwork is built on top of the auto-encoder architecture which works flawlessly to identify patterns in user given dataset. We also use the Neural Net to build a dictionary for lossless compression of data using the Huffman Compression Algorithm.

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

