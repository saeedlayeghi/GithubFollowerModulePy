# GithubFollowerModulePy
A basic module that makes it easy to see how many followers a specific github account has. ```python3+```
Uses proxies once you paste in your proxies in ```proxies.txt``` if you do not want to use proxies just leave the file empty.

# How to use
Copy 'followermodulegithub.py' file to the same directory as your Python script.
```python
# You can import it into your Python tool like:

import asyncio
import followermodulegithub

asyncio.run(followermodulegithub.run(urlquery='Z3NTL3'))
# Returns the amount of followers the user Z3NTL3 has!
# Output: 47

# Error Handling
# If failes it wont throw a error it would return integer 456 so make if statements to catch error for int 456
# Example:

d = asyncio.run(followermodulegithub.run(urlquery='Z3NTL3'))
if d == 456:
  print('err')
else:
  pass # no err

# Z3NTL3 can be replaced with the queu of the github profile name. Dont parse https://github.com/Z3NTL3 only the github profile name 
```
# Required Modules
``bs4`` ```pip3 install bs4```<br>
``requests`` ```pip3 install requests```<br>
