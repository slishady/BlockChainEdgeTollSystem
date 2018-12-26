import json
import web3

from web3 import Web3
from solc import compile_source
from web3.contract import ConciseContract

# Solidity source code
contract_source_code = '''
pragma solidity ^0.4.2;

contract PC2 {

    struct Channel {
        address sender;
        address recipient;
        uint collateral;
    }


    mapping (address => mapping (address => Channel)) public channels;

    function openChannel(address recipient) public payable {
        //perform some validation first
        if (msg.value == 0) { 
            revert(); 
        }
        
        if (recipient == msg.sender) { 
            revert(); 
        }

        if (channels[msg.sender][recipient].collateral > 0) {
            revert();
        }

        channels[msg.sender][recipient] = Channel({
            sender:msg.sender,
            recipient: recipient,
            collateral: uint(msg.value)
        });
    }


    function closeChannel(
        address sender, 
        address recipient, 
        uint valueTransferred,
        uint8 v, 
        bytes32 r, 
        bytes32 s
    ) 
    public 
    {
        // Check channel exists
        if (channels[sender][recipient].collateral == 0) {
            revert();
        }

        // Load channel into memory
        Channel memory channel = channels[sender][recipient];

        // Make sure value transferred is less than or equal to collateral
        if (msg.sender != channel.recipient) {
            revert();
        }

        // Make sure value transferred is less than or equal to collateral
        if (channel.collateral < valueTransferred) {
            revert();
        }

        if (!verifySignature(sender, recipient, valueTransferred, v, r, s)) {
            revert();
        }

        // Settle up
        settleBalances(channel, valueTransferred);

        // Remove mapping
        delete channels[sender][recipient];
    }


    function settleBalances(
        Channel channel, 
        uint valueTransferred
    ) 
    private 
    {

        channel.recipient.transfer((valueTransferred));
        channel.sender.transfer((channel.collateral - valueTransferred));
    }


    function verifySignature(
        address sender, 
        address recipient, 
        uint valueTransferred,
        uint8 v, 
        bytes32 r, 
        bytes32 s
    ) 
    public view returns (bool)
    {
        // Required for providers such as: Geth, Parity, TestRPC
        // bytes memory prefix = "\x19Ethereum Signed Message:\n32";

        // 2 Step Validate Signature with sha3 (alias for keccak256)
        bytes32 messageHash = keccak256(abi.encodePacked(
            sender,
            recipient,
            valueTransferred
        ));

        // bytes32 prefixedHash = keccak256(abi.encodePacked(
        //     prefix,
        //     messageHash
        // ));

        address signerAddress = ecrecover(messageHash,v,r,s);

        if (signerAddress != sender) {
            return false;
        }
        if (channels[sender][recipient].collateral < valueTransferred){
            return false;
        }
        return true;
    }


    function getChannelCollateral(
        address sender, 
        address recipient
    ) 
    public view returns (uint) 
    {
        Channel memory channel = channels[sender][recipient];
        return channel.collateral;
    }

}
'''

compiled_sol = compile_source(contract_source_code) # Compiled source code
contract_interface = compiled_sol['<stdin>:Greeter']

# web3.py instance
w3 = Web3("http://127.0.0.1:7545")

# set pre-funded account as sender
w3.eth.defaultAccount = w3.eth.accounts[0]

# Instantiate and deploy contract
Greeter = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])

# Submit the transaction that deploys the contract
tx_hash = Greeter.constructor().transact()

# Wait for the transaction to be mined, and get the transaction receipt
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

# Create the contract instance with the newly-deployed address
greeter = w3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=contract_interface['abi'],
)

# Display the default greeting from the contract
print('Default contract greeting: {}'.format(
    greeter.functions.greet().call()
))

print('Setting the greeting to Nihao...')
tx_hash = greeter.functions.setGreeting('Nihao').transact()

# Wait for transaction to be mined...
w3.eth.waitForTransactionReceipt(tx_hash)

# Display the new greeting value
print('Updated contract greeting: {}'.format(
    greeter.functions.greet().call()
))

# When issuing a lot of reads, try this more concise reader:
reader = ConciseContract(greeter)
assert reader.greet() == "Nihao"