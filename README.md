# platform-operations

A minimal Python GH policy project.



## Outcome

1. Pull all repos.
2. Add to dictionary.
3. Look through all repos to see if any args are out of compliance.
4. If they are then `PATCH` to update the args to meet our compliance.
5. Pluses ...
   1. Send security alerts to admins showing what repos where out of compliance.
   2. Add tesing into this ptoject using Pytest.