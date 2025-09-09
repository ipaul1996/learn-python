"""
In today's world of web application many I/O operations takes a lot of time.
In our applications if we run them sequentially, we will see a compund performance
impact. For example, if an application needs to download 100 web pages or 100 queries
each of which takes 1 sec to execute, our application would take at least 100 sec to
respond. However, if we were to exploit concurrency and start the downloads and wait 
simultaneously, in theory, we could complete these operations in as little as 1 second. 
Python asyncio library has been designed to handle these highly concurrent workloads.

"""