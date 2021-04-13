#!/bin/bash
bee start \
  --verbosity 5 \
    --swap-enable \
  --swap-endpoint https://rpc.slock.it/goerli \
  --debug-api-enable \
  --clef-signer-enable \
  --clef-signer-endpoint /var/lib/bee-clef/clef.ipc \
--password-file /root/bee-clef/beepwd
