import requests, bs4, sys, time, os
test = "init"
def refresh(cnt):
        url = 'http://live.arseblog.com/index.php/liveblog/index'; #Standard url for arseblog liveblog
        global test
        res = requests.get(url); # get source code of page
        soup = bs4.BeautifulSoup(res.text); # make a bs object
        livecontent0 = soup.select('.subheader p');
        if count != 0 and test != livecontent0[0].getText():
                print("UPDATE UPDATE UPDATE UPDATE UPDATE UPDATE");
                print(str(livecontent0[0].getText() + "\n"));
                for i in range(5):
                        duration = 1  # second
                        freq = 1500  # Hz
                        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
                        if livecontent0[0].getText()[-2:] == "1)":
                                os.system("spd-say 'Arsenal Goal Arsenal Goal'")

        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n");
        livecontent1 = soup.select('li .update-header');# get p elements enclosed in li tags
        livecontent2 = soup.select('li .update-body');# get p elements enclosed in li tags
        cnt=len(livecontent1)-cnt;#Resetting value of cnt. Doing this so as to ensure no duplicate entries are printed.
        for i in range(cnt-1,-1,-1):
                print(str(livecontent1[i].getText()+"\n"));
                print(str(livecontent2[i].getText()+"\n"));
                print(str("________________________________________________________________________\n"));
        test = livecontent0[0].getText();
        return len(livecontent1);
count=0;
while True:
        count = refresh(count);
        time.sleep(45);
