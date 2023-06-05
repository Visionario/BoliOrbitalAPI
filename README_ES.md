## API Bolivarcoin/Bolicoin (RPC)

### Node API Rpc clase principal para Bolivarcoin/Bolicoin

### For english [README.md](./README.md)
___
_ADVERTENCIA_: _Este documento y documentación está en desarrollo, y estará disponible en próximas versiones_ 

_ADVERTENCIA_: _Esta es una versión BETA estable, problemas y pull request son bienvenidos_. 
____
Este proyecto es una primera versión beta pública
de [Propuesta DAO a superbloque 764,336 para desarrollo API y APPs periféricas alrededor del núcleo](https://bit.ly/Superbloque764336)

Esta API es una primera capa para comunicarse con la blockchain Bolivarcoin/Bolicoin usando un nodo común o masternode con credenciales de usuario.
usuario.

Sobre esta API, los desarrolladores pueden crear aplicaciones, frontends, bots, monederos remotos, notificadores, transacciones, monitorización, etc.

_____

## Bolivarcoin Blockchain Compatibilidad

**Versión de Bolivarcoin**: 2000002 (v2.0.0.2-g)    
**Versión del protocolo**: 70212

Puede verificar la versión usando el comando _getinfo_ en la consola del nodo.
Ejemplo:
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

## Instalación

Desde PyPi:
pip install boli_orbital_api

Desde el código fuente:
git clone https://github.com/Visionario/BoliOrbitalAPI

_____

## Uso

Uso básico:
Comunícate con tu nodo local, debe estar ejecutándose en el mismo pc


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
La API Orbital envía un json con {"result":..., "errors":...}

Por favor, eche un vistazo a [docs](./docs/using.md) para más detalles.
____



