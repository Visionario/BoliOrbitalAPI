from pprint import pprint

from boli_orbital_api import *

node: Node = Node(rpc_user="Your_RPC_User", rpc_password="Your_RPC_Password")
pprint(node.is_online)
pprint(node.getblockhash(1050203))
pprint(node.getblock("0000000000006b05f874022e3992423b538d23b2314c33ff388b0a04f575843e"))
pprint(node.getblock("0000000000006b05f874022e3992423b538d23b2314c33ff388b0a04f575843e", False))
pprint(node.all_node_info)
