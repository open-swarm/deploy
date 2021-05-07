#!/bin/bash
bee start \
  --verbosity 5 \
    --swap-enable \
  --swap-endpoint http://194.233.68.169:8545 \
  --debug-api-enable \
  --clef-signer-enable \
  --clef-signer-endpoint /var/lib/bee-clef/clef.ipc \
--password-file /root/bee-clef/beepwd
