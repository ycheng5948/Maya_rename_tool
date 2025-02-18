# Maya_rename_tool
**Making renaming elements in Maya easily and quickly**

![UI](https://github.com/user-attachments/assets/77afc9e7-4326-41e1-b89d-7e0f52276cbe)

Also have a quick tutorial on Youtube:<br/>
  <a href="https://www.youtube.com/watch?v=ggXCXy8W468"><img src="https://img.youtube.com/vi/ggXCXy8W468/0.jpg" alt="IMAGE ALT TEXT"></a><br/>
  https://www.youtube.com/watch?v=ggXCXy8W468
<br/>

A personal project of creating a Maya tool to rename multiple elements back in 2022/2023.<br/>
Perfect for my character rig that has "too many fingers."<br/>
Also a great practice for me to build a UI in Maya so it's easier to navigate and looks prettier. ¯\\\_(ツ)\_/¯

Fastest way:<br/>
Simply copy and paste the code to a new tab in Maya Script Editor.<br/>
Select all and middle-mouse-button drag the code to the desired shelf for quick access.

<br/>----------<br/>

Or the slower but more tidier way:<br/>
1. Delete or comment out the last line at the end of the code
```
#IN Maya
rename_tool_UI.rename_tool() #comment this line out
```

2. Create a `rename_tool_UI.py` file and place it in your desired script folder, which might look a bit like: 
`C:\Users\user\Documents\maya\$MAYA_VERSION\scripts\$SCRIPT_FOLDER\rename_tool_UI.py`<br/>
3. In Maya Script editor, type or copy and paste the following:
```
from $SCRIPT_FOLDER import rename_tool_UI
rename_tool_UI.rename_tool()
```
> Make sure that the `$SCRIPT_FOLDER` has been changed to whatever you've named your script folder
> Remember to run `reload(rename_tool_UI)` in Maya Script Editor if you made any changes to the .py file

## Features

- **Quick Selection**<br/>
  Select specific elements within your current selection
  > Ideally, the quick selection is used to filter certain elements within a group<br/>
  > `select hierarchy` button is mainly made for adding the side to elements in the group or for joint selection, since most of the time only the parent joint gets selected from the `viewport`

- **Suffix and Prefix**<br/>
  Customizing names and adding it as prefix or suffix
  
- **Quick Sides**<br/>
  Adding sides as prefixes or suffixes to the element(s)
  > Both prefixes and suffixes on either side will be labeled in caps

- **Quick Sufix (type)**<br/>
  Adding common suffixes for the selected element(s)
  
- **Rename**<br/>
  Specify a certain name and decide how the elements should be sorted in
  If more than one element is selected but an order isn't selected (the `-` option from the dropdown menu), the new names would follow Maya's default order system
  > `Numeric_0` order would add the number `0` at the end of the first selected element, while `Numeric_1` begins with `1`<br/>
  > `Alphabetic` is a two-letter-based system that would run from `A` to `Z` and continue with `AA`, `AB`, `AC`, ... `ZZ`<br/>
  >> ***Consider a different way of labeling if you have more than `676`(26^2) elements selected**

- **Check**<br/>
  Check the desired name before hitting `Rename`
