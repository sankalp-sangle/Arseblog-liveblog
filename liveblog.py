import requests, bs4, sys, time
def refresh(cnt):
	url = 'http://live.arseblog.com/index.php/liveblog/index'; #Standard url for arseblog liveblog
	res = requests.get(url); # get source code of page
	soup = bs4.BeautifulSoup(res.text); # make a bs object
	livecontent0 = soup.select('.subheader p');
	print(str(livecontent0[0].getText() + "\n"));
	print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n");
	livecontent1 = soup.select('li .update-header');# get p elements enclosed in li tags
	livecontent2 = soup.select('li .update-body');# get p elements enclosed in li tags
	cnt=len(livecontent1)-cnt;#Resetting value of cnt. Doing this so as to ensure no duplicate entries are printed.
	for i in range(cnt-1,-1,-1):
		print(str(livecontent1[i].getText()+"\n"));
		print(str(livecontent2[i].getText()+"\n"));
		print(str("________________________________________________________________________\n"));
	return len(livecontent1);
count=0;
while True:
        count = refresh(count);
        time.sleep(45);


