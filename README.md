# Sprint Challenge: Hash Tables and Blockchain

This challenge allows you to practice the concepts and techniques learned over the past week and apply them in a concrete project. This Sprint, we learned how hash tables combine two data structures to get the best of both worlds and were introduced into the fascinating world of blockchains. In your challenge this week, you will demonstrate proficiency by solving algorithms in Python using hash tables and add another key feature to your blockchain.

## Instructions

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This is an individual assessment. All work must be your own. Your challenge score is a measure of your ability to work independently using the material covered through this sprint. You need to demonstrate proficiency in the concepts and objectives introduced and practiced in preceding days.

You are not allowed to collaborate during the Sprint Challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your PM and Instructor in your cohort help channel on Slack. Your work reflects your proficiency in Python and your command of the concepts and techniques in related to hash tables and blockchains.

You have three hours to complete this challenge. Plan your time accordingly.

## Commits

Commit your code regularly and meaningfully. This helps both you (in case you ever need to return to old code for any number of reasons and your project manager.

## Description

This sprint challenge is divided up into three parts:  Hash tables coding, blockchain coding, and a short interview covering parts of hash tables and blockchain.

## Interview Questions

Explain in detail the workings of a dynamic array:
* What is the runtime complexity to access an array, add or remove from the front, and add or remove from the back?
- The runtime complexity of accessing an array is N(1). To access an array, it is a continious block of memory that is being accessed. Also - each entry into the array occupies the same amount of space in memory, so to access an individual entry within the array - taking the starting space in RAM, plus the space per entry * the index of the entry allows access to it. All of those computations are not reliant on N, so it is O(1).
- The runtime complexity to add/remove to the front of an array is N. This is because to add a value to the front of an array, it requires shifting each value in the array from the ith index to the ith+1. This requires traversing the list. The same concept with removing, except everything is shifted from the ith index to the ith-1.
- To add/remove from the back fo the array is constant! This leverages the same properties as mentioned above with accessing an array. Since the memory is continious in memory, to access the most recent value in the array it is a matter of starting at the initial memory address, plus the current length of the array times the space each entry takes. This allows constant runtime complexity to add one additional value, or to identify the most recent value and remove it.


* What is the worse case scenario if you try to extend the storage size of a dynamic array?
- The worst case scenario for resizing a dynamic array is N, since a new array in memory is generated, and you traverse the list copying the entire array entry by entry to the new allocated array.



Explain how a blockchain is structured. What are the blocks, what is the chain? How is the data organized?
 A blockchain is structured by having a series of ledger entries called blocks, that are linked in time by referencing previous hashes. An individual block has several key elements, first being the hash of the previous block to show that it builds on the most updated chain. Next, there is a "proof" which is a nonce that is cycled through to provide a valid hash of the block showing a desired amount of leading 0's to achieve the appropriate difficulty the network has agreed upon. Additionally, there are trnsactions of coins from members of the network.

Explain how proof of work functions. How does it operate. How does this protect the chain from attack. What kind of attack is possible? Proof of work relies on cryptographic hashing functions that are aysmetric (easy to compute, impossible to reverse engineer) and deterministic (each person sees the same hashes). As the likelyhood for a given digit in a hash to be 1 out of 16 (for SHA256 and other Hex based hashes), you can rely on that random distribution to be able to prove a certain amount of effort has been put into validating the minted block. This protects the chain from attack as a dishonest miner who wishes to change the state of the previous ledger entries will fundamentally alter the hash of the block such that all of the work will not be valid (it will not meet the proper amount of leading 0's). This incentivies honest cooperative behavior to continue mining on the longest chain with themost work. A 51% attack is when a majority of computational hashing power in the network is being diverted to an individual or group of people who will always win a hashing race and able to provide more work than the rest of the honest ators. with a 51% attack, previous blocks can be undone and transactions within those blocks can be double spent (sent to new parties instead), if those original coins are controlled by dishonest actors.

## Project Set Up

#### [Hash Tables]

For the hash tables portion of the sprint challenge, you'll be working through two algorithm problems that are amenable to being solved efficiently using a hash table. You know the drill at this point. Navigate into each exercise's directory, read the instructions for the exercise laid out in the README, implement your solution in the .py skeleton file, then make sure your code passes the tests by running the test script with make tests.

A hash table implementation has been included for you already. Your task is to get the tests passing (using a hash table to do it). You can remind yourself of what hash table functions are available by looking at the hashtable.py file that is included in each exercise directory (note that the hash table implementations for both exercises differ slightly).

*You may not use any advanced, built-in Python functions to solve these problems.*

#### [Blockchain]

For the blockchain portion of the challenge, you will be writing code for a new miner that will solve a different Proof of Work algorithm than the one we have been working with.

Your goal is to mine at least one coin.  Keep in mind that with many people competing over the same coins, this may take a long time.  By our math, we expect that an average solution should be the first to find a solution at least once in an hour or two of mining.  

## Minimum Viable Product

#### [Hash Tables](https://github.com/LambdaSchool/Sprint-Challenge--Hash-BC/tree/master/hashtables)

#### [Blockchain](https://github.com/LambdaSchool/Sprint-Challenge--Hash-BC/tree/master/blockchain)


### Rubric

| *OBJECTIVE*                                                                                                     | *TASK*             | *1 - DOES NOT MEET EXPECTATIONS*                                                                                            | *2 - MEETS EXPECTATIONS*                                                                                                       | *3 - EXCEEDS EXPECTATIONS                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| implement and describe how high-level array functions work down to the memory level                             | Interview Question | The student fully explains two or fewer of the bulleted items in the solution repo\. | The student fully explains at least 3 of the items in the bulleted list\.                                | The student fully explains 4 or more items from the bulleted list\.           |
| implement and utilize basic hash table + handle collisions and resizing in a hash table                         | Hash Problem 1 & 2 | Tests do not pass on one or both problems, or solutions do not use hash tables.                                             | Tests pass on both problems.  Solution utilizes a hash table.                                                                  | Tests pass on on both problems with solutions utilizing hash tables, linear runtime complexity, no flake8 complaints.                                 |
| diagram and code a simple blockchain, utilizing a cryptographic hash                                            | Interview Question | The student fully explains two or fewer of the bulleted items in the solution repo\. | The student fully explains at least 3 of the items in the bulleted list\.                                | The student fully explains 4 or more items from the bulleted list\.           |
| utilize a Proof of Work process to protect a blockchain from attack                                             | Blockchain Problem | The student is unable to mine a coin before the end of lunch.                                                               | The student was able to mine a coin before the end of lunch.                                                                   | The student presented a unique solution that was able to mine more than 100 coins before the end of lunch.                                            |
| build a protocol to allow nodes in a blockchain network to communicate to share blocks and determine consensus. | Interview Question | The student fully explains two or fewer of the bulleted items in the solution repo\. | The student fully explains at least 3 of the items in the bulleted list\.                                | The student fully explains 4 or more items from the bulleted list\.           |
