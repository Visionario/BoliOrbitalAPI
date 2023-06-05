# TODO

### Publish/Subscribe and callbacks for:
- alertnotify
- blocknotify
- walletnotify
- instantsendnotify

### Publish/Subscribe and callbacks for:
- zmqpubhashblock
- zmqpubhashtx
- zmqpubhashtxlock
- zmqpubrawblock
- zmqpubrawtx
- zmqpubrawtxlock

### dumphdinfo
- Returns an object containing sensitive private info about HD wallet.

### Sign and verify messages with the private key of an address
- signmessage
- verifymessage

### Dump private key of an address
- dumpprivkey

### Encrypt you wallet
- encryptwallet

### Import address, Electrum Wallets, private keys and public keys
- importaddress
- importelectrumwallet
- importprivkey
- importwallet

### mnsync
- Masternodes Sync status, updates to the next step or resets it entirely

### Some networking functions
- getaddednodeinfo
- getconnectioncount
- getnettotals
- getnetworkinfo
- getpeerinfo
- listbanned
- setnetworkactive 

### voteraw
- Compile and relay a governance vote with provided external signature instead of signing vote internally

### setban/clearbanned/listbanned Nodes
- setban
- listbanned
- clearbanned

###  disconnectnode

### Creates a multi-signature address with n signature of m keys required.
- createmultisig


### addnode
- Add or remove a node from the addnode list

### Many others methods from Core 