Opencast RPM Build Infrastructure
=================================

This repository contains automation scripts to build RPMs for [Opencast](https://opencast.org).

- Builds run on GitHub Actions
- Builds are run on release branches only
- RPMs are distibuted to Opencast's S3 storage


Branch Cut
----------

Create and update latest release branch
```
git checkout develop
git checkout -b r/18.x
echo r/18.x > branch.version
```

Update `develop` branch
```
git checkout develop
git merge r/18.x
sed -i 's/GPG_KEY_OC18/GPG_KEY_OC19/g' .github/workflows/build-*.yml
echo develop > branch.version
echo 19 > oc.version
```
