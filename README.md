# Senior-Research
Project for Completing my Degree

Uses Python

My Senior Project Research Topic: Analyzing Cookie Data

Explanation of Research <br>
The process for collecting the cookie data for this research was conducted very sequentially. Data was collected from five websites of five different website domains: .gov, .org, .com, .edu, and .net. For a total of 25 websites. 

One of the variables being closely observed was the last accessed and creation time attributes of the cookie. This was done in hope that if a cookie's last accessed time varied from the creation time it would suggest that the cookie was accessed from a different website. For this to hold true all the cookie data needed to be wiped before beginning the data collection process. Then once the process of data collection began, there could be no mistakes upon accidental revisitation of a website after the initial data collection. 

This process was vigorously precise. Example: Website 1 was visited. The data in the cookies.sqlite file was saved to a text file. Website 2 was visited. The cookies.sqlite file was saved to a new text file. And So On... 

Explanation of Code Files <br>
The cookie data was saved in various files and formats due to the complexity of the data collection. This led to a few different methods for analyzing the data files. 
<br>fileReader.py all the data was combined into one file manually then processed (this did not seem the most efficient).<br>
Data_manipulation.py was an attempt at processing the data better. This code required the data to be manually combined into the 5 groups for processing. (getting better I think) <br>
Data_manipulation_V2.py was designed to process each file individually. 

<br>Data Being Processed<br>
One of the codes' main properties is converting the Unix timestamps data of cookie attributes into human readable time. The calculation of whether the cookies were persistent or not was also calculated. Persistent cookies are cookies which last longer than the browsing session. The persistency of a cookie is determined by the expires attribute. If the expires attribute is set to a time in the future than the cookie is persistent. If the cookie was a persitent cookie, then the lifetime of the cookie was also calculated by the difference of (expired time - creation time). 

<br>NOTE: The research and development of this code is far from complete.
