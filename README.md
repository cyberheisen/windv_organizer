# windv_organizer
A script to move windv output files into a year/month/day folder structure

[WinDv](http://windv.mourek.cz/) is a legacy Windows application used to capture video from DV camcorder devices. The default output format for the capture files provides a date and timestamp as part of the filename.  This simple script will iterate through the output files, parse the date information, and create/move the files appropriately to a folder structure following the format: `/year/month/day`.

I put this script together quickly to solve a specific need and didn't add much in terms of error correction and bug fixes.  I'm posting it here to help others who may have a large number of windv files they want to organize better.  

**USE AT YOUR OWN RISK**


*much appreciation to Petr Mourek, the author of [WinDv](http://windv.mourek.cz/), for providing free software to digitize my family's old DV home movies.*
