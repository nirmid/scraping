# How to run the program ? 

In the main directory of the project run in the terminal:

```bash
python main.py
```
The program will run and create an "out" directory, in which all the results files will be put

## How to add another marketplace ?

One should implement a Class of WebScrap specific for the marketplace

## Questions after project

What would have you done differently, if eBay blocked your IP?

Illegal approach: I would have used a Proxy or a VPN.

Legal approach: Use Ebay API.


How would you improve the process in order to retrieve more items?

using AWS EC2 instances and hadoop or spark framework in order to devide the workload between several computers.  


In what ways could you improve the process through the application of AI?

Could improve by idetenifying the elements in the marketplace website in order to scrape.
For example to train a model so that it can extract the elements that are needed in order to scrape, so configuring a new marketplace would be much easier and faster.