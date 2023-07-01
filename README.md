# Your own personal Mock HTTP server 

Today web development invovles writing API and consuming APIs.  As consumers of
API, we tend to quickly use the inbuilt library of our programming language (I am looking at you Axios and requests) slap something together, get some API data back and are happy.  Well... until the API server you are using returns something other than HTTP 200 OK.  

Welcome to real world APIs development where a 429 means you are coming on too
fast :-).   So now we have the uneviable task of dealing with
403/500/429/301 and so on. So the purpose of the personal mock HTTP server is
simple. It allows us to...

1. Test our client code reacts to various HTTP response codes 
2. Test how our client code behaves with a "bad" server that throws an error code with a random delay.
3.  Be able to do all this on an Aeroplane flight with no Wifi (otherwise you have http://httpstat.us/ already) 

With these constraints in mind I wrote a quick utility in Python called []HTTPServerMock](https://github.com/vivekhub/httpservermock). That can run locally on your computer and provide various HTTP response codes based on the URL.  It has two end points

1.  ```/code/XXX```  returns XXX as the response code for the request.
2.  ```/slow/XXX```  After a random wait for N seconds,  returns the XXX as response code for the request.

I built this on top of the builtin ```http.server``` module and using the ThreadingHTTPServer.  The source code is quite self explanatory.

What other features do you want on your HTTP mock server?  Drop me a note.


# Running the server

Run it as ```python3 HTTPserverMock.py```.  


