#!/bin/sh

set -u 

ROOT="/nfs/nas4.irisa.fr/temp_transfert/bouge/Sauvegarde_OVH_2022-04-21"
KEY="Perso"

export ROOT KEY 

mkdir -p "${ROOT}/Groups/${KEY}"

find "${ROOT}" -type d -name "${KEY}" -print0 \
    | xargs -0 -I % sh ./move.sh %