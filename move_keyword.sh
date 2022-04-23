#!/bin/sh

ROOT="/nfs/nas4.irisa.fr/temp_transfert/bouge/Sauvegarde_OVH_2022-04-21"

KEY="Perso"

mkdir -p "${ROOT}/Groups/${KEY}"

function move_keyword_directory () {
    DIR="$1"
    TARGET="${ROOT}/Groups/${KEY}/${DIR}"
    BRANCH="$(dirname ${TARGET})"
    echo DIR "==>" BRANCH
    # mkdir -p "${BRANCH}"
    # mv "${DIR}"  "${BRANCH}"
}
export -f move_keyword_directory

find "${ROOT}" -type d -iname "${KEY}" -print0 \
    | xargs -0 move_keyword_directory 