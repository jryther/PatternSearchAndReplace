#Project 4
#Josh Ryther
#02/17/20

import re

#Search string
lorem_ipsum = '''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor. 
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo. 
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida 
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum 
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum 
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus 
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''

pattern= "[^a-zA-Z]"
#B-Searching for sequences and ranges
#C-Search using a wildcard
results= re.findall(pattern, lorem_ipsum)
print(len(results))

pattern2= 'sit[-:]amet'
#C-Search using a special character
occurrences_sit_amet= re.findall(pattern2, lorem_ipsum)
print(len(occurrences_sit_amet))

replace_results= re.sub(pattern2, 'sit amet', lorem_ipsum)
#A-Searching for literal characters
occurrences_sit_amet= re.findall('sit amet', replace_results)
print(len(occurrences_sit_amet))