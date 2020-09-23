#! /bin/bash

#
# Copyright 2020, Cray Inc.  All Rights Reserved.
#

unset WORKDIR
cleanup() {
  if [ "${WORKDIR}" != "" ]; then
    if mount | grep "${WORKDIR}"/mount > /dev/null; then
      umount "${WORKDIR}"/mount
    fi
    rm -rf "${WORKDIR}" > /dev/null
  fi
  exit 1
}

trap cleanup ERR
trap cleanup INT

if [ -z "$1" ]; then
  echo "Please specify a BOS Session Template ID"
  echo "usage: get_img_tarball.sh <BOS-Session-Template-ID>" >&2
  exit 1
fi

TEMPLATE_ID="$1"
WORKDIR=$(mktemp -d /tmp/get_img_tarball.XXXXXXXX)
cd "${WORKDIR}" > /dev/null
MANIFEST="$(
  cray bos v1 sessiontemplate describe "${TEMPLATE_ID}" --format json |
  jq '.boot_sets.computes.path' |
  sed -e 's:^.*/\([^/]*/[^/]*\)"$:\1:'
)"
cray artifacts get boot-images "${MANIFEST}" manifest.json > /dev/null
SQUASHFS_IMG="$(
  jq '
    .artifacts[] |
    select(.type == "application/vnd.cray.image.rootfs.squashfs") |
    .link.path
  ' manifest.json |
  sed -e 's:^.*/\([^/]*/[^/]*\)"$:\1:'
)"
cray artifacts get boot-images "${SQUASHFS_IMG}" rootfs.squashfs > /dev/null
mkdir -p "${WORKDIR}"/mount
mount -o loop,rdonly rootfs.squashfs "${WORKDIR}"/mount
(cd "${WORKDIR}"/mount; tar --xattrs --xattrs-include='*' -czf "${WORKDIR}/${TEMPLATE_ID}.tgz" .) > /dev/null
umount "${WORKDIR}"/mount
rm -rf rootfs.squashfs manifest.json > /dev/null
echo ${WORKDIR}/${TEMPLATE_ID}.tgz
exit 0
