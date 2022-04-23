#!/bin/sh

set -u 

ROOT="/nfs/nas4.irisa.fr/temp_transfert/bouge/Sauvegarde_OVH_2022-04-21"
KEY="Perso"
KEY="$1"

if test -z "${KEY}"
then
    echo "Please provide a key"
    exit
fi


export ROOT KEY 

mkdir -p "${ROOT}/Groups/${KEY}"

set -x
find "${ROOT}"/Backup* "${ROOT}"/LACIE* "${ROOT}"/LaCie* "${ROOT}"/WD* \
     -type d -name "*${KEY}*" -print0 -prune \
    | xargs -0 -I % sh ./move_keyword.d/move.sh %