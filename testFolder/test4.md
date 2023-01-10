We currently have break glass to allow ReadOnly Users to become Admins and in that process we can monitor
what their actions are.

We have seen users abusing this break glass option when it is not needed and the users fail as well to feedback what they have done, making the Resiliency Team look into the logs to check the actions.

We have decided to have the option of blacklisting users breaking glass into any environments (other than non-prod) as to enforce the non break glass option for abussive users. Bellow instructions on how to perform such Blacklist.

The repo to allow to blacklist users from using break glass is -
https://dev.azure.com/vfuk-digital/Digital/_git/dx-infra-iam-roles

The release pipeline for the repo is -
https://dev.azure.com/vfuk-digital/Digital/_release?_a=releases&view=mine&definitionId=1137

1. Create a branch on the dx-infra-iam-roles repo

2. Add the user ID (for example name.lastname@vodafone.com) to the users/blacklist/blacklist.txt file and make sure that the place holder user is not there anymore (dummy_placeholder@vodafone.com)

3. Make sure there is ONE user per line

4. Create a PR and let the Resiliency Team know about it so they can review and approve

5. Release code so the user will be blacklisted from breaking glass in ALL environemnts except in non-prod (lower) environment.

6. If deleting all users from the users/blacklist/blacklist.txt put a place holder user there (dummy_placeholder@vodafone.com) so the file will not dissapear when using git

