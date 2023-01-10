In case of a major failures for SMS calls i.e NotifyCustomer.2 calls , we need to take a call on disabling the OTAC functionality as it will reduce the impact on login journey 

Steps to follow in order to disable the OTAC on VOXI Login Journey **

We need to create a new branch under dal-services-configuration in Repos. 

Open VSTS -> Go To Repos -> Branches ->  

https://vfuk-digital.visualstudio.com/Digital/_git/dal-services-configuration/branches

![rds-db-failover](../../../assets/Voxi-2FA-Enable-Disable/Voxi_2FA1.png)

To disable the 2FA , we need to navigate to the file AUTHORIZATION-V1.yml under prod1-green environment path

Flag Name : disable2FAForVoxi (default value: false) 

change the value to "true" (disable2FAForVoxi: true)

PFB the highlighted part in below screenshot : 

![rds-db-failover](../../../assets/Voxi-2FA-Enable-Disable/Voxi_2FA2.png)


Now click on Commit

![rds-db-failover](../../../assets/Voxi-2FA-Enable-Disable/Voxi_2FA3.png)

After commit step is done , you have to create a Pull Request , see below highlighted part in screenshot

![rds-db-failover](../../../assets/Voxi-2FA-Enable-Disable/Voxi_2FA4.png)

In that Below fields need to be updated.

Title: Give some title.

Description: Give some summary.

After creating the pull request the created person need to approve and set auto complete. During the time of Raising / Lowering the other person need to approve and complete the merge . 

Additional Steps:
•	Under Pipelines go to  Releases  dal-services-configuration 
•	In dal-services-configuration  Click on latest Release
•	Verify if the latest release is the one which you are looking for . 
•	Manually deploy in Prod1- Green.

![rds-db-failover](../../../assets/Voxi-2FA-Enable-Disable/Voxi_2FA5.png)

Now Test the functionality on actual site 

Hit voxi.co.uk and perform login journey using the existing test credentials - 

We should not get the page to enter the OTAC . 

For enabling back the OTAC , all the steps will remain same . Just change the variable value back to false 

File - AUTHORIZATION-V1.yml

Flag - disable2FAForVoxi (default value: false)

To enable back the VOXI 2FA, change the value to "false" (disable2FAForVoxi: false)


**Sanity Check**
Post lowering the holding page Please perform the specific journey **without VPN**

https://pipe.com

