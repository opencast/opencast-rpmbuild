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
git checkout -b r/22.x
echo r/22.x > branch.version
git commit branch.version -m 'Update for r/22.x release branch'
git push origin r/22.x
```

Update `develop` branch
```
git checkout develop
git merge r/22.x
sed -i 's/GPG_KEY_OC22/GPG_KEY_OC23/g' .github/workflows/build-*.yml
echo develop > branch.version
echo 23 > oc.version
git add .github/workflows/ branch.version oc.version
git commit -m 'Prepare develop for Opencast 23'
git push origin develop
```

Next, update build trigger branches
```
vim .github/workflows/trigger-updates.yml
```

Finally, make sure that all workflows run properly and none fails:
- [GitHub Actions](https://github.com/opencast/opencast-rpmbuild/actions)
