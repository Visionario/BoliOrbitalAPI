"""
    Node API Rpc main class for Bolivarcoin/Bolicoin blockchain (Layer 1)

        BOLICOIN COMPATIBLE VERSION: v2.0.0.2-g
        Bolicoin/Bolivarcoin platform and cryptocurrency from http://bolis.info

    __author__: "Asdrúbal Velásquez Lagrave - Twitter/Telegram: @Visionario"
    __copyright__: "2018-2023"
    __credits__: [""]
    __license__: "MIT"
    __version__: 0.9b17
    __maintainer__: "Asdrúbal Velásquez Lagrave"
    __email__: "hello@orbital.center"
    __status__: "BETA"
    __app_name__: "Node API Rpc main class for Bolivarcoin/Bolicoin blockchain (Layer 1)",
    __url__: "https://orbital.center"

"""
from typing import Any

from orjson import dumps
from requests import Response, exceptions as request_exceptions, post

from .logger import setup_logger

__all__ = [
    "Node",
    "GobjectListSignals",
    "GobjectListTypes",
    "MasternodeCountOptions",
    "MasternodeStartModes",
    "MnListModes",
    "About",
    "VERSION",
]

VERSION = "0.9b17"

# LOGGER
logger = setup_logger(__name__)


class GobjectListSignals:
    """See gobject_list()"""
    ALL = 'all'
    VALID = 'valid'
    FUNDING = 'funding'
    DELETE = 'delete'
    ENDORSED = 'endorsed'


class GobjectListTypes:
    """See gobject_list()"""
    ALL = 'all'
    PROPOSALS = 'proposals'
    TRIGGERS = 'triggers'
    WATCHDOGS = 'watchdogs'


class MasternodeCountOptions:
    """See masternode_count()"""
    EMPTY = ''
    ALL = 'all'
    PS = 'ps'
    ENABLED = 'enabled'
    QUALIFY = 'qualify'


class MasternodeStartModes:
    """See masternode_start_mode()"""
    ALL = 'all'
    MISSING = 'missing'
    DISABLED = 'disabled'


class MnListModes:
    """See masternodelist()"""
    ACTIVESECONDS = 'activeseconds'
    ADDR = 'addr'
    FULL = 'full'
    INFO = 'info'
    LASTPAIDBLOCK = 'lastpaidblock'
    LASTPAIDTIME = 'lastpaidtime'
    LASTSEEN = 'lastseen'
    PAYEE = 'payee'
    PROTOCOL = 'protocol'
    PUBKEY = 'pubkey'
    RANK = 'rank'
    STATUS = 'status'


def _process_result(result):
    """Process results coming from RAW calls"""
    try:
        if result.get('result') is not None:  # OK
            return {"result": result.get('result'), 'errors': False}
        else:  # Error!!!
            return {"result": None, "errors": result.get('errors', True)}

    except BaseException as e:
        return {"result": None, "errors": f'{e}'}


# ╻ ╻┏━┓╻  ╻  ┏━╸╺┳╸
# ┃╻┃┣━┫┃  ┃  ┣╸  ┃
# ┗┻┛╹ ╹┗━╸┗━╸┗━╸ ╹
class _Wallet:
    """Wallet methods"""

    def raw_call(self, *args, **kwargs) -> Any:
        pass

    def getwalletinfo(self) -> dict:
        """
            getwalletinfo
            Returns an object containing various wallet state info.

            Result:
            {
              "walletversion": xxxxx,     (numeric) the wallet version
              "balance": xxxxxxx,         (numeric) the total confirmed balance of the wallet in BOLIVARCOIN
              "unconfirmed_balance": xxx, (numeric) the total unconfirmed balance of the wallet in BOLIVARCOIN
              "immature_balance": xxxxxx, (numeric) the total immature balance of the wallet in BOLIVARCOIN
              "txcount": xxxxxxx,         (numeric) the total number of transactions in the wallet
              "keypoololdest": xxxxxx,    (numeric) the timestamp (seconds since GMT epoch) of the oldest pre-generated key in the key pool
              "keypoolsize": xxxx,        (numeric) how many new keys are pre-generated (only counts external keys)
              "keypoolsize_hd_internal": xxxx, (numeric) how many new keys are pre-generated for internal use (used for change outputs, only appears if the wallet is using this feature, otherwise external keys are used)
              "keys_left": xxxx,          (numeric) how many new keys are left since last automatic backup
              "unlocked_until": ttt,      (numeric) the timestamp in seconds since epoch (midnight Jan 1 1970 GMT) that the wallet is unlocked for transfers, or 0 if the wallet is locked
              "paytxfee": x.xxxx,         (numeric) the transaction fee configuration, set in BOLIVARCOIN/kB
              "hdchainid": "<hash>",      (string) the ID of the HD chain
              "hdaccountcount": xxx,      (numeric) how many accounts of the HD chain are in this wallet
                [
                  {
                  "hdaccountindex": xxx,         (numeric) the index of the account
                  "hdexternalkeyindex": xxxx,    (numeric) current external childkey index
                  "hdinternalkeyindex": xxxx,    (numeric) current internal childkey index
                  }
                  ,...
                ]
            }

            Examples:
            > bolivarcoin-cli getwalletinfo
            > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getwalletinfo", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:14776/

        """
        return _process_result(self.raw_call("getwalletinfo"))

    def getbalance(self) -> dict:
        """
            getbalance ( "account" minconf addlockconf includeWatchonly )

            If account is not specified, returns the server's total available balance.
            If account is specified (DEPRECATED), returns the balance in the account.
            Note that the account "" is not the same as leaving the parameter out.
            The server total may be different to the balance in the default "" account.

            Arguments:
            1. "account"        (string, optional) DEPRECATED. The selected account, or "*" for entire wallet. It may be the default account using "".
            2. minconf          (numeric, optional, default=1) Only include transactions confirmed at least this many times.
            3. addlockconf      (bool, optional, default=false) Whether to add 5 confirmations to transactions locked via InstantSend.
            4. includeWatchonly (bool, optional, default=false) Also include balance in watchonly addresses (see 'importaddress')

            Result:
            amount              (numeric) The total amount in BOLIVARCOIN received for this account.

            Examples:

            The total amount in the wallet
            > bolivarcoin-cli getbalance

            The total amount in the wallet at least 5 blocks confirmed
            > bolivarcoin-cli getbalance "*" 6

            As a json rpc call
            > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getbalance", "params": ["*", 6] }' -H 'content-type: text/plain;' http://127.0.0.1:14776/
        """
        # TODO: Add parameters -> getbalance ( "account" minconf addlockconf includeWatchonly )
        return _process_result(self.raw_call("getbalance"))

    def getnewaddress(self, label: str = "") -> dict:
        """
            getnewaddress ( "account" )

            Returns a new Bolivarcoin address for receiving payments.
            If 'account' is specified (DEPRECATED), it is added to the address book
            so payments received with the address will be credited to 'account'.

            Arguments:
            1. "account"        (string, optional) DEPRECATED. The account name for the address to be linked to. If not provided, the default account "" is used. It can also be set to the empty string "" to represent the default account. The account does not need to exist, it will be created if there is no account by the given name.

            Result:
            "bolivarcoinaddress"    (string) The new bolivarcoin address

            Examples:
            > bolivarcoin-cli getnewaddress
            > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getnewaddress", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:14776/

        """
        return _process_result(self.raw_call("getnewaddress", params=[label]))

    def getaddressesbyaccount(self, label: str = "") -> dict:
        """
            getaddressesbyaccount "account"

            DEPRECATED. Returns the list of addresses for the given account.

            Arguments:
            1. "account"  (string, required) The account name.

            Result:
            [                     (json array of string)
              "bolivarcoinaddress"  (string) a bolivarcoin address associated with the given account
              ,...
            ]

            Examples:
            > bolivarcoin-cli getaddressesbyaccount "tabby"
            > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getaddressesbyaccount", "params": ["tabby"] }' -H 'content-type: text/plain;' http://127.0.0.1:14776/
             (code -1)

        """
        return _process_result(self.raw_call("getaddressesbyaccount", params=[label]))

    def sendtoaddress(
            self,
            address: str,
            amount: float,
            comment: str = '',
            comment_to: str = '',
            subtractfeefromamount: bool = False
    ) -> dict:
        """
            sendtoaddress "bolivarcoinaddress" amount ( "comment" "comment-to" subtractfeefromamount use_is use_ps )

            Send an amount to a given address.

            Arguments:
            1. "bolivarcoinaddress" (string, required) The bolivarcoin address to send to.
            2. "amount"      (numeric or string, required) The amount in BOLIVARCOIN to send. eg 0.1
            3. "comment"     (string, optional) A comment used to store what the transaction is for.
                                         This is not part of the transaction, just kept in your wallet.
            4. "comment-to"  (string, optional) A comment to store the name of the person or organization
                                         to which you're sending the transaction. This is not part of the
                                         transaction, just kept in your wallet.
            5. subtractfeefromamount  (boolean, optional, default=false) The fee will be deducted from the amount being sent.
                                         The recipient will receive less amount of Bolivarcoin than you enter in the amount field.
            6. "use_is"      (bool, optional) Send this transaction as InstantSend (default: false)
            7. "use_ps"      (bool, optional) Use anonymized funds only (default: false)

            Result:
            "transactionid"  (string) The transaction id.

            Examples:
            > bolivarcoin-cli sendtoaddress "AJw5Dqdh47muwzqN1tsmhAiFrvoKqCpna8" 0.1
            > bolivarcoin-cli sendtoaddress "AJw5Dqdh47muwzqN1tsmhAiFrvoKqCpna8" 0.1 "donation" "seans outpost"
            > bolivarcoin-cli sendtoaddress "AJw5Dqdh47muwzqN1tsmhAiFrvoKqCpna8" 0.1 "" "" true
            > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "sendtoaddress", "params": ["AJw5Dqdh47muwzqN1tsmhAiFrvoKqCpna8", 0.1, "donation", "seans outpost"] }' -H 'content-type: text/plain;' http://127.0.0.1:14776/

        """
        if amount <= 0:
            return {"result": None, "error": "amount <= 0"}
        return _process_result(
            self.raw_call(
                "sendtoaddress", params=[
                    address,
                    amount,
                    comment,
                    comment_to,
                    subtractfeefromamount]
            )
        )


# ╻ ╻╺┳╸╻╻
# ┃ ┃ ┃ ┃┃
# ┗━┛ ╹ ╹┗━╸
class _Utils:
    """Utils methods"""

    def raw_call(self, *args, **kwargs) -> Any:
        pass

    def getinfo(self) -> dict:
        """
            getinfo
            Returns an object containing various state info.

            Result:
            {
              "version": xxxxx,           (numeric) the server version
              "protocolversion": xxxxx,   (numeric) the protocol version
              "walletversion": xxxxx,     (numeric) the wallet version
              "balance": xxxxxxx,         (numeric) the total bolivarcoin balance of the wallet
              "privatesend_balance": xxxxxx, (numeric) the anonymized bolivarcoin balance of the wallet
              "blocks": xxxxxx,           (numeric) the current number of blocks processed in the server
              "timeoffset": xxxxx,        (numeric) the time offset
              "connections": xxxxx,       (numeric) the number of connections
              "proxy": "host:port",     (string, optional) the proxy used by the server
              "difficulty": xxxxxx,       (numeric) the current difficulty
              "testnet": true|false,      (boolean) if the server is using testnet or not
              "keypoololdest": xxxxxx,    (numeric) the timestamp (seconds since GMT epoch) of the oldest pre-generated key in the key pool
              "keypoolsize": xxxx,        (numeric) how many new keys are pre-generated
              "unlocked_until": ttt,      (numeric) the timestamp in seconds since epoch (midnight Jan 1 1970 GMT) that the wallet is unlocked for transfers, or 0 if the wallet is locked
              "paytxfee": x.xxxx,         (numeric) the transaction fee set in BOLIVARCOIN/kB
              "relayfee": x.xxxx,         (numeric) minimum relay fee for non-free transactions in BOLIVARCOIN/kB
              "errors": "..."           (string) any error messages
            }

            Examples:
            > bolivarcoin-cli getinfo
            > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getinfo", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:14776/

        """
        return _process_result(self.raw_call("getinfo"))

    def validateaddress(self, address: str) -> dict:
        """
            validateaddress "bolivarcoinaddress"

            Return information about the given bolivarcoin address.

            Arguments:
            1. "bolivarcoinaddress"     (string, required) The bolivarcoin address to validate

            Result:
            {
              "isvalid" : true|false,       (boolean) If the address is valid or not. If not, this is the only property returned.
              "address" : "bolivarcoinaddress", (string) The bolivarcoin address validated
              "scriptPubKey" : "hex",       (string) The hex encoded scriptPubKey generated by the address
              "ismine" : true|false,        (boolean) If the address is yours or not
              "iswatchonly" : true|false,   (boolean) If the address is watchonly
              "isscript" : true|false,      (boolean) If the key is a script
              "pubkey" : "publickeyhex",    (string) The hex value of the raw public key
              "iscompressed" : true|false,  (boolean) If the address is compressed
              "account" : "account"         (string) DEPRECATED. The account associated with the address, "" is the default account
              "hdkeypath" : "keypath"       (string, optional) The HD keypath if the key is HD and available
              "hdchainid" : "<hash>"        (string, optional) The ID of the HD chain
            }

            Examples:
            > bolivarcoin-cli validateaddress "AJw5Dqdh47muwzqN1tsmhAiFrvoKqCpna8"
            > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "validateaddress", "params": ["AJw5Dqdh47muwzqN1tsmhAiFrvoKqCpna8"] }' -H 'content-type: text/plain;' http://127.0.0.1:14776/
             (code -1)

        """
        return _process_result(self.raw_call("validateaddress", params=[address]))

    def getblockhash(self, index: int = 0) -> dict:
        """
            getblockhash index

            Returns hash of block in best-block-chain at index provided.

            Arguments:
            1. index         (numeric, required) The block index

            Result:
            "hash"         (string) The block hash

            Examples:
            > bolivarcoin-cli getblockhash 1000
            > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getblockhash", "params": [1000] }' -H 'content-type: text/plain;' http://127.0.0.1:14776/
             (code -1)

        """

        return _process_result(self.raw_call("getblockhash", params=[index] if index else None))

    def getblock(self, index: str = '', verbose: bool = True) -> dict:
        """
            getblock "hash" ( verbose )

            If verbose is false, returns a string that is serialized, hex-encoded data for block 'hash'.
            If verbose is true, returns an Object with information about block <hash>.

            Arguments:
            1. "hash"          (string, required) The block hash
            2. verbose           (boolean, optional, default=true) true for a json object, false for the hex encoded data

            Result (for verbose = true):
            {
              "hash" : "hash",     (string) the block hash (same as provided)
              "confirmations" : n,   (numeric) The number of confirmations, or -1 if the block is not on the main chain
              "size" : n,            (numeric) The block size
              "height" : n,          (numeric) The block height or index
              "version" : n,         (numeric) The block version
              "merkleroot" : "xxxx", (string) The merkle root
              "tx" : [               (array of string) The transaction ids
                 "transactionid"     (string) The transaction id
                 ,...
              ],
              "time" : ttt,          (numeric) The block time in seconds since epoch (Jan 1 1970 GMT)
              "mediantime" : ttt,    (numeric) The median block time in seconds since epoch (Jan 1 1970 GMT)
              "nonce" : n,           (numeric) The nonce
              "bits" : "1d00ffff", (string) The bits
              "difficulty" : x.xxx,  (numeric) The difficulty
              "chainwork" : "xxxx",  (string) Expected number of hashes required to produce the chain up to this block (in hex)
              "previousblockhash" : "hash",  (string) The hash of the previous block
              "nextblockhash" : "hash"       (string) The hash of the next block
            }

            Result (for verbose=false):
            "data"             (string) A string that is serialized, hex-encoded data for block 'hash'.

            Examples:
            > bolivarcoin-cli getblock "00000000000fd08c2fb661d2fcb0d49abb3a91e5f27082ce64feed3b4dede2e2"
            > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getblock", "params": ["00000000000fd08c2fb661d2fcb0d49abb3a91e5f27082ce64feed3b4dede2e2"] }' -H 'content-type: text/plain;' http://127.0.0.1:14776/

        """

        return _process_result(self.raw_call("getblock", params=[index, verbose] if bool(index) else []))


# ╺┳╸┏━┓┏━┓┏┓╻┏━┓┏━┓┏━╸╺┳╸╻┏━┓┏┓╻┏━┓
#  ┃ ┣┳┛┣━┫┃┗┫┗━┓┣━┫┃   ┃ ┃┃ ┃┃┗┫┗━┓
#  ╹ ╹┗╸╹ ╹╹ ╹┗━┛╹ ╹┗━╸ ╹ ╹┗━┛╹ ╹┗━┛
class _Transactions:
    """Transactions methods"""

    def raw_call(self, *args, **kwargs) -> Any:
        pass

    def gettransaction(self, txid: str) -> dict:
        """
            gettransaction "txid" ( includeWatchonly )

            Get detailed information about in-wallet transaction <txid>

            Arguments:
            1. "txid"                (string, required) The transaction id
            2. "includeWatchonly"    (bool, optional, default=false) Whether to include watchonly addresses in balance calculation and details[]

            Result:
            {
              "amount" : x.xxx,        (numeric) The transaction amount in BOLIVARCOIN
              "instantlock" : true|false, (bool) Current transaction lock state
              "confirmations" : n,     (numeric) The number of blockchain confirmations
              "blockhash" : "hash",    (string) The block hash
              "blockindex" : xx,       (numeric) The index of the transaction in the block that includes it
              "blocktime" : ttt,       (numeric) The time in seconds since epoch (1 Jan 1970 GMT)
              "txid" : "transactionid",   (string) The transaction id.
              "time" : ttt,            (numeric) The transaction time in seconds since epoch (1 Jan 1970 GMT)
              "timereceived" : ttt,    (numeric) The time received in seconds since epoch (1 Jan 1970 GMT)
              "bip125-replaceable": "yes|no|unknown"  (string) Whether this transaction could be replaced due to BIP125 (replace-by-fee);
                                                               may be unknown for unconfirmed transactions not in the mempool
              "details" : [
                {
                  "account" : "accountname",      (string) DEPRECATED. The account name involved in the transaction, can be "" for the default account.
                  "address" : "bolivarcoinaddress",      (string) The bolivarcoin address involved in the transaction
                  "category" : "send|receive",    (string) The category, either 'send' or 'receive'
                  "amount" : x.xxx,               (numeric) The amount in BOLIVARCOIN
                  "label" : "label",              (string) A comment for the address/transaction, if any
                  "vout" : n,                     (numeric) the vout value
                }
                ,...
              ],
              "hex" : "data"                      (string) Raw data for transaction
            }

            Examples:
            > bolivarcoin-cli gettransaction "1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d"
            > bolivarcoin-cli gettransaction "1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d" true
            > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "gettransaction", "params": ["1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d"] }' -H 'content-type: text/plain;' http://127.0.0.1:14776/

        """
        # TODO: Add parameters --> gettransaction "txid" ( includeWatchonly )
        return _process_result(self.raw_call("gettransaction", params=[txid]))

    def getlisttransactions(
            self,
            account: str = "*",
            count: int = 10,
            from_number: int = 0,
            includewatchonly: bool = False
    ) -> dict:
        """
        Bolicoin uses "*" as default account

            listtransactions    ( "account" count from includeWatchonly)

            Returns up to 'count' most recent transactions skipping the first 'from' transactions for account 'account'.

            Arguments:
            1. "account"        (string, optional) DEPRECATED. The account name. Should be "*".
            2. count            (numeric, optional, default=10) The number of transactions to return
            3. from             (numeric, optional, default=0) The number of transactions to skip
            4. includeWatchonly (bool, optional, default=false) Include transactions to watchonly addresses (see 'importaddress')

            Result:
            [
              {
                "account":"accountname",  (string) DEPRECATED. The account name associated with the transaction.
                                                            It will be "" for the default account.
                "address":"bolivarcoinaddress",  (string) The bolivarcoin address of the transaction. Not present for
                                                            move transactions (category = move).
                "category":"send|receive|move", (string) The transaction category. 'move' is a local (off blockchain)
                                                            transaction between accounts, and not associated with an address,
                                                            transaction id or block. 'send' and 'receive' transactions are
                                                            associated with an address, transaction id and block details
                "amount": x.xxx,          (numeric) The amount in BOLIVARCOIN. This is negative for the 'send' category, and for the
                                                     'move' category for moves outbound. It is positive for the 'receive' category,
                                                     and for the 'move' category for inbound funds.
                "vout": n,                (numeric) the vout value
                "fee": x.xxx,             (numeric) The amount of the fee in BOLIVARCOIN. This is negative and only available for the
                                                     'send' category of transactions.
                "instantlock" : true|false, (bool) Current transaction lock state. Available for 'send' and 'receive' category of transactions.
                "confirmations": n,       (numeric) The number of blockchain confirmations for the transaction. Available for 'send' and
                                                     'receive' category of transactions. Negative confirmations indicate the
                                                     transation conflicts with the block chain
                "trusted": xxx            (bool) Whether we consider the outputs of this unconfirmed transaction safe to spend.
                "blockhash": "hashvalue", (string) The block hash containing the transaction. Available for 'send' and 'receive'
                                                      category of transactions.
                "blockindex": n,          (numeric) The index of the transaction in the block that includes it. Available for 'send' and 'receive'
                                                      category of transactions.
                "blocktime": xxx,         (numeric) The block time in seconds since epoch (1 Jan 1970 GMT).
                "txid": "transactionid",  (string) The transaction id. Available for 'send' and 'receive' category of transactions.
                "time": xxx,              (numeric) The transaction time in seconds since epoch (midnight Jan 1 1970 GMT).
                "timereceived": xxx,      (numeric) The time received in seconds since epoch (midnight Jan 1 1970 GMT). Available
                                                      for 'send' and 'receive' category of transactions.
                "comment": "...",         (string) If a comment is associated with the transaction.
                "label": "label"          (string) A comment for the address/transaction, if any
                "otheraccount": "accountname",  (string) For the 'move' category of transactions, the account the funds came
                                                      from (for receiving funds, positive amounts), or went to (for sending funds,
                                                      negative amounts).
                "bip125-replaceable": "yes|no|unknown"  (string) Whether this transaction could be replaced due to BIP125 (replace-by-fee);
                                                                 may be unknown for unconfirmed transactions not in the mempool
              }
            ]

            Examples:

            List the most recent 10 transactions in the systems
            > bolivarcoin-cli listtransactions

            List transactions 100 to 120
            > bolivarcoin-cli listtransactions "*" 20 100

            As a json rpc call
            > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "listtransactions", "params": ["*", 20, 100] }' -H 'content-type: text/plain;' http://127.0.0.1:14776/


        """
        return _process_result(
            self.raw_call(
                "listtransactions", params=[
                    account,
                    count,
                    from_number,
                    includewatchonly
                ]
            )
        )


# ┏┳┓╻┏┓╻╻┏┓╻┏━╸
# ┃┃┃┃┃┗┫┃┃┗┫┃╺┓
# ╹ ╹╹╹ ╹╹╹ ╹┗━┛
class _Mining:
    """Mining methods"""

    def raw_call(self, *args, **kwargs) -> Any:
        pass


# ┏┓╻┏━╸╺┳╸╻ ╻┏━┓┏━┓╻┏
# ┃┗┫┣╸  ┃ ┃╻┃┃ ┃┣┳┛┣┻┓
# ╹ ╹┗━╸ ╹ ┗┻┛┗━┛╹┗╸╹ ╹
class _Network:
    """Network methods"""

    def raw_call(self, *args, **kwargs) -> Any:
        pass

    def getnetworkinfo(self) -> dict:
        """
            getnetworkinfo
            Returns an object containing various state info regarding P2P networking.

            Result:
            {
              "version": xxxxx,                      (numeric) the server version
              "subversion": "/Bolivarcoin Core:x.x.x/",     (string) the server subversion string
              "protocolversion": xxxxx,              (numeric) the protocol version
              "localservices": "xxxxxxxxxxxxxxxx", (string) the services we offer to the network
              "localrelay": true|false,              (bool) true if transaction relay is requested from peers
              "timeoffset": xxxxx,                   (numeric) the time offset
              "connections": xxxxx,                  (numeric) the number of connections
              "networkactive": true|false,           (bool) whether p2p networking is enabled
              "networks": [                          (array) information per network
              {
                "name": "xxx",                     (string) network (ipv4, ipv6 or onion)
                "limited": true|false,               (boolean) is the network limited using -onlynet?
                "reachable": true|false,             (boolean) is the network reachable?
                "proxy": "host:port"               (string) the proxy that is used for this network, or empty if none
              }
              ,...
              ],
              "relayfee": x.xxxxxxxx,                (numeric) minimum relay fee for non-free transactions in BOLIVARCOIN/kB
              "localaddresses": [                    (array) list of local addresses
              {
                "address": "xxxx",                 (string) network address
                "port": xxx,                         (numeric) network port
                "score": xxx                         (numeric) relative score
              }
              ,...
              ]
              "warnings": "..."                    (string) any network warnings (such as alert messages)
            }

            Examples:
            > bolivarcoin-cli getnetworkinfo
            > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getnetworkinfo", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:14776/

        """
        return _process_result(self.raw_call("getnetworkinfo"))


# ┏┳┓┏━┓┏━┓╺┳╸┏━╸┏━┓┏┓╻┏━┓╺┳┓┏━╸
# ┃┃┃┣━┫┗━┓ ┃ ┣╸ ┣┳┛┃┗┫┃ ┃ ┃┃┣╸
# ╹ ╹╹ ╹┗━┛ ╹ ┗━╸╹┗╸╹ ╹┗━┛╺┻┛┗━╸
class _Masternode:
    """
    Masternode methods
            masternode "command"...
            Set of commands to execute masternode related actions

            Arguments:
            1. "command"        (string or set of strings, required) The command to execute

            Available commands:
              count        - Print number of all known masternodes (optional: 'ps', 'enabled', 'all', 'qualify')
              current      - Print info on current masternode winner to be paid the next block (calculated locally)
              genkey       - Generate new masternodeprivkey
              outputs      - Print masternode compatible outputs
              start-alias  - Start single remote masternode by assigned alias configured in masternode.conf
              start-<mode> - Start remote masternodes configured in masternode.conf (<mode>: 'all', 'missing', 'disabled')
              status       - Print masternode status information
              list         - Print list of all known masternodes (see masternodelist for more info)
              list-conf    - Print masternode.conf in JSON format
              winner       - Print info on next masternode winner to vote for
              winners      - Print list of masternode winners

    """

    def raw_call(self, *args, **kwargs) -> Any:
        pass

    def masternode_count(self, option: MasternodeCountOptions = MasternodeCountOptions.EMPTY) -> dict:
        """
        Print number of all known masternodes
        masternode count ps
        masternode count enabled
        masternode count all
        masternode count qualify

            option: Possible values: ['ps', 'enabled', 'all', 'qualify']
        """
        # See members of MasternodeCountOptions (must be same)
        MASTERNODE_COUNT_OPTIONS = ['', 'all', 'ps', 'enabled', 'qualify']

        if not option:
            params = ["count"]
        elif option not in MASTERNODE_COUNT_OPTIONS:
            return {'result': f'Available options are: {MASTERNODE_COUNT_OPTIONS}', 'errors': True}
        else:
            params = ["count", option]
        return _process_result(self.raw_call("masternode", params=params))

    def masternode_current(self) -> dict:
        """
        Print info on current masternode winner to be paid the next block (calculated locally)

        masternode current

        """
        return _process_result(self.raw_call("masternode", params=['current']))

    def masternode_outputs(self) -> dict:
        """
        Print masternode compatible outputs

        masternode outputs

        """
        return _process_result(self.raw_call("masternode", params=['outputs']))

    def masternode_status(self) -> dict:
        """
        Print masternode status information
        masternode status

        return:
            {
              "outpoint": "cc2ad40cbf9bf37357cf50019fc88744d56b6ff48d00cb0985cec7bcdd2b169a-1",
              "service": "123.456.789.012:42997",
              "payee": "babSyYWEznQBgHMqo4T5xAdFZLme7bpzZC",
              "status": "Masternode successfully started"
            }


        """
        return _process_result(self.raw_call("masternode", params=['status']))

    def masternode_genkey(self) -> dict:
        """
        Generate new masternodeprivkey
        masternode genkey
        """
        return _process_result(self.raw_call("masternode", params=['genkey']))

    def masternode_winner(self) -> dict:
        """
        Print info on next masternode winner to vote for

        masternode winner

        """
        return _process_result(self.raw_call("masternode", params=['winner']))

    def masternode_winners(self) -> dict:
        """
        Print list of masternode winners

        masternode winners

        return:
            {
              "1050231": "bJJL68a68RsoiYiXXSUJVvednEJzfPyhjc:3, bTaUd3FnGVyPQqfDWNVuHvAYh9nS5G6Ddd:1",
              "1050232": "bKisyEJuYSTEGFuCgJ97z7Kj4tiH7eLa5j:4",
              "1050233": "bZGErYrUJv3gxfJqaQNrhTQem4R2SUJSTA:5, bauejpLQMSSnhtPXsZ5emYa1e4S6qBTENn:1, bJNDJXCfYoMV5btyabcRbBsGeGpo54TpfA:1",
              "1050234": "bKFDE6EHDQJMbD4tuEdkCWkKbUgyYsrHP8:3, bM7Tu2owEn9w6oMWQJS8jJnSqmgqPeUi37:1",
              "1050235": "bWjwiv9dLtVBTTw9mb7scLWagxAgUwzHbQ:4, bRQS7jNnnT1LML4g5uhSZZstvKYvSnznug:1",
              "1050236": "bEzHyW2V9ern4NJuHWJ5kUPTHvg1JN4vjd:2, bPimPnZ1N33ryWEenhCYJjYz3tenwXW2RA:1, bMyoS7hMqv1eJ79yz1NsgjMBGX5Q4bup9M:1, bVhgKRirSNHhpBU4TSJNGvbmeEStsA91y8:1",
              "1050237": "bEUjTghasEiaKbh3D63Fbn8QfBrJRXpRxf:2, baa1zkUz8rDiyaAzWXYu5vw1Af82oKJY6P:1, bCmmrNAt2uEiBkdR7r7cQvknKTQhmySzkT:1",
              "1050238": "bD1ATJnv68cfaoVtqvH8UtNDPA4UZVSBFB:6, bLeRs5s1RAF5m14TEi2kBNc72EmEC74YEt:2",
              "1050239": "bNjYRDBVFKkN39y8HX4FHz2Xx3rSbZkweg:4, bRywFFcaRLYTnLEHTV5CGKZadwRK2NN6gQ:1",
              "1050240": "baLzJQerBTWfRAsTZUbCGFmkS2sLaXZP1R:6, bNM64eaNL8gDD5ZsnCcNvX1uNXvazyxyiZ:1",
              "1050241": "bNC1cxPXT4s6PdkYfhyF9UnEhzmnb1p94V:5, bbuHiaDwaSvSnceaGHhTtrLZvz8vAL2MdT:1",
              "1050242": "bFMeTZA5ymQB5wQU85fvpy46BCD7YvWuS7:4, bN2HAq1Ds68KeNUk23vW88ULFApE96HXXD:1",
              "1050243": "bT8mrM3GBAm9zhbyRZvPLqRxrQM4g3LEwt:1, bFiQ816UzM81a4r1gAKUnDTpic9PCh37Dq:2, bU7w6FNYsAjDndvvuDVMhrUunPK8TCBdDc:2",
              "1050244": "bKro33f6Z5sH2mQjeHwWoM3xTrrXATqJo5:1, bKvoZRHCsWnqocSdxMajHiuW1q6XB3yxmy:4, bT8mrM3GBAm9zhbyRZvPLqRxrQM4g3LEwt:1",
              "1050245": "bRumHGvbJkHUq8sr6C26KVLad83QCv7Bkm:4, bYadqN4GVbXYctqUkb7c3QYK4ZZJ6TwtYV:2",
              "1050246": "bTaUd3FnGVyPQqfDWNVuHvAYh9nS5G6Ddd:4, bPimPnZ1N33ryWEenhCYJjYz3tenwXW2RA:1",
              "1050247": "bSHcSBNnSjeATNn75nvAG2XLNA7PJujUM5:3, bYadqN4GVbXYctqUkb7c3QYK4ZZJ6TwtYV:1",
              "1050248": "baAt3x29fAZJ5vxW6mcL8cRx21r9VZT4np:4, bEz5ZsttwaMvEb1kS74mtyQn3Mx6DSFYo5:1, bRQS7jNnnT1LML4g5uhSZZstvKYvSnznug:1, bZNQTFPCRjc2bypADsNMZNJnb8hKkhvi2C:1",
              "1050249": "baAt3x29fAZJ5vxW6mcL8cRx21r9VZT4np:6, bX2x9NKRnSjKziL4vECzUYnkNs9CRY81Ru:3",
              "1050250": "bS9ZZAsizKMQ41c97o83xFKRPnjR5GddVS:6, bKUWQ5wVV7E7ihX3b6uFQDbrM8PQf1mcpg:1, bPNTdxsZPpz91BxwUYb7fy8Kn1QtLiMFWR:1",
              "1050251": "bJNDJXCfYoMV5btyabcRbBsGeGpo54TpfA:3, bER46jBVob6QHUtaz24oSunNtE3JkeWjUV:1, bEDMCx5FPUvPAkDNnuHbgYaFYdTN6RsYmV:1",
              "1050252": "Unknown",
              "1050253": "Unknown",
              "1050254": "Unknown",
              "1050255": "Unknown",
              "1050256": "Unknown",
              "1050257": "Unknown",
              "1050258": "Unknown",
              "1050259": "Unknown",
              "1050260": "Unknown"
            }

        """
        return _process_result(self.raw_call("masternode", params=['winners']))

    def masternode_list_conf(self) -> dict:
        """
        Print masternode.conf in JSON format
        masternode list-conf
        """
        return _process_result(self.raw_call("masternode", params=['list-conf'], return_binary=True))

    def masternode_start_alias(self, alias) -> dict:
        """
        Start single remote masternode by assigned alias configured in masternode.conf

        masternode start-alias alias

        """
        return _process_result(self.raw_call("masternode", params=['start-alias', alias]))

    def masternode_start_mode(self, mode: MasternodeStartModes = MasternodeStartModes.ALL) -> dict:
        """start-<mode> - Start remote masternodes configured in masternode.conf
        (<mode>: 'all', 'missing', 'disabled')

        masternode start-all
        masternode start-missing
        masternode start-disabled

        """
        # See MasternodeStartModes must be same)
        MASTERNODE_START_MODES = ['all', 'missing', 'disabled']

        if mode in MASTERNODE_START_MODES:
            params = [f'start-{mode}']
        else:
            return {'result': f'Available modes are: {MASTERNODE_START_MODES}', 'errors': True}

        return _process_result(self.raw_call("masternode", params=params))

    def masternodelist(self, mode: MnListModes = MnListModes.STATUS, mn_filter: str = ''):
        """
            masternodelist ( "mode" "filter" )
            Get a list of masternodes in different modes

            Arguments:
            1. "mode"      (string, optional/required to use filter, defaults = status) The mode to run list in
            2. "filter"    (string, optional) Filter results. Partial match by outpoint by default in all modes,
                                                additional matches in some modes are also available

            Available modes:
              activeseconds  - Print number of seconds masternode recognized by the network as enabled
                               (since latest issued "masternode start/start-many/start-alias")
              addr           - Print ip address associated with a masternode (can be additionally filtered, partial match)
              full           - Print info in format 'status protocol payee lastseen activeseconds lastpaidtime lastpaidblock IP'
                               (can be additionally filtered, partial match)
              info           - Print info in format 'status protocol payee lastseen activeseconds sentinelversion sentinelstate IP'
                               (can be additionally filtered, partial match)
              lastpaidblock  - Print the last block height a node was paid on the network
              lastpaidtime   - Print the last time a node was paid on the network
              lastseen       - Print timestamp of when a masternode was last seen on the network
              payee          - Print Bolivarcoin address associated with a masternode (can be additionally filtered,
                               partial match)
              protocol       - Print protocol of a masternode (can be additionally filtered, exact match)
              pubkey         - Print the masternode (not collateral) public key
              rank           - Print rank of a masternode based on current block
              status         - Print masternode status: PRE_ENABLED / ENABLED / EXPIRED / WATCHDOG_EXPIRED / NEW_START_REQUIRED /
                               UPDATE_REQUIRED / POSE_BAN / OUTPOINT_SPENT (can be additionally filtered, partial match)

                EXAMPLE
                {
                "ad06255e05cc22b5abb74187e2008fd022bd192b1bac065bc87ae3070a9761fb-0": "NEW_START_REQUIRED 70212 bJG26MWSpxiYLada8orPxz8mwpUYubvJFh 1676268599  1065786 1.1.0 current 167.86.105.73:49053",
                }

        """
        return _process_result(self.raw_call("masternodelist", params=[mode, mn_filter]))

    def mnsync_status(self):
        """Returns the sync status (mnsync status)"""
        return _process_result(self.raw_call("mnsync", params=['status']))

    def mnsync_next(self):
        """Returns the sync status to the next step (mnsync next)"""
        return _process_result(self.raw_call("mnsync", params=['next']))

    def mnsync_reset(self):
        """Reset mnsync (mnsync reset)"""
        return _process_result(self.raw_call("mnsync", params=['reset']))


# ╻ ╻┏━╸╻  ┏━┓
# ┣━┫┣╸ ┃  ┣━┛
# ╹ ╹┗━╸┗━╸╹
class _Help:
    """ Help class for get help directly from node

        There is no error correction on sentence

    """

    def raw_call(self, *args, **kwargs) -> Any:
        pass

    def get_help(self, method: str = ""):
        """
            == Addressindex ==
            getaddressbalance
            getaddressdeltas
            getaddressmempool
            getaddresstxids
            getaddressutxos

            == Blockchain ==
            getbestblockhash
            getblock "hash" ( verbose )
            getblockchaininfo
            getblockcount
            getblockhash index
            getblockhashes timestamp
            getblockheader "hash" ( verbose )
            getblockheaders "hash" ( count verbose )
            getchaintips ( count branchlen )
            getdifficulty
            getmempoolinfo
            getrawmempool ( verbose )
            getspentinfo
            gettxout "txid" n ( includemempool )
            gettxoutproof ["txid",...] ( blockhash )
            gettxoutsetinfo
            verifychain ( checklevel numblocks )
            verifytxoutproof "proof"

            == Bolivarcoin ==
            getgovernanceinfo
            getpoolinfo
            getsuperblockbudget index
            gobject "command"...
            masternode "command"...
            masternodebroadcast "command"...
            masternodelist ( "mode" "filter" )
            mnsync [status|next|reset]
            privatesend "command"
            sentinelping version
            spork <name> [<value>]
            voteraw <masternode-tx-hash> <masternode-tx-index> <governance-hash> <vote-signal> [yes|no|abstain] <time> <vote-sig>

            == Control ==
            debug ( 0|1|addrman|alert|bench|coindb|db|lock|rand|rpc|selectcoins|mempool|mempoolrej|net|proxy|prune|http|libevent|tor|zmq|bolivarcoin|privatesend|instantsend|masternode|spork|keepass|mnpayments|gobject )
            getinfo
            help ( "command" )
            stop

            == Generating ==
            generate numblocks
            getgenerate
            setgenerate generate ( genproclimit )

            == Mining ==
            getblocktemplate ( "jsonrequestobject" )
            getmininginfo
            getnetworkhashps ( blocks height )
            prioritisetransaction <txid> <priority delta> <fee delta>
            submitblock "hexdata" ( "jsonparametersobject" )

            == Network ==
            addnode "node" "add|remove|onetry"
            clearbanned
            disconnectnode "node"
            getaddednodeinfo dummy ( "node" )
            getconnectioncount
            getnettotals
            getnetworkinfo
            getpeerinfo
            listbanned
            ping
            setban "ip(/netmask)" "add|remove" (bantime) (absolute)
            setnetworkactive true|false

            == Rawtransactions ==
            createrawtransaction [{"txid":"id","vout":n},...] {"address":amount,"data":"hex",...} ( locktime )
            decoderawtransaction "hexstring"
            decodescript "hex"
            fundrawtransaction "hexstring" includeWatching
            getrawtransaction "txid" ( verbose )
            sendrawtransaction "hexstring" ( allowhighfees instantsend )
            signrawtransaction "hexstring" ( [{"txid":"id","vout":n,"scriptPubKey":"hex","redeemScript":"hex"},...] ["privatekey1",...] sighashtype )

            == Util ==
            createmultisig nrequired ["key",...]
            estimatefee nblocks
            estimatepriority nblocks
            estimatesmartfee nblocks
            estimatesmartpriority nblocks
            validateaddress "bolivarcoinaddress"
            verifymessage "bolivarcoinaddress" "signature" "message"

            == Wallet ==
            abandontransaction "txid"
            addmultisigaddress nrequired ["key",...] ( "account" )
            backupwallet "destination"
            dumphdinfo
            dumpprivkey "bolivarcoinaddress"
            dumpwallet "filename"
            encryptwallet "passphrase"
            getaccount "bolivarcoinaddress"
            getaccountaddress "account"
            getaddressesbyaccount "account"
            getbalance ( "account" minconf addlockconf includeWatchonly )
            getnewaddress ( "account" )
            getrawchangeaddress
            getreceivedbyaccount "account" ( minconf addlockconf )
            getreceivedbyaddress "bolivarcoinaddress" ( minconf addlockconf )
            gettransaction "txid" ( includeWatchonly )
            getunconfirmedbalance
            getwalletinfo
            importaddress "address" ( "label" rescan p2sh )
            importelectrumwallet "filename" index
            importprivkey "bolivarcoinprivkey" ( "label" rescan )
            importpubkey "pubkey" ( "label" rescan )
            importwallet "filename"
            instantsendtoaddress "bolivarcoinaddress" amount ( "comment" "comment-to" subtractfeefromamount )
            keepass <genkey|init|setpassphrase>
            keypoolrefill ( newsize )
            listaccounts ( minconf addlockconf includeWatchonly)
            listaddressgroupings
            listlockunspent
            listreceivedbyaccount ( minconf addlockconf includeempty includeWatchonly)
            listreceivedbyaddress ( minconf addlockconf includeempty includeWatchonly)
            listsinceblock ( "blockhash" target-confirmations includeWatchonly)
            listtransactions    ( "account" count from includeWatchonly)
            listunspent ( minconf maxconf ["address",...] )
            lockunspent unlock [{"txid":"txid","vout":n},...]
            move "fromaccount" "toaccount" amount ( minconf "comment" )
            sendfrom "fromaccount" "tobolivarcoinaddress" amount ( minconf addlockconf "comment" "comment-to" )
            sendmany "fromaccount" {"address":amount,...} ( minconf addlockconf "comment" ["address",...] subtractfeefromamount use_is use_ps )
            sendtoaddress "bolivarcoinaddress" amount ( "comment" "comment-to" subtractfeefromamount use_is use_ps )
            setaccount "bolivarcoinaddress" "account"
            settxfee amount
            signmessage "bolivarcoinaddress" "message"

        """
        return _process_result(self.raw_call("help", params=[method]))


# ┏━╸┏━┓╻ ╻┏━╸┏━┓┏┓╻┏━┓┏┓╻┏━╸┏━╸
# ┃╺┓┃ ┃┃┏┛┣╸ ┣┳┛┃┗┫┣━┫┃┗┫┃  ┣╸
# ┗━┛┗━┛┗┛ ┗━╸╹┗╸╹ ╹╹ ╹╹ ╹┗━╸┗━╸
# https://dashcore.readme.io/docs/core-api-ref-remote-procedure-calls-dash
class _Governance:
    """Governance methods"""

    def raw_call(self, *args, **kwargs) -> Any:
        pass

    def getgovernanceinfo(self) -> dict:
        """
            getgovernanceinfo
            Returns an object containing governance parameters.

                Result:
                {
                  "governanceminquorum": xxxxx,           (numeric) the absolute minimum number of votes needed to trigger a governance action
                  "masternodewatchdogmaxseconds": xxxxx,  (numeric) sentinel watchdog expiration time in seconds
                  "proposalfee": xxx.xx,                  (numeric) the collateral transaction fee which must be paid to create a proposal in BOLIVARCOIN
                  "superblockcycle": xxxxx,               (numeric) the number of blocks between superblocks
                  "lastsuperblock": xxxxx,                (numeric) the block number of the last superblock
                  "nextsuperblock": xxxxx,                (numeric) the block number of the next superblock
                  "maxgovobjdatasize": xxxxx,             (numeric) maximum governance object data size in bytes
                }
"""
        return _process_result(self.raw_call("getgovernanceinfo", params=[]))

    def gobject_get(self, hash: str = '') -> dict:
        """
        Get governance object by hash

        gobject get <governance-hash>
        """
        return _process_result(self.raw_call("gobject", params=['get', hash]))

    def gobject_getvotes(self, hash: str = '') -> dict:
        """
        Get all votes for a governance object hash (including old votes)

        gobject getvotes <governance-hash>

        """
        return _process_result(self.raw_call("gobject", params=['getvotes', hash]))

    def gobject_deserialize(self, hex_string: str = '') -> dict:
        """Fixme: Retorna Strings
        Deserialize governance object from hex string to JSON
        gobject deserialize <data-hex>
        """
        return _process_result(self.raw_call("gobject", params=['deserialize', hex_string]))

    def gobject_count(self) -> dict:
        """Count governance objects and votes

        Return:
            Governance Objects: 7 (Proposals: 7, Triggers: 0, Watchdogs: 0/0, Other: 0; Erased: 0), Votes: 879
            """

        return _process_result(self.raw_call("gobject", params=['count']))

    def gobject_list(
            self,
            signal: GobjectListSignals = GobjectListSignals.ALL,
            type: GobjectListTypes = GobjectListTypes.ALL
    ) -> dict:
        """
        List governance objects (can be filtered by signal and/or object type)

        :param signal: should be 'valid', 'funding', 'delete', 'endorsed' or 'all'
        :param type: should be 'proposals', 'triggers', 'watchdogs' or 'all'
        :return:

        """
        return _process_result(self.raw_call("gobject", params=['list', signal, type]))


# ┏┓ ╻  ┏━┓┏━╸╻┏ ┏━╸╻ ╻┏━┓╻┏┓╻
# ┣┻┓┃  ┃ ┃┃  ┣┻┓┃  ┣━┫┣━┫┃┃┗┫
# ┗━┛┗━╸┗━┛┗━╸╹ ╹┗━╸╹ ╹╹ ╹╹╹ ╹
class _BlockChain:
    def raw_call(self, *args, **kwargs) -> Any:
        pass

    def getblockcount(self) -> dict:
        """
            getblockcount

            Returns the number of blocks in the longest block chain.

            Result:
            n    (numeric) The current block count

            Examples:
            > bolivarcoin-cli getblockcount
            > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getblockcount", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:14776/

        """
        return _process_result(self.raw_call("getblockcount"))

    def getblockchaininfo(self) -> dict:
        """
            getblockchaininfo
            Returns an object containing various state info regarding block chain processing.

            Result:
            {
              "chain": "xxxx",        (string) current network name as defined in BIP70 (main, test, regtest)
              "blocks": xxxxxx,         (numeric) the current number of blocks processed in the server
              "headers": xxxxxx,        (numeric) the current number of headers we have validated
              "bestblockhash": "...", (string) the hash of the currently best block
              "difficulty": xxxxxx,     (numeric) the current difficulty
              "mediantime": xxxxxx,     (numeric) median time for the current best block
              "verificationprogress": xxxx, (numeric) estimate of verification progress [0..1]
              "chainwork": "xxxx"     (string) total amount of work in active chain, in hexadecimal
              "pruned": xx,             (boolean) if the blocks are subject to pruning
              "pruneheight": xxxxxx,    (numeric) heighest block available
              "softforks": [            (array) status of softforks in progress
                 {
                    "id": "xxxx",        (string) name of softfork
                    "version": xx,         (numeric) block version
                    "enforce": {           (object) progress toward enforcing the softfork rules for new-version blocks
                       "status": xx,       (boolean) true if threshold reached
                       "found": xx,        (numeric) number of blocks with the new version found
                       "required": xx,     (numeric) number of blocks required to trigger
                       "window": xx,       (numeric) maximum size of examined window of recent blocks
                    },
                    "reject": { ... }      (object) progress toward rejecting pre-softfork blocks (same fields as "enforce")
                 }, ...
              ],
              "bip9_softforks": [       (array) status of BIP9 softforks in progress
                 {
                    "id": "xxxx",        (string) name of the softfork
                    "status": "xxxx",    (string) one of "defined", "started", "lockedin", "active", "failed"
                 }
              ]
            }

            Examples:
            > bolivarcoin-cli getblockchaininfo
            > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getblockchaininfo", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:14776/

        """
        return _process_result(self.raw_call("getblockchaininfo"))

    def getdifficulty(self) -> dict:
        """
        Returns the proof-of-work difficulty as a multiple of the minimum difficulty.

        Result:
        n.nnn       (numeric) the proof-of-work difficulty as a multiple of the minimum difficulty.

        """
        return _process_result(self.raw_call("getdifficulty"))


# ┏┓╻┏━┓╺┳┓┏━╸
# ┃┗┫┃ ┃ ┃┃┣╸
# ╹ ╹┗━┛╺┻┛┗━╸
class Node(
    _Utils,
    _Wallet,
    _BlockChain,
    _Network,
    _Transactions,
    _Governance,
    _Masternode,
    _Help
):
    """ Main RPC/API Class

        Communicate with nodes via RPC

        BOLICOIN COMPATIBLE VERSION: v2.0.0.2-g
    """

    def __init__(
            self,
            rpc_user: str | None = None,
            rpc_password: str | None = None,
            rpc_port: int = 3563,
            server_ip: str = "127.0.0.1",
            scheme: str = 'http',
            core_type: int = 1,
            name: str = '',
            ticker: str = 'BOLI',
            is_masternode: bool = False,
            app_id: str = 'standard',
    ):

        self.server_ip = server_ip
        self.rpc_port = rpc_port
        self.rpc_user = rpc_user
        self.rpc_password = rpc_password
        self.scheme = scheme
        self.core_type = core_type
        self.name = name
        self.ticker = ticker
        self.is_masternode = is_masternode
        self.app_id = f"Orbital_{app_id}"

        self._headers = {'content-type': 'text/plain;', }
        self._data = {"jsonrpc": "2.0", "id": self.app_id, "method": ""}

        # save valid node state and error if exists
        self._valid_node: bool = False
        self._node_error: dict = {"error": None}

        logger.debug(f"Version: {self.api_version}")

        # Check connection and test if a valid node
        self._connect()

    def _check_online_status(self):
        try:  # It will fail if not communication
            blockcount = self.getblockcount()
            if blockcount.get('result', None) is None:
                return False
            self._valid_node = True
            return True
        except:
            self._valid_node = False
            return False

    def _connect(self):
        """
        Test connection with node and verify is a valid Node
        """
        logger.debug("Connecting node...")
        self._check_online_status()

    def raw_call(
            self,
            method: str,
            params=None,
            return_binary=False
    ) -> Any:
        """ Rpc communication raw_call main method

        It will return:
        # OK JSON
        {"result": response.json()['result'], 'errors': None} When OK

        # OK BINARY
        {"result": response.content, 'errors': None} When OK

        # Server responds but NOT OK
        {"result": response.json()['result'], 'errors': None} When server responds but error in command or sintaxis

        # NO connect or communication fail
        {"result": response, 'errors': f'{e}'}

        return_binary: Some methods prefer use binary version instead JSON

        """

        self._data["params"] = [] if params is None else params

        self._data["method"] = method

        logger.debug(f"raw_call: method:{method} params:{params}")

        response: Response = Response()
        try:
            # print(self._data, dumps(self._data), sep="\n")
            response = post(
                url=f'{self.scheme}://{self.server_ip}:{self.rpc_port}/',
                headers=self._headers,
                data=dumps(self._data),
                auth=(self.rpc_user, self.rpc_password)
            )

            if response.status_code == 200:
                self._valid_node = True
                if return_binary:
                    return {"result": response.content, 'errors': None}
                else:
                    return {"result": response.json()['result'], 'errors': None}

            else:
                self._valid_node = False
                return {"result": response.json()['result'], 'errors': response.json()['error']}


        except request_exceptions.RequestException as e:
            logger.warning(f'{self.name} raw_call request_exceptions.RequestException error')
            self._valid_node = False
            return {"result": None, 'errors': f'{e}'}

        except BaseException as e:
            logger.warning(f"{self.name} raw_call BaseException: {e}")
            self._valid_node = False
            return {"result": None, 'errors': f'{e}'}

    # OBLIGATORIO ENTENDER PREREQUISITOS
    # https://github.com/BlockchainCommons/Learning-Bitcoin-from-the-Command-Line/blob/master/04_5_Sending_Coins_with_Automated_Raw_Transactions.md
    def fundrawtransaction(
            self,
            recipients_with_amounts: dict,  # {"address..1":amount..1,"address..2":amount..2,...}
    ):
        """Sending Coins with Automated Raw Transactions"""

        # Step one: Get unfinished TX with createrawtransaction
        try:
            # {'result': '01000000000100d2496b000000001976a9144486f188fd5361906cf9a0c1cd1105f913a080f488ac00000000', 'errors': None}
            rawtransaction = self.raw_call(
                method='createrawtransaction',
                params=[
                    [],
                    recipients_with_amounts,
                ]
            )

            if rawtransaction['errors'] is not None:
                return {"result": rawtransaction.get('result', None), "errors": rawtransaction.get('errors', True)}

            # print("rawtransaction", rawtransaction)

        except BaseException as e:
            logger.critical(f'{self.name} fundrawtransaction BaseException "rawtransaction" error: {e}')
            return {"result": None, "errors": e}

        # Step two: Fund that bare-bones transaction
        try:
            fund = self.raw_call(
                method='fundrawtransaction',
                params=[rawtransaction['result']]
            )

            # print(f"fund {fund}")

            if fund['errors'] is not None:
                return {"result": fund.get('result', None), "errors": fund.get('errors', True)}

            hex = fund['result']['hex']
            changepos = fund['result']['changepos']
            fee = fund['result']['fee']

            # try:
            #     print(f"hex {hex}")
            #     print(f"changepos {changepos}")
            #     print(f"errors {fund['errors']}")
            #     print(f"fee {float(fee):.8f}")
            # except:
            #     pass


        except BaseException as e:
            logger.critical(f'{self.name} fundrawtransaction BaseException "fund" error: {e}')
            return {"result": None, "errors": e}

        # Decode decoderawtransaction
        try:
            decoded = self.raw_call(
                method='decoderawtransaction',
                params=[hex]
            )
            # print(f"decoded {decoded}")

            if decoded['errors'] is not None:
                return {"result": decoded.get('result', None), "errors": decoded.get('errors', True)}

        except BaseException as e:
            logger.critical(f'{self.name} fundrawtransaction BaseException "decoded" error: {e}')
            return {"result": None, "errors": e}

        # Step 3: Signs the transaction signrawtransaction
        try:
            signed = self.raw_call(
                method='signrawtransaction',
                params=[hex]
            )

            # print(f"signed {signed}")

            if signed['errors'] is not None:
                return {"result": signed.get('result', None), "errors": signed.get('errors', True)}

            signedhex = signed['result']['hex']
            # print(f"signedhex {signedhex}")

        except BaseException as e:
            logger.critical(f'{self.name} fundrawtransaction BaseException "signed" error: {e}')
            return {"result": None, "errors": e}

        # Step 4: Send RAW Transaction sendrawtransaction
        try:
            sent = self.raw_call(
                method='sendrawtransaction',
                params=[signedhex]
            )

            # print(f"sent {sent}")

            if sent['errors'] is not None:
                return {"result": sent.get('result', None), "errors": sent.get('errors', True)}

        except BaseException as e:
            logger.critical(f'{self.name} fundrawtransaction BaseException "sent" error: {e}')
            return {"result": None, "errors": e}

        # SUCCESS TXID Acquired
        # SUCCESS TXID Acquired
        # SUCCESS TXID Acquired
        # SUCCESS TXID Acquired
        return {
            "txid": sent['result'],
            "fee": fee,
            "errors": sent['errors']
        }

    @property
    def is_online(self) -> bool:
        self._check_online_status()
        return self._valid_node

    @property
    def all_node_info(self) -> dict:
        """Execute three methods to get all status info about this node

        TODO: Use multiple raw call (batch requests)
            https://dashcore.readme.io/docs/core-api-ref-remote-procedure-calls#batch-requests
            curl --user 'MNMIO34333:KSAJSHDSS' --data-binary '''
              [
                {
                  "method": "getblockhash",
                  "params": [0],
                  "id": "foo"
                },
                {
                  "method": "getinfo",
                  "params": [1],
                  "id": "foo2"
                }
              ]''' \
              --header 'Content-Type: text/plain;' localhost:62026
        """
        return {
            "getblockchaininfo": self.getblockchaininfo(),
            "getnetworkinfo": self.getnetworkinfo(),
            "getwalletinfo": self.getwalletinfo()
        }

    @property
    def api_version(self) -> str:
        return VERSION


class About:

    @classmethod
    def about(cls):
        return {
            '__author__': "Asdrúbal Velásquez Lagrave - Twitter/Telegram: @Visionario",
            '__copyright__': "2018-2023",
            '__credits__': [""],
            '__license__': "MIT",
            '__version__': VERSION,
            '__maintainer__': "Asdrúbal Velásquez Lagrave",
            '__email__': "hello@orbital.center",
            '__status__': "BETA",
            '__app_name__': "API RPC main class for Bolivarcoin/Bolicoin nodes (Layer 1)",
            '__url__': "https://orbital.center",
        }
