# Simple voting system based on NFT ownership
This SmartPy contract is a simple voting application that allows users to vote for different options using a non-fungible token (NFT) as an eligibility criterion. It also includes a quiz that the user must complete before being allowed to vote. The contract consists of three classes: NFT, Quizz, and Vote.

## NFT
This class extends the FA2 contract and creates a non-fungible token. The NFT is used to determine if a user is eligible to vote in the poll. Only users who hold the NFT are allowed to vote.

## Quizz
This class creates a quiz that the user must complete before being allowed to vote. The quiz consists of three questions, and the user must answer all three questions correctly to be allowed to vote. If the user answers a question incorrectly, they must wait 30 seconds before attempting the quiz again.

## Vote
This class allows users to vote for different options. Before voting, the user must complete the quiz and hold the NFT. Once the user has passed the quiz and is eligible to vote, they can vote for one of three options.

## Running the Contract
To run this contract, the SmartPy library must be installed. After installing the library, navigate to the directory where the contract is saved and run the command 'smartpy compile app.py my_output_directory'. The contract can then be deployed to a Tezos network using a wallet that supports the FA2 standard.

## Testing
The contract includes a test suite that can be run using the command smartpy test my_contract.py. The test suite includes tests for each of the three classes and ensures that the contract is functioning as expected.

## Disclaimer
This contract is provided as an example only and should not be used in production without significant modification and testing. Smart contract development is complex and requires a deep understanding of blockchain technology, cryptography, and programming. It is essential to thoroughly test any smart contract before deploying it to a production environment.

## Improvement axis
In this code, the main improvement axis is the verification of participation in the quiz and therefore the creation of the quiz contract associated with the user, We can do this with automate création of a SMC Vote for each SMC Quizz
