# Gerrit Code Review sandbox chart

This Helm chart provides examples of how to start playing with
Gerrit Code Review on k8s.

**This is not a production-grade chart. It is an example.**

The chart installs a simple Gerrit Code Review server playground with
the DEVELOPMENT_BECOME_ANY_ACCOUNT authenticaytion:

- Gerrit administrator can login as 'admin' with password 'secret'
- An embedded H2 DB is used for storing groups
- Git protocol is exposes over SSH (port 29418) and HTTP (port 8080)

The [values.yaml](values.yaml) exposes a few of the configuration options in the
charts, though there are some that are not exposed there (like
`.image`).

You can deploy this chart with `helm install incubator/gerrit`. Or
you can see how this chart would render with `helm install --dry-run
--debug incubator/gerrit`.
