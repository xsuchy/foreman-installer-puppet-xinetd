#!/bin/bash
set -e 
set -o pipefail
git merge -m "Merge remote-tracking branch 'puppet-xinetd/master' by rel-eng/build.sh" puppet-xinetd/master
#just test if we are able to create srpm, and do not proceed if there is big change in code
tito build --test --srpm

HASH=$(git show puppet-xinetd/master  |grep commit |head -n1 | awk '{print $2}' |cut -c-7)
sed -i "s/%global foreman_hash .*$/%global foreman_hash .$HASH/" foreman-puppet-xinetd.spec
git add foreman-puppet-xinetd.spec
git commit -m 'Automatic rebase to latest nightly puppet-xinetd'
tito tag --accept-auto-changelog
git push && git push --tags
tito release koji
