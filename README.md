# pypingd
A Python Daemon for Pinging Things

## Project Goals
Sometimes you just need to ping things and get a summary of what is reachable and what isn't.

Let's start with what a configuration file might look like:

```
[this.host]
frequency=3 # Ping every 3 minutes
down=1 # Declared down if 1 ping test fails

[that.host]
frequency=1 # Ping every minute
down=5 # Declared down if 5 consecutive ping tests fail

[8.8.8.8]

[8.8.4.4]
```

For `this.host` the daemon will ping `this.host` (FQDN) every 3 minutes.  Let's say for release 1.0 the daemon sends 5 ICMP ECHO_REQUESTs.  If 5 ICMP ECHO_RESPONSEs come back then the test passes.  

If the test fails then the host is declared unavailable and an alert will be noted on the status page.

Now, for `that.host`, we will ping every minute.  However, only after 5 consecutive tries, if the pings fail, will the host be marked unavailable.

## Examples




