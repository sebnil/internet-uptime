internet-uptime
=======================================

Small script to check if my internet provider is providing me with internet. 

## How to use
  1. Scheduled to run quite often (every minute, every 15 minutes or whatever). I use a Jenkins script for this.
  2. Parse the output in xxxx-xx-xx uptime.csv


```bat
python internet-uptime.py
```

Will output into 2019-02-10 uptime.csv (current date obviously)
```
1549787883.520305,2019-02-10T08:38:03,1
```


 
## Support my creation of open source software:
[![Flattr this git repo](http://api.flattr.com/button/flattr-badge-large.png)](https://flattr.com/submit/auto?user_id=sebnil&url=https://github.com/sebnil/internet-uptime)

<a href='https://ko-fi.com/A0A2HYRH' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://az743702.vo.msecnd.net/cdn/kofi2.png?v=0' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>