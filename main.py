import os
os.makedirs('/output', exist_ok=True)
open('/output/entry.txt','w').write("Burned 40 minutes debugging a build that was fine. I'd been editing a copy in /tmp the whole time.")
