# FTP commands

# STEPS TO CONNECT FTP
    *Step1:*
        Launch command prompt and move to the directory where all your files are located. Because this is the place from which you can move your files to server and download it on the same folder
    *Step2:*
        Enter the command
        ftp domainname
    *Step 3:* Enter the username when asked, followed by the password.

    *Step 4:* You can see the connection being established. Now you are allowed to perform actions on your files on the sever.

#  These are the FTP commands:

## Help
        Request a list of all available FTP commands.
## ascii:
        to turn on ascii mode.
## status:
        to display how the current FTP session is configured.
## prompt:
        to turn on/off interactive mode.
## ls:
        directory listing equivalent to dir.
## ls -l:
        long directory listing, more detail.
## pwd:
        Display current directory name
## cd:
        Change directory.
## lcd:
        change the local current directory.
## get:
        download the file from the FTP server.
## put:
        upload file to the server on at a time.
## mget:
        download multiple files from the FTP server.
## mput:
        upload multiple files to the FTP server.
## binary:
        to turn on binary mode.
## delete:
        delete any file on FTP server.
## mkdir:
        to make directory on FTP server.
## ascii :
        Set the file transfer mode to ASCII (Note: this is the default mode for most FTP programs).
## quit/close/bye/disconnect:
        disconnect from the FTP server.
## ! :
        Preceding a command with the exclamation point will cause the command to execute on the local system instead of the remote system.
