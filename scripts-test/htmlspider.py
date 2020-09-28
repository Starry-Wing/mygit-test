import wget

def craw(url,fname):
	wget.download(url,fname);

def main():
	url=str(input('url:'))
	fname=str(input('fname:'))
	craw(url,'d:/test/'+fname+'.html')
	#print(fstr)

main()