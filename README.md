# GithubFollowerModulePy
Een basic module die ervoor zorgt dat je gemakkelijk kan zien hoeveel volgers een specifiek github account heeft.

# How to use
Copy 'followermodulegithub.py' file to the same directory as your Python script.
```python
# You can import it into your Python tool like:

import asyncio
import followermodulegithub

stdout = asyncio.run(followermodulegithub.run(urlquery='Z3NTL3'))
print(stdout)
# Returns the amount of followes the profile has!
# Output: 47

# Z3NTL3 can be replaced with the queu of the github profile name. Dont parse https://github.com/Z3NTL3 only the github profile name 
```
