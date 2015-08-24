# archve-header
A simple python script to add a banner to sites archived with tools like HTTrack.

Place in the root directory of the archived site, and run with Python 2.7.x.

Takes two arguments:

1) A mandatory positional argument that contains the banner message.
2) An optional list of links (-l or --link) that will be appended after the above message. The link format is: --link linktext linkurl

Example:
python addheader.py "This is a test message" --link google1 www.google.com --link google2 www.google.com  
