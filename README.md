# Bolivarcoin/Bolicoin API (RPC)

### Node API Rpc main class for Bolivarcoin/Bolicoin

#### Para español vaya a [README en español](./README_ES.md)

___
_WARNING_: _This document and documentation is in development, and it will be available on next releases_

_WARNING_: _This is a BETA stable version, issues and pull request are very welcome_
____
This project is a first public beta version
of [Propuesta DAO a superbloque 764,336 para desarrollo API y APPs periféricas alrededor del núcleo](https://bit.ly/Superbloque764336)

This API is a first layer to communicate with Bolivarcoin/Bolicoin blockchain using a common node or masternode with user
credentials.

On top of this API, developers can build Apps, frontends, bots, remote wallets, notifiers, transactions, monitoring, etc.

_____

## Bolivarcoin Blockchain Compatibility

**Bolivarcoin version**: 2000002 (v2.0.0.2-g)    
**Protocol version**: 70212

You can to verify version using _getinfo_ command on node console.
Example:
> getinfo

```json
{
  "version": 2000002,
  "protocolversion": 70212,
  "walletversion": 120200,
  "balance": 15658.49718641,
  "privatesend_balance": 0.00000000,
  "blocks": 1234567,
  "timeoffset": 0,
  "connections": 8,
  "proxy": "",
  "difficulty": 12345678.901234,
  "testnet": false,
  "keypoololdest": 1440858873,
  "keypoolsize": 1999,
  "paytxfee": 0.00000000,
  "relayfee": 0.00001000,
  "errors": ""
}
```

_____

## Installation

From PyPi:
pip install boli_orbital_api

From source code:
git clone https://github.com/Visionario/BoliOrbitalAPI

_____

## Usage

Basic use:
Communicate with your local node, it must be running on same pc

```python
from boli_orbital_api import Node

node = Node(rpc_user="user", rpc_password="password")
node.is_online
# True
node.getinfo()
# {'result': {'version': 2000002, 'protocolversion': 70212, 'walletversion': 120200, 'balance': 15658.49718641, 'privatesend_balance': 0.0, 'blocks': 1234567, 'timeoffset': 0, 'connections': 8, 'proxy': '', 'difficulty': 36237.78062774216, 'testnet': False, 'keypoololdest': 1440858873, 'keypoolsize': 1999, 'paytxfee': 0.0, 'relayfee': 1e-05, 'errors': ''}, 'errors': False}

```

```json
{
  "result": {
    "version": 2000002,
    "protocolversion": 70212,
    "walletversion": 120200,
    "balance": 15658.49718641,
    "privatesend_balance": 0.00000000,
    "blocks": 1234567,
    "timeoffset": 0,
    "connections": 8,
    "proxy": "",
    "difficulty": 12345678.901234,
    "testnet": false,
    "keypoololdest": 1440858873,
    "keypoolsize": 1999,
    "paytxfee": 0.00000000,
    "relayfee": 0.00001000,
    "errors": ""
  },
  "errors": false
}
```

Orbital API sends a json with {"result":..., "errors":...}

Please take a look to [docs](./docs/using.md) for details.
____



