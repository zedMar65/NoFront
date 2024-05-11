# NoFront
---
### Description

NF is a free open-source tool to make low level internet communication simple and bare bone and as the name suggests it has NO front end
It does not seek to replace www but could be used as a simpler, non centralized solution for smaller, more secure networks

---
### Usage

#### Console
```
.\Console
$NfConsole:C:\> help
command structure:
Command -set_configure configure [-set_not_required_configue] not_required configure
<- General ->
ls <- lst files
cd <- move between dirs
run -f File.nf [-c] configures <- run an nf file
compile -f File.nf <- compile an nf file
name -v variable -m name_of_variable <- makes name_of variable same as variable (can be used to name ips)
set -v variable_name -val value  <- sets variable_name to value
<- Net ->
connect -ip ip [-p] pass <- establish connection to a server
post -ip ip [-p] pass -m messsege <- sends data to ip with pass
get -ip ip [-p] pass [-c] configures <- sends a request to ip
ping -ip <- pings ip
api -ip ip -c configures <-sends rest api request
<- Moderation ->
break <- breaks code/connection/request
mute -ip ip <- mutes ip
ban -ip <- nans ipfrom your device
<- Database ->
only with scripts
```
```
-val float/int/char/string/array/object
-m str messege formated as "{a}{b}".format(a=var1,=b=var2)
-p password
-ip desired ip address or name or web link
-f name the file to run
-c configures for the nf file
```

#### Coding
```
Some Code >> File.nf
python Compiler.py -f File.nf
.\File
```
#### Syntax


---

### todo
* add console
* add coding
* add compiler
* write language documentation