# Overview
This guide gives a brief overview of ioxclient and its usage.

## What is ioxclient?

**"ioxclient"** is a command line tool provided as part of Cisco IOx SDK. This utility is primarily meant for assisting application development for Cisco's IOx platforms. It aims to increase developer productivity by providing easy to use CLI to perform most common operations such as :

* App life cycle management [install, activate, deactivate, uninstall, start, stop, upgrade etc.,]
* Application troubleshooting [view and manage application logs]
* Life cycle management and troubleshooting for IOx services
* Cartridge management [install, uninstall, view info, upgrade etc.,]
* Platform management [view platform information, health, platform logs, techsupport snapshots, network information etc.,]
* Provides a notion of profiles that captures connection information to an IOx device and switch between multiple profiles.

It interacts with the software (CAF) running in IOx platform via well defined REST APIs.

# Installing ioxclient

ioxclient is typically distributed along with IOx SDK. It is also available as a stand alone, single, distributable binary for 32 and 64 bit platforms of MAC, Windows and Linux operating systems.

Please download the right version for your development machine. Once downloaded, it is advisable to mark it as executable (chmod 777) and place it somewhere it system path for easier usage.

Below is an overview of the commands supported by the tool. They will be described in more detail in the following sections.

# Using ioxclient

## General guidelines

* ioxclient has commands and subcommands.
* Each command/subcommand may require you to pass appropriate parameters
* Some commands may also show up an interactive commandline wizard where appropriate values needs to be keyed in.
* Each command/subcommand also has a "short name" as well. You can use the full command name or the short name.  Below is an overview of top level commands. The short names are also shown:

```
~$ ioxclient
NAME:
   ioxclient - Command line tool to assist in app development for Cisco IOx platforms

USAGE:
   ioxclient [global options] command [command options] [arguments...]

VERSION:
   1.4.5.0

AUTHOR:
  Cisco Systems - <iox-support@cisco.com>

COMMANDS:
   debug, dbg           Set debug to on or off
   errorcodes, err      Get ioxclient error code to description map in JSON format
   showguide, guide     View ioxclient reference guide
   application, app     Manage lifecycle of applications
   service, svc         Manage lifecycle of services
   package, pkg         Package an iox application/service/cartridge. Produces an IOx compatible archive
   platform, plt        Manage IOx platform
   cartridge, cr        Create/Delete/List cartridges
   fogportal, fogp      FogPortal operations
   profiles, pr         Profile related commands
   docker, dkr          Commands for using docker tools for IOx app development
   layer, lr            Manage lifecycle of application layers
   show, sh             Show Smart License information
   license, lic         Execute licensing commands
   call-home, call      Set destination address for Smart License callhome
   help, h              Shows a list of commands or help for one command

GLOBAL OPTIONS:
   --profile                    Override the profile to be used for the current command
   --non-interactive-mode       execute the command in non-interactive mode
   --help, -h                   show help
   --generate-bash-completion
   --version, -v                print the version

```

For instance,

```
$ ioxclient showguide
<-- is same as -->
$ ioxclient guide
```

* Whenever the tool asks for inputs, a default value is indicated in square brackets ([]). If you are okay with the default value, just hit enter and the tool will use the value shown as the default. For example:

```
Your IOx platform's port number[8443] :   <= Hitting enter will cause the port to be 8443.
```

* To get help, simply type:

```
$ ioxclient -h OR ioxclient --help
```

* To get help for a specific command/subcommand :

```
~$ ioxclient  application
NAME:
   ioxclient application - Manage lifecycle of applications

USAGE:
   ioxclient application command [command options] [arguments...]

COMMANDS:
   list, li		List installed applications on the system
   run, r		Install, activate and start the application
   install, in		Install an application
   start, sta		Start an installed application
   stop, stp		Stop an installed application
   restart, rs		Restart an installed application
   status, sts		Get current status of an installed application
   info, inf		Get info pertaining to an installed application
   activate, act	Activate application
   deactivate, deact	Deactivate Application
   uninstall, unin	Uninstall an installed application
   upgrade, upgr	Upgrade an application
   getconfig, getconf	Get config information of an installed application
   setconfig, setconf	Set config information for an installed application from the specified file
   getloginfo, loginf	Get log files info for an installed application
   taillog, tllg	Get last n lines from a specific log file
   console, con		Connect to the console of the application
   downloadlog, dllg	Download application log files
   metrics, met		Get resource usage metrics of installed applications
   help, h		Shows a list of commands or help for one command

OPTIONS:
   --help, -h			show help
   --generate-bash-completion


~$ ioxclient  application install
NAME:
   install - Install an application

USAGE:
   command install [command options] <application_id> <archive or project dir> [docker_image]

DESCRIPTION:
   
Install uploads the app or service to the device, reserves application 
id and optionally resolve service dependencies. Specify activation-payload 
if you want dependent services to be started during install
if you want to install an application by using IOx layers, please look below for command usage.
    ioxclient application install [--rsa-key<> --cert<>] --layer appid <project_dir> <docker_image>


OPTIONS:
   --layers, -l             Use this flag to install an application using IOx layers. When this option is specified all the other options are ignored
   --resolve-dependencies, --rd     Use this flag to activate automatic resolution of dependencies
   --service-source, --src      Use this flag to specify the source from which the dependent services will looked for
   --service-activation-payload, -p     Use this flag to pass activation payload for activating services
   --rsa-key, -k            Use this option to specify a RSA key in PEM format to sign the package
   --certificate, -c            Use this option to specify a x509 Certificate in PEM format
   --skip-signing           Use this option to skip package signing


```

* Notation for command parameters.
 * any parameter indicated within <> is mandatory
 * any parameter indicated within \[\] is optional. If it is not specified, a default value is assumed. The defaults are indicated in the "help" for that command.
  * Mandatory parameter example:


```
~$ ioxclient  application install myapp
Insufficient Args.

NAME:
   install - Install an application

```

   * Optional parameter example:

```
~$ ioxclient  platform events -h
NAME:
   events - Get platform events

USAGE:
   command events [fromseq] [toseq]. If not specified, default value is -1

```


## Configuring ioxclient

The first time ioxclient is used, a wizard will be shown asking a few questions based on which ioxclient will configure itself. It will also create a "default" profile that captures connection information with an IOx device. Creating and using additional profiles will be described in further sections.

```
~$ ioxclient
Config file not found :  /home/hvishwanath/.ioxclientcfg.yaml
Creating one time configuration..
Your / your organization's name : cisco
Your / your organization's URL : www.cisco.com
Your IOx platform's IP address[127.0.0.1] : 72.163.111.112
Your IOx platform's port number[8443] : 8443
Authorized user name[root] : appdev
Password for appdev :
Local repository path on IOx platform[/software/downloads]:
URL Scheme (http/https) [https]: https
API Prefix[/iox/api/v2/hosting/]:
Your IOx platform's SSH Port[2222]: 22
Your RSA key, for signing packages, in PEM format[]: 
Your x.509 certificate in PEM format[]: 
Activating Profile  default

```

* The tool creates a default profile. Each profile has information about how to connect to a specific Cisco IOx platform.
* RSA key and corresponding x.509 certificate are optional. The key and certificate when provided will be used to sign the generated package.
* The profile data is stored in $HOME/.ioxclientcfg.yaml file. Do not attempt to manually edit this file. Use `ioxclient profiles` commands to manipulate profile related information. Described in detail in the sections below.

## Managing profiles

ioxclient facilitates working with multiple IOx devices. Connection information to each such device is stored as a profile. Any ioxclient command used, is always run in the context of the currently *active* profile.

Profiles can be managed via `ioxclient profiles` and its subcommands.

```
~$ ioxclient  profiles
Active Profile :  default
NAME:
   ioxclient profiles - Profile related commands

USAGE:
   ioxclient profiles command [command options] [arguments...]

COMMANDS:
   list, l	List all existing profiles
   show, s	Show currently active profile
   create, c	Create a new profile
   activate, a	Activate specified profile
   delete, d	Delete specified profile
   reset, rs	Reset profile data
   help, h	Shows a list of commands or help for one command

OPTIONS:
   --help, -h			show help
   --generate-bash-completion

```

### Creating a profile

If you want to interact with a new IOx device, add relevant information by creating a profile. Give a handy name to the profile so that it is easier to remember while switching between profiles.

```
~$ ioxclient  profiles create
Active Profile :  default
Enter a name for this profile : sandbox
Your IOx platform's IP address[127.0.0.1] : 192.168.3.1
Your IOx platform's port number[8443] :
Authorized user name[root] : appdev
Password for appdev :
Local repository path on IOx platform[/software/downloads]:
URL Scheme (http/https) [https]:
API Prefix[/iox/api/v2/hosting/]:
Your IOx platform's SSH Port[2222]: 22
Your RSA key, for signing packages, in PEM format[]: 
Your x.509 certificate in PEM format[]: 
Activating Profile  sandbox

```

* RSA key and corresponding x.509 certificate are optional. The provided key and certificated will be used to sign the generated package.
> Note: When a new profile is created, it automatically gets activated.

### Listing existing profiles

```
~$ ioxclient  profiles list
Active Profile :  sandbox
Profile Name :  default
	Host IP:  72.163.111.112
	Host Port:  8443
	Auth Keys:  YXBwZGV2OmFwcGRldg==
	Auth Token:
	Api Prefix:  /iox/api/v2/hosting/
	URL Scheme:  https
	RSA Key:
	Certificate:
Profile Name :  sandbox
	Host IP:  192.168.3.1
	Host Port:  8443
	Auth Keys:  YXBwZGV2OmFwcGRldg==
	Auth Token:
	Api Prefix:  /iox/api/v2/hosting/
	URL Scheme:  https
	RSA Key:  /home/dev/Documents/iox/key.pem
	Certificate: /home/dev/Documents/iox/cert.pem

```

### Show currently activated profile

```
~$ ioxclient  profiles show
Active Profile :  sandbox
Profile Name :  sandbox
	Host IP:  192.168.3.1
	Host Port:  8443
	Auth Keys:  YXBwZGV2OmFwcGRldg==
	Auth Token:
	Api Prefix:  /iox/api/v2/hosting/
	URL Scheme:  https
	RSA Key:  /home/dev/Documents/iox/key.pem
	Certificate: /home/dev/Documents/iox/cert.pem

```

### Activating a profile

```
~$ ioxclient  profiles activate sandbox
Active Profile :  default
Activating Profile  sandbox

```

### Deleting a profile

```
~$ ioxclient  profiles delete sandbox
Active Profile :  sandbox
Deleting profile  sandbox

```

> Note that deleting "default" profile is not supported.

```
~$ ioxclient  profiles delete default
Active Profile :  default
Cannot delete the default profile
If you want startover, use the 'reset' command instead

```

> Note: Editing an existing profile is not supported. If you would like to reuse an existing profile name, simply delete it and recreate it with desired values.

### Overriding profile for a given command

`ioxclient` commands operate in the context of the currently active profile. However, in some use cases you may want to use a specific profile for a given command without changing active profile. This can be achieved by passing a valid profile name to the global `--profile` option.

When `--profile` option is set, `ioxclient` will use the profile name passed to the option for the currently run command. After the execution of the command, the previously active profile will be restored back.

```
$ ./ioxclient --profile local application list
Currently active profile :  default
Overriding profile to local for this command
Activating Profile  local
Command Name: application-list
List of installed App :
 1. py         --->    RUNNING
Activating Profile  default

```


### Resetting config information

This removes the existing configuration information stored by the tool. After this command, just type `ioxclient` which will prompt for fresh config information.

```
~$ ioxclient  profiles reset
Active Profile :  default
Your current config details will be lost. Continue (Y/n) ? : Y
Current config backed up at  /tmp/hvishwanath/ioxclient291276906
Config data deleted.

```

> When reset is issued, the tool backs up the existing config into a temporary file. If you want to store it, make sure you copy the temporary file to a location you will remember.

## Application management

The following sections describe usage of ioxclient to manage applications. Below are the application management commands:

```
$ ./ioxclient  application
NAME:
   ioxclient application - Manage lifecycle of applications

USAGE:
   ioxclient application command [command options] [arguments...]

COMMANDS:
   list, li		List installed applications on the system
   install, in		Install an application
   local_install, lin   Install an application that is already present on the target device
   run, r		Install, activate and start the application
   start, sta		Start an installed application
   stop, stp		Stop an installed application
   restart, rs		Restart an installed application
   status, sts		Get current status of an installed application
   info, inf		Get info pertaining to an installed application
   activate, act	Activate application
   deactivate, deact	Deactivate Application
   uninstall, unin	Uninstall an installed application
   upgrade, upgr	Upgrade an application
   getconfig, getconf	Get config information of an installed application
   setconfig, setconf	Set config information for an installed application from the specified file
   logs, lgs		Manage log files
   cores, cores     Manage core files
   datamount, dm	Manage contents of application's data mount directory
   appdata, appdata	Manage files in the appdata directory under datamount
   console, con		Connect to the console of the application
   exec, ex     Execute a specific command directly in a container-based application
   metrics, met		Get resource usage metrics of installed applications
   help, h		Shows a list of commands or help for one command

OPTIONS:
   --help, -h			show help
   --generate-bash-completion

```

> Ensure that you have right profile activated.

### Packaging an application

`ioxclient` provides ability to package an already created application.

```
$ ioxclient package
NAME:
   package - Package an iox application/service/cartridge. Produces an IOx compatible archive

USAGE:
   command package [command options] <path_to_dir>

OPTIONS:
   --use-targz          Use this to use gz compression on package
   --skip-schema-validation Use this flag to skip package descriptor schema validation
   --layers, -l         Use this option to package application layers by specifying IOx layers directory
   --rsa-key, -k        Use this option to specify a RSA key in PEM format to sign the package
   --certificate, -c    Use this option to specify a x509 Certificate in PEM format
   --skip-signing       Use this option to skip package signing

```

```
/home/dev/Documents/iox/pkg$ ioxclient package -k ../key.pem -c ../cert.pem .
Currently active profile :  local
Command Name:  package
Using rsa key and cert provided via command line to sign the package
Checking if package descriptor file is present..
Validating descriptor file /home/dev/Documents/iox/pkg/package.yaml with package schema definitions
Parsing descriptor file..
Found schema version  2.5
Loading schema file for version  2.5
Validating package descriptor file..
File /home/dev/Documents/iox/pkg/package.yaml is valid under schema version 2.5
Created Staging directory at :  /tmp/198111141
Copying contents to staging directory
Checking for application runtime type
Couldn't detect application runtime type
Creating an inner envelope for application artifacts
Generated  /tmp/198111141/artifacts.tar.gz
Calculating SHA1 checksum for package contents..
Parsing Package Metadata file :  /tmp/198111141/.package.metadata
Wrote package metadata file :  /tmp/198111141/.package.metadata
Root Directory :  /tmp/198111141
Output file:  /tmp/170359488
Path:  .package.metadata
SHA1 : 09679c5d4b25e4673f1e7d4b7dd2c725a8d5d6cf
Path:  artifacts.tar.gz
SHA1 : 9633a0126b6f02350fe6b5bc185e47acc56abc04
Path:  package.yaml
SHA1 : 7c0a205ff916215538f85e9ff3b34babaac39f0f
Generated package manifest at  package.mf
Signed the package and the signature is available at package.cert
Generating IOx Package..
Package generated at /home/dev/Documents/iox/pkg/package.tar

```

* Options RSA key and certificate should be used to provide a private key and cert pair to sign the package.
* The provided key and certificate pair will take precedence over the ones specified in the active profile

> In the above command "." is supplied - indicating that package the current directory.
> ioxclient ensures that the path supplied for package command contains all the required files before packaging.
> Refer to IOx package documentation for more details about the structure and layout of the package.
> Successful completion of this command creates a "package.tar(.gz)" that can be used for installation on your IOx device.

### Installing an application

```
~/projects/sample-apps-v2/paas/python/nettest$ ioxclient  application install nettest ./package.tar.gz
Currently using profile :  default
Command Name: application-install
Installation Successful. App is available at :  https://127.0.0.1:8443/iox/api/v2/hosting/apps/nettest
Successfully deployed
```

### Installing an application with dependent IOx Services

A user who wants the dependencies of the application to be taken care of, can specify the ioxclient to resolve dependencies in two methods -

There are three flags available to achieve this functionality -

* **--resolve-dependencies or --rd** : specify this flag to enable automatic dependency resolution
* **--service-source or --src** : specify a folder containing service bundles to use them for dependency resolution. If no folder is specified, fogportal will be searched for the required packages.
* **--service-activation-payload or --p** - where the path of the activation payload for services is specified.

#### Resolve Service Dependencies from the Fog portal -
 Here, the installer searches for the required services from the Fog portal, downloads them into a temp folder and installs, activates using the activation payload, and runs them in order to install the required application


```
~/projects/sample-apps-v2/paas/python/nettest$ ioxclient  application install nettest ./package.tar.gz --resolve-dependencies --service-activation-payload activation-file.json
```

Output -

```
~$ioxclient app in oauth sample-oauth.tar --rd --p test_resources\nat-activation.json
Currently active profile :  vm211
Command Name: application-install
Resolve Dependencies flag specified by user
Reading  sample-oauth.tar ......
Parsing  sample-oauth.tar .yaml
map[sample-app:{{{sample-app} { paas {[{1 true urn:cisco:system:service:nbi}]} {50}} {[]}} false 2 sample-oauth.tar -1 false}]map[]map[urn:cisco:system:service:nbi:{{1 true urn:cisco:syste
Checking CAF for the already existing services
Existing services in CAF are -
Resolving dependencies from Fog portal
Checking fog portal for the dependencies that are not in CAF
Requesting  http://10.78.106.35:8090/api/v1/fogportal/service_bundles/
Requesting -   http://10.78.106.35:8090/api/v1/fogportal/service_bundles/
The following services are available in the Fog portal
1 .  Middleware Message Broker
2 .  middleware-core
Saving current configuration
Constructing a Dependency tree for sample-app
|_sample-app
|_|_middleware-core
|_|_|_Middleware Message Broker
Checking CPU architecture compatibility of the service  Middleware Message Broker
Middleware Message Broker  is present in the FogPortal
Downloading  Middleware Message Broker ....
200 OK

C:\Users\cheb\AppData\Local\Temp\185222e322175b49ebe62449798d47f48dbe449932d5b752e2c7a2321031952b with 3319559 bytes downloaded
Service bundle to be stored in  C:\Users\cheb\AppData\Local\Temp\185222e322175b49ebe62449798d47f48dbe449932d5b752e2c7a2321031952b
Installation Successful. Service is available at : https://10.78.106.211:8443/iox/api/v2/hosting/service-bundles/MiddlewareMessageBroker
Successfully deployed
Payload file : test_resources\nat-activation.json. Will pass it as application/json in request body..
Service MiddlewareMessageBroker is Activated
Service MiddlewareMessageBroker is Started

Resolved status of  Middleware Message Broker  -  true
middleware-core  is present in the FogPortal
Downloading  middleware-core ....
200 OK

C:\Users\cheb\AppData\Local\Temp\9b22331ad31f16c00c108f7c4de8cda0796304632664175cbece439d18a21ca8 with 13270313 bytes downloaded
Service bundle to be stored in  C:\Users\cheb\AppData\Local\Temp\9b22331ad31f16c00c108f7c4de8cda0796304632664175cbece439d18a21ca8
Installation Successful. Service is available at : https://10.78.106.211:8443/iox/api/v2/hosting/service-bundles/middlewareCore
Successfully deployed
Payload file : test_resources\nat-activation.json. Will pass it as application/json in request body..
Service middlewareCore is Activated
Service middlewareCore is Started

Resolved status of  middleware-core  -  true
Installation Successful. App is available at : https://10.78.106.211:8443/iox/api/v2/hosting/apps/oauth
Successfully deployed
```

#### Resolve Service Dependencies from the folder -
 In this case, the specified folder is searched for the required dependencies and the ones required are installed, activated and started in order to install the application.

```
~/projects/sample-apps-v2/paas/python/nettest$ ioxclient  application install nettest ./package.tar.gz --resolve-dependencies --src path/to/service/bundles --service-activation-payload activation-file.json
```

Output -

```
~$ioxclient app in apc package.tar.gz --rd localrepo --f path/to/folder --p activation-file.json
Currently active profile :  vm211
Command Name: application-install
Resolve Dependencies flag specified by user
Reading  test_resources\fog-apps\apcargo-fog-app-master-72c451defc2c1f2e33bcc4ef24745e0b4019dcb0\package.tar.gz ......
Reading .yaml of  package.tar.gz
Checking CAF for the already existing services
Existing services in CAF are -
Flag for Local repository dependency resolution recognized
Searching the specified local repo for the dependencies..
Unpacking  dartBroker.tar.gz
Reading  test_resources\svc-bundles\dartBroker.tar.gz ......
Reading .yaml of  dartBroker.tar.gz
Unpacking  mw-package.tar.gz
Reading  test_resources\svc-bundles\mw-package.tar.gz ......
Reading .yaml of  mw-package.tar.gz
Resolving dependencies for  APCargo
|_Resolving  APCargo
|_|_Resolving  iox:middleware:core
|_|_|_Resolving  Middleware Message Broker
Installation Successful. Service is available at : https://10.78.106.211:8443/iox/api/v2/hosting/service-bundles/MiddlewareMessageBroker
Successfully deployed
Payload file : test_resources\nat-activation.json. Will pass it as application/json in request body..
Service MiddlewareMessageBroker is Activated
Service MiddlewareMessageBroker is Started

Resolved status of  Middleware Message Broker  -  true
Installation Successful. Service is available at : https://10.78.106.211:8443/iox/api/v2/hosting/service-bundles/ioxMiddlewareCore
Successfully deployed
Payload file : test_resources\nat-activation.json. Will pass it as application/json in request body..
Service ioxMiddlewareCore is Activated
Service ioxMiddlewareCore is Started

Resolved status of  iox:middleware:core  -  true
Installation Successful. App is available at : https://10.78.106.211:8443/iox/api/v2/hosting/apps/apc
Successfully deployed
```

### Installing an application package already available on the device

If the application package is too large to transfer over http, please copy the package to the device by other means and use the below command to install the application

```

dev@dev-VirtualBox:~$ ioxclient application local_install 
Insufficient Args.

NAME:
   local_install - Install an application that is already present on the target device

USAGE:
   command local_install <application_id> <path_to_package_on_the_platform>

dev@dev-VirtualBox:~$ ioxclient application local_install test /home/iox/package.tar
Currently active profile :  caf
Command Name:  application-local_install
Attempting to install app already available on the platform at /home/root/iox/package.tar
Installation Successful. App is available at : https://10.41.51.109:8443/iox/api/v2/hosting/apps/test 
Successfully deployed
dev@dev-VirtualBox:~$ 
 
```

### Activating application

An application has to be activated before starting. At the time of activation, the developer/administrator has to supply the right resource mapping based on what the application needs.

> Refer IOx application states documentation for more information about application states.
> Refer IOx application descriptor documentation for more information about application resource requirements.

For ex, the above installed app asks for network interface. That interface has to be associated with the right logical network available on the device. Similarly, you could assign the right device, map external ports etc.,

```
$ ./ioxclient  application activate
NAME:
   activate - Activate application

USAGE:
   command activate [command options] <application_id>

DESCRIPTION:

Activation of an app causes the resources to be committed.
Pass a JSON file with the right payload. Here is a sample:

* port_map: The mode (auto, 1to1) governs how the ports are mapped.
* If no mode is given, auto is the default
* A mode can be specified, and you can still set a custom port mapping for individual/range of ports that overrides the mode settings.
{
	"resources": {
		"profile": "custom",
		"cpu": "50",
		"memory": "50",
		"disk": "100",
		"devices": [{
			"type": "serial",
			"label": "HOST_DEV1",
			"device-id": "/dev/ttyS1"
		}],
		"network": [{
			"interface-name": "eth0",
			"network-name": "iox-nat0",
			"port_map": {
				"mode": "auto",
				"tcp": {
					"9000": "15000",
					"10100-10200": "20100-20200"
				},
				"udp": {
					"19000": "25000"
				}
			}
		}]
	}
}


OPTIONS:
   --payload 	Pass the path to a JSON file containing your payload
   --debug 	Set to on/off.

```

> Pass a JSON file path to --payload that contains the right activation payload.

For the above app, we will use a "activation.json" that contains the right content.

```json
{
	"resources": {
		"profile": "c1.small",
		"network": [{"interface-name": "eth0", "network-name": "iox-nat0"}]
	}
}

```

> We are associating "eth0" interface requested by the app to "iox-nat0" network available on the device
> We are also setting the resource profile to "c1.small"

> **A note about "--debug" flag**
>> At the time of activation, you can set the `--debug on`. Setting this instructs the IOx platform to activate this app in debug mode. For platforms that use LXC container technology this means that even if the application stops/crashes, the container is still kept running, so that you can connect to the application console for further debugging.

Here is a sample activation command:

```
~/projects/sample-apps-v2/paas/python/nettest$ ioxclient  application activate nettest --payload activation.json
Currently using profile :  default
Command Name: application-activate
Payload file : activation.json. Will pass it as application/json in request body..
App nettest is Activated

```

### Starting the application

```
~/projects/sample-apps-v2/paas/python/nettest$ ioxclient  application start nettest
Currently using profile :  default
Command Name: application-start
App nettest is Started
```

### View application information

```
~/projects/sample-apps-v2/paas/python/nettest$ ioxclient  application info nettest
Currently using profile :  default
Command Name: application-info
Details of App : nettest
-----------------------------
{
 "appCustomOptions": "",
 "appType": "paas",
 "author": "Cisco Systems",
 "authorLink": "http://www.cisco.com",
 "dependsOn": {
  "cartridges": [
   {
    "id": "urn:cisco:system:cartridge:language-runtime:python",
    "version": "2.7"
   }
  ]
 },
 "description": "Provides a REST end point on port 9000 and also tests outbound traffic",
 "id": "nettest",
 "is_service": false,
 "name": "PyNetTest",
 "networkInfo": {
  "eth0": {
   "ipv4": "192.168.223.10",
   "ipv6": null,
   "libvirt_network": "dpbr_n_0",
   "mac": "52:54:99:99:00:00",
   "mac_address": "52:54:99:99:00:00",
   "network_name": "iox-nat0",
   "port_mappings": {
    "tcp": [
     [
      9000,
      40003
     ]
    ],
    "udp": [
     [
      10000,
      42003
     ]
    ]
   }
  }
 },
 "resources": {
  "cpu": 200,
  "disk": 10,
  "memory": 64,
  "network": [
   {
    "interface-name": "eth0",
    "network-name": "iox-nat0",
    "ports": {
     "tcp": [
      9000
     ],
     "udp": [
      10000
     ]
    }
   }
  ],
  "profile": "c1.small",
  "vcpu": 1
 },
 "state": "RUNNING",
 "toolkitServicesUsed": null,
 "version": "1.5"
}

```

### Listing all the applications on the system

```
~/projects/sample-apps-v2/paas/python/nettest$ ioxclient  application list
Currently using profile :  default
Command Name: application-list
List of installed apps :
 1. nettest    --->    STOPPED

```

### View application status

```
~/projects/sample-apps-v2/paas/python/nettest$ ioxclient  application status nettest
Currently using profile :  default
Command Name: application-status
App nettest is RUNNING
```

### Get application bootstrap configuration

```
$ ioxclient application getconfig nettest
Currently using profile :  default
Command Name: application-getconfig
Retrieved app config successfully. Content stored at nettest-app_config.ini

```

### Setting application bootstrap configuration

You can set the application bootstrap configuration by passing a new configuration file.

Usage:

```
$ ioxclient  application setconfig
NAME:
   setconfig - Set config information for an installed application from the specified file

USAGE:
   command setconfig <application_id> <config_file> [log_level]

```

If the content is present in a "config.ini" file, you can use the command as below:

```
$ioxclient application setconfig nettest config.ini
Currently using profile :  default
Command Name: application-setconfig
Successfully updated apps configuration.

```

### Managing application logs

`ioxclient` provides CLIs to manage application log files.

#### Getting application log information

```
$ ./ioxclient  application logs info py
Currently active profile :  default
Command Name: application-logs-info

Log file information for :  py
	Size_bytes : 1.275576e+06
	Download_link : /admin/download/logs?filename=py-stdout.log
	Timestamp : Fri May 13 22:42:29 2016
	Filename : stdout.log

	Download_link : /admin/download/logs?filename=py-container_log_py.log
	Timestamp : Fri May 13 16:38:11 2016
	Filename : container_log_py.log
	Size_bytes : 17064

```

#### Downloading a log file

Download a log file by its name. If name is not provided, it is prompted for.

```
$ ./ioxclient  application logs download
NAME:
   download - Download a log file

USAGE:
   command download <application_id>[file_path]

$ ./ioxclient  application logs download py stdout.log
Currently active profile :  default
Command Name: application-logs-download
Retrieved log file successfully. Content stored at py-c3Rkb3V0LmxvZw==

```

#### Viewing last few lines of a particular log file

You can view last n lines of a log file by providing its name and the number of lines to be tailed. If the parameters are not part of the command, they are prompted for.

```
$ ./ioxclient  application logs tail
NAME:
   tail - Get last n lines from a specific log file

USAGE:
   command tail <application_id>[file_path][n_lines]


 $ ./ioxclient  application logs tail  py stdout.log 3
 Currently active profile :  default
 Command Name: application-logs-tail
 App/Service : py, Logfile : stdout.log, viewing last 3 lines
 1 packets transmitted, 1 packets received, 0% packet loss
 round-trip min/avg/max = 42.133/42.133/42.133 ms

```
#### Deleting a log file

Delete a log file by its name. If not provided, it is prompted for.

```
$ ./ioxclient  application logs delete
NAME:
   delete - Delete a log file

USAGE:
   command delete <application_id>[file_path]

$ ./ioxclient  application logs delete py stdout.log
Currently active profile :  default
Command Name: application-logs-delete
Log file stdout.log successfully deleted

```

#### Purge all application log files

```
$ ./ioxclient  app logs purge py
Currently active profile :  default
Command Name: application-logs-purge
All application log files are successfully purged

```

### Managing application core files

Applications may coredump generating core files. `ioxclient` provides CLIs to manage these core files.

#### List application core files

```
$ ioxclient app cores list
NAME:
   list - List core files

USAGE:
   command list <app_id>


$ ioxclient app cores list py
Currently active profile :  local
Command Name: application-cores-list
Core file list:
------------------------
1. core.ping.162.1465195133 (413696.000000 bytes)

```

#### Download core files

```
$ ioxclient app cores download
NAME:
   download - Download a core file

USAGE:
   command download <app_id>[file_path]

$ ioxclient app cores download py core.ping.162.1465195133
Currently active profile :  local
Command Name: application-cores-download
Downloading file core.ping.162.1465195133
Read bytes :  413696
App corefile successfully downloaded at core.ping.162.1465195133

```

### Download app's datamount contents

An app will be provisioned with a data mount disk where the app typically stores its data that needs to be persisted. You can download the contents of this disk as a compressed tar ball.

```
$ ./ioxclient  application datamount download py
Currently active profile :  local
Command Name: application-datamount-download
Read bytes :  2697
Datamount Content for py is downloaded at py-datamount.tar.gz
$ tar tzvf py-datamount.tar.gz
drwxr-xr-x root/root         0 2016-05-13 16:37 py/
-rw-r--r-- root/root       453 2016-05-13 16:37 py/.env
drwx------ root/root         0 2016-05-13 16:37 py/lost+found/
drwxr-xr-x root/root         0 2016-05-13 22:18 py/appdata/
-rw------- root/root      3714 2016-05-13 21:59 py/appdata/12network_config.yaml
drwxr-xr-x root/root         0 2016-05-13 22:55 py/logs/
-rw-r--r-- root/root        84 2016-05-13 22:55 py/logs/watchDog.log
-rw-r--r-- root/root      1923 2016-05-13 22:55 py/logs/stdout.log
-rw-r--r-- root/root        18 2016-05-13 16:37 py/package_config.ini

```

### Managing contents of "appdata" directory

IOx CAF provides file management to upload, download adhoc data files. These files are typically stored in `appdata` directory in the persistent storage.

```
$ ./ioxclient app appdata
NAME:
   ioxclient application appdata - Manage files in the appdata directory under datamount

USAGE:
   ioxclient application appdata command [command options] [arguments...]

COMMANDS:
   view, vi		View the files/directories under appdata. If a file is chosen, it will be downloaded
   upload, upload	Upload a new file to a target path
   delete, del		Delete a file/directory under appdata
   help, h		Shows a list of commands or help for one command

OPTIONS:
   --help, -h			show help
   --generate-bash-completion

```

#### Upload adhoc data files

```
$ ./ioxclient app appdata upload
NAME:
   upload - Upload a new file to a target path

USAGE:
   command upload <application_id><input_file><target_path>

$ ./ioxclient app appdata upload py test_resources/app.tar.gz 1/2/app.tar.gz
Currently active profile :  local
Command Name: application-appdata-upload
Upload Successful. File is available at :  https://127.0.0.1:8443/iox/api/v2/hosting/apps/py/appdata/1/2/app.tar.gz
https://127.0.0.1:8443/iox/api/v2/hosting/apps/py/appdata/1/2/app.tar.gz

```

#### View / Download adhoc data files

```
$ ./ioxclient app appdata view
NAME:
   view - View the files/directories under appdata. If a file is chosen, it will be downloaded

USAGE:
   command view <application_id>[file_path]

$ ./ioxclient app appdata view py 1/2
Currently active profile :  local
Command Name: application-appdata-view
Directory Listing for path: 1/2
                         Name	 Type	  Size
-----------------------------------------------------------
                   app.tar.gz	 file	4958.000000

$ ./ioxclient app appdata view py 1/2/app.tar.gz
Currently active profile :  local
Command Name: application-appdata-view
Downloading file 1/2/app.tar.gz
Read bytes :  4958
File 1/2/app.tar.gz is downloaded at app.tar.gz

```
#### Delete adhoc data files/directories

```
$ ./ioxclient app appdata delete
NAME:
   delete - Delete a file/directory under appdata

USAGE:
   command delete <application_id><file_path>


$ ./ioxclient app appdata delete py 1
Currently active profile :  local
Command Name: application-appdata-delete
File or Directory 1 successfully deleted!

```
### Connecting to application console

You can connect to the console of your application.

While creating your profile, if the SSH_PORT is configured, `ioxclient` automatically tries to connect and drop you into a shell connected to applications console. If the port is not configured, then it prints out a template command that you can execute using a ssh client.

```
$ ./ioxclient application console py
Currently active profile :  default
Command Name: application-console
Console setup is complete..
The device's SSH port is not configured! Cannot auto connect!Please run the below command :
ssh -p {SSH_PORT} -i py.pem appconsole@127.0.0.1

```

> SSH_PORT is the ssh port on which the SSH server on the device is bound. Note that it can be a non standard port depending on the NAT rules configured on the device.

If the SSH_PORT is configured correctly, you will be automatically connected. Hit `Ctrl+C` to exit.

```
$ ./ioxclient application console py
Currently active profile :  local
Command Name: application-console
Console setup is complete..
Attempting to automatically connect.., press Ctrl+C to exit
Connecting to appconsole@127.0.0.1:22 using pem file py.pem
Connected to domain py
Escape character is ^]


root@ir800-lxc:~# ps
ps
  PID USER       VSZ STAT COMMAND
    1 root      4208 S    init [5]
  118 root      7784 S    udhcpc -R -b -p /var/run/udhcpc.eth0.pid -i eth0
  122 root      7784 S    {startcontainer.} /bin/sh /bin/startcontainer.sh
  127 root      294m S    python /appdir/app/main.py
  139 root      7784 S    /sbin/syslogd -n -O /var/log/messages
  142 root      7784 S    /sbin/klogd -n
  145 root     12012 S    -sh
 5274 root      7784 S    /sbin/getty 38400 tty2
 5275 root     10548 S    ping -c 1 www.google.com
 5276 root     12012 R    ps
root@ir800-lxc:~# ^C
$
```

### Getting application metrics

The metrics command shows the resources used by the application.

```
~$ ioxclient  application metrics nettest
Currently using profile :  default
Command Name: application-metrics
Host ID : 564D7AD1-641A-3FC3-0C41-3313E82D27AB
-------------------Resource usage by app------------------
AppID : nettest, RUNNING
	memory (current, in KB) : 6688
	cpu (current, in percent) : 0.01
	network (current, in bytes) : 99601
	disk (current, in MB) : 0.03

```


### Stopping the application

```
~/projects/sample-apps-v2/paas/python/nettest$ ioxclient  application stop nettest
Currently using profile :  default
Command Name: application-stop
App nettest is Stopped

```

### Deactivating the application

```
~/projects/sample-apps-v2/paas/python/nettest$ ioxclient  application deactivate nettest
Currently using profile :  default
Command Name: application-deactivate
App nettest is Deactivated

```

### Upgrading the application

```
$ ioxclient application upgrade nettest app.tar.gz
Currently using profile :  default
Command Name: application-upgrade
Preserve app data across upgrade(y/N)? [y] :
Upgrade Successful. App is available at :  https://127.0.0.1:8443/iox/api/v2/hosting/apps/ioxclient_test_app/nettest
Upgrade successful.

```

### Uninstalling the application

```
$ ioxclient application uninstall nettest
Currently using profile :  default
Command Name: application-uninstall
Successfully uninstalled app  nettest

```

### Install, activate, and start application in one shot

The run command essentially combines all the steps to reach a running application in one command. A package must be specified to install, activate, and start. Additionally a specific activation payload can be given to customize the resources upon activation.

Payload sample:

```
$ cat sample_payload
{
    "resources": {
        "profile": "custom",
        "cpu": "50",
        "memory": "50",
        "disk": "100",
        "devices": [{
            "type": "serial",
            "label": "HOST_DEV1",
            "device-id": "/dev/ttyS1"
        }],
        "network": [{
            "interface-name": "eth0",
            "network-name": "iox-nat0",
            "port_map": {
                "mode": "auto",
                "tcp": {
                    "9000": "15000",
                    "10100-10200": "20100-20200"
                },
                "udp": {
                    "19000": "25000"
                }
            }
        }]
    }
}

```

Running the command:

```
$ ioxclient application run nettest package.tar --payload sample_payload
Currently active profile :  default
Command Name: application-run
Installation Successful. App is available at : https://127.0.0.1:8443/iox/api/v2/hosting/apps/nettest
Successfully deployed
Payload file : sample_payload. Will pass it as application/json in request body..
App nettest is Activated
App nettest is Started

```

## Managing IOx services lifecycle

The service management commands are available via `ioxclient service` set of commands. The operation and usage of these commands are same as that of the application management commands.

```
$ ioxclient  service
NAME:
   ioxclient service - Manage lifecycle of services

USAGE:
   ioxclient service command [command options] [arguments...]

COMMANDS:
   list, li		            List installed services on the system
   install, in		        Install a service
   start, sta		        Start an installed service
   stop, stp		        Stop an installed service
   restart, rs		        Restart an installed service
   status, sts		        Get current status of an installed service
   info, inf		        Get info pertaining to an installed service
   activate, act	        Activate Service
   deactivate, deact	    Deactivate Service
   uninstall, unin	        Uninstall an installed service
   upgrade, upgr	        Upgrade a service
   getconfig, getconf	    Get config information of an installed service
   setconfig, setconf	    Set config information for an installed service from the specified file
   infrastructure,infra     Used for device provisioning, messaging,
   logs, lgs		        Manage log files
   datamount, dm	        Manage contents of service's data mount directory
   appdata, appdata	        Manage files in the appdata directory under datamount
   console, con		        Connect to the console of the service
   metrics, met		        Get resource usage metrics of installed services
   help, h		            Shows a list of commands or help for one command

OPTIONS:
   --help, -h			show help
   --generate-bash-completion


```

### Installing a service with dependent IOx Services

A user who wants the dependencies of the services to be taken care of, can specify the ioxclient to resolve dependencies in two methods -

There are three flags available to achieve this functionality -

* **--resolve-dependencies or --rd** : specify this flag to enable automatic dependency resolution
* **--service-source or --src** : specify a folder containing service bundles to use them for dependency resolution. If no folder is specified, fogportal will be searched for the required packages.
* **--service-activation-payload or --p** - where the path of the activation payload for services is specified.

#### Resolve Service Dependencies from the Fog portal
 Here, the ioxclient searches for the required services from the Fog portal, downloads them into a temp folder and installs, activates using the activation payload, and runs them in order to install the required service


A sample service install is as follows -


```
~$ioxclient svc in mw test_resources\svc-bundles\mw-core.tar.gz --rd --p test_resources\nat-activation.json
```
**Sample Output**

```
Currently active profile :  vm211
Command Name: service-install
Resolve Dependencies flag specified by user
Reading  test_resources\svc-bundles\mw-core.tar.gz ......
Parsing  mw-core.tar.gz .yaml
Checking CAF for the already existing services
Existing services in CAF are -
Resolving dependencies from Fog portal
Checking fog portal for the dependencies that are not in CAF
Requesting  https://128.107.5.61:443/api/v1/fogportal/service_bundles/
Requesting -   https://128.107.5.61:443/api/v1/fogportal/service_bundles/
The following services are available in the Fog portal
1 .  middleware-core
2 .  Middleware Message Broker
Saving current configuration
Constructing a Dependency tree for middleware-core
|_middleware-core
|_|_Middleware Message Broker
Checking CPU architecture compatibility of the service  Middleware Message Broker
Middleware Message Broker  is present in the FogPortal
Downloading  Middleware Message Broker ....
Service bundle to be stored in  C:\Users\xyz\AppData\Local\Temp\185222e322175b49ebe62449798d47f48dbe449932d5b752e2c7a2321031952b
Installing the service  Middleware Message Broker
Installation Successful. Service is available at : https://10.78.106.211:8443/iox/api/v2/hosting/service-bundles/MiddlewareMessageBroker
Successfully deployed
Activating the service  Middleware Message Broker
Payload file : test_resources\nat-activation.json. Will pass it as application/json in request body..
Service MiddlewareMessageBroker is Activated
Starting the service  Middleware Message Broker
Service MiddlewareMessageBroker is Started

Resolved status of  Middleware Message Broker  -  true
Installation Successful. Service is available at : https://10.78.106.211:8443/iox/api/v2/hosting/service-bundles/mw
Successfully deployed

```

#### Resolve Service Dependencies from the folder
 In this case, the specified folder is searched for the required dependencies and the ones required are installed, activated and started in order to install the service.

```
~$ioxclient svc in mw test_resources\svc-bundles\mw-core.tar.gz --rd --src test_resources\svc-bundles -p test_resources\nat-activation.json
```

**Sample Output**

```
 Currently active profile :  vm211
 Command Name: service-install
 Resolve Dependencies flag specified by user
 Reading  test_resources\svc-bundles\mw-core.tar.gz ......
 Parsing  mw-core.tar.gz .yaml
 Checking CAF for the already existing services
 Existing services in CAF are -
 Resolving dependencies from the specified Local respository
 Searching the specified local repo for the dependencies..
 Unpacking  MessageBus.tar.gz
 Reading  test_resources\svc-bundles\MessageBus.tar.gz ......
 Parsing  MessageBus.tar.gz .yaml
 Unpacking  mw-core.tar.gz
 Reading  test_resources\svc-bundles\mw-core.tar.gz ......
 Parsing  mw-core.tar.gz .yaml
 Saving current configuration
 Constructing a Dependency tree for middleware-core
 |_middleware-core
 |_|_Middleware Message Broker
 Checking CPU architecture compatibility of the service  Middleware Message Broker
 Installing the service  Middleware Message Broker
 Installation Successful. Service is available at : https://10.78.106.211:8443/iox/api/v2/hosting/service-bundles/MiddlewareMessageBroker
 Successfully deployed
 Activating the service  Middleware Message Broker
 Payload file : test_resources\nat-activation.json. Will pass it as application/json in request body..
 Service MiddlewareMessageBroker is Activated
 Starting the service  Middleware Message Broker
 Service MiddlewareMessageBroker is Started

 Resolved status of  Middleware Message Broker  -  true
 Installation Successful. Service is available at : https://10.78.106.211:8443/iox/api/v2/hosting/service-bundles/mw
 Successfully deployed

```

## Platform management

ioxclient also provides CLIs to view and manage platform related information. Here are the list of platform commands:

```
~$ ioxclient  platform
NAME:
   ioxclient platform - Manage IOx platform

USAGE:
   ioxclient platform command [command options] [arguments...]

COMMANDS:
   resourcemanager, rsmgr       View resource manager information
   autoconfigcli, ac            Auto configure IOS CLI support
   tech-support, ts             Manage techsupport snapshots
   certificate, cert            Manage CA-signed certificate on the platform
   signedpackages, signpkg      Enable/Disable package signature validation on the platform
   device, dvc                  Manage serial/usb devices on this platform
   network, nw                  Manage logical networks on the platform
   core, core                   Manage core files on the platform
   logs, logs                   Manage platform log files
   diagnostics, diag            Get platform diagnostics
   capability, cap              Get platform capability info
   cafmetrics, cafmet           Get CAF metrics
   reset, rset                  IOX reset. Reset IOX to factory defaults
   events, ev                   Get platform events
   errors, err                  Get platform errors
   health, hlt                  Get platform health info
   info, inf                    Get platform info
   scp, scp                     SCP a file to IOx device
   help, h                      Shows a list of commands or help for one command

OPTIONS:
   --help, -h                   show help
   --generate-bash-completion

```
### View resource manager data

CAF has an internal resource manager responsible for allocating and keeping track of resources such as cpu, memory, disk, serial devices etc., to applications.

#### View Resource Profile definitions

A Resource Profile encapsulates a set of resources (cpu, memory etc.,) under a unique name in a consistent fashion across all cisco's IOx platforms. To see the supported resource profile definitions and their values:

```
$ ioxclient platform  resourcemanager profiles
Currently using profile :  local
Command Name: plt-rsmgr-profiles
Profile Definitions :
-----------------------------
{
 "c1.large": {
  "cpu": 600,
  "memory": 256,
  "vcpu": 1
 },
 "c1.medium": {
  "cpu": 400,
  "memory": 128,
  "vcpu": 1
 },
 "c1.small": {
  "cpu": 200,
  "memory": 64,
  "vcpu": 1
 },
 "c1.tiny": {
  "cpu": 100,
  "memory": 32,
  "vcpu": 1
 },
 "c1.xlarge": {
  "cpu": 1200,
  "memory": 256,
  "vcpu": 1
 },
 "default": {
  "cpu": 200,
  "memory": 64,
  "vcpu": 1
 }
}

```

#### View resource allocation information

It is possible to view the inventory of resources and allocations maintained by resource manager.

```
$ ioxclient platform resourcemanager allocations
Currently using profile :  local
Command Name: plt-rsmgr-allocations
Resource Allocation Info :
-----------------------------
{
"cpu": {
 "app_cpu_allocations": [
  {
   "py": 600
  },
  {
   "sim": 200
  }
 ],
 "available_cpu": 200,
 "total_cpu": 1000
},
"devices": {
 "app_device_mapping": []
},
"disk": {
 "app_disk_allocations": [
  {
   "py": 10
  },
  {
   "sim": 30
  }
 ],
 "available_persistent_disk": 216,
 "total_persistent_disk": 256
},
"memory": {
 "app_memory_allocations": [
  {
   "py": 256
  },
  {
   "sim": 64
  }
 ],
 "available_memory": 4800,
 "total_memory": 5120
}
}

```

### Manage techsupport snapshots on the device

Techsupport snapshots are basically archive files that contain critical platform logs, statistics about platform health etc., These files can be used to analyze and troubleshoot any issues on the platform.

Techsupport commands are as below:

```
~$ ioxclient  platform techsupport
NAME:
   ioxclient platform techsupport - Manage techsupport snapshots

USAGE:
   ioxclient platform techsupport command [command options] [arguments...]

COMMANDS:
   list, li		List all existing techsupport files
   create, c		Create a new techsupport snapshot file
   delete, d		Delete a techsupport snapshot file
   download, dnld	Download a techsupport snapshot file
   help, h		Shows a list of commands or help for one command

OPTIONS:
   --help, -h			show help
   --generate-bash-completion

```

#### Create a techsupport snapshot

```
~$ ioxclient  platform techsupport create
Currently using profile :  default
Command Name: plt-ts-create
A new techsupport snapshot has been generated. File name is  tech_support_2016-01-08_04.00.55.tar.gz

```

#### List techsupport files on the platform

```
~$ ioxclient platform techsupport list
Currently using profile :  default
Command Name: plt-ts-list
List of techsupport files on the system :
1  ---> tech_support_2016-01-08_04.00.55.tar.gz
2  ---> tech_support_2016-01-05_14.35.41.tar.gz
3  ---> tech_support_2016-01-05_13.42.14.tar.gz
4  ---> tech_support_2016-01-05_14.30.04.tar.gz
5  ---> tech_support_2016-01-07_10.22.56.tar.gz
6  ---> tech_support_2016-01-05_14.34.51.tar.gz
7  ---> tech_support_2016-01-05_14.34.15.tar.gz
8  ---> tech_support_2016-01-05_13.11.08.tar.gz
9  ---> tech_support_2016-01-05_14.05.59.tar.gz

```

#### Download a techsupport snapshot

```
~$ ioxclient  platform techsupport download
Currently using profile :  default
Command Name: plt-ts-download
List of techsupport files in the system :
1  ---> tech_support_2016-01-08_04.00.55.tar.gz
2  ---> tech_support_2016-01-05_14.35.41.tar.gz
3  ---> tech_support_2016-01-05_13.42.14.tar.gz
4  ---> tech_support_2016-01-05_14.30.04.tar.gz
5  ---> tech_support_2016-01-07_10.22.56.tar.gz
6  ---> tech_support_2016-01-05_14.34.51.tar.gz
7  ---> tech_support_2016-01-05_14.34.15.tar.gz
8  ---> tech_support_2016-01-05_13.11.08.tar.gz
9  ---> tech_support_2016-01-05_14.05.59.tar.gz
Choose the file (1:9) : 1
Read bytes :  3205206
Techsupport snapshot successfully downloaded at  tech_support_2016-01-08_04.00.55.tar.gz

```

#### Deleting a techsupport snapshot

```
~$ ioxclient  platform techsupport delete
Currently using profile :  default
Command Name: plt-ts-delete
List of techsupport files in the system :
1  ---> tech_support_2016-01-08_04.00.55.tar.gz
2  ---> tech_support_2016-01-05_14.35.41.tar.gz
3  ---> tech_support_2016-01-05_13.42.14.tar.gz
4  ---> tech_support_2016-01-05_14.30.04.tar.gz
5  ---> tech_support_2016-01-07_10.22.56.tar.gz
6  ---> tech_support_2016-01-05_14.34.51.tar.gz
7  ---> tech_support_2016-01-05_14.34.15.tar.gz
8  ---> tech_support_2016-01-05_13.11.08.tar.gz
9  ---> tech_support_2016-01-05_14.05.59.tar.gz
Choose the file (1:9) : 1
Tech support file tech_support_2016-01-08_04.00.55.tar.gz successfully deleted

```

### Getting CAF Metrics
There are variety of stats genereated by CAF. These can be used to find out how system is performing. How is the system is being used etc.
For accessing CAF metrics use:
```
$ ioxclient plt cafmetrics
Currently active profile :  def_newapi
Command Name: plt-cafmetrics
Available Metrics:
------------------------
1. RESTAPI
2. SYSTEM
3. HASYNC
4. PUSHNOT
5. MONITOR
6. RESOURCE
7. CAF
8. all
Choose the metrics file you want to download [1-8] :6
-------------CAF Metrics----------------
{
 "global": {
  "available_cpu": {
   "value": 1000
  },
  "available_memory": {
   "value": 256
  },
  "available_persistent_disk": {
   "value": 256
  },
  "total_cpu": {
   "value": 1000
  },
  "total_memory": {
   "value": 256
  },
  "total_persistent_disk": {
   "value": 256
  }
 }
}
```

### CAF Metrics RESTAPI
The RESTAPI metric provides the following information for a REST API request:

*    Time taken to service the request
*    Total noumber of requests
*    Average time taken to serve the request
*    Maximum time taken to serve the request
*    Minimum time taken to serve the request
*    Total number of errors
*    Most recent error

The following example shows the metrics for REST API requests: 
```
$ioxclient plt cafmet RESTAPI
Currently active profile :  def_newapi
Command Name: plt-cafmetrics
-------------CAF Metrics----------------
{
 "/iox/api/v2/hosting/apps": {
  "error_cnt": {
   "count": 1
  },
  "time": {
   "75_percentile": 0.510253,
   "95_percentile": 0.510253,
   "999_percentile": 0.510253,
   "99_percentile": 0.510253,
   "avg": 0.17064899999999997,
   "count": 3,
   "max": 0.510253,
   "min": 0.000562,
   "std_dev": 0.2941058293148913
  }
 },
 "/iox/api/v2/hosting/apps/lxc/state": {
  "error_cnt": {
   "count": 1
  },
  "time": {
   "75_percentile": 0.462845,
   "95_percentile": 0.462845,
   "999_percentile": 0.462845,
   "99_percentile": 0.462845,
   "avg": 0.231929,
   "count": 2,
   "max": 0.462845,
   "min": 0.001013,
   "std_dev": 0.3265645389689456
  }
 }
}
```
### CAF Metrics SYSTEM
The SYSTEM metric provides the following details about system health and system resources.

*  CPU
*    CPU usage percentage
*    Statistics for each CPU
*    CPU stats for system, user, guest
*  Memory
*    Memory usage percentage
*    Physical memory stats - used, free, total
*    Virtual memory stats - used, free, total
*    Swap memory stats - used, free, total
*  Disk
*    Disk usage stats for each mounted partition - free, used, total
*    Number of reads, write
*  Network
*    Network statistics for each interface
*    Bytes received and sent
*    Errors - in, out
*    Packets - sent, received
*    Drops - in, out
*  System load
*    Average in 1 minute, 5 minutes, 15 minutes

The following example shows the metrics for cpu, disk, network, system
```
ioxclient plt cafmet SYSTEM
Currently active profile :  def_newapi
Command Name: plt-cafmetrics
-------------CAF Metrics----------------
{
 "cpu": {
  "cpu_percent": {
   "75_percentile": 1,
   "95_percentile": 2.4299999999999997,
   "999_percentile": 8,
   "99_percentile": 8,
   "avg": 0.8521739130434783,
   "count": 46,
   "max": 8,
   "min": 0,
   "std_dev": 1.2152254716141786
  }
 },
 "cpu0": {
  "guest": {
   "value": 0
  },
  "guest_nice": {
   "value": 0
  },
  "idle": {
   "value": 17766.72
  },
  "iowait": {
   "value": 4.99
  },
  "irq": {
   "value": 0
  },
  "nice": {
   "value": 0
  },
  "softirq": {
   "value": 4.52
  },
  "steal": {
   "value": 0
  },
  "system": {
   "value": 60.41
  },
  "user": {
   "value": 165.5
  }
 },
 "df-root": {
  "free": {
   "value": 2.805202944e+09
  },
  "total": {
   "value": 1.9945680896e+10
  },
  "used": {
   "value": 1.6103698432e+10
  }
 },
 "disk-loop0": {
  "read_bytes": {
   "value": 0
  },
  "read_count": {
   "value": 0
  },
  "read_time": {
   "value": 0
  },
  "write_bytes": {
   "value": 0
  },
  "write_count": {
   "value": 0
  },
  "write_time": {
   "value": 0
  }
 },
 "disk-sda1": {
  "read_bytes": {
   "value": 1.307874304e+09
  },
  "read_count": {
   "value": 58236
  },
  "read_time": {
   "value": 22140
  },
  "write_bytes": {
   "value": 1.336438784e+09
  },
  "write_count": {
   "value": 33865
  },
  "write_time": {
   "value": 13348
  }
 },
 "global": {
  "uptime": {
   "value": 18065
  }
 },
 "loadavg": {
  "15min": {
   "value": 0.05
  },
  "1min": {
   "value": 0
  },
  "5min": {
   "value": 0.02
  }
 },
 "nic-eth0": {
  "bytes_recv": {
   "value": 8.0668528e+07
  },
  "bytes_sent": {
   "value": 9.446851e+06
  },
  "dropin": {
   "value": 0
  },
  "dropout": {
   "value": 0
  },
  "errin": {
   "value": 0
  },
  "errout": {
   "value": 0
  },
  "packets_recv": {
   "value": 63178
  },
  "packets_sent": {
   "value": 30176
  }
 },
 "nic-lo": {
  "bytes_recv": {
   "value": 6.795144e+06
  },
  "bytes_sent": {
   "value": 6.795144e+06
  },
  "dropin": {
   "value": 0
  },
  "dropout": {
   "value": 0
  },
  "errin": {
   "value": 0
  },
  "errout": {
   "value": 0
  },
  "packets_recv": {
   "value": 7473
  },
  "packets_sent": {
   "value": 7473
  }
 },
 "phymem": {
  "active": {
   "value": 1.91465472e+09
  },
  "available": {
   "value": 6.443024384e+09
  },
  "buffers": {
   "value": 2.36244992e+08
  },
  "cached": {
   "value": 1.18059008e+09
  },
  "free": {
   "value": 5.026189312e+09
  },
  "inactive": {
   "value": 7.3773056e+08
  },
  "percent": {
   "value": 22.6
  },
  "total": {
   "value": 8.329035776e+09
  },
  "usage_percent": {
   "75_percentile": 3.302940672e+09,
   "95_percentile": 3.3031110656e+09,
   "999_percentile": 3.303133184e+09,
   "99_percentile": 3.303133184e+09,
   "avg": 3.2841046817391305e+09,
   "count": 46,
   "max": 3.303133184e+09,
   "min": 2.147483647e+09,
   "std_dev": 2.127291142627017e+07
  },
  "used": {
   "value": 3.302846464e+09
  }
 },
 "swap": {
  "free": {
   "value": 1.071640576e+09
  },
  "percent": {
   "value": 0
  },
  "sin": {
   "value": 0
  },
  "sout": {
   "value": 0
  },
  "total": {
   "value": 1.071640576e+09
  },
  "used": {
   "value": 0
  }
 },
 "virtmem": {
  "free": {
   "value": 1.071640576e+09
  },
  "percent": {
   "value": 0
  },
  "sin": {
   "value": 0
  },
  "sout": {
   "value": 0
  },
  "total": {
   "value": 1.071640576e+09
  },
  "usage_percent": {
   "75_percentile": 0,
   "95_percentile": 0,
   "999_percentile": 0,
   "99_percentile": 0,
   "avg": 0,
   "count": 46,
   "max": 0,
   "min": 0,
   "std_dev": 0
  },
  "used": {
   "value": 0
  }
 }
}
```

### CAF Metrics CAF
The CAF metric provides the following information that relates to CAF process
*  Threads - Detailed information about the CAF threads and their states
*    Current state, is daemon or not 
*  Processes
*    Number, state, is daemon or not
*  Memory
*    Current memory used
*    Increase in memory, maximum memory used, minimum memory used
*  Garbage collector statistics
*    Object count, reference count, referrent count
The following example shows the CAF metrics for threads, memory and processes
```
$ioxclient plt cafmet CAF
Currently active profile :  def_newapi
Command Name: plt-cafmetrics
-------------CAF Metrics----------------
{
 "gc": {
  "collection.count0": {
   "value": 641
  },
  "collection.count1": {
   "value": 11
  },
  "collection.count2": {
   "value": 1
  },
  "objects.count": {
   "value": 32839
  },
  "referents.count": {
   "value": 0
  },
  "referrers.count": {
   "value": 0
  }
 },
 "memory": {
  "memory.increase": {
   "75_percentile": 0,
   "95_percentile": 0.34746093749999873,
   "999_percentile": 45.2890625,
   "99_percentile": 45.2890625,
   "avg": 0.5328634510869565,
   "count": 92,
   "max": 45.2890625,
   "min": 0,
   "std_dev": 4.721528918533509
  },
  "memory.usage": {
   "value": 49.0234375
  }
 },
 "processes": {
  "alive": {
   "value": 0
  },
  "count": {
   "value": 0
  },
  "daemon": {
   "value": 0
  }
 },
 "threads": {
  "CP Server Thread-10.alive": {
   "value": true
  },
  "CP Server Thread-10.daemon": {
   "value": true
  },
  "CP Server Thread-11.alive": {
   "value": true
  },
  "CP Server Thread-11.daemon": {
   "value": true
  },
  "CP Server Thread-4.alive": {
   "value": true
  },
  "CP Server Thread-4.daemon": {
   "value": true
  },
  "CP Server Thread-5.alive": {
   "value": true
  },
  "CP Server Thread-5.daemon": {
   "value": true
  },
  "CP Server Thread-6.alive": {
   "value": true
  },
  "CP Server Thread-6.daemon": {
   "value": true
  },
  "CP Server Thread-7.alive": {
   "value": true
  },
  "CP Server Thread-7.daemon": {
   "value": true
  },
  "CP Server Thread-8.alive": {
   "value": true
  },
  "CP Server Thread-8.daemon": {
   "value": true
  },
  "CP Server Thread-9.alive": {
   "value": true
  },
  "CP Server Thread-9.daemon": {
   "value": true
  },
  "MainThread.alive": {
   "value": true
  },
  "MainThread.daemon": {
   "value": false
  },
  "MonitoringService.alive": {
   "value": true
  },
  "MonitoringService.daemon": {
   "value": true
  },
  "total_threads": {
   "value": 13
  }
 }
}
```
### CAF Metrics HASYNC
The HASYNC metric provides the following information about the CAF HA service:

*   Date and time when the last successful sync was performed 
*   Last successful command
*   Total number of errors
*   Last error
The following example shows the hasync metrics 
```
$ioxclient plt cafmet HASYNC
Currently active profile :  def_newapi
Command Name: plt-cafmetrics
-------------CAF Metrics----------------
    {
      "hasync": {
        "last_rsync_cmd": {
          "value": [
            "/home/mrathees/CAF/iox-dev/core/caf/scripts/sync_data.sh",
            "/sw/opt/cisco/caf",
            "/tmp",
            "/tmp/sync_exclude.lst",
            "300",
            "120"
          ]
        },
        "last_rsync_at": {
          "value": "2017-02-08 14:10:47.615738"
        }
      }
    }
```
### CAF Metrics MONITOR
The MONITOR metric provides the following information about the CAF monitoring service:

*   Last operation performed by the monitoring service
*   Total number of errors
*   Last error
*   Total number of successful operations
The following example shows monitoring metrics:
```
ioxclient plt cafmt MONITOR
Currently active profile :  def_newapi
Command Name: plt-cafmetrics
-------------CAF Metrics----------------
{
 "monitor": {
  "last_operation": {
   "value": "2017-02-07 23:38:06.822355:App:lxc state is changed to start by monitoring service"
  },
  "success_cnt": {
   "count": 1
  }
 }
}
```
### CAF Metrics RESOURCE
The RESOURCE metric provides the following information about CAF resources and how they are being used:

*   Current resource allocation (memory, CPU, persistent storage)
*   Resource allocation per app
The following example shows resource metrics:
```
$ioxclient plt cafmet RESOURCE
Currently active profile :  def_newapi
Command Name: plt-cafmetrics
-------------CAF Metrics----------------
{
 "global": {
  "available_cpu": {
   "value": 800
  },
  "available_memory": {
   "value": 192
  },
  "available_persistent_disk": {
   "value": 246
  },
  "total_cpu": {
   "value": 1000
  },
  "total_memory": {
   "value": 256
  },
  "total_persistent_disk": {
   "value": 256
  }
 },
 "lxc": {
  "cpu": {
   "value": 200
  },
  "disk": {
   "value": 10
  },
  "memory": {
   "value": 64
  }
 }
}
```
### CAF Metrics PUSHNOT
The PUSHNOT metric provides the following information abou the push/async notification service:

*    Total number of events sent
*    Last event
*    Total number of connection errors
*    Last error
*    Total number of solicited events
*    Total number of unsolicited events
The following example shows push notification metrics:
```
$ioxclient plt cafmet PUSHNOT
Currently active profile :  def_newapi
Command Name: plt-cafmetrics
-------------CAF Metrics----------------
{
  "websocket": {
    "last_connection_url": {
      "value": "wss://10.0.2.16:8444/api/v1/appmgr/notification"
    },
    "connection_error": {
      "count": 3
    },
    "first_connection_opened_at": {
      "value": "2017-01-31 13:28:04.893358"
    },
    "total_connections_closed": {
      "count": 1
    },
    "websocket_uptime": {
      "count": 1,
      "999_percentile": 569.472773,
      "99_percentile": 569.472773,
      "min": 569.472773,
      "95_percentile": 569.472773,
      "75_percentile": 569.472773,
      "std_dev": 0,
      "max": 569.472773,
      "avg": 569.472773
    },
    "last_connection_opened_at": {
      "value": "2017-01-31 13:28:04.893368"
    },
    "last_connection_tried_at": {
      "value": "2017-01-31 13:37:29.358293"
    },
    "last_retry_count": {
      "value": 3
    },
    "connection_tries": {
      "count": 2
    },
    "last_connection_closed_at": {
      "value": "2017-01-31 13:37:34.366171"
    },
    "last_websocket_uptime": {
      "value": "0:09:29.472773"
    },
    "total_connection_open_try": {
      "count": 4
    },
    "total_connections_opened": {
      "count": 1
    }
  },
  "event": {
    "total_events": {
      "count": 7
    },
    "metrics_cnt": {
      "count": 5
    },
    "last_event": {
      "value": "Source: None. Type : publish_app_metrics. AppID: None Payload [OrderedDict([('host_id', '8A1477CA-73D0-45A6-8637-71B5F2738AC2'), ('resource_usage', [OrderedDict([('app_id', 'python'), ('type', 'APP'), ('app_status', 'RUNNING'), ('timestamp', '2017-01-31 13:36:19'), ('memory', {'current': 9172L, 'unit': 'KB'}), ('cpu', {'current': 0.01, 'unit': 'percent'}), ('network', {'current': 51573, 'unit': 'bytes'}), ('disk', {'current': 0.03, 'unit': 'MB'})])])])]"
    },
    "app_metrics_collect_freq": {
      "value": "120"
    },
    "last_event_time": {
      "value": "2017-01-31 13:36:22.908443"
    },
    "app_metrics_publish_freq": {
      "value": "120"
    },
    "unsoliciated_cnt": {
      "count": 2
    }
  }
}
```

### CAF Metrics TASKMGR
The TASKMGR metric provides the following task manager statistics:

*    Total number of tasks in queue
*    Execution  time information for each task
*    Status of each task
The following example shows the task manager metrics:
```
$ioxclient plt cafmet TASKMGR
Currently active profile :  def_newapi
Command Name: plt-cafmetrics
-------------CAF Metrics----------------
{                                                                                                                                                                                
  "task-75a6e92c-e2ff-47b4-b78a-5a27f81754e0": {                                                                                                                                 
    "runtime": {                                                                                                                                                                 
      "count": 9,                                                                                                                                                                
      "999_percentile": 0.005129,                                                                                                                                                
      "99_percentile": 0.005129,                                                                                                                                                 
      "min": 0.000036,                                                                                                                                                           
      "95_percentile": 0.005129,                                                                                                                                                 
      "75_percentile": 0.0012374999999999999,                                                                                                                                    
      "std_dev": 0.001711348769570689,                                                                                                                                           
      "max": 0.005129,                                                                                                                                                           
      "avg": 0.000933111111111111                                                                                                                                                
    },                                                                                                                                                                           
    "task_status": {                                                                                                                                                             
      "value": "queued"                                                                                                                                                          
    }                                                                                                                                                                            
  },                                                                                                                                                                             
  "task-c265d99c-802f-45cc-9d21-d89b0ea961b6": {                                                                                                                                 
    "runtime": {                                                                                                                                                                 
      "count": 1,                                                                                                                                                                
      "999_percentile": 0.168591,                                                                                                                                                
      "99_percentile": 0.168591,                                                                                                                                                 
      "min": 0.168591,                                                                                                                                                           
      "95_percentile": 0.168591,                                                                                                                                                 
      "75_percentile": 0.168591,                                                                                                                                                 
      "std_dev": 0,                                                                                                                                                              
      "max": 0.168591,                                                                                                                                                           
      "avg": 0.168591                                                                                                                                                            
    },
    "task_status": {
      "value": "queued"
    }
  },
  "task": {
    "total_tasks": {
      "count": 4
    }
  },
  "task-605f9e4e-f204-4844-8251-3561159dc65a": {
    "runtime": {
      "count": 7,
      "999_percentile": 0.007237,
      "99_percentile": 0.007237,
      "min": 0.000052,
      "95_percentile": 0.007237,
      "75_percentile": 0.000108,
      "std_dev": 0.0027045195154636634,
      "max": 0.007237,
      "avg": 0.0011038571428571428
    },
    "task_status": {
      "value": "queued"
    }
  },
  "task-e3fa8afc-f775-4735-8167-62da0540fb92": {
    "runtime": {
      "count": 7,
      "999_percentile": 0.003189,
      "99_percentile": 0.003189,
      "min": 0.000039,
      "95_percentile": 0.003189,
      "75_percentile": 0.000097,
      "std_dev": 0.0011817132840559446,
      "max": 0.003189,
      "avg": 0.0005094285714285715
    },
    "task_status": {
      "value": "queued"
    }
  }
}
```
### Resetting CAF
The following command restores will restore the CAF to factory default settings. It also removes all CAF artifacts, including apps and cartridges.
```
$ ioxclient plt reset
Currently active profile :  def_newapi
Command Name: plt-reset
Reset flag set. Reset will be done on next restart.
```

### Managing core files

Core dumps may get generated on the platform following a nasty issue. You can view, download and manage core files.

Core file commands:

```
~$ ioxclient  platform core
NAME:
   ioxclient platform core - Manage core files on the platform

USAGE:
   ioxclient platform core command [command options] [arguments...]

COMMANDS:
   list, li		List all existing core files
   delete, d		Delete a corefile snapshot file
   download, dnld	Download a corefile snapshot file
   help, h		Shows a list of commands or help for one command

OPTIONS:
   --help, -h			show help
   --generate-bash-completion

```

#### Listing core files on the platform

```
~$ ioxclient  platform core list
Currently using profile :  default
Command Name: plt-core-list
No core files found!

```

#### Downloading core files

```
~$ ioxclient  platform core download

```

#### Deleting core files

```
~$ ioxclient platform core delete
```

### Manage devices available on the platform

IOx devices may support peripheral devices like serial or usb ports and make it available for applications. `ioxclient` provides a few CLIs to view and manage these devices.

#### List all devices available on the platform

```
$ ioxclient platform device list
Currently active profile :  local
Command Name: plt-device-list
-------------Device Info----------------
{
 "ds_dev_ids": {},
 "serial": [
  {
   "available": true,
   "device_id": "/dev/ttyS2",
   "device_name": "async1",
   "port": null,
   "slot": null,
   "type": "serial",
   "used_by": null
  },
  {
   "available": true,
   "device_id": "/dev/ttyS1",
   "device_name": "async0",
   "port": null,
   "slot": null,
   "type": "serial",
   "used_by": null
  }
 ],
 "usbdev": [],
 "usbport": []
}
```

#### List devices of a specific type

```
$ ioxclient platform device list serial
Currently active profile :  local
Command Name: plt-device-list
-------------Device Info (serial)----------------
{
 "serial": [
  {
   "available": true,
   "device_id": "/dev/ttyS2",
   "device_name": "async1",
   "port": null,
   "slot": null,
   "type": "serial",
   "used_by": null
  },
  {
   "available": true,
   "device_id": "/dev/ttyS1",
   "device_name": "async0",
   "port": null,
   "slot": null,
   "type": "serial",
   "used_by": null
  }
 ]
}
```

#### View platform device configuration

```
$ ioxclient  platform device get_config
Currently active profile :  local
Command Name: plt-device-get_config
-------------Device Configuration----------------
{
 "console": {
  "enabled": true,
  "group_name": "libvirtd",
  "setup_script": "setupconsole.sh",
  "teardown_script": "teardownconsole.sh",
  "user_name": "appconsole"
 },
 "scp": {
  "enabled": true,
  "setup_script": "setupscpuser.sh",
  "teardown_script": "teardownscpuser.sh",
  "user_name": "scpuser"
 },
 "serial": [
  {
   "device_id": "/dev/ttyS1",
   "device_name": "async0",
   "setup_script": null,
   "teardown_script": null
  },
  {
   "device_id": "/dev/ttyS2",
   "device_name": "async1",
   "setup_script": null,
   "teardown_script": null
  }
 ],
 "supported_device_types": [
  "serial"
 ]
}
```
### Managing logical networks on the platform

The hosting infrastructure on the device creates multiple logical networks based on the platform configuration.

> Refer network related documentation for your platform for more details.

`ioxclient` provides commands to manage these logical networks.

```
$ ./ioxclient  platform network
NAME:
   ioxclient platform network - Manage logical networks on the platform

USAGE:
   ioxclient platform network command [command options] [arguments...]

COMMANDS:
   list, li			List all available networks
   info, inf			View information pertaining a network
   getconfig, gconf		Get Network Configuration
   setconfig, sconf		Set Network Configuration. Pass a json file containing new config
   getmacregistry, macreg	View Current MAC/Hardware address allocation information
   getportregistry, portreg	View Current Port allocation information
   getdefaultnetwork, gdn	View the current default network in the system
   setdefaultnetwork, sdn	Set default network in the system. Pass a file with appropriate JSON payload
   bridge, br			Manage network bridges on the platform
   help, h			Shows a list of commands or help for one command

OPTIONS:
   --help, -h			show help
   --generate-bash-completion

```

#### Listing networks available on the device

```
$ ./ioxclient  platform network list
Currently active profile :  local
Command Name: plt-network-list
List of networks:
 1. name=>iox-bridge0     :: type=>bridge, source_bridge=>svcbr_0
 2. name=>iox-nat0        :: type=>nat, source_bridge=>svcbr_0

```

#### Get information pertaining to a network

```
$ ./ioxclient  platform network info iox-nat0
Currently active profile :  local
Command Name: plt-network-info
Details of the network: iox-nat0
-----------------------------
{
 "app_ip_map": {},
 "description": "Maja Maja Network - nat",
 "external_interface": "VPG0",
 "gateway_ip": "192.168.40.33",
 "ip_end": "192.168.40.62",
 "ip_start": "192.168.40.34",
 "name": "iox-nat0",
 "nat_range_cidr": "192.168.40.32/27",
 "network_type": "nat",
 "private_route_table": "10",
 "repofolder": "/sw/opt/cisco/caf/work/network",
 "source_linux_bridge": "svcbr_0",
 "subnet_mask": "255.255.255.224"
}

```

#### List hosting bridges on the system

Logical networks are created based on the bridges configured for application hosting. To list:

```
$ ./ioxclient  platform network bridge list
Currently active profile :  local
Command Name: plt-network-bridge-list
List of hosting bridges:
[
 {
  "bridge_ip": {
   "mode": "dhcp"
  },
  "default_mode": "bridge",
  "description": "Maja Maja Network",
  "dynamically_created": false,
  "external_interface": "VPG0",
  "interface": "svcbr_0",
  "interface_info": {
   "interface_name": "svcbr_0",
   "ipv4_address": "192.168.196.128",
   "ipv6_address": "fe80::20c:29ff:fe2d:27ab/64",
   "mac_address": "00:0c:29:2d:27:ab",
   "status": "UP",
   "subnet_mask": "255.255.255.0"
  },
  "lease_info": {
   "dns": "192.168.196.2",
   "domain_name": "\"cisco.com\"",
   "fixed_address": "192.168.196.128",
   "routers": "192.168.196.2",
   "subnet_mask": "255.255.255.0"
  },
  "logical_network_info": {
   "iox-bridge0": {
    "type": "bridge"
   },
   "iox-nat0": {
    "gateway_ip": "192.168.40.33",
    "ip_end": "192.168.40.62",
    "ip_range": "192.168.40.34-192.168.40.62",
    "ip_start": "192.168.40.34",
    "nat_range_cidr": "192.168.40.32/27",
    "subnet_mask": "255.255.255.224",
    "type": "nat"
   }
  },
  "supported_modes": [
   "nat",
   "bridge"
  ],
  "vlan_id": null
 }
]

```

#### Get information from a bridge

```
$ ./ioxclient  platform network bridge info svcbr_0
Currently active profile :  local
Command Name: plt-network-bridge-info
Bridge Details:
-----------------------------
{
 "bridge_ip": {
  "mode": "dhcp"
 },
 "default_mode": "bridge",
 "description": "Maja Maja Network",
 "dynamically_created": false,
 "external_interface": "VPG0",
 "interface": "svcbr_0",
 "interface_info": {
  "interface_name": "svcbr_0",
  "ipv4_address": "192.168.196.128",
  "ipv6_address": "fe80::20c:29ff:fe2d:27ab/64",
  "mac_address": "00:0c:29:2d:27:ab",
  "status": "UP",
  "subnet_mask": "255.255.255.0"
 },
 "lease_info": {
  "dns": "192.168.196.2",
  "domain_name": "\"cisco.com\"",
  "fixed_address": "192.168.196.128",
  "routers": "192.168.196.2",
  "subnet_mask": "255.255.255.0"
 },
 "logical_network_info": {
  "iox-bridge0": {
   "type": "bridge"
  },
  "iox-nat0": {
   "gateway_ip": "192.168.40.33",
   "ip_end": "192.168.40.62",
   "ip_range": "192.168.40.34-192.168.40.62",
   "ip_start": "192.168.40.34",
   "nat_range_cidr": "192.168.40.32/27",
   "subnet_mask": "255.255.255.224",
   "type": "nat"
  }
 },
 "supported_modes": [
  "nat",
  "bridge"
 ],
 "vlan_id": null
}

```

#### Creating new networks

If your platform supports, new networks can be created and configured. To do so, you will need to create a bridge on an appropriate physical interface by passing the right JSON payload.

Here is the command help:

```
$ ./ioxclient  platform network bridge create
NAME:
   create - Create logical networks

USAGE:
   command create <json_file_with_input>

DESCRIPTION:

To create a network, pass a JSON file containing appropriate payload.
Below is a sample payload.
{
	"description": "Dynamic Network",
	"vlan_id": "10",
	"external_interface": "intsvc0",
	"supported_modes": ["nat", "bridge"],
	"bridge_ip": {
		"mode": "static",
		"ip": "192.168.0.15",
		"subnet_mask": "255.255.255.0",
		"bridge_gw_ip": "192.168.0.1",
		"dns": "8.8.4.4",
		"domain": "abc.com"
	},
	"nat": {
		"nat_range_cidr": "192.168.10.32/27"
	}
}
*vlan_id is optional
*mode can be static or dhcp. In case of dhcp, ip, bridge_gw_ip, dns, domain etc., are not needed.

```

Here is a sample CLI interaction to create a new bridge. This will result in automatic creation of bridge svcbr_1 and bridge and nat logical networks on top of it.

Sample payload:

```
$ cat test_resources/br_create.json
{
	"description": "Dynamic Network",
	"vlan_id": "10",
	"external_interface": "eth0",
	"supported_modes": ["nat", "bridge"],
	"bridge_ip": {
		"mode": "static",
		"ip": "192.168.0.15",
		"subnet_mask": "255.255.255.0",
		"bridge_gw_ip": "192.168.0.1",
		"dns": "8.8.4.4",
		"domain": "abc.com"
	},
	"nat": {
		"nat_range_cidr": "192.168.10.32/27"
	}
}

```

```
$ ./ioxclient  platform network bridge create test_resources/br_create.json
Currently active profile :  local
Command Name: plt-network-bridge-create
Payload file : test_resources/br_create.json. Will pass it as application/json in request body..
Network creation successful. Bridge is available at :  https://127.0.0.1:8443/iox/api/v2/hosting/platform/networks/hosting_bridges/svcbr_1

$ ./ioxclient  platform network list
Currently active profile :  local
Command Name: plt-network-list
List of networks:
 1. name=>iox-bridge1     :: type=>bridge, source_bridge=>svcbr_1
 2. name=>iox-bridge0     :: type=>bridge, source_bridge=>svcbr_0
 3. name=>iox-nat0        :: type=>nat, source_bridge=>svcbr_0
 4. name=>iox-nat1        :: type=>nat, source_bridge=>svcbr_1

```

#### Edit networks
It is possible to edit network configuration. Refer to the help below:

```
$ ./ioxclient  platform network bridge edit
Insufficient Args.

NAME:
   edit - Edit information pertaining a bridge

USAGE:
   command edit <bridge_id> <json_file_with_input>

DESCRIPTION:

Currently it is allowed only to change description and nat range of a network.
Below is a sample JSON payload.
{
	"description": "Dynamic Network",
	"nat": {
		"nat_range_cidr": "192.168.10.32/27"
	}
}

```

#### Deleting networks
Dynamically created/configured networks can be deleted. Below, we delete svcbr_1, which causes the iox-bridge1 and iox-nat1 to be deleted.

```
$ ./ioxclient  platform network bridge delete svcbr_1
Currently active profile :  local
Command Name: plt-network-bridge-delete
Networks on bridge %s deleted successfully! svcbr_1

$ ./ioxclient  platform network list
Currently active profile :  local
Command Name: plt-network-list
List of networks:
 1. name=>iox-bridge0     :: type=>bridge, source_bridge=>svcbr_0
 2. name=>iox-nat0        :: type=>nat, source_bridge=>svcbr_0

```

#### Get network configuration

To view the current network configuration of the platform:

```
~$ ioxclient  platform network getconfig
Currently using profile :  default
Command Name: plt-network-getconfig
Current Network Configuration:
-------------------------------------
{
 "default_bridge": "svcbr_0",
 "enabled": true,
 "host_mode": false,
 "hosting_bridges": {
  "svcbr_0": {
   "default_mode": "bridge",
   "dhcp_lease_file": "/var/lib/dhcp/dhclient.svcbr_0.leases",
   "external_interface": "VPG0",
   "nat": {
    "gateway_ip": "192.168.223.1",
    "ip_range": "192.168.223.10-192.168.223.254",
    "setup_private_routing": false,
    "subnet_mask": "255.255.255.0"
   },
   "supported_modes": [
    "nat",
    "bridge"
   ]
  }
 },
 "local_mac_registry": true,
 "network_name_prefix": "iox",
 "tcp_pat_port_range": "40000-41000",
 "udp_pat_port_range": "42000-43000"
}

```

#### Setting network configuration

Currently setting network configuration is not allowed. This section will be updated when it is supported.

#### Get MAC registry mapping

You can view the MAC Registry maintained by the platform that associates an app with a MAC address.

```
~$ ioxclient  platform network getmacregistry
Currently using profile :  default
Command Name: plt-network-getmacregistry
Mac Registry:
-------------------------------------
{
 "generated_addresses": [
  "52:54:99:99:00:00"
 ],
 "registry": {
  "nettest": {
   "eth0": {
    "mac_address": "52:54:99:99:00:00",
    "network_name": "iox-nat0"
   }
  }
 }
}

```

#### Get port registry mapping

You can view the port registry metadata that maintains port mapping for apps.

```
~$ ioxclient  platform network getportregistry
Currently using profile :  default
Command Name: plt-network-getportregistry
Port Registry:
-------------------------------------
{
 "PORT_REGISTRY": {
  "nettest": {
   "eth0": {
    "mappings": {
     "tcp": [
      [
       9000,
       40003
      ]
     ],
     "udp": [
      [
       10000,
       42003
      ]
     ]
    },
    "network_type": "nat"
   }
  },
 }
}

```

#### Get default network on the platform

Out of the available logical networks, one of them will be used as a default network.

To view this information:

```
~$ ioxclient  platform network getdefaultnetwork
Currently using profile :  default
Command Name: plt-network-getdefaultnetwork
Default Network:
-------------------------------------
{
 "default_network": "iox-bridge0"
}

```

#### Set default network on the platform

The default network can also be set by supplying the right payload. In the below case, we are sending a json file that has the following:

```
# File:
{
    "default_network": "iox-nat0"
}
```

Use :

```
~$ ioxclient  platform network setdefaultnetwork dn.json
Currently using profile :  default
Command Name: plt-network-setdefaultnetwork
Payload file : dn.json. Will pass it as application/json in request body..
Default Network:
-------------------------------------
{
 "default_network": "iox-nat0"
}

```

### Manage platform log files

#### Download platform logs (including CAF and system logs)

You can view the list of platform log files, choose one of them and download it current working directory.

```
~$ ioxclient  platform logs download
Currently active profile :  local
Command Name: plt-logs-download
1. boot.log
2. syslog.1
3. alternatives.log.1
4. caf.log
5. syslog.2.gz
6. syslog
Choose the log file you want to download [1-6] : 4
Retrieved log file successfully. Content stored at plog-Y2FmLmxvZy40

```

#### Get CAF logger levels

View the current log levels for different CAF loggers.

```
$ ioxclient  platform logs getlevel
Currently active profile :  local
Command Name: plt-logs-getlevel
-------------CAF Log levels----------------
{
 "cartridge": "debug",
 "command_wrapper": "debug",
 "connector_management": "debug",
 "oauth_service": "debug",
 "oauthlib": "debug",
 "other": "debug",
 "overrides": "debug",
 "pdservices": "debug",
 "rest_apis": "debug",
 "rfs_composer": "debug",
 "runtime.proxy": "debug",
 "system_information": "debug",
 "utils": "debug"
}

```

#### Set CAF logger levels

```
$ ioxclient platform logs setlevel info
Currently active profile :  local
Command Name: plt-logs-setlevel
Successfully set log level to info

```
### Get platform diagnostics
Diagnostics can be run on the platform to see information about disk usage, memory, networking etc. Use the below command to run diagnostics.

```
~$ ioxclient platform diagnostics
Currently active profile :  mica
Command Name:  plt-diagnostics
1. summary
2. memory
3. disk
4. process
5. networking
6. application
7. all
Choose the diagnostic [1-7] : 2
Do you want detailed output (y/n)?n
eid: iox-ir809-11
pfm: IR809G-LTE-GA-K9
s/n: JMX2020X021
boot: 2017-11-09 02:46:00
time: 2017-11-14 23:57:50
load: 23:57:50 up 5 days, 21:11, 2 users, load average: 0.00, 0.07, 0.09

--Free Memory--
 total used free shared buff/cache available
Mem: 936 102 422 12 412 787

--Meminfo--
MemTotal: 959484 kB
MemFree: 432636 kB
MemAvailable: 806760 kB

--Top Memory Usage--
 PPID PID %CPU %MEM RSS TIME STIME CMD
 1 12008 0.4 8.3 80040 00:34:46 Nov09 python /home/root/iox/caf/scripts/startup.pyc /home/root/iox/caf/config/system-config.ini /home/root/iox/caf/config/log-config.ini
 1 726 0.0 2.0 19916 00:04:18 Nov09 python /home/root/fap/tpmc.py
 1 11220 0.0 1.2 12084 00:00:49 Nov09 /usr/sbin/libvirtd --daemon --listen
 1 30604 0.0 0.8 7692 00:00:00 23:41 /usr/lib64/libvirt/libvirt_lxc --name nt02Test --console 22 --security=none --handshake 25 --veth vnet1
 1 623 0.0 0.5 5612 00:00:00 Nov09 /sbin/klogd

```

Detailed version of any of the diagnostics can also be seen using the below inputs.

```
~$ ioxclient platform diagnostics
Currently active profile :  mica
Command Name:  plt-diagnostics
1. summary
2. memory
3. disk
4. process
5. networking
6. application
7. all
Choose the diagnostic [1-7] : 3
Do you want detailed output (y/n)?y

eid: iox-ir809-11
pfm: IR809G-LTE-GA-K9
s/n: JMX2020X021
boot: 2017-11-09 02:46:00
time: 2017-11-14 23:55:14
load: 23:55:14 up 5 days, 21:09, 2 users, load average: 0.01, 0.11, 0.12

--Free Disk--
Filesystem             1024-blocks   Used Available Capacity Mounted on
/dev/root                   407321 255478    130391      67% /oldroot
devtmpfs                    478876    216    478660       1% /dev
tmpfs                           40      0        40       0% /oldroot/mnt/.psplash
tmpfs                       479740    200    479540       1% /run
tmpfs                       479740   7944    471796       2% /var/volatile
tmpfs                       479740   4552    475188       1% /oldroot/ovfs-rw
none                        479740   4552    475188       1% /
/dev/sdb                    807088 443988    321272      59% /software
cgroup                      479740      0    479740       0% /sys/fs/cgroup
/dev/mapper/caf_cc_dev        6907     83      6415       2% /software/caf/CC
/dev/loop1                    2989     34      2666       2% /software/caf/work/repo-lxc/lxc-data/nt02Test
/dev/loop2                  114877   9618     99327       9% /software/caf/work/repo-lxc/nt02Test/rootfs_mnt
/dev/loop3                    2989     34      2666       2% /software/caf/work/repo-lxc/lxc-data/lxcapp
/dev/loop4                   83956  68889     15067      83% /software/caf/work/repo-lxc/lxcapp/rootfs_mnt

--Mount--
/dev/sda1 on /oldroot type ext3 (ro,noatime,errors=continue,user_xattr,acl,barrier=1,data=ordered)
devtmpfs on /oldroot/dev type devtmpfs (rw,relatime,size=478876k,nr_inodes=119719,mode=755)
sysfs on /oldroot/sys type sysfs (rw,relatime)
proc on /oldroot/proc type proc (rw,relatime)
tmpfs on /oldroot/mnt/.psplash type tmpfs (rw,relatime,size=40k)
debugfs on /oldroot/sys/kernel/debug type debugfs (rw,relatime)
tmpfs on /oldroot/run type tmpfs (rw,nosuid,nodev,mode=755)
tmpfs on /oldroot/var/volatile type tmpfs (rw,relatime)
smackfs on /oldroot/sys/fs/smackfs type smackfs (rw,relatime)
devpts on /oldroot/dev/pts type devpts (rw,relatime,gid=5,mode=620,ptmxmode=000)
tmpfs on /oldroot/ovfs-rw type tmpfs (rw,relatime)
none on / type overlay (rw,relatime,lowerdir=/,upperdir=/ovfs-rw/upperdir,workdir=/ovfs-rw/workdir)
devtmpfs on /dev type devtmpfs (rw,relatime,size=478876k,nr_inodes=119719,mode=755)
sysfs on /sys type sysfs (rw,relatime)
proc on /proc type proc (rw,relatime)
debugfs on /sys/kernel/debug type debugfs (rw,relatime)
tmpfs on /run type tmpfs (rw,nosuid,nodev,mode=755)
tmpfs on /var/volatile type tmpfs (rw,relatime)
smackfs on /sys/fs/smackfs type smackfs (rw,relatime)
devpts on /dev/pts type devpts (rw,relatime,gid=5,mode=620,ptmxmode=000)
/dev/sdb on /software type ext3 (rw,noatime,errors=continue,barrier=1,data=ordered)
/dev/sdb on /oldroot/software type ext3 (rw,noatime,errors=continue,barrier=1,data=ordered)
cgroup on /sys/fs/cgroup type tmpfs (rw,relatime,mode=755)
cgroup on /sys/fs/cgroup/cpuset type cgroup (rw,relatime,cpuset)
cgroup on /sys/fs/cgroup/cpu type cgroup (rw,relatime,cpu)
cgroup on /sys/fs/cgroup/cpuacct type cgroup (rw,relatime,cpuacct)
cgroup on /sys/fs/cgroup/blkio type cgroup (rw,relatime,blkio)
cgroup on /sys/fs/cgroup/memory type cgroup (rw,relatime,memory)
cgroup on /sys/fs/cgroup/devices type cgroup (rw,relatime,devices)
cgroup on /sys/fs/cgroup/freezer type cgroup (rw,relatime,freezer)
cgroup on /sys/fs/cgroup/net_cls type cgroup (rw,relatime,net_cls)
cgroup on /sys/fs/cgroup/perf_event type cgroup (rw,relatime,perf_event)
cgroup on /sys/fs/cgroup/debug type cgroup (rw,relatime,debug)
nfsd on /proc/fs/nfsd type nfsd (rw,relatime)
/dev/mapper/caf_cc_dev on /software/caf/CC type ext3 (rw,relatime,errors=continue,user_xattr,acl,barrier=1,data=ordered)
/software/caf/datastore/nt02Test_data.ext4 on /software/caf/work/repo-lxc/lxc-data/nt02Test type ext4 (rw,noatime,data=ordered)
/software/caf/work/repo/nt02Test/extract_archive/app.ext2 on /software/caf/work/repo-lxc/nt02Test/rootfs_mnt type ext2 (rw,noatime,errors=continue,user_xattr,acl)
/software/caf/datastore/lxcapp_data.ext4 on /software/caf/work/repo-lxc/lxc-data/lxcapp type ext4 (rw,noatime,data=ordered)
/software/caf/work/repo/lxcapp/extract_archive/rootfs.img on /software/caf/work/repo-lxc/lxcapp/rootfs_mnt type ext2 (rw,noatime,errors=continue,user_xattr,acl)
tracefs on /oldroot/sys/kernel/debug/tracing type tracefs (rw,relatime)


--Top Disk Usage--
/*:
Error: 651M     /oldroot
25M     /home
11M     /lib64
7.5M    /boot
5.7M    /bin
3.8M    /lib
3.3M    /etc
1.1M    /usr
84K     /var
12K     /lost+found
6.0K    /sbin
4.0K    /mnt
2.0K    /selinux
2.0K    /ovfs-rw
2.0K    /ovfs
2.0K    /media
2.0K    /downloads
du: cannot access '/oldroot/proc/455/task/455/fdinfo/4': No such file or directory
du: cannot access '/oldroot/proc/455/task/455/fd/4': No such file or directory
du: cannot access '/oldroot/proc/455/fdinfo/4': No such file or directory
du: cannot access '/oldroot/proc/455/fd/4': No such file or directory
/software/*:
507M    /software/caf
48K     /software/techsupport
20K     /software/apps
16K     /software/lost+found
12K     /software/downloads
4.0K    /software/tmp
4.0K    /software/backup
```

### View platform capability information

Each platform exposes its capabilities in terms of available resources, supported language runtimes, application types etc.,

```
~$ ioxclient  platform capability
Currently using profile :  default
Command Name: plt-capability
-------------Platform Capability----------------
{
 "compute_nodes": [
  {
   "apphosting_cpu_shares": 8192,
   "id": "564D7AD1-641A-3FC3-0C41-3313E82D27AB",
   "installed_cartridges": [
    {
     "author": "Cisco Systems",
     "authorLink": "http://www.cisco.com",
     "cpuarch": "x86_64",
     "dependson": null,
     "description": "Yocto 1.7.2 iox-core-image-minimal rootfs",
     "handleas": [
      "overlay",
      "mountable"
     ],
     "id": "Yocto_1.7.2_for_IR800_1.0_x86_64",
     "name": "Yocto 1.7.2 for IR800",
     "payload": "ir800_yocto-1.7.2.ext2",
     "provides_info": [
      {
       "id": "urn:cisco:system:cartridge:baserootfs:yocto",
       "used_by": [
        {
         "id": "Azul_Java_1.8_for_IR800_1.0_x86_64",
         "type": "cartridge"
        },
        {
         "id": "Python_2.7_for_IR800_1.0_x86_64",
         "type": "cartridge"
        }
       ],
       "version": "1.7.2"
      }
     ],
     "runtime": "None",
     "runtime_version": "None",
     "type": "baserootfs",
     "version": "1.0"
    },
    {
     "author": "Cisco Systems",
     "authorLink": "http://www.cisco.com",
     "cpuarch": "x86_64",
     "dependson": [
      {
       "id": "urn:cisco:system:cartridge:baserootfs:yocto",
       "version": "1.7.2"
      }
     ],
     "description": "Python 2.7 language runtime bundle",
     "handleas": [
      "overlay",
      "mountable"
     ],
     "id": "Python_2.7_for_IR800_1.0_x86_64",
     "name": "Python 2.7 for IR800",
     "payload": "ir800_yocto-1.7.2_python-2.7.3.ext2",
     "provides_info": [
      {
       "id": "urn:cisco:system:cartridge:language-runtime:python",
       "used_by": [
        {
         "id": "nettest",
         "type": "app"
        }
       ],
       "version": "2.7.3"
      }
     ],
     "runtime": "None",
     "runtime_version": "None",
     "type": "language-runtime",
     "version": "1.0"
    },
    {
     "author": "Cisco Systems",
     "authorLink": "http://www.cisco.com",
     "cpuarch": "x86_64",
     "dependson": [
      {
       "id": "urn:cisco:system:cartridge:baserootfs:yocto",
       "version": "1.7.2"
      }
     ],
     "description": "Java 1.8 language runtime bundle 1.8.0_65-8.10.0.1",
     "handleas": [
      "overlay",
      "mountable"
     ],
     "id": "Azul_Java_1.8_for_IR800_1.0_x86_64",
     "name": "Azul Java 1.8 for IR800",
     "payload": "ir800_yocto-1.7.2_zre1.8.0_65.8.10.0.1.ext2",
     "provides_info": [
      {
       "id": "urn:cisco:system:cartridge:language-runtime:java",
       "used_by": [],
       "version": "1.8"
      }
     ],
     "runtime": "None",
     "runtime_version": "None",
     "type": "language-runtime",
     "version": "1.0"
    }
   ],
   "installed_services": [],
   "name": "hvishwanath-tiramisu",
   "resources": {
    "cpu": {
     "available": 800,
     "info": {
      "cpu_arch": "x86_64",
      "family": 0,
      "frequency": 0,
      "model": 0,
      "model_name": "",
      "number_cores": 4,
      "stepping": 0
     },
     "total": 1000,
     "vcpu_count": 1
    },
    "devices": {
     "serial": [
      {
       "available": true,
       "device_id": "/dev/ttyS2",
       "device_name": "async1",
       "port": null,
       "slot": null,
       "used_by": null
      },
      {
       "available": true,
       "device_id": "/dev/ttyS1",
       "device_name": "async0",
       "port": null,
       "slot": null,
       "used_by": null
      }
     ]
    },
    "memory": {
     "available": 192,
     "total": 256
    },
    "networks": [
     {
      "app_ip_map": {},
      "external_interface": "VPG0",
      "gateway_ip": null,
      "ip_end": null,
      "ip_start": null,
      "name": "iox-bridge0",
      "network_type": "bridge",
      "private_route_table": "10",
      "repofolder": "/sw/opt/cisco/caf/work/network",
      "source_linux_bridge": "svcbr_0",
      "subnet_mask": null
     },
     {
      "app_ip_map": {
       "nettest": {
        "eth0": {
         "ipv4": "192.168.223.10",
         "mac_address": "52:54:99:99:00:00"
        }
       }
      },
      "external_interface": "VPG0",
      "gateway_ip": "192.168.223.1",
      "ip_end": "192.168.223.254",
      "ip_start": "192.168.223.10",
      "name": "iox-nat0",
      "network_type": "nat",
      "private_route_table": "10",
      "repofolder": "/sw/opt/cisco/caf/work/network",
      "source_linux_bridge": "svcbr_0",
      "subnet_mask": "255.255.255.0"
     }
    ],
    "storage": {
     "available": 246,
     "total": 256
    }
   },
   "supported_app_schemas": [
    {
     "validator_schema": "schema_1.0.json",
     "version": "1.0"
    },
    {
     "validator_schema": "schema_2.0.json",
     "version": "2.0"
    }
   ],
   "supported_app_types": [
    "docker",
    "paas",
    "lxc",
    "vm"
   ],
   "supported_profile_types": [
    "c1.tiny",
    "c1.small",
    "c1.medium",
    "c1.large",
    "default",
    "custom"
   ]
  }
 ],
 "mgmt_api_version": "2.0",
 "min_app_manifest_version": "1.0",
 "product_id": "default"

```

### View platform events

Every operation on a platform generates events. Events can be viewed using this command.

```
~$ ioxclient  platform events
Currently using profile :  default
Command Name: plt-events
Host ID : 564D7AD1-641A-3FC3-0C41-3313E82D27AB
Event : 1
	event_type : caf_started
	severity : INFO
	timestamp: 2016-01-08 09:30:50 +0530 IST
	app_id : <nil>
	message : CAF started
	sequence_number : 1

```

This command also can take optional [fromseq] and [toseq] numbers that fetches a subset of events.

```
~$ ioxclient  platform events -h
NAME:
   events - Get platform events

USAGE:
   command events [fromseq] [toseq]. If not specified, default value is -1

```

### Debuggability

Debuggability provides information about the errors that occur during various operations on the platform.

```
~$ ioxclient  platform errors -h
NAME:
   ioxclient platform errors - Get platform errors

USAGE:
   ioxclient platform errors command [command options] [arguments...]

COMMANDS:
   list, li             Get most recent CAF errors.
   forward, fwd         List errors from the beginning
   detail, d            Get details about a record
   filter, flt          Display records based on a filter phrase
   statistics, stat     Get statistics
   help, h              Shows a list of commands or help for one command

OPTIONS:
   --help, -h                   show help
   --generate-bash-completion

```
#### Display platform errors in reverse order
To display records with most recent errors starting first, use the below command. This command defaults the 
number of records displayed to 10. 

```
~$ioxclient platform errors list
Currently active profile :  mycaf
Command Name:  plt-errors-list
Defaulting number of records to 10
Record: 148
ERROR   2017-11-14 23:45:31,101 [controller.py:2412 - _upgradeConnector()] Exception while upgrading app: <type 'exceptions.IOError'>
Record: 147
ERROR   2017-11-14 23:45:30,197 [controller.py:2367 - _upgradeConnector()] Exception while deploying new package : [Errno 28
Record: 146
ERROR   2017-11-14 23:45:30,180 [controller.py:2119 - _deployConnector()] Exception while deploying connector:paas. Exception:[Errno 28
Record: 145
ERROR   2017-11-14 23:42:51,871 [libvirtcontainer.py:148 - start()] Failed to start container LXC Container : Name: lxcapp, UUID: aac8191f-2a0e-4183-ac14-225b54a6bdd8, Error: unsupported configuration: Unable to find security driver for model smack
Record: 144
ERROR   2017-11-14 23:42:08,130 [controller.py:1596 - _activateConnector()] Error in Activating the container , cause App Activation error: Platform does not have enough cpu resource, available cpu 132
Record: 143
ERROR   2017-11-14 23:42:08,129 [controller.py:1446 - _activateConnector()] Error in check resources availability Platform does not have enough cpu resource, available cpu 132
Record: 142
ERROR   2017-11-14 23:41:24,267 [controller.py:1596 - _activateConnector()] Error in Activating the container , cause App Activation error: Platform does not have enough cpu resource, available cpu 132
Record: 141
ERROR   2017-11-14 23:41:24,266 [controller.py:1446 - _activateConnector()] Error in check resources availability Platform does not have enough cpu resource, available cpu 132
Record: 140
ERROR   2017-11-14 23:41:20,907 [controller.py:1596 - _activateConnector()] Error in Activating the container , cause App Activation error: Platform does not have enough cpu resource, available cpu 132
Record: 139
ERROR   2017-11-14 23:41:20,906 [controller.py:1446 - _activateConnector()] Error in check resources availability Platform does not have enough cpu resource, available cpu 132
Press enter to list more records, or record number to see details about the record, or q to quit:

```

A different number can be specified after the list command to display any other number of records.

```
~$ioxclient platform errors list 5
Currently active profile :  mycaf
Command Name:  plt-errors-list
Record: 148
ERROR   2017-11-14 23:45:31,101 [controller.py:2412 - _upgradeConnector()] Exception while upgrading app: <type 'exceptions.IOError'>
Record: 147
ERROR   2017-11-14 23:45:30,197 [controller.py:2367 - _upgradeConnector()] Exception while deploying new package : [Errno 28
Record: 146
ERROR   2017-11-14 23:45:30,180 [controller.py:2119 - _deployConnector()] Exception while deploying connector:paas. Exception:[Errno 28
Record: 145
ERROR   2017-11-14 23:42:51,871 [libvirtcontainer.py:148 - start()] Failed to start container LXC Container : Name: lxcapp, UUID: aac8191f-2a0e-4183-ac14-225b54a6bdd8, Error: unsupported configuration: Unable to find security driver for model smack
Record: 144
ERROR   2017-11-14 23:42:08,130 [controller.py:1596 - _activateConnector()] Error in Activating the container , cause App Activation error: Platform does not have enough cpu resource, available cpu 132
Press enter to list more records, or record number to see details about the record, or q to quit: 144

Record number of any of the records can be entered in the above prompt to see the details of that record.
```

#### Display platform errors in ascending order
To display records with the initial errors starting first, use the below command. This command
defaults the number of records displayed to 10.

```
~$ioxclient platform errors forward
Currently active profile :  mycaf
Command Name:  plt-errors-forward
Defaulting number of records to 10
Record: 137
ERROR   2017-11-14 23:32:12,051 [controller.py:1446 - _activateConnector()] Error in check resources availability Platform does not have enough cpu resource, available cpu 132
Record: 138
ERROR   2017-11-14 23:32:12,052 [controller.py:1596 - _activateConnector()] Error in Activating the container , cause App Activation error: Platform does not have enough cpu resource, available cpu 132
Record: 139
ERROR   2017-11-14 23:41:20,906 [controller.py:1446 - _activateConnector()] Error in check resources availability Platform does not have enough cpu resource, available cpu 132
Record: 140
ERROR   2017-11-14 23:41:20,907 [controller.py:1596 - _activateConnector()] Error in Activating the container , cause App Activation error: Platform does not have enough cpu resource, available cpu 132
Record: 141
ERROR   2017-11-14 23:41:24,266 [controller.py:1446 - _activateConnector()] Error in check resources availability Platform does not have enough cpu resource, available cpu 132
Record: 142
ERROR   2017-11-14 23:41:24,267 [controller.py:1596 - _activateConnector()] Error in Activating the container , cause App Activation error: Platform does not have enough cpu resource, available cpu 132
Record: 143
ERROR   2017-11-14 23:42:08,129 [controller.py:1446 - _activateConnector()] Error in check resources availability Platform does not have enough cpu resource, available cpu 132
Record: 144
ERROR   2017-11-14 23:42:08,130 [controller.py:1596 - _activateConnector()] Error in Activating the container , cause App Activation error: Platform does not have enough cpu resource, available cpu 132
Record: 145
ERROR   2017-11-14 23:42:51,871 [libvirtcontainer.py:148 - start()] Failed to start container LXC Container : Name: lxcapp, UUID: aac8191f-2a0e-4183-ac14-225b54a6bdd8, Error: unsupported configuration: Unable to find security driver for model smack
Record: 146
ERROR   2017-11-14 23:45:30,180 [controller.py:2119 - _deployConnector()] Exception while deploying connector:paas. Exception:[Errno 28
Press enter to list more records, or record number to see details about the record, or q to quit:

```

A different number can be specified after the list command to display any other number of records.

```
~$ioxclient platform errors forward 5
Currently active profile :  mycaf
Command Name:  plt-errors-forward
Record: 137
ERROR   2017-11-14 23:32:12,051 [controller.py:1446 - _activateConnector()] Error in check resources availability Platform does not have enough cpu resource, available cpu 132
Record: 138
ERROR   2017-11-14 23:32:12,052 [controller.py:1596 - _activateConnector()] Error in Activating the container , cause App Activation error: Platform does not have enough cpu resource, available cpu 132
Record: 139
ERROR   2017-11-14 23:41:20,906 [controller.py:1446 - _activateConnector()] Error in check resources availability Platform does not have enough cpu resource, available cpu 132
Record: 140
ERROR   2017-11-14 23:41:20,907 [controller.py:1596 - _activateConnector()] Error in Activating the container , cause App Activation error: Platform does not have enough cpu resource, available cpu 132
Record: 141
ERROR   2017-11-14 23:41:24,266 [controller.py:1446 - _activateConnector()] Error in check resources availability Platform does not have enough cpu resource, available cpu 132
Press enter to list more records, or record number to see details about the record, or q to quit:
```

#### Display detailed information about a record
A detailed information including traceback and errors that follow a certain error can be viewed using the 
below command. The number of the record must be specified as an argument to the command.

```
~$ioxclient platform errors detail
NAME:
   detail - Get details about a record

USAGE:
   command detail <error_id>

Example: ~$ioxclient platform errors detail 137
Currently active profile :  mycaf
Command Name:  plt-errors-detail

                ----LEADING LINES----
2017-11-14 23:32:12,044 [runtime.hosting:DEBUG] [Thread-14] [resourcemanager.py:263 - construct_cpu_shares_from_cpu_units()] app cpu shares : 6831
2017-11-14 23:32:12,045 [runtime.hosting:INFO] [Thread-14] [resourcemanager.py:807 - resolve_app_resource_dependencies()] Network manifest: [{'ipv6_required': True, 'interface-name': 'eth0', 'ports': {'udp': [10000], 'tcp': [9000]}}]
2017-11-14 23:32:12,046 [runtime.hosting:DEBUG] [Thread-14] [resourcemanager.py:814 - resolve_app_resource_dependencies()] Associating eth0 with network iox-bridge0
2017-11-14 23:32:12,047 [runtime.hosting:DEBUG] [Thread-14] [resourcemanager.py:913 - resolve_app_resource_dependencies()] Updated resources: {'profile': u'custom', 'network': [{'interface-name': 'eth0', 'port_map': None, 'network-name': u'iox-bridge0', 'ipv6_required': True, 'mode': None, 'ipv6': {}, 'ports': {'udp': [10000], 'tcp': [9000]}, 'ipv4': {}}], 'memory': 64, 'vcpu': 1, 'disk': 2, 'cpu': 6831}
2017-11-14 23:32:12,047 [runtime.hosting:DEBUG] [Thread-14] [controller.py:1432 - _activateConnector()] App resources: {'profile': u'custom', 'network': [{'interface-name': 'eth0', 'port_map': None, 'network-name': u'iox-bridge0', 'ipv6_required': True, 'mode': None, 'ipv6': {}, 'ports': {'udp': [10000], 'tcp': [9000]}, 'ipv4': {}}], 'memory': 64, 'vcpu': 1, 'disk': 2, 'cpu': 6831}
2017-11-14 23:32:12,048 [runtime.hosting:DEBUG] [Thread-14] [controller.py:1436 - _activateConnector()] Resolved app resource dependencies: {'profile': u'custom', 'network': [{'interface-name': 'eth0', 'port_map': None, 'network-name': u'iox-bridge0', 'ipv6_required': True, 'mode': None, 'ipv6': {}, 'ports': {'udp': [10000], 'tcp': [9000]}, 'ipv4': {}}], 'memory': 64, 'vcpu': 1, 'disk': 2, 'cpu': 6831}
2017-11-14 23:32:12,048 [runtime.hosting:DEBUG] [Thread-14] [controller.py:1439 - _activateConnector()] Checking resource availability..
2017-11-14 23:32:12,049 [runtime.hosting:DEBUG] [Thread-14] [resourcemanager.py:271 - construct_cpu_units_from_shares()] construct cpu units
2017-11-14 23:32:12,050 [runtime.hosting:DEBUG] [Thread-14] [resourcemanager.py:276 - construct_cpu_units_from_shares()] total cpu:732.0 parent cpu shares: 10000.0 app shares: 6831 app_cpu_units: 500
2017-11-14 23:32:12,050 [runtime.hosting:DEBUG] [Thread-14] [platformcapabilities.py:192 - check_runtime_resource_availability()] check runtime resources, requested by App, cpu: 500, memory: 64

                ----RECORD LINE----
2017-11-14 23:32:12,051 [runtime.hosting:ERROR] [Thread-14] [controller.py:1446 - _activateConnector()] Error in check resources availability Platform does not have enough cpu resource, available cpu 132

                ----FOLLOWING LINES----
2017-11-14 23:32:12,052 [runtime.hosting:ERROR] [Thread-14] [controller.py:1596 - _activateConnector()] Error in Activating the container , cause App Activation error: Platform does not have enough cpu resource, available cpu 132
Traceback (most recent call last):
  File "/tmp/tmpdrDwuj/ir829/caf/src/appfw/runtime/controller.py", line 1447, in _activateConnector
AppActivationError: App Activation error: Platform does not have enough cpu resource, available cpu 132
2017-11-14 23:32:12,053 [runtime.hosting:DEBUG] [Thread-14] [controller.py:1637 - _deactivateConnector()] DeActivating connector testLxc
2017-11-14 23:32:12,054 [runtime.hostingmanager:DEBUG] [Thread-14] [hostingmgmt.py:129 - get_instance()] Hosting manager initialization not completed
2017-11-14 23:32:12,054 [runtime.hostingmanager:DEBUG] [Thread-14] [hostingmgmt.py:129 - get_instance()] Hosting manager initialization not completed
2017-11-14 23:32:12,055 [runtime.hostingmanager:DEBUG] [Thread-14] [hostingmgmt.py:129 - get_instance()] Hosting manager initialization not completed
2017-11-14 23:32:12,056 [runtime.hostingmanager:DEBUG] [Thread-14] [hostingmgmt.py:129 - get_instance()] Hosting manager initialization not completed
2017-11-14 23:32:12,056 [utils:DEBUG] [Thread-14] [utils.py:1005 - wrappedFunction()] Synchronizing function 'deactivateConnector' with args '(<appfw.runtime.connectorwrapper.ConnectorWrapper object at 0x7f9308090d10>, False), {}'
2017-11-14 23:32:12,057 [utils:DEBUG] [Thread-14] [utils.py:986 - wrappedFunction()] Synchronizing function 'setConnectorState' with args '(<appfw.runtime.connectorwrapper.ConnectorWrapper object at 0x7f9308090d10>, 'DEPLOYED'), {}'
2017-11-14 23:32:12,057 [utils:DEBUG] [Thread-14] [utils.py:1009 - wrappedFunction()] Done synchronizing on function 'deactivateConnector'
2017-11-14 23:32:12,058 [runtime.hosting:DEBUG] [MonitoringService] [monitoring.py:428 - _update_app_infomap()] Updating the apps map

```

#### Filter platform errors based on category or user-input
Platform records can be filtered based on whether they are critical records, errors, warnings. The records
can also be filtered based on a user input keyword.

```
~$ ioxclient platform errors filter
NAME:
   ioxclient platform errors filter - Display records based on a filter phrase

USAGE:
   ioxclient platform errors filter command [command options] [arguments...]

COMMANDS:
   critical, cr         Filter critical records
   error, err           Filter error records
   warning, warn        Filter warning records
   keyword, key         Filter based on the user-input keyword provided. Accepts regular expressions
   help, h              Shows a list of commands or help for one command

OPTIONS:
   --help, -h                   show help
   --generate-bash-completion

```

#### Display platform statistics
This command displays statistics on errors, local time  and device uptime.

```
~$ioxclient platform errors statistics
Currently active profile :  mycaf
Command Name:  plt-errors-statistics

caf_uptime:     3d 20:43:59
device_uptime:  3d 20:44:8
last_timestamp_str:     2017-11-09 16:15:14,966
local_time_str: 2017-11-13 12:26:04 UTC
num_critical_last_caf:  0
num_error_last_caf:     27
num_warning_last_caf:   41

```

### Get system health

System health information provides valuable data about the what is going on in the platform.

```
~$ ioxclient  platform health
Currently using profile :  default
Command Name: plt-health
-------------System Health----------------
{
 "cpu": {
  "cpu_count": 4,
  "load_average": {
   "min1": 0.45,
   "min15": 0.3,
   "min5": 0.42
  },
  "tasks": {
   "stopped": 0,
   "total": 547,
   "zombie": 0
  },
  "utilization": {
   "idle": 0.9764563446970509,
   "io_wait": 0.00015042774858185456,
   "system": 0.004910452673346573,
   "user": 0.017777448568410233
  }
 },
 "interfaces": [
  {
   "bandwidth_available": "N/A",
   "bandwidth_used_rx": 0,
   "bandwidth_used_tx": 0,
   "name": "docker0",
   "packets_dropped_rx": 0,
   "packets_dropped_tx": 0,
   "packets_rx": 0,
   "packets_tx": 0,
   "tx_queue_len": 0
  },
  {
   "bandwidth_available": "N/A",
   "bandwidth_used_rx": 512,
   "bandwidth_used_tx": 512,
   "name": "lo",
   "packets_dropped_rx": 0,
   "packets_dropped_tx": 0,
   "packets_rx": 3039,
   "packets_tx": 3039,
   "tx_queue_len": 0
  },
  {
   "bandwidth_available": "N/A",
   "bandwidth_used_rx": 0,
   "bandwidth_used_tx": 0,
   "name": "virbr0",
   "packets_dropped_rx": 0,
   "packets_dropped_tx": 0,
   "packets_rx": 0,
   "packets_tx": 0,
   "tx_queue_len": 0
  },
  {
   "bandwidth_available": "10000Mb/s",
   "bandwidth_used_rx": 217,
   "bandwidth_used_tx": 806,
   "name": "vnet0",
   "packets_dropped_rx": 0,
   "packets_dropped_tx": 0,
   "packets_rx": 7542,
   "packets_tx": 18277,
   "tx_queue_len": 1000
  },
  {
   "bandwidth_available": "10Mb/s",
   "bandwidth_used_rx": 0,
   "bandwidth_used_tx": 0,
   "name": "dpbr_0-nic",
   "packets_dropped_rx": 0,
   "packets_dropped_tx": 0,
   "packets_rx": 0,
   "packets_tx": 0,
   "tx_queue_len": 500
  },
  {
   "bandwidth_available": "10000Mb/s",
   "bandwidth_used_rx": 517,
   "bandwidth_used_tx": 506,
   "name": "veth0_0",
   "packets_dropped_rx": 0,
   "packets_dropped_tx": 0,
   "packets_rx": 7037,
   "packets_tx": 3082,
   "tx_queue_len": 1000
  },
  {
   "bandwidth_available": "N/A",
   "bandwidth_used_rx": 762,
   "bandwidth_used_tx": 261,
   "name": "svcbr_0",
   "packets_dropped_rx": 0,
   "packets_dropped_tx": 0,
   "packets_rx": 33114,
   "packets_tx": 28337,
   "tx_queue_len": 0
  },
  {
   "bandwidth_available": "10Mb/s",
   "bandwidth_used_rx": 0,
   "bandwidth_used_tx": 0,
   "name": "dpbr_n_0-nic",
   "packets_dropped_rx": 0,
   "packets_dropped_tx": 0,
   "packets_rx": 0,
   "packets_tx": 0,
   "tx_queue_len": 500
  },
  {
   "bandwidth_available": "N/A",
   "bandwidth_used_rx": 302,
   "bandwidth_used_tx": 721,
   "name": "dpbr_n_0",
   "packets_dropped_rx": 0,
   "packets_dropped_tx": 0,
   "packets_rx": 7535,
   "packets_tx": 8219,
   "tx_queue_len": 0
  },
  {
   "bandwidth_available": "N/A",
   "bandwidth_used_rx": 1024,
   "bandwidth_used_tx": 0,
   "name": "dpbr_0",
   "packets_dropped_rx": 0,
   "packets_dropped_tx": 0,
   "packets_rx": 2955,
   "packets_tx": 0,
   "tx_queue_len": 0
  },
  {
   "bandwidth_available": "10000Mb/s",
   "bandwidth_used_rx": 506,
   "bandwidth_used_tx": 517,
   "name": "veth1_0",
   "packets_dropped_rx": 0,
   "packets_dropped_tx": 0,
   "packets_rx": 3082,
   "packets_tx": 7037,
   "tx_queue_len": 1000
  },
  {
   "bandwidth_available": "1000Mb/s",
   "bandwidth_used_rx": 706,
   "bandwidth_used_tx": 317,
   "name": "eth0",
   "packets_dropped_rx": 0,
   "packets_dropped_tx": 0,
   "packets_rx": 30039,
   "packets_tx": 35810,
   "tx_queue_len": 1000
  }
 ],
 "memory": {
  "free": 1.787211776e+09,
  "swap_used": 507904,
  "total": 4.130541568e+09,
  "used": 2.343329792e+09
 },
 "storage": [
  {
   "free": 1.2095512576e+10,
   "name": "/dev/sda1",
   "reads_sec": 1.010304e+09,
   "size": 1.89862912e+10,
   "writes_sec": 2.5219072e+08
  },
  {
   "free": 1.1388100608e+10,
   "name": "/dev/sdb1",
   "reads_sec": 5.52911872e+08,
   "size": 3.1571570688e+10,
   "writes_sec": 3.9825408e+08
  },
  {
   "free": 3.075072e+06,
   "name": "/dev/loop0",
   "reads_sec": 0,
   "size": 1.2762112e+07,
   "writes_sec": 0
  },
  {
   "free": 0,
   "name": "/dev/loop1",
   "reads_sec": 0,
   "size": 5.7787392e+07,
   "writes_sec": 0
  },
  {
   "free": 0,
   "name": "/dev/loop2",
   "reads_sec": 0,
   "size": 1.9841024e+07,
   "writes_sec": 0
  },
  {
   "free": 1.872896e+06,
   "name": "/dev/loop3",
   "reads_sec": 0,
   "size": 2.018304e+06,
   "writes_sec": 0
  },
  {
   "free": 1.0617856e+07,
   "name": "/dev/loop4",
   "reads_sec": 0,
   "size": 1.2131328e+07,
   "writes_sec": 0
  }
 ],
 "system": {
  "localtime": 1.452264874e+09,
  "tzone": "IST(UTC+5:30:00)",
  "uptime": 17568
 }
}
```

### View platform information

Platform information provides details about cpu, network, storage etc., on the platform.

```
~$ ioxclient  platform info
Currently using profile :  d829
Command Name: plt-info
-------------System Info----------------
{
 "arp_cache": [
  {
   "address": "10.78.106.27",
   "hwaddress": "00:0c:29:53:8d:6b",
   "iface": "svcbr_0"
  },
  {
   "address": "9.42.7.33",
   "hwaddress": "88:5a:92:f0:51:b9",
   "iface": "svcbr_0"
  },
  {
   "address": "192.168.1.1",
   "hwaddress": "5c:a4:8a:54:02:c7",
   "iface": "svcbr_0"
  },
  {
   "address": "10.78.106.98",
   "hwaddress": "00:0c:29:dd:9d:f2",
   "iface": "svcbr_0"
  },
  {
   "address": "10.78.106.1",
   "hwaddress": "00:00:0c:07:ac:0a",
   "iface": "svcbr_0"
  },
  {
   "address": "10.78.106.18",
   "hwaddress": "00:0c:29:f1:8f:10",
   "iface": "svcbr_0"
  },
  {
   "address": "10.78.106.3",
   "hwaddress": "00:1b:2b:f6:86:80",
   "iface": "svcbr_0"
  },
  {
   "address": "10.78.106.107",
   "hwaddress": "00:0c:29:4d:4d:6c",
   "iface": "svcbr_0"
  },
  {
   "address": "9.42.5.36",
   "hwaddress": "3c:08:f6:5c:5e:c8",
   "iface": "svcbr_0"
  },
  {
   "address": "10.78.106.2",
   "hwaddress": "00:1b:2b:f6:92:80",
   "iface": "svcbr_0"
  },
  {
   "address": "10.78.106.90",
   "hwaddress": "4c:4e:35:e5:4a:46",
   "iface": "svcbr_0"
  }
 ],
 "cpu": {
  "cpu_arch": "x86_64",
  "family": 0,
  "frequency": 0,
  "model": 0,
  "model_name": "",
  "number_cores": 2,
  "stepping": 0
 },
 "dns_resolver": {
  "domain": "",
  "nameservers": [
   "72.163.128.140"
  ],
  "search": "cisco"
 },
 "hostname": "iox-caf",
 "interfaces": [
  {
   "ipv4_address": "172.17.42.1",
   "ipv4_netmask": "255.255.0.0",
   "mtu": 1500,
   "name": "docker0",
   "type": "Ethernet"
  },
  {
   "ipv4_address": "",
   "ipv4_netmask": "",
   "mtu": 1500,
   "name": "dpbr_0",
   "type": "Ethernet"
  },
  {
   "ipv4_address": "10.10.10.1",
   "ipv4_netmask": "255.255.255.0",
   "mtu": 1500,
   "name": "dpbr_n_0",
   "type": "Ethernet"
  },
  {
   "ipv4_address": "",
   "ipv4_netmask": "",
   "mtu": 1500,
   "name": "eth0",
   "type": "Ethernet"
  },
  {
   "ipv4_address": "127.0.0.1",
   "ipv4_netmask": "255.0.0.0",
   "mtu": 65536,
   "name": "lo",
   "type": "Local"
  },
  {
   "ipv4_address": "10.78.106.63",
   "ipv4_netmask": "255.255.255.128",
   "mtu": 1500,
   "name": "svcbr_0",
   "type": "Ethernet"
  },
  {
   "ipv4_address": "192.168.122.1",
   "ipv4_netmask": "255.255.255.0",
   "mtu": 1500,
   "name": "virbr0",
   "type": "Ethernet"
  }
 ],
 "ipv4_routing": [
  {
   "destination": "0.0.0.0",
   "flags": "UG",
   "gateway": "10.78.106.1",
   "genmask": "0.0.0.0",
   "iface": "svcbr_0",
   "metric": 0
  },
  {
   "destination": "10.10.10.0",
   "flags": "U",
   "gateway": "0.0.0.0",
   "genmask": "255.255.255.0",
   "iface": "dpbr_n_0",
   "metric": 0
  },
  {
   "destination": "10.78.106.0",
   "flags": "U",
   "gateway": "0.0.0.0",
   "genmask": "255.255.255.128",
   "iface": "svcbr_0",
   "metric": 0
  },
  {
   "destination": "172.17.0.0",
   "flags": "U",
   "gateway": "0.0.0.0",
   "genmask": "255.255.0.0",
   "iface": "docker0",
   "metric": 0
  },
  {
   "destination": "192.168.122.0",
   "flags": "U",
   "gateway": "0.0.0.0",
   "genmask": "255.255.255.0",
   "iface": "virbr0",
   "metric": 0
  }
 ],
 "memory": {
  "size": 2.098847744e+09,
  "swap": 1.071640576e+09
 },
 "ntp_server": "",
 "storage": [
  {
   "filesystem": "ext4",
   "mount": "/",
   "name": "/dev/sda1",
   "size": 1.5718137856e+10
  },
  {
   "filesystem": "ext2",
   "mount": "/sw/opt/cisco/caf/cartridges/rootfs-dhcp_1.0_x86_64/mntpoint",
   "name": "/dev/loop0",
   "size": 2.537984e+07
  },
  {
   "filesystem": "ext2",
   "mount": "/sw/opt/cisco/caf/cartridges/python2.7_0.4_x86_64/mntpoint",
   "name": "/dev/loop1",
   "size": 6.90432e+07
  },
  {
   "filesystem": "ext2",
   "mount": "/sw/opt/cisco/caf/cartridges/mnt/Yocto_1.7.2_for_IR800_1.0_x86_64",
   "name": "/dev/loop2",
   "size": 1.275392e+07
  },
  {
   "filesystem": "ext2",
   "mount": "/sw/opt/cisco/caf/cartridges/mnt/Python_2.7_1.0_x86_64",
   "name": "/dev/loop3",
   "size": 1.9838976e+07
  }
 ],
 "system_id": "564DB932-AA60-7A0F-EC55-EA3B0E23C966",
 "version": ""
}

```

### SCP files to the platform

On supported platforms, it is possible to copy local files over SCP. Please note that for this feature to work, you should be using `ioxclient` in an environment where `scp` executable is available in `$PATH`. If present, the operation is automatically started. If ioxclient encounters an error, it prints out a command that has to be manually executed.

```
$ ./ioxclient platform scp test_resources/cartridge.tar.gz
Currently active profile :  local
Command Name: plt-scp
Downloaded scp keys to pscp.pem
Running command : [scp -P 22 -i pscp.pem test_resources/cartridge.tar.gz scpuser@127.0.0.1:/]

cartridge.tar.gz                                   100% 1167     1.1KB/s   00:00

```

> Note that the certificate from the platform will be downloaded to pscp.pem

### Auto Configuring the platform

Today, when we start a  application in IOX, it gets the IP address from DHCP server (on IR8xx) platform. In order to
connect to application from outside world we need to configure IOS ( specifically NAT configuration ). That
configuration is done manually today and it requires change every time the application IP is changed. 
The autoconfig feature will automate the addition of these NAT configuration on IOS whenever a application is deployed
without any user intervention. It will also delete the configuration that was added to IOS when the application is
stopped.
The feature is available on IR800 platform (829). This feature is disabled by default. The user has to enable this
feature using iox-client.
The autoconfig feature uses telnet to connect to ios and make the configuration changes in ios.

#### How to enable the feature:

You can enable the autoconfig feature using the ioxclient. ioxclient uses REST-API's to pass the information to CAF
which it stores in a config file and the values set are persisted across reboots.

```
path_for_ioxclient>/ioxclient platform autoconfigcli setconfig -h
NAME:
   setconfig - Set Autoconfigcli Configuration.
USAGE:
   command setconfig [command options]
OPTIONS:
   --enable                     Enable autoconfig
   --disable                    Disable autoconfig
   --ios-host                   Provide the ip address of the host. If no value is provided, the default gateway will be used.
   --ios-port '0'               Telnet Port to use to communicate with ios.
   --ios-exec-password          Exec password to log into ios
   --external-interface         External interface to use when configuring NAT rules.
   --external-interface-type    Type for option "external-interface". Valid values are {intf|vlan|tag}.

```

Options explained:

* --enable: This is to enable the feature. If the feature is enabled, NAT entries are added/deleted in ios when the
container starts/stops.
* --disable: This is to disable the feature. If the feature is disabled after NAT entries were added in ios, the entries
will be deleted when the feature is disabled.
* --ios-host: IP address of ios. if no value is configured, the default gateway is used which works for 829 platform.
* --iox-port: The telnet port to communicate with ios. The default value of 23 is used.
* -- ios-exec-password: The exec password for ios. This feature will not work if the password is not configured. Please
note that this value is saved as plain text on the guest-os. 
* --external-interface:  The external interface or vlan that one can use to connect to ios.
    * it could be a interface (example:gigabitEthernet2) that is configured for connectivity from outside.
    * it could be a vlan (example:vlan200)  that is configured for connectivity from outside,
    * A tag can be placed on a interface or a vlan in the description text as shown below. In the vlan config below, we have
used the tag as "iox-apps". You can use this tag as external interface and select the external-inteface-type as tag

```
tag usage

interface Vlan1
description iox-apps
ip dhcp relay information check-reply
no ip dhcp client request tftp-server-address
ip dhcp client lease 365 0 0
ip address dhcp
ip nat outside
ip virtual-reassembly in

```

* --external-interface-type. Valid values are "intf|vlan|tag"

Examples:

```
# To enable the feature.
 <path_for_ioxclient>/ioxclient platform autoconfigcli setconfig --enable
Currently active profile :  sandeep
Command Name: plt-ac-setconfig
Autoconfigcl:
-------------------------------------
"The following key:values were saved. enabled:True "
  
# To disable the feature
 <path_for_ioxclient>/ioxclient platform autoconfigcli setconfig --disable
Currently active profile :  sandeep
Command Name: plt-ac-setconfig
Autoconfigcl:
-------------------------------------
"The following key:values were saved. enabled:False "
  
# To set external-interface-type as tag iox-apps
 <path_for_ioxclient>/ioxclient platform ac sc --external-interface iox-apps --external-interface-type tag
Currently active profile :  sandeep
Command Name: plt-ac-setconfig
Autoconfigcl:
-------------------------------------
"The following key:values were saved. external_interface_type:tag external_interface:iox-apps "

```

### Manage package signature validation on the platform

```

dev@dev-VirtualBox:~$ ioxclient platform signedpackages

NAME:
   ioxclient platform signedpackages - Enable/Disable package signature validation on the platform

USAGE:
   ioxclient platform signedpackages command [command options] [arguments...]

COMMANDS:
   enable, e		Enable package signature validation on the platform
   disable, d		Disable package signature validation on the platform
   get, g		Get package signature validation configuration of the platform
   trustanchor, ta	Manage trust anchor on the platform
   help, h		Shows a list of commands or help for one command
   
OPTIONS:
   --help, -h			show help
   --generate-bash-completion	

```

#### Enable package signature validation
To enable package signature validation on the platform use the below command:

```

dev@dev-VirtualBox:~$ ioxclient platform signedpackages enable
Currently active profile :  829
Command Name:  plt-sign-pkg-enable
Saving current configuration
Successfully updated package signature validation capability on the device to true

```

#### Get package signature validation configuration
To check if package signature validation is enabled on the platform use the below command

```

dev@dev-VirtualBox:~$ ioxclient platform signedpackages get
Currently active profile :  829
Command Name:  plt-sign-pkg-get
Package signature validation is enabled on the platform: true

```

#### Disable package signature validation
To disable package signature validation on the platform use the below command

```
dev@dev-VirtualBox:~$ ioxclient platform signedpackages disable 
Currently active profile :  829
Command Name:  plt-sign-pkg-disable
Successfully updated package signature validation capability on the device to false

```

### Manage Trust Anchor on the platform
To manage the trust anchor used for validating packages' signature refer to the below command

```

dev@dev-VirtualBox:~$ ioxclient platform signedpackages trustanchor
NAME:
   ioxclient platform signedpackages trustanchor - Manage trust anchor on the platform

USAGE:
   ioxclient platform signedpackages trustanchor command [command options] [arguments...]

COMMANDS:
   get, g   Get info of the trust anchor in use on the platform
   set, s   Add/Replace trust anchor on the platform.
        The file to be uploaded has to be a tar.gz file with following files:
         -info.txt #contains plain-text. 
         -ca-chain.cert.pem #file containing concatenated certificates and CRL in PEM format.
   delete, d    Delete the trust anchor being used by the platform
   help, h  Shows a list of commands or help for one command
   
OPTIONS:
   --help, -h           show help
   --generate-bash-completion      

```

#### Add or Replace trust anchor on the platform
To add or replace trust anchor use the below command

```

dev@dev-VirtualBox:~$ ioxclient platform signedpackages trustanchor set ./trust_anchor.tar.gz 
Currently active profile :  829
Command Name:  plt-sign-pkg-ta-set
Response from the server:  Imported trust anchor file successfully

```
* Note that the trust anchor needs to be a tar.gz file and should contain info.txt and cert.pem files.

#### Get Trust Anchor Info
To get information about the trust anchor used by the platform to validate package signatures use the below command

```
dev@dev-VirtualBox:~$ ioxclient platform signedpackages trustanchor get
Currently active profile :  829
Command Name:  plt-sign-pkg-ta-get

------------ Trust anchor info -----------
checksum: 096b889a655312addadf51a1c62f1a6338bf5c32
metadata: Sample metadata file content

```

#### Delete Trust Anchor
To delete the trust anchor used by the platform to validate package signatures use the below command

```

dev@dev-VirtualBox:~$ ioxclient platform signedpackages trustanchor delete
Currently active profile :  mycaf
Command Name:  plt-sign-pkg-ta-delete
Successfully deleted the trust anchor on the platform

```

* Note that when trust anchor is deleted, package signature validation is disabled.
* Before re-enabling package signature validation, a trust anchor needs to be uploaded to the platform.

## Managing cartridges on the platform

A cartridge is a deployable, pluggable piece of software that provides functionality and content to be consumed by the requesting application or service on an IOx node.

> Refer cartridge documentation for more details

Cartridge management commands:

```
~$ ioxclient  cartridge
NAME:
   ioxclient cartridge - Create/Delete/List cartridges

USAGE:
   ioxclient cartridge command [command options] [arguments...]

COMMANDS:
   list, li		List all existing cartridges
   install, in		Install a cartridge from its archive
   uninstall, unin	Uninstall a cartridge
   upgrade, upgr	Upgrade a cartridge
   info, inf		View information of a cartridge
   help, h		Shows a list of commands or help for one command

OPTIONS:
   --help, -h			show help
   --generate-bash-completion


```

### List cartridges installed on the system

```
~$ ioxclient  cartridge list
Currently using profile :  d829
Command Name: cartridge-list
List of installed cartridges :
 1. Python_2.7_1.0_x86_64 : Python 2.7, Python 2.7 language runtime bundle
 2. Yocto_1.7.2_for_IR800_1.0_x86_64 : Yocto 1.7.2 for IR800, Yocto 1.7.2 iox-core-image-minimal rootfs

```

### Installing a cartridge

```
~$ ioxclient  cartridge install ~/Downloads/cartridges/ir800_yocto-1.7.2_zre1.8.0_65.8.10.0.1.tar
Currently using profile :  d829
Command Name: cartridge-install
Installation Successful. Cartridge is available at :  https://10.78.106.63:8443/iox/api/v2/hosting/cartridges/Azul_Java_1.8_for_IR800_1.0_x86_64

```

### Get cartridge information

```
~$ ioxclient  cartridge info Azul_Java_1.8_for_IR800_1.0_x86_64
Currently using profile :  d829
Command Name: cartridge-info
Details of Cartridge : Azul_Java_1.8_for_IR800_1.0_x86_64
-----------------------------
{
 "author": "Cisco Systems",
 "authorLink": "http://www.cisco.com",
 "cpuarch": "x86_64",
 "dependson": [
  {
   "id": "urn:cisco:system:cartridge:baserootfs:yocto",
   "version": "1.7.2"
  }
 ],
 "description": "Java 1.8 language runtime bundle 1.8.0_65-8.10.0.1",
 "handleas": [
  "overlay",
  "mountable"
 ],
 "id": "Azul_Java_1.8_for_IR800_1.0_x86_64",
 "name": "Azul Java 1.8 for IR800",
 "payload": "ir800_yocto-1.7.2_zre1.8.0_65.8.10.0.1.ext2",
 "provides_info": [
  {
   "id": "urn:cisco:system:cartridge:language-runtime:java",
   "used_by": [],
   "version": "1.8"
  }
 ],
 "runtime": "None",
 "runtime_version": "None",
 "type": "language-runtime",
 "version": "1.0"
}

```

### Uninstalling a cartridge

```
~$ ioxclient  cartridge uninstall Azul_Java_1.8_for_IR800_1.0_x86_64
Currently using profile :  d829
Command Name: cartridge-uninstall
Successfully uninstalled cartridge Azul_Java_1.8_for_IR800_1.0_x86_64

```

### Upgrading a cartridge

```
~$ ioxclient  cartridge upgrade
NAME:
   upgrade - Upgrade a cartridge

USAGE:
   command upgrade <cartridge_id> <cartridge_archive>

```

## Troubleshooting

You can turn on ioxclient debugs to get more information about the requests being sent to the platform.

To turn on/off debug, pass on or off to debug command.

```
~$ ioxclient  debug on
Setting ioxclient debug to  true
```

Turning on debugging prints additional information for commands:

```
~$ ioxclient  cartridge info Python_2.7_1.0_x86_64
Currently using profile :  d829
Command Name: cartridge-info
2016/01/08 15:21:15 GET /iox/api/v2/hosting/cartridges/Python_2.7_1.0_x86_64 HTTP/1.1
Host: 10.78.106.63:8443
X-Token-Id: 8877176d-f843-441a-ad87-09994ac42763

<snip>

```

## Fog Portal Management


Fog portal commands are

```
NAME:
   ioxclient fogportal - FogPortal operations

USAGE:
   ioxclient fogportal command [command options] [arguments...]

COMMANDS:
   init, in             Initialize fog profile
   service, svc         Service management operations using Fogportal
   help, h              Shows a list of commands or help for one command
```

### Initializing Fog Portal

The details of the fog portal, i.e the URL at which the fog portal can be reached has to be set in order execute operations on the fog portal using the fogportal init command

```
~$ioxclient fogportal init
Enter the Fog portal IP[127.0.0.1] :
10.78.106.35
Enter the fogportal Port[443]:
8090
Enter the API prefic[/api/v1/fogportal]:
/api/v1/fogportal/
Saving current configuration

```

### Fog portal service list

In order to list all the services available in the fog portal, use the fogportal service list command as follows

```
~$ioxclient fogportal svc li
Currently active profile :  vm211
Command Name: fogportal-service-list
The following services are present in the fog portal
Middleware Message Broker
         urn:cisco:system:service:message-broker  -  0.9.4
IOx Middleware Services
         urn:cisco:system:service:nbi  -  0.9.4
         urn:cisco:system:service:provisioning  -  0.9.4
         urn:cisco:system:service:mqttstoreandforward  -  0.9.4
         urn:cisco:system:service:coapstoreandforward  -  0.9.4
         urn:cisco:system:service:stream-analytics  -  0.9.4
         urn:cisco:system:service:plugin:coap-client  -  0.9.4
         urn:cisco:system:service:coap-proxy  -  0.9.4
         urn:cisco:system:service:plugin:mqtt-broker  -  0.9.4
         urn:cisco:system:service:plugin:coap-server  -  0.9.4
```

### Fog portal service info

This command provides all the information regarding a particular service that is available in the fog portal

```
~$ioxclient fogp svc info "Middleware Message Broker"
Currently active profile :  vm211
Command Name: fogportal-service-info
{
        "_links": {
                "package": "/api/v1/fogportal/service_bundles/downloads/0725bf1de53025ce1065cfe58519681e873b33074a1f0c319f0db3705a6c8fe9"
        },
        "id": "0725bf1de53025ce1065cfe58519681e873b33074a1f0c319f0db3705a6c8fe9",
        "Metadata": {
                "app": {
                        "cpuarch": "x86_64",
                        "type": "lxc",
                        "depends-on": {
                                "services": null
                        },
                        "resources": {
                                "cpu": "200"
                        }
                },
                "service-bundle": {
                        "provides": [
                                {
                                        "id": "urn:cisco:system:service:message-broker",
                                        "api-version": 1,
                                        "version": "0.9.4",
                                        "port-mapping": [
                                                "eth0:tcp:8080"
                                        ]
                                }
                        ]
                }
        },
        "name": "Middleware Message Broker"
}

```


### Fog portal service install

The fog portal service install command is used to install a service that is available in the fog portal. The service install can be proceeded in two types


#### With dependency resolution

If the user wants the ioxclient to take care of installing the required dependencies for the service, the user can specify the --rd flag which looks for the required dependencies in the fog portal and installs them before installing the specified service. The user can also specify a payload for the activation of the dependent services using the service-activation-payload flag.

```
~$ioxclient fogp svc in middleware-core --rd --p test_resources\nat-activation.json

```
**Sample Output**

```
Currently active profile :  vm211
Command Name: fogportal-service-install
Requesting  http://10.78.106.35:8090/api/v1/fogportal/service_bundles/
Requesting -   http://10.78.106.35:8090/api/v1/fogportal/service_bundles/
The following services are available in the Fog portal
1 .  Middleware Message Broker
2 .  middleware-core
Checking CAF for the already existing services
Existing services in CAF are -
0 .  Middleware Message Broker
|_middleware-core
|_|_Middleware Message Broker
Checking CPU architecture compatibility of the service  Middleware Message Broker
Middleware Message Broker  is present in the FogPortal
Downloading  Middleware Message Broker ....
200 OK

C:\Users\xyz\AppData\Local\Temp\0725bf1de53025ce1065cfe58519681e873b33074a1f0c319f0db3705a6c8fe9 with 27648719 bytes downloaded
Service bundle to be stored in  C:\Users\cheb\AppData\Local\Temp\0725bf1de53025ce1065cfe58519681e873b33074a1f0c319f0db3705a6c8fe9
Installation Successful. Service is available at : https://10.78.106.211:8443/iox/api/v2/hosting/service-bundles/MiddlewareMessageBroker
Successfully deployed
Payload file : test_resources\nat-activation.json. Will pass it as application/json in request body..
Service MiddlewareMessageBroker is Activated
Service MiddlewareMessageBroker is Started

Resolved status of  Middleware Message Broker  -  true
200 OK

C:\Users\xyz\AppData\Local\Temp\a01a7a94565479f90d1525b25ca53f75292bff5b18844076ab76adc4169944a6 with 13265026 bytes downloaded
Installation Successful. Service is available at : https://10.78.106.211:8443/iox/api/v2/hosting/service-bundles/middlewareCore
Successfully deployed

```

#### Without dependency resolution

This follows a straight forward installation of the specified service from the fog portal without checking for any of the dependencies.


```
~$ ioxclient fogp svc in middleware-core --p test_resources\nat-activation.json

```
**Sample Output**

```
Currently active profile :  vm211
Command Name: fogportal-service-install
Requesting  http://10.78.106.35:8090/api/v1/fogportal/service_bundles/
The following services are available in the Fog portal
1 .  Middleware Message Broker
2 .  middleware-core

200 OK

C:\Users\xyz\AppData\Local\Temp\a01a7a94565479f90d1525b25ca53f75292bff5b18844076ab76adc4169944a6 with 13265026 bytes downloaded
Installation Successful. Service is available at : https://10.78.106.211:8443/iox/api/v2/hosting/service-bundles/middlewareCore
Successfully deployed

```

## Smart License Management

These commands enable smart licensing support for IOx platforms and lets customers to register the device and manage licenses via CSSM.

### Smart License management commands

```
~$ ioxclient license smart
NAME:
   ioxclient license smart - Execute Smart Licensing commands

USAGE:
   ioxclient license smart command [command options] [arguments...]

COMMANDS:
   register, r          Register device for Smart Licensing
   deregister, d        Deregister device from Smart Licensing
   renew, rn            Manually renew Smart Licensing
   help, h              Shows a list of commands or help for one command

OPTIONS:
   --help, -h                   show help
   --generate-bash-completion

```
#### Smart License Register command
Register this device with Cisco using an ID token. Using the id token the customer got from the CSSM the agent will register this product with Cisco and receive back an identity certificate. Use the below command to register the device.

```
~$ioxclient license smart register idtoken
NAME:
   idtoken - Use Registration Token to register device

USAGE:
   command idtoken <token> [force]

```
#### Smart License Deregister command
Unregister the device from Cisco. All Smart Licensing entitlements and certificates on the platform will be removed.

```
~$ ioxclient license smart deregister
Currently active profile :  mycaf
Command Name:  license-smart-deregister

```
#### Smart License Renew commands
Initiate a manual update of the license registration information with Cisco.

```
~$ ioxclient license smart renew
NAME:
   ioxclient license smart renew - Manually renew Smart Licensing

USAGE:
   ioxclient license smart renew command [command options] [arguments...]

COMMANDS:
   ID, id       Renew registration with Smart Licensing
   auth, a      Renew authorization of Smart Licenses in use
   help, h      Shows a list of commands or help for one command

OPTIONS:
   --help, -h                   show help
   --generate-bash-completion

```

### Smart License show commands

```
~$ ioxclient show license
NAME:
   ioxclient show license - Show Smart Licensing state information

USAGE:
   ioxclient show license command [command options] [arguments...]

COMMANDS:
   status, st           Show overall Smart Licensing status
   summary, sum         Show Smart Licensing status summary
   UDI, udi             Show the Device UDI
   usage, u             Show Smart Licensing license usage
   all, a               Show all Smart Licensing information
   tech-support, ts     Show Smart Licensing tech support information
   config, conf         Show Smart Licensing configuration
   help, h              Shows a list of commands or help for one command

OPTIONS:
   --help, -h                   show help
   --generate-bash-completion

```
### Smart License Debug level commands
Turn on debug logging in the agent using the below command.

```
~$ioxclient debug smart_lic
NAME:
   ioxclient debug smart_lic - Set smart licensing debug level

USAGE:
   ioxclient debug smart_lic command [command options] [arguments...]

COMMANDS:
   error, err   Enable error level logging. value can be set to on or off
   debug, dbg   Enable debug level logging. value can be set to on or off
   trace, tr    Enable trace level logging. value can be set to on or off
   all, all     Enable all logging. value can be set to on or off
   help, h      Shows a list of commands or help for one command

OPTIONS:
   --help, -h                   show help
   --generate-bash-completion

```
### Smart License Call Home setup command
This command specifies the destination URL to which Call Home messages (including licensing requests) are sent.

```
~$ ioxclient call-home destination-address http
NAME:
   http - Set destination address. Cisco Smart Software Manager is the default destination

USAGE:
   command http <URL>

```
## IOx Services Infrastructure commands

IOx infrastructure is a set of services that can be used to apply functions on the data streams. The infrastructure service provides a common data model that represents a normalized form of the data stream to be consumed by any service or application. All incoming and outgoing data streams are consumed and emitted in this normalized data model enabling services and applications to be developed independent of the source and destinations of the data streams.

IOx Service Infrastructure Commands:

```
~$ioxclient svc infra
NAME:
   ioxclient service infrastructure - Used for device provisioning, messaging,

USAGE:
   ioxclient service infrastructure command [command options] [arguments...]

COMMANDS:
   nbi                  Supports RESTful / Websocket interface for configuring the services
   metrics, met         Get middleware metrics
   provisioning, prov   Provisions the specified function
   messaging, msg       Provides messaging services
   logservice           Use log services to view the available modules and set their log levels
   help, h              Shows a list of commands or help for one command

OPTIONS:
   --help, -h                   show help
   --generate-bash-completion


```

### Initializing a profile
Usually, the NorthBound REST / Websocket Interface is automatically initialized by the ioxclient. But for situations which require manual initialization, the user can choose to use the nbi init function

Command structure

```
 ~$ ioxclient svc infra nbi

 NAME:
    ioxclient service infrastructure nbi - Supports RESTful / Websocket interface for configuring the services

 USAGE:
    ioxclient service infrastructure nbi command [command options] [arguments...]

 COMMANDS:
    init, in     Initialise North bound gateway details manually
    help, h      Shows a list of commands or help for one command

 OPTIONS:
    --help, -h                   show help
    --generate-bash-completion
```

 Sample initialization -

 ```
 ~$ioxclient svc infra nbi init
 Enter the North bound gateway IP address[ 10.78.106.211 ] :
 10.78.106.211
 Enter the North bound gateway Port[40001]: 443
 Enter the North bound gateway api prefix[/api/v1/mw/]:/api/v1/mw
 Enter the North bound gateway URL scheme[https]:https
 Saving current configuration

 ```

### Device Provisioning

All devices that IOx infrastructure service is going to monitor, manage and communicate with, needs to be configured using RESTful APIs. The device provisioning is three steps process, where data models like data-schema(s), deviceType and device endpoint are configured. A device is of a certain device type. The device type defines one or more sensors and schema of the data emitted by each sensor. The device type also defines the protocol(s) supported by that class of devices, and properties that are relevant for the corresponding protocol handlers.

```
NAME:
   ioxclient service infrastructure provisioning - Provisions the specified function

USAGE:
   ioxclient service infrastructure provisioning command [command options] [arguments...]

COMMANDS:
   dataschemas, ds      Provision dataschemas
   devicetypes, dt      Display the details of the device
   devices, dev         Display the details of the device
   help, h              Shows a list of commands or help for one command
```

#### Provision Data-schema

As data would be consumed from variety of data sources, this data needs to be represented in a common normalized form. The Data Schema defines such a contract and once protocol handler acquires the data from a device it needs to be mapped to the corresponding data schema.

We can create, delete, update or read the information of a particular data schema using below commands.

Dataschema provisioning commands are -

```
~$ioxclient service infrastructure provisioning dataschemas
NAME:
   	ioxclient service infrastructure provisioning dataschemas - Provision dataschemas

USAGE:
   ioxclient service infrastructure provisioning dataschemas command [command options] [arguments...]

COMMANDS:
   create, cr   Add a dataschema
   info, inf    List all/specified dataschemas
   delete, del  Delete a dataschema
   update, up   Update a given schema
   help, h      Shows a list of commands or help for one command

OPTIONS:
   --help, -h                   show help
   --generate-bash-completion

```

##### Create dataschema
```
~$ioxclient service infrastructure provisioning dataschemas create -f test_resources\middleware-files\dataschema.json

Currently active profile :  vm211
Command Name: provisioning-dataschemas-create
Sending https request to  https://10.78.106.211:40001/api/v1/mw/provisioning/dataschemas/
Successfully added object
```

##### Update dataschema
```
~$ioxclient service infrastructure prov ds up temperatureSchema -f test_resources\middleware-files\dataschemaUpdate.json

Currently active profile :  vm211
Command Name: provisioning-dataschemas-update
Updating at https://10.78.106.211:40001/api/v1/mw/provisioning/dataschemas/temperatureSchema
Successfully updated Policies
```

##### Dataschema Info
```
~$ioxclient service infrastructure prov ds info

Currently active profile :  vm211
Command Name: service-infrastructure-provisioning-dataschemas-info
https://10.78.106.211:40001/api/v1/mw/provisioning/dataschemas/

```

The user could also specify a particular dataschemaId to view information of only a single dataschema

##### Delete dataschema

```
~$ioxclient infrastructure svc prov ds del temperatureSchema

Currently active profile :  vm211
Command Name: service-provisioning-dataschemas-delete
Url is  https://10.78.106.211:40001/api/v1/mw/provisioning/dataschemas/sortingstation
Successfully Deleted  dataschema   temperatureSchema

```

#### Provision Device type

As same type of physical devices can be installed at many places, key common characteristics of these devices are grouped as Device Type. This is not a one-to-one mapping to a serial number or SKU of a manufacturer but tries to abstract out key elements of a device like meta-data and key specifications like sensors and actuator entities.

##### Create devicetype

```
~$ioxclient svc infrastructure prov devicetypes cr -f test_resources\middleware-files\devicetype.json

Currently active profile :  vm211
Command Name: service-infrastructure-provisioning-devicetypes-create
Sending https request to  https://10.78.106.211:40001/api/v1/mw/provisioning/devicetypes/
Successfully added the  devicetype
```
##### Device Type Info

```
~$ioxclient svc infrastructure prov dt info

Currently active profile :  vm211
Command Name: service-infrastructure-provisioning-devicetypes-info
https://10.78.106.211:40001/api/v1/mw/provisioning/devicetypes/
{
        "kind": "model#devicetype#collection",
        "deviceTypes": [
                {
                        "kind": "model#devicetype",
                        "description": "",
                        "displayName": "",
                        "createdAt": "2016-06-08T20:13:03.267+0000",
                        "updatedAt": "2016-06-08T20:13:03.267+0000",
                        "deviceTypeId": "TestModbusDeviceType",
                        "protocol": "modbus",
                        "protocolHandler": "urn:cisco:system:service:protocolHandler:modbus-tcp",
                        "sensors": [
                                {
                                        "name": "LightSensor",
                                        "dataSchemaId": "sortingstation",
                                        "description": "",
                                        "contentHandler": {
                                                "contentType": "raw",
                                                "protocolProperties": {},
                                                "contentMappings": [
                                                        {
                                                                "fieldName": "sensor1",
                                                                "expression": ".",
                                                                "protocolProperties": {
                                                                        "style": "digital",
                                                                        "mode": "write",
                                                                        "registerRange": "10001-1"
                                                                }
                                                        },
                                                        {
                                                                "fieldName": "sensor2",
                                                                "expression": ".",
                                                                "protocolProperties": {
                                                                        "style": "digital",
                                                                        "mode": "write",
                                                                        "registerRange": "10001-1"
                                                                }
                                                        }
                                                ],
                                                "properties": {}
                                        }
                                }
                        ]
                }
        ]
}
```

##### Update a device type

```
~$ioxclient svc infrastructure prov dt up TestModbusDeviceType -f test_resources\middleware-files\devicetype.json

Currently active profile :  vm211
Command Name: service-infrastructure-provisioning-devicetypes-update
Updating at  https://10.78.106.211:40001/api/v1/mw/provisioning/devicetypes/TestModbusDeviceType
Successfully updated  devicetype

```

##### Delete a device type

```
~$ioxclient svc infrastructure prov dt delete TestModbusDeviceType

Currently active profile :  vm211
Command Name: service-infrastructure-provisioning-devicetypes-delete
Updating at  https://10.78.106.211:40001/api/v1/mw/provisioning/devicetypes/TestModbusDeviceType
Successfully deleted devicetype

```

#### Provision Device

Devices are representation of connected physical entity that conforms to a device type. A device can be representing a person with a heart monitor implant, a farm animal with a bio-chip transponder, an automobile that has built-in sensors to alert the driver when tire pressure is low or any other natural or man-made object that can be assigned an IP address and provided with the ability to transfer data over a network.

##### Create a device
```
~$ioxclient svc infrastructure prov devices cr -f test_resources\middleware-files\device.json

Currently active profile :  vm211
Command Name: service-infrastructure-provisioning-devices-create
Sending https request to  https://10.78.106.211:40001/api/v1/mw/provisioning/devices/
Successfully added the  device
```

##### Device Info

```
~$ioxclient svc infrastructure prov devices info

Currently active profile :  vm211
Command Name: service-infrastructure-provisioning-devices-info
https://10.78.106.211:40001/api/v1/mw/provisioning/devices/
{
        "kind": "model#device#collection",
        "devices": [
                {
                        "kind": "model#device",
                        "description": "",
                        "displayName": "",
                        "createdAt": "2016-06-08T20:39:37.362+0000",
                        "updatedAt": "2016-06-08T20:39:37.362+0000",
                        "deviceId": "DeviceA",
                        "deviceTypeId": "TestModbusDeviceType",
                        "metadata": {
                                "skuCode": "sk3465tyu",
                                "serialNo": "567e",
                                "urn": "shipping/container/A",
                                "additionalProperties": {}
                        },
                        "connectionProperties": [
                                {
                                        "protocol": "modbus",
                                        "properties": {
                                                "host": "10.10.10.10",
                                                "port": 502,
                                                "pollingInterval": 10,
                                                "healthCheckInterval": 5000
                                        }
                                }
                        ]
                }
        ]
}
```

##### Delete a device
```
~$ioxclient svc infrastructure prov dev del DeviceA

Currently active profile :  vm211
Command Name: service-infrastructure-provisioning-devices-delete
Url is  https://10.78.106.211:40001/api/v1/mw/provisioning/devices/DeviceA         Successfully Deleted  device   DeviceA

```

> Note: A device is dependent on a device type which is also dependent on a dataschema. And hence, in order to remove a dataschema, there should not be any device type using that particular dataschema, and no device should come under that device type.

#### IOx Messaging Service

##### Managing topics

Commands under managing topics are:

```
~$ioxclient service infrastructure messaging topics
NAME:
ioxclient service infrastructure messaging topics - create/delete/publish topics

USAGE:
ioxclient service infrastructure messaging topics command [command options] [arguments...]

COMMANDS:
create, cr   Create a topic
delete, del  Delete a topic
publish, pub Publish into a topic
help, h      Shows a list of commands or help for one command

```

###### Creating a topic

Any topic of the user's choice can be created by specifying a name for a topic to be created

```
~$ioxclient svc infrastructure messaging topics cr sampleTopic

Currently active profile :  vm211
Command Name: service-infrastructure-topics-create
Url formed is -  https://10.78.106.211:40001/api/v1/mw/topics/sampleTopic
Successfully added Topic
```

###### Publishing to a topic

Data can be published to a topic either by passing the json data in the required format as command line argument or by specifying a file using the --file flag

```
~$ioxclient svc infrastructure messaging topics publish --file test_resources\middleware-files\topics.json

Currently active profile :  vm211
Command Name: service-infrastructure-topics-publish-create
Sending https request to  https://10.78.106.211:40001/api/v1/mw/topics/publish/
{
    "topic": "sampleTopic",
    "context" : {
        "prop1": "value1",
        "prop2": "value2"
    },
    "message" : {
        "id": 5,
        "severity": "warn",
        "description": "unable to contact northbound"
    }
}


Successfully published the  topic
```

###### Deleting a topic

A topic can be deleted by specifying the name of the topic

```
~$ioxclient svc infrastructure messaging topics del sampleTopic

Currently active profile :  vm211
Command Name: service-infrastructure-topics-delete
Url is  https://10.78.106.211:40001/api/v1/mw/topics/sampleTopic
Successfully Deleted sampleTopic

```
##### Publish / Subscribe Messages using Websockets

IOx Service infrastructure allows using websockets to allow the user to publish or subscribe to/from a topics.

```
~$ioxclient service infrastructure websocket

NAME:
   ioxclient service infrastructure websocket - To stream data from the socket

USAGE:
   ioxclient service infrastructure websocket command [command options] [arguments...]

COMMANDS:
   subscribe, sub       Stream data from a websocket
   publish, pub         Publish data through a websocket
   help, h              Shows a list of commands or help for one command
```
###### Topic Subscription using websocket

```
~$ioxclient svc infra msg ws sub sampleTopic

Currently active profile :  vm211
Command Name: service-infrastructure-messaging-websocket-subscribe
{"context":{"prop1":"value1","prop2":"value2"},"topic":"sampleTopic","message":{"id":5,"severity":"warn","description":"This is a sample publish"}}
{"context":{"prop1":"value1","prop2":"value2"},"topic":"sampleTopic","message":{"id":5,"severity":"warn","description":"This is a sample 2nd publish"}}
{"context":{"prop1":"value1","prop2":"value2"},"topic":"sampleTopic","message":{"id":5,"severity":"warn","description":"This is a sample 3rd publish"}}
```

###### Publish Messages Using websocket

```
~$ioxclient svc infra msg ws pub test_resources\middleware-files\topics.json

Currently active profile :  vm211
Command Name: service-infrastructure-messaging-websocket-publish
No of characters written  247
```

#### IOx Service Infrastructure - Metrics

In order to aid in troubleshooting issues, IOX Service Infrastructure maintains various metrics. These metrics are mostly in the form of counters, meters, guages, histograms, etc

##### View metrics

```
~$ioxclient service infrastructure metrics
Currently active profile :  vm211
Command Name: service-infrastructure-metrics
https://10.78.106.211:40001/api/v1/mw/metrics
0 .  system:service:protocolHandler:mqtt-broker
1 .  system:service:mqttstoreandforward
2 .  logconfig
3 .  system:service:coapstoreandforward
4 .  token
5 .  system:service:coap-proxy
6 .  system:service:protocolHandler:modbus-async-tcp
7 .  system:service:protocolHandler:coap-server
8 .  mlib-rpc.IOxMiddlewareServices
9 .  mlib-threadpool.IOxMiddlewareServices
10 .  system:service:provisioning
11 .  system:service:data:snapshot
14 .  mlib-pubsub.IOxMiddlewareServices
Enter the serial Number of the required metric
1
{
       "stats": [
               {
                       "name": "numberOfNBIRequestsFailed",
                       "type": "counter",
                       "count": 0
               },
               {
                       "name": "numberOfNBIRequestsSucceeded",
                       "type": "counter",
                       "count": 0
               },
               {
                       "name": "numberOfPolicies",
                       "type": "counter",
                       "count": 0
               }
       ],
       "policies": {
               "type": "composite",
               "kind": "sf#policy#collection"
       }
}

```

### Log services

The log services allow us to list the modules and their log levels of a particular service. A user could also set the log level of a particular module with this command
The command structure of log services is

```
~$ioxclient service infrastructure logservice --help
NAME:
   logservice - Use log services to view the available modules and set their log levels

USAGE:
   command logservice [command options]

DESCRIPTION:
   To list the modules of a service -
ioxclient service infra --service service_name
In order to set the log level of a module in a given service,
ioxclient service infra --service svc_name --module mod_name -- level log_level

OPTIONS:
   --service, --svc     Specify the service of the module
   --module, --mod      Specify the module who's log level has to be set
   --level, --lvl       Specify the log level that is to be set

```

#### List modules

To list th modules and their log levels of a given service, specify the service name using the --service flag as follows

```
~$ioxclient service infra logservice --svc mw
Currently active profile :  vm211
Command Name: service-infrastructure-logservice
Sending HTTP request to  -  https://10.78.106.211:40001/api/v1/mw/logs/mw/modules
-------------HTTP Response----------------
{
 "system:service:protocolHandler:modbus-async-tcp": "warning",
 "urn:cisco:system:service:data:snapshot": "trace",
 "urn:cisco:system:service:provisioning": "error"
}
```

#### Set log level module

To set the log level of a module, specify the service name using the --service flag, the module with the --module flag and the log level using the --level flag
The log levels could be INFO, WARN,ERROR,DEBUG,TRACE

```
~$ioxclient service infra logservice --service mw --module system:service:protocolHandler:modbus-async-tcp --level trace
Currently active profile :  vm211
Command Name: service-infrastructure-logservice
Sending HTTP request to  -  https://10.78.106.211:40001/api/v1/mw/logs/mw/modules/system:service:protocolHandler:modbus-async-tcp?level=trace
Successfully changed the log level of  system:service:protocolHandler:modbus-async-tcp  to  trace
```

In order to verify the succesful setting of the log level, list the modules using
```
~$ioxclient service infra logservice --service mw
```

The log level of the module which was updated should show the same log level
In the above example, we set the log level of "system:service:protocolHandler:modbus-async-tcp" to "trace"
Hence, the list should be displaying this -
```
~$ioxclient service infra logservice --service mw
Currently active profile :  vm211
Command Name: service-infrastructure-logservice
Sending HTTP request to  -  https://10.78.106.211:40001/api/v1/mw/logs/mw/modules
-------------HTTP Response----------------
{
 "system:service:protocolHandler:modbus-async-tcp": "trace",
 "urn:cisco:system:service:data:snapshot": "trace",
 "urn:cisco:system:service:provisioning": "error"
}
```

## Commands For Docker Workflow

On select platforms, developers will be able to utilize well known docker tools to easily create applications for IOx platforms. `ioxclient` provides convenient wrapper CLIs to aid in this process.

> **To use the below commands, A machine (remote or local) with the Docker daemon installed is required. ioxclient uses client libraries to make a connection to the daemon. These connection settings can be configured using init command at any time. By default, the settings will automatically be configured to use this local machine as the target. It is recommended that the target machine have a minimum Docker version of 1.10 (API 1.22).

```
$ ioxclient docker
NAME:
   ioxclient docker - Commands for using docker tools for IOx app development

USAGE:
   ioxclient docker command [command options] [arguments...]


COMMANDS:
   package, pkg	Package an existing docker image as an IOx application
   help, h	Shows a list of commands or help for one command
   init, in	Initialize configuration for internal Docker client

OPTIONS:
   --help, -h			show help
   --generate-bash-completion

```
### Configure internal Docker client settings using the Init command

By default, ioxclient will set to connect locally via Unix socket to the Docker daemon upon using any Docker related commands. If the target Docker server is not your local machine, the client settings can be changed to point to the correct server. The API version can also be adjusted to match the server to ensure compatibility.

> NOTE: At this time, ioxclient only supports http connections without authentication (in addition to local Unix sockets).

```
$ ioxclient docker init
Enter the URI for the Docker daemon to use[unix:///var/run/docker.sock]: http://sample.cisco.com:2376
Enter the API version that the target daemon is running[v1.22]: 1.24
Saving current configuration
```

### Packaging an existing docker image as IOx application

With docker workflow support, you can use any existing docker image (public/private) and convert it to an IOx compatible image.

> NOTE: The size of the iox application package may be huge depending on the docker image that you are using. If the size exceeds the available resources on your target platform, you may not be able to install the application.

```
$ ioxclient  docker package
Insufficient Args.

NAME:
   package - Package an existing docker image as an IOx application

USAGE:
   command package [command options] <docker_image> <project_dir>

DESCRIPTION:

Usage: ioxclient docker package <image_name> <project_dir>
image_name
  -> is a valid docker image name.
project_dir
  -> should be a directory location that has the required IOx files.
  At a minimum, must have package.yaml file. Can also contain other
  files such as package_config.ini etc.,

Example: docker package cisco/alpine:3.3 .
image_name is cisco/alpine:3.3
project_dir is "." signifying current directory

To generate layers from a docker image: 
        ioxclient docker package --layers <image_name> <project_dir>
To generate layers from an IOx package:
        ioxclient docker package --layers <iox_package> <project_dir>


OPTIONS:
	--package-type, -p		Use this option to specify the rootfs type: ext2 or ufs.
	--auto, -a			Use this flag to build IOx package according to labels in the docker image.This option has lower precedence over package-type option
	--use-targz			Use this to use gz compression on package
	--skip-schema-validation	Use this flag to skip package descriptor schema validation
	--descriptor-merge, -m		enable addition/override of information from docker inspect to package.yaml
	--labels, -l			Pass label(s) to be translated into IOx application descriptor fields.
	--headroom, -r '0'		For LXC type apps, specify the headroom (in MB) that needs to be created in the rootfs. Default is 5MB or 20 percent of rootfs size, whichever is greater
	--layers, -s			Use this flag to package docker image as IOx compatible layers
	--rsa-key, -k			Use this option to specify a RSA key in PEM format to sign the package
	--certificate, -c		Use this option to specify a x509 Certificate in PEM format
	--skip-signing			Use this option to skip package signing

```

To package, you will need to supply :

* Image name of the docker image to be used. If the image is not locally present, it will be pulled from the registry configured in the docker daemon on your system.
* Path to a project directory that contains IOx related files. A package descriptor file (`package.yaml`) is no longer required but recommended if readily available or if strict values are required. Otherwise ioxclient will generate a descriptor file from the LABELS in the specified Docker image. The directory can contain other optional files (ex. `package_config.ini` etc.,)

`ioxclient` uses its internal Docker client to connect to the remote Docker server/daemon as configured in the ioxclient configuration file. This will silently default to the system's Docker daemon but can be changed using the docker init commmand.  Contacts the configured Docker daemon in the background to save the docker image in an IOx compatible format and produces a `rootfs.tar` file that contains the contents of the original docker image. It then uses the files present in the project directory to create a IOx application package and prints out the path. 

> **NOTE: The docker image name supplied should already be pulled and present in the configured docker daemon.**

The outcome of package descriptor file (`package.yaml`) generation differs based on the existence of the file and whether other options were specified.

1. package.yaml exists in project folder.
* If the package descriptor file is present, ioxclient will use this exact copy to include in the generated package. This was original default behavior when this CLI was originally introduced.

2. package.yaml exists in project folder and the --descriptor-merge flag is enabled.
* With the --descriptor-merge flag specified and the package.yaml file present in project folder, ioxclient will merge information from the Docker image (LABELS, CMD, AUTHOR, etc.) and the existing package.yaml. Information from the Docker image will only override fields that can be translated, otherwise the rest of the fields will be left as is in the final package.yaml.

3. package.yaml exists in project folder and --descriptor-merge and --labels flags are specified.
* In addition to having an existing package.yaml and --descriptor-merge option, --labels flags provides the user with the ability to change fields in resultant package.yaml directly through ioxclient. Labels specified via command line will override those from Docker metadata and existing in the package.yaml. See section on Label Format below.

4. No package.yaml is present
* ioxclient will attempt to generate a package.yaml on the fly using the metadata of the Docker image specified. A copy will be placed in the project directory.

5. No package.yaml is present with --labels option specified.
* Will allow the user to change fields in the generated package.yaml in addition to those brought in by Docker image metadata. Labels specified via command line will override those specified in image.. See section on Labels

An example of package generation with an existing package.yaml file:

```
$ pwd
/home/hvishwanath/projects/sample-apps-v2/docker/nodeapp
$ ls -la
total 12
drwxrwxr-x 2 hvishwanath hvishwanath 4096 Aug 23 14:51 .
drwxrwxr-x 6 hvishwanath hvishwanath 4096 Aug 19 16:07 ..
-rw-rw-r-- 1 hvishwanath hvishwanath  513 Aug 23 14:51 package.yaml

$ ioxclient docker package cisco/baserootfs:latest .
Currently active profile :  local
Command Name: docker-package
Attempting to save docker image  cisco/baserootfs:latest
Running command : [docker save cisco/baserootfs:latest -o rootfs.tar]
Checking if package descriptor file is present..
Created Staging directory at :  /tmp/hvishwanath/903471683
Copying contents to staging directory
Checking for application runtime type
Couldn't detect application runtime type
Creating an inner envelope for application artifacts
Generated  /tmp/hvishwanath/903471683/artifacts.tar.gz
Calculating SHA1 checksum for package contents..
Root Directory :  /tmp/hvishwanath/903471683
Output file:  /tmp/hvishwanath/152127686
Path:  artifacts.tar.gz
SHA1 : ae8ebd3e64febc14f09452d2e5f18745d277e60f
Path:  package.yaml
SHA1 : 2675a7d79f514bb77dd4943d4ae67875da6418aa
Generated package manifest at  package.mf
Generating IOx Package..
Package docker image cisco/baserootfs:latest at /home/hvishwanath/projects/sample-apps-v2/docker/nodeapp/package.tar
```

An example to generate a signed package.

To generate a signed package, a private key and corresponding x509 Certificate in PEM format are required.

```
dev@dev-VirtualBox:~/Documents/iox/alpine/pkg$ ls -l
total 0
dev@dev-VirtualBox:~/Documents/iox/alpine/pkg$ ioxclient docker package -k ~/iox/key.pem -c ~/iox/cert.pem alpine:3.3 ./
Currently active profile :  default
Command Name:  docker-package
Warning: package.yaml not present in project folder. Will attempt to generate one.
No app type specified.
Checking device capabilitties using active profile.
WARNING: Unable to get device capabilities using active profile.
Generating IOx package of type docker with rootfs consisting of layers
Removing emulation layers in docker rootfs, if any
The docker image is better left in it's pristine state
Replacing symbolically linked layers in docker rootfs, if any
Finding the minimum schema version for the descriptor file
Setting the descriptor schema version to 2.2
Validating generated descriptor file.
Validating descriptor file /tmp/desc221599723 with package schema definitions
Parsing descriptor file..
Found schema version  2.2
Loading schema file for version  2.2
Validating package descriptor file..
File /tmp/desc221599723 is valid under schema version 2.2
Package MetaData file was not found at  /home/dev/Documents/iox/alpine/pkg/.package.metadata
Wrote package metadata file :  /home/dev/Documents/iox/alpine/pkg/.package.metadata
Using rsa key and cert provided via command line to sign the package
Checking if package descriptor file is present..
Skipping descriptor schema validation..
Created Staging directory at :  /tmp/954550862
Copying contents to staging directory
Checking for application runtime type
Couldn't detect application runtime type
Creating an inner envelope for application artifacts
Including  rootfs.tar
Generated  /tmp/954550862/artifacts.tar.gz
Calculating SHA1 checksum for package contents..
Parsing Package Metadata file :  /tmp/954550862/.package.metadata
Wrote package metadata file :  /tmp/954550862/.package.metadata
Root Directory :  /tmp/954550862
Output file:  /tmp/715460437
Path:  .package.metadata
SHA1 : fc3ce3b8ee377e6149a9ccff2b03e28a97102fbb
Path:  artifacts.tar.gz
SHA1 : 7091ca785b96cebdd7eedd65d9c3b4fd103ecbfb
Path:  package.yaml
SHA1 : 425f4de862257214106e2fa70494078bd359a74a
Generated package manifest at  package.mf
Signed the package and the signature is available at package.cert
Generating IOx Package..
Package docker image alpine:3.3 at /home/dev/iox/alpine/pkg/package.tar

```



An example using Dockerfile labels.

First we'll inspect the Dockerfile contents:
```
$ cat Dockerfile
FROM alpine:3.3

RUN apk add --update nodejs -X http://dl-4.alpinelinux.org/alpine
COPY server.js /server.js

LABEL cisco.resources.profile=custom \
      cisco.resources.cpu=500 \
      cisco.resources.memory=256 \
      cisco.resources.disk=50 \
      cisco.resources.network.0.interface-name=eth0 \
      cisco.resources.network.0.ports.tcp=[9000,9001]

EXPOSE 8000
CMD ["node", "/server.js"]
```

Build the new image using the Docker CLIs:

```
$ sudo docker build -t iox-nodejs .
Sending build context to Docker daemon 3.072 kB
Step 1 : FROM alpine:3.3
 ---> 6c2aa2137d97
Step 2 : RUN apk add --update nodejs -X http://dl-4.alpinelinux.org/alpine
 ---> Using cache
 ---> 823e5e51b3f5
Step 3 : COPY server.js /server.js
 ---> Using cache
 ---> 052a5acba3e0
Step 4 : LABEL cisco.resources.profile custom cisco.type docker cisco.resources.cpu 500 cisco.resources.memory 256 cisco.resources.disk 50 cisco.resources.network.0.interface-name eth0 cisco.resources.network.0.ports.tcp [9000,9001]"
 ---> Running in 66fa72a57586
 ---> f3f2aaa59d4f
Removing intermediate container 66fa72a57586
Step 5 : EXPOSE 8000
 ---> Running in cbfa6ffc0c38
 ---> d14acf591149
Removing intermediate container cbfa6ffc0c38
Step 6 : CMD node /server.js
 ---> Running in 16a72cf1445a
 ---> 12f28e6877f5
Removing intermediate container 16a72cf1445a
Successfully built 12f28e6877f5
```

Now build the IOx package using ioxclient and specify the newly created Docker image:

```
$ sudo ioxclient docker package iox-nodejs .
Currently active profile : IR829
Command Name: docker-package
Warning: package.yaml not present in project folder. Will attempt to generate one.
app type is docker. Retrieving ufs capability info
Checking device capabilitties using active profile.
WARNING: Unable to get device capabilities using active profile.
Generating IOx package of type docker with rootfs consisting of layers
Removing emulation layers in docker rootfs, if any
The docker image is better left in it's pristine state
Replacing symbolically linked layers in docker rootfs, if any
Finding the minimum schema version for the descriptor file
Setting the descriptor schema version to 2.2
Validating generated descriptor file.
Validating descriptor file /tmp/desc687408607 with package schema definitions
Parsing descriptor file..
Found schema version  2.2
Loading schema file for version  2.2
Validating package descriptor file..
File /tmp/desc687408607 is valid under schema version 2.2
Package MetaData file was not found at  /home/dev/Documents/iox/alpine/.package.metadata
Wrote package metadata file :  /home/dev/Documents/iox/alpine/.package.metadata
No rsa key and/or certificate files to sign the package
Checking if package descriptor file is present..
Skipping descriptor schema validation..
Created Staging directory at :  /tmp/681579954
Copying contents to staging directory
Checking for application runtime type
Couldn't detect application runtime type
Creating an inner envelope for application artifacts
Including  rootfs.tar
Generated  /tmp/681579954/artifacts.tar.gz
Calculating SHA1 checksum for package contents..
Parsing Package Metadata file :  /tmp/681579954/.package.metadata
Wrote package metadata file :  /tmp/681579954/.package.metadata
Root Directory :  /tmp/681579954
Output file:  /tmp/700032873
Path:  .package.metadata
SHA1 : 877217f33ea6957debc918c3bdc96d255ce37d60
Path:  artifacts.tar.gz
SHA1 : 75dbb9a63650f14b1ec8b406a4c6a61e78852ab4
Path:  package.yaml
SHA1 : e66668bc7c4d243cffe184252631698c04b9c106
Generated package manifest at  package.mf
Generating IOx Package..
Package docker image iox-nodejs at /repo/packages/iox/apps/docker/nodejs/tmp/package.tar
```

package.yaml should contain fields that were specified using the LABEL directive in the Dockerfile along with the CMD (starting process for container) and EXPOSE (expose ports):
```
$ cat package.yaml
descriptor-schema-version: "2.2"
info:
  name: iox-nodejs
  version: latest
app:
  cpuarch: x86_64
  resources:
    cpu: "500"
    disk: "50"
    memory: "256"
    network:
    - interface-name: eth0
      ports:
        tcp:
        - "9000"
        - "9001"
        - "8000"
    profile: custom
  startup:
    rootfs: rootfs.tar
    target:
    - '"node"'
    - '"/server.js"'
  type: docker
```

### IOx package descriptor fields defined in Dockerfile

Certain IOx descriptor fields can be incorporated in Docker images using the LABEL instruction when building from Dockerfile. This allow specific resources such as disk, memory, CPU architecture, etc. to be predefined when automatically generating the package descriptor upon package creation.

The format for the label is a key/value pair with the key prepended with the string “cisco” to differentiate from other labels that the author may include in the image. The key needs to follow the node structure of the IOx package descriptor schema (starts at the “app” root) in order for the resultant file to be valid. The value can be written as a plain old string or a set of values.

Reference on the syntax of inputting Labels in Dockerfile can be found here:
https://docs.docker.com/engine/reference/builder/#/label


Examples below of Dockerfile snippets:

Adding a simple profile definition:

```
LABEL cisco.resources.profile c1.large
```

Defining the resource profile for the container and defining the network device name along with additional ports to map to container (when NAT’ing is enabled):

```
LABEL cisco.resources.profile=c1.large \
      cisco.resources.network.0.interface-name=eth0 \
      cisco.resources.network.0.ports.tcp=[9000,9001]
```

* For boolean values (true and false), please use the following format: "**'\<value\>'**"

* Note that the network node is described as an array in the package descriptor schema so the proceeding node in this notation will be the index of the element trying to be accessed starting from 0.

* Also, note that values can be written in array format using brackets to enclose the list and commas to separate each value without spaces in between.

A example on how to generate a complete package descriptor file using LABELs

```

LABEL cisco.info.name="Cisco agent" \
      cisco.info.description="Cisco agent for CAT9K" \
      cisco.info.version="0.1" \
      cisco.info.author-link="http://www.cisco.com" \
      cisco.info.author-name="Cisco Systems" \
      cisco.type=docker \
      cisco.cpuarch=x86_64 \
      cisco.resources.profile=custom \
      cisco.resources.cpu=500 \
      cisco.resources.memory=256 \
      cisco.resources.disk=50 \
      cisco.resources.network.0.interface-name=eth0 \
      cisco.resources.network.0.ports.tcp=[9000,9001] \
      cisco.resources.devices.0.type=usbdev \
      cisco.resources.devices.0.label="HOST_DEV829" \
      cisco.resources.devices.0.usage="Brief description of usage" \
      cisco.resources.devices.0.function="storage" \
      cisco.resources.devices.0.mandatory="'true'" \
      cisco.resources.devices.0.mount-point="/extra/storage/"

EXPOSE 8000
CMD ["node", "/server.js"]

```

Below is the corresponding package descriptor file generated by ioxclient

```
descriptor-schema-version: "2.5"
info:
  name: Cisco agent
  description: Cisco agent for CAT9K
  version: "0.1"
  author-link: http://www.cisco.com
  author-name: Cisco Systems
app:
  cpuarch: x86_64
  resources:
    cpu: "500"
    devices:
    - function: storage
      label: HOST_DEV829
      mandatory: true
      mount-point: /extra/storage/
      type: usbdev
      usage: Brief description of usage
    disk: "50"
    memory: "256"
    network:
    - interface-name: eth0
      ports:
        tcp:
        - "9000"
        - "9001"
        - "8000"
    profile: custom
    visualization: true
  startup:
    rootfs: rootfs.tar
    target:
    - '"node"'
    - '"/server.js"'
  type: docker

```

### Generating an LXC package
To generate an IOx package of type LXC please look at the below example. 

Please note that LXC package generation is only supported in Linux and Darwin based operating systems

```
dev@dev-VirtualBox:~/iox/alpine/pkg$ sudo ioxclient docker package alpine:3.3 ./
Currently active profile :  caf
Command Name:  docker-package
Using the package descriptor file in the project dir
Validating descriptor file package.yaml with package schema definitions
Parsing descriptor file..
Found schema version  2.2
Loading schema file for version  2.2
Validating package descriptor file..
File package.yaml is valid under schema version 2.2
Generating IOx LXC package
Docker image rootfs size in 1M blocks:  5
Creating iox package with rootfs size in 1M blocks:  10
Parsing Package Metadata file :  /home/dev/iox/alpine/pkg/.package.metadata
Wrote package metadata file :  /home/dev/iox/alpine/pkg/.package.metadata
No rsa key and/or certificate files to sign the package
Checking if package descriptor file is present..
Skipping descriptor schema validation..
Created Staging directory at :  /tmp/960654222
Copying contents to staging directory
Checking for application runtime type
Couldn't detect application runtime type
Creating an inner envelope for application artifacts
Generated  /tmp/960654222/artifacts.tar.gz
Calculating SHA1 checksum for package contents..
Parsing Package Metadata file :  /tmp/960654222/.package.metadata
Wrote package metadata file :  /tmp/960654222/.package.metadata
Root Directory :  /tmp/960654222
Output file:  /tmp/147610005
Path:  .package.metadata
SHA1 : 44a53959f93c3013442f8fd9266fb6843d9d9ada
Path:  artifacts.tar.gz
SHA1 : fa7a0347e046eab3dd768998fc9252b2c0dd5aef
Path:  package.yaml
SHA1 : 7c224ba9655d5ec8f9c9feb5b3bcfd13060af30d
Generated package manifest at  package.mf
Generating IOx Package..
Package docker image alpine:3.3 at /home/dev/iox/alpine/pkg/package.tar

```

* Note: One can increase the size of the rootfs by using the "--headroom" option to specify the additional disk space (in MB) that needs to be added 

## Docker Layering support in IOx
Going forward, IOx will support deployment of individual docker layers packaged using ioxclient. This way, everytime an application is installed on a device, some or all of the available layers on the device that an application is dependent on will be reused, instead of copying them. This will greatly reduce the bandwidth required to deploy applications with common docker layers.

Below are some of the examples on how to generate and deploy applications using layering support in IOx.

### Generate Individual Layers From Docker Image

To generate individual layers from a docker image use the below command.

```

dev@dev-VirtualBox:~/iox/alpine/pkg$ ioxclient docker package --layers alpine:3.3 ./
Currently active profile :  default
Command Name:  docker-package
Warning: package.yaml not present in project folder. Will attempt to generate one.
Retrieving docker image 
Generating IOx Layers
Generating package metadata
Finding the minimum schema version for the descriptor file
Setting the descriptor schema version to 2.2
Validating generated descriptor file.
Validating descriptor file /tmp/desc052669482 with package schema definitions
Parsing descriptor file..
Found schema version  2.2
Loading schema file for version  2.2
Validating package descriptor file..
File /tmp/desc052669482 is valid under schema version 2.2
Parsing Package Metadata file :  /home/dev/iox/alpine/pkg/.package.metadata
Wrote package metadata file :  /home/dev/iox/alpine/pkg/.package.metadata
Generating IOx app package
No rsa key and/or certificate files to sign the package
Checking if package descriptor file is present..
Skipping descriptor schema validation..
Checking if package descriptor file is present..
Skipping descriptor schema validation..
Created Staging directory at :  /tmp/300082412
Copying contents to staging directory
Checking for application runtime type
Couldn't detect application runtime type
Creating an inner envelope for application artifacts
Generated  /tmp/300082412/artifacts.tar.gz
Calculating SHA1 checksum for package contents..
Parsing Package Metadata file :  /tmp/300082412/.package.metadata
Wrote package metadata file :  /tmp/300082412/.package.metadata
Root Directory :  /tmp/300082412
Output file:  /tmp/792682843
Path:  .package.metadata
SHA1 : b5b32f07e95f21fb846af21789649408b8023f29
Path:  artifacts.tar.gz
SHA1 : b1bf4c45a010b0d2f79b860f2dd393865e267436
Path:  package.yaml
SHA1 : 425f4de862257214106e2fa70494078bd359a74a
Generated package manifest at  package.mf
Generating IOx Package..
Package docker image alpine:3.3 at /home/dev/iox/alpine/pkg/package.tar, iox layers: iox_layers

```

Generated layers will be placed in a directory named "iox\_layers" inside the project directory. 
If a need arises to modify the package.yaml or package\_config.in files  and repackage the application, use the "iox\_layers" directory to create an IOx compatible package (ioxclient package). 

An example to package an application using already generated layers.

```
dev@dev-VirtualBox:~/iox/alpine/pkg$ ls -l
total 8
drwxrwxr-x 2 dev dev 4096 Jul 24 11:57 iox_layers
-rwxr--r-- 1 dev dev  212 Jul 24 11:57 package.yaml

dev@dev-VirtualBox:~/iox/alpine/pkg$ ioxclient package --layers ./iox_layers/ ./
Currently active profile :  default
Command Name:  package
No rsa key and/or certificate files to sign the package
Checking if package descriptor file is present..
Validating descriptor file /home/dev/iox/alpine/pkg/package.yaml with package schema definitions
Parsing descriptor file..
Found schema version  2.2
Loading schema file for version  2.2
Validating package descriptor file..
File /home/dev/iox/alpine/pkg/package.yaml is valid under schema version 2.2
Checking if package descriptor file is present..
Skipping descriptor schema validation..
Created Staging directory at :  /tmp/116629525
Copying contents to staging directory
Checking for application runtime type
Couldn't detect application runtime type
Creating an inner envelope for application artifacts
Generated  /tmp/116629525/artifacts.tar.gz
Calculating SHA1 checksum for package contents..
Parsing Package Metadata file :  /tmp/116629525/.package.metadata
Wrote package metadata file :  /tmp/116629525/.package.metadata
Root Directory :  /tmp/116629525
Output file:  /tmp/626259568
Path:  .package.metadata
SHA1 : 11f4783460e5faec6797e9e693d174192d5466fd
Path:  artifacts.tar.gz
SHA1 : 299b79f918ed33a41dcfd3d91e3a11c1cee55af2
Path:  package.yaml
SHA1 : 425f4de862257214106e2fa70494078bd359a74a
Generated package manifest at  package.mf
Generating IOx Package..
Package generated at /home/dev/iox/alpine/pkg/package.tar

```

* The generated package does not the include actual layers. So, to install an application using the above generated package, all the required layers should already be deployed on the device.
* For a much easier way to install an application using layers, we recommend the "ioxclient application install --layers " command.

An example to generate layers from an existing IOx docker application package

```

dev@dev-VirtualBox:~/iox/alpine/pkg$ ioxclient docker package --layers ./package.tar ./
Currently active profile :  caf
Command Name:  docker-package
Extracting rootfs.tar from provided IOx package
Using the package descriptor file in the project dir
Validating descriptor file package.yaml with package schema definitions
Parsing descriptor file..
Found schema version  2.2
Loading schema file for version  2.2
Validating package descriptor file..
File package.yaml is valid under schema version 2.2
Generating IOx Layers
Generating package metadata
Parsing Package Metadata file :  /home/dev/iox/alpine/pkg/.package.metadata
Wrote package metadata file :  /home/dev/iox/alpine/pkg/.package.metadata
Generating IOx app package
No rsa key and/or certificate files to sign the package
Checking if package descriptor file is present..
Skipping descriptor schema validation..
Checking if package descriptor file is present..
Skipping descriptor schema validation..
Created Staging directory at :  /tmp/893768253
Copying contents to staging directory
Checking for application runtime type
Couldn't detect application runtime type
Creating an inner envelope for application artifacts
Generated  /tmp/893768253/artifacts.tar.gz
Calculating SHA1 checksum for package contents..
Parsing Package Metadata file :  /tmp/893768253/.package.metadata
Wrote package metadata file :  /tmp/893768253/.package.metadata
Root Directory :  /tmp/893768253
Output file:  /tmp/627339896
Path:  .package.metadata
SHA1 : 38d3627bb74664642c3b2d90ea5a5008c8e7aa98
Path:  artifacts.tar.gz
SHA1 : 2d7f919cd89912dcee072ef7a93589953b0cb86c
Path:  package.yaml
SHA1 : 425f4de862257214106e2fa70494078bd359a74a
Generated package manifest at  package.mf
Generating IOx Package..
Package docker image  at /home/dev/iox/alpine/pkg/package.tar, iox layers: iox_layers

dev@dev-VirtualBox:~/iox/alpine/pkg$ ls -l
total 16
drwxrwxr-x 2 dev dev 4096 Jul 24 13:55 iox_layers
-rw-rw-r-- 1 dev dev 6144 Jul 24 13:55 package.tar
-rwxr--r-- 1 dev dev  212 Jul 24 13:55 package.yaml

```

* Note: Do not use the directory where the original package.tar is present as the project directory. The command will overwrite the original package.tar file. 

### Installing an Application From a Docker Image
To install an application directly from a docker image instead of going through packaging and installation steps, please look at the below example.

```

dev@dev-VirtualBox:~/iox/alpine/pkg$ ioxclient application install --layers test ./ alpine:3.3
Currently active profile :  caf
Command Name:  application-install
Warning: package.yaml not present in project folder. Will attempt to generate one.
Retrieving docker image 
Generating IOx Layers
Generating package metadata
Finding the minimum schema version for the descriptor file
Setting the descriptor schema version to 2.2
Validating generated descriptor file.
Validating descriptor file /tmp/desc367045569 with package schema definitions
Parsing descriptor file..
Found schema version  2.2
Loading schema file for version  2.2
Validating package descriptor file..
File /tmp/desc367045569 is valid under schema version 2.2
Parsing Package Metadata file :  /home/dev/iox/alpine/pkg/.package.metadata
Wrote package metadata file :  /home/dev/iox/alpine/pkg/.package.metadata
Generating IOx app package
No rsa key and/or certificate files to sign the package
Checking if package descriptor file is present..
Skipping descriptor schema validation..
Checking if package descriptor file is present..
Skipping descriptor schema validation..
Created Staging directory at :  /tmp/005324187
Copying contents to staging directory
Checking for application runtime type
Couldn't detect application runtime type
Creating an inner envelope for application artifacts
Generated  /tmp/005324187/artifacts.tar.gz
Calculating SHA1 checksum for package contents..
Parsing Package Metadata file :  /tmp/005324187/.package.metadata
Wrote package metadata file :  /tmp/005324187/.package.metadata
Root Directory :  /tmp/005324187
Output file:  /tmp/947273278
Path:  .package.metadata
SHA1 : 0a31b6b204d9d3e99d009fed2d29114035fc0eee
Path:  artifacts.tar.gz
SHA1 : 7bb3e4c09e02ee78e3759d1b6ef72532097817b7
Path:  package.yaml
SHA1 : 425f4de862257214106e2fa70494078bd359a74a
Generated package manifest at  package.mf
Generating IOx Package..
Package docker image alpine:3.3 at /home/dev/iox/alpine/pkg/package.tar, iox layers: iox_layers
Following layers are missing on the device:  "9d2df2afed0b40cfecf86308306882a37f983aa3fd93e32ba352cbc5a731328f"
Installing layer  iox_layers/9d2df2afed0b40cfecf86308306882a37f983aa3fd93e32ba352cbc5a731328f.tar.gz
Layer got added successfully.Successfully uploaded the layer 9d2df2afed0b40cfecf86308306882a37f983aa3fd93e32ba352cbc5a731328f
Installation Successful. App is available at : https://10.41.50.94:8443/iox/api/v2/hosting/apps/test 
Successfully deployed

dev@dev-VirtualBox:~/Documents/iox/img/ac5/x86/alpine/pkg$ 
dev@dev-VirtualBox:~/Documents/iox/img/ac5/x86/alpine/pkg$ ioxclient application list
Currently active profile :  caf
Command Name:  application-list
List of installed App : 
 1. test       --->   DEPLOYED

```
* Note: Using the above command, one can also deploy a signed package by providing the key and certificate using -k and -c options.

### Manage Docker Applications' Layers
To manage the life cycle of docker applications' layers on the platform/device refer to the below command

```

dev@dev-VirtualBox:~$ ioxclient layer
NAME:
   ioxclient layer - Manage life cycle of application layers

USAGE:
   ioxclient layer command [command options] [arguments...]

COMMANDS:
   list, l  List deployed layers on the device
   add, a   add/deploy a particular layer to the device
   delete, d    delete a particular layer or all unused layers on the device
   help, h  Shows a list of commands or help for one command
   
OPTIONS:
   --help, -h           show help
   --generate-bash-completion   
   
``` 

#### Get a List of all the layers deployed 
To get a list of all the layers currently deployed on the device, in JSON format, use the below command

```
dev@dev-VirtualBox:~$ ioxclient layer list
Currently active profile :  829
Command Name:  layer-list
List of deployed layers:
{
 "layers": [
  {
   "docker_id": "cf6fd3a072756da50619d3701c701f4a83792799fd61a24aeac0ac53302b9d28",
   "layer_id": "45d5e45babebea2e70c7354be8a17ceda8a8db9e74b429e142a86d8697a59b2d",
   "size": 42333184,
   "symlinked_to": [
    "test"
   ],
   "used_by": [
    "test"
   ]
  },
  {
   "docker_id": "1a2e8a316114edb1b164dd645c4d49913c0b5cccf27142e026b7b0bdcb5f836b",
   "layer_id": "cbede313b877303ac45010c4635432722f3db8c986ae3c082db1d0a916a1b18f",
   "size": 1171968,
   "symlinked_to": [
    "test"
   ],
   "used_by": [
    "test"
   ]
  },
  {
   "docker_id": "8dc8920290fc4566437bca6e5bedf637f902e79d5f0e603bdb7e3df121ceca6f",
   "layer_id": "5f70bf18a086007016e948b04aed3b82103a36bea41755b6cddfaf10ace3c6ef",
   "size": 1024,
   "symlinked_to": [
    "test"
   ],
   "used_by": [
    "test"
   ]
  }
 ]
}

```

#### Add a Layer
To add a particular layer to the device use the below command

```

dev@dev-VirtualBox:~$ ioxclient layer add ./0ae878fde72e7076f919fb4c5f5ebff461f524365f870f970ac463eb4d047536.tar.gz
Currently active profile :  829
Command Name:  layer-add
Layer got added successfully.
Successfully uploaded the layer 0ae878fde72e7076f919fb4c5f5ebff461f524365f870f970ac463eb4d047536

```

* Individual layers from a docker image can be generated using the command "ioxclient docker package". Please refer to the command's documentation for further details.

#### Delete a Layer
To delete a particular layer use the below command

```

dev@dev-VirtualBox:~$ ioxclient layer delete -h
NAME:
   delete - delete a particular layer or all unused layers on the device

USAGE:
   command delete [layer_id]

DESCRIPTION:
   
To delete a particular layer specify the layer id as an argument as shown below

    ioxclient layer delete <layer_id>

To delete all unused layers on the device, use the below command

    ioxclient layer delete 


dev@dev-VirtualBox:~$ ioxclient layer delete 0ae878fde72e7076f919fb4c5f5ebff461f524365f870f970ac463eb4d047536
Currently active profile :  829
Command Name:  layer-delete
Successfully removed the layer  0ae878fde72e7076f919fb4c5f5ebff461f524365f870f970ac463eb4d047536

dev@dev-VirtualBox:~$ ioxclient layer delete
Currently active profile :  829
Command Name:  layer-delete
Delete all the unused layers on the device[y/n]:y
Moving forward with execution of the command
Successfully removed all unused layers 

```

* Note: Layer id is the layer's file name excluding the tar.gz extension.

