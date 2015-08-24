import os
import re
import argparse


message = 'This is a static, archived version of a site created for Digital Humanities 101 at the University of California, Los Angeles, in Fall 2014'
programLink = '<a href=\"www.google.com\"> UCLA Digital Humanities Program</a>'
syllabusLink = '<a href=\"www.google.com\"> Syllabus for DH101</a>'
newDiv = '<div style=\"position:fixed;left:0;top:0;width:100%!important;height=20px;background-color:#FF6A6A;\">'+message+ ' '+programLink+ ' '+syllabusLink+'</div>'


def main(message, links):

	#compose the list of links
	if links:
		composedLinks = ['<a href=\"'+link[1]+'\">'+link[0]+'</a>' for link in links]


	#compose arguments into the message
	newDiv = '<div style=\"position:fixed;left:0;top:0;width:100%!important;height=20px;background-color:#FF6A6A;\">'+message+' '+' '.join(composedLinks)+'</div>'

	for root, dirs, files in os.walk('.'):
		for ffile in files:
			if ffile.endswith('.html'):
				with open(os.path.join(root, ffile), 'r') as htmledit:
					print os.path.join(root, ffile)
					text = re.sub(r'(<body[^>]*>)', r'\1\n'+newDiv, htmledit.read())
					htmledit.close()
					with open(os.path.join(root, ffile),'w') as htmlwrite:
						htmlwrite.write(text)
						htmlwrite.close()
					
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Insert a simple banner into each html file in the given directory and all subdirectories it contains. Intended for use with websites archived using httrack or similar.')
	
	parser.add_argument('message', type=str, help='The main banner message')
	parser.add_argument('--link','-l', type=str, nargs=2, action='append', help='Optional link(s) to be added after the message. Format is \"-link linktext linkurl\". So if we wanted to add two links to Google to the end of our message we would include two -link arguments like so: -link google1 www.google.com -link google2 www.google.com ')

	args = parser.parse_args()

	print args.message
	print args.link

	main(args.message, args.link)