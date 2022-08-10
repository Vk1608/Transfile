# Transfile
 Transfile : A peer-to-peer file sharing system with tracker
 

Prerequisites:

1) All the libraries should be correctly installed

	pip install msgpack
	pip install aioconsole
	pip install beautifultable
	pip install tqdm
	pip install asyncio

2) Only run for windows (with some tweak in asyncio can work on linux)

3) IP and Port should be free and available to use.


How to use?

#NOTE: Terminal must be opened in the folder where both README.txt and transfile folder is located.

To run tracker:

1) Open a terminal in this location.
2) Run Command : "python -m transfile tracker"
3) In Tracker terminal enter help to see available commands.


Available Commands for TRACKER:

>> help: Print available commands <br />
>> start <host IP> <port> : To setup a TCP server to connect all peers and tracker <br />
>> exit : To exit tracker <br />
>> list_peers : List all connected peers <br />
>> list_files: All available files published by active peers <br />
>> list_chunkinfo : List all available chunks of a file and to what peer it belongs <br />


To run peer:

1) Open a terminal in this location.
2) Run Command : "python -m transfile peer"
3) In Peer terminal enter help to see available commands.


Available Commands for PEER:

>> help: Print available commands <br />
>> connect <host IP> <port> : To connect a TCP portol tracker <br />
>> exit : To disconnect and exit peer <br />
>> list_files: All available files published by active peers <br />
>> publish <filename> : Publish a local file available to download by other peers (file must exist in same folder) <br />
>> download <filename> <location> : Download a remote file to a local path (path must also include filename to be saved with, alongwith extension) <br />
  

Bugs and limitation:

Only work for windows.
Size of each chunk is limited to 256kb (although can be changed from code)
File can only be downloaded if publisher is still connected.
