#This script is not any general purpose script.

Well the purpose of this script was that my ISP used a transparent proxy hosted at http://10.10.2.1

which required authentication and will logout if remained inactive for 15 minutes.

But there was some problem with their server they tend to reset my connection even if i am using internet.

I tried talking to the person who installed my connection but i don't think he could do it cause the proxy

was built by third party agency.

So i took it to myself and thought of it as the opportunity to learn selenium module which i was trying for a
long time.


After developing the script i have to run it continuously.

So there was a problem since i was using phantomjs webdriver which created the instance of phantomjs process everytime the script runs .

So after sometime there was so many processes with name phantomjs resulting in computer hang after sometime therefore i used :-

```
   killall phantomjs
```   
which killed every process with name phantomjs.
