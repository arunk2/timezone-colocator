# Timezone Colocator

Timezone colocator - Identify timezones which can be co-located for optimal resource utilization

## Requirement
It is normal practice most of the SaaS products works completely on cloud 24/7/365. Most of the B2B products among them work during office hours. There is every reason one might think to reuse the the resources (like cloud servers), which are used only during working hours by colocating the data of customer in same servers. 

### Important:
Such a sharing/colocation is possible only when we are sure that their operating time are mutually exclusive

## Solution
The timezone across the globe is well known and we can identify the non-overlapping timezones easily with a program. For a given timezone one can easily list the timezones, which can be used to colocate.

## Usage
```
$ python colocator.py  <<<TIME_ZONE>>>

example:

$ python colocator.py  "Asia/Kolkata"
```
