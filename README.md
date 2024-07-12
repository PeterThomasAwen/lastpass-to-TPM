# lastpass-to-TPM
Converts lasspass export files (lastpass_export.csv) and convert them to a team_password_manager_import.csv 

Steps

1. Export passwords from last pass
  
    Export from the LastPass browser extension

    Open your LastPass browser extension by clicking the LastPass icon in the browser toolbar and log in to your account.

    Open the Account tab and select Fix a problem yourself and choose Export vault items. 

    Enter your LastPass Master Password and select Continue.

    A CSV file with your LastPass items is downloaded to your device. (lastpass_export.csv)

2. chmod +x lastpassToTPM.py
   
4. Place your lastpass_export.csv in the same directory.

5. Run the script using "python lastpassToTPM.py" 
