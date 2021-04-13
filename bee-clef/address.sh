#!/bin/bash
echo '{"id": 1, "jsonrpc": "2.0", "method": "account_list"}' | nc -U /var/lib/bee-clef/clef.ipc