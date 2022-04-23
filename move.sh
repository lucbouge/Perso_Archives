#!/bin/sh 

DIR="$1"
TARGET="${ROOT}/Groups/${KEY}/${DIR}"
BRANCH="$(dirname ${TARGET})"
echo DIR "==>" BRANCH
# mkdir -p "${BRANCH}"
# mv "${DIR}"  "${BRANCH}"
