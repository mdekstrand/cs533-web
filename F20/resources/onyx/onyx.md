# Remotely Using Onyx
{% import 'video.md' as media %}

If you want to use Jupyter notebooks on Onyx nodes, there are a few extra steps you need to do.
There is a video at the end of this page walking through the process.

## Install Anaconda

Connect to the Onyx head node.  From the command line, run:

    $ ssh username@onyx.boisestate.edu

On Windows, you can use MobaXterm.

Follow the instructions in [Software Installation](software.md#onyx) to install the software.
I recommend accepting all defaults, which will set up your shell to automatically activate Conda next time you log in.
Due to network file system performance, I recommend using Miniconda instead of the full Anaconda platform, so we only install the packages we need.

Log out of Onyx.

## Preparing VPN Access

Directly connecting to `onyx.boisestate.edu` — called the ‘head node’ — is fine for transferring files, installing the software, and other light work, but not for substantial computing.
For actually doing work, we need to connect to one of the ‘Onyx nodes’, individual computers in the Boise State CS department computing system.
These computers are numbered with 2–3 digit numbers and have names like `onyxnode03.boisestate.edu`.

Only the Onyx head node accepts connections from outside the Boise State network.
To connect to one of the normal Onyx nodes, you need to be on the Boise State network.
There are two ways to do this from the outside.

### OpenSSH ProxyJump

Set up SSH to use `onyx.boisestate.edu` a ‘jump host’ (sometimes called a ‘bastion host’).
OpenSSH has direct support for jump hosts, and this is probably the easiest way to set things up on macOS and Linux.
On Windows, you will need to install a version of OpenSSH that supports jump hosts.[^1]

=== "Linux"

    OpenSSH is already installed in most Linux distributions.

    If the directory `~/.ssh` does not exist, create it with `mkdir ~/.ssh`.

=== "macOS"

    OpenSSH is included with macOS, and recent operating system versions support `ProxyJump`.

    If the directory `~/.ssh` does not exist, create it with `mkdir ~/.ssh`.

=== "Windows"

    [MobaXterm][] supports jump hosts through the SSH installation in its “local terminal” feature.

    1.  Install MobaXterm
    2.  Click "Start local terminal"
    3.  Set up the SSH configuration:

            mkdir -p ~/.ssh
            apt-cyg install nano
            nano ~/.ssh/config

    Then proceed with the configuration below.  You can also use [MSYS2][] if you prefer.

[MobaXterm]: https://mobaxterm.mobatek.net/
[MSYS2]: https://www.msys2.org/

To set up jump host connections, modify the file `~/.ssh/config` (the file `config` in the `.ssh` subdirectory of your home directory) to contain the following lines:

    Host onyxnode*.boisestate.edu
        User username
        ProxyJump onyx.boisestate.edu
    
    Host onyx.boisestate.edu
        User username
    
If the file does not yet exist, create it.
The `User` lines make SSH automatically fill in your username when you connect to Onyx in the future, so it's more convenient to connect.

### Boise State VPN

You can also use the [Boise State VPN](https://bsuvpn-offcampus.boisestate.edu/).
For this, you will need to set up [Duo Security](https://www.boisestate.edu/oit-accounts/multi-factor-authentication-duo/) for the two-factor authentication.
I have requested VPN access for all students in the class.

## Connecting to Nodes

Once you have done either of these steps, you can connect to a node:

    $ ssh onyxnode03.boisestate.edu

If you are using `ProxyJump`, SSH will prompt you for your password twice — once to set up the proxy, and again to log in.
On Windows, enter the host name into your SSH client.

Once you are logged in to a node, you can run `uptime` to see how heavily-loaded it is, and `w` to see if anyone else is logged in.
An idle node will have a load average of close to 0 when you run `uptime`.

If the node is in use, log out and try a different node.
Consult the beginning-of-the-year e-mail from Ben for a list of available nodes.

All nodes (and the head node) share the same home directory, so your files will be available no matter which node you use.

## Using Jupyter

Once you have logged into the Onyx node you want to use, change into the directory where you're keeping your class files or the specific project you want to work on and start the notebook server:

    $ cd CS533/project-dir
    $ jupyter notebook --no-browser

The `--no-browser` option is to keep Jupyter from trying to start a browser; if you're logged in through MobaXterm, it usually sets up X11 forwarding, and without this option Jupyter will start Firefox on the Onyx node and try to display it on your computer.
It will be much more efficient to use Jupyter's network interface than to tunnel an entire browser over remote display.

The notebook server will print out some log messages; at the bottom you will see something like

```
    Or copy and paste one of these URLs:
        http://localhost:8888/?token=9539c85b91af17bb3fc3d5a4f71b113874af33d6b5c6d245
     or http://127.0.0.1:8888/?token=9539c85b91af17bb3fc3d5a4f71b113874af33d6b5c6d245
```

You now need to set up an **SSH tunnel** to connect to the server.
Note the *port number* from the URL (the numbers after `localhost:`, in this case 8888).
Create an SSH tunnel that tunnels that port from your local computer to the port on your node.
From the command line, you can do this by opening another terminal and running:

    ssh -L 8888:localhost:8888 onyxnode03.boisestate.edu

This tunnels port 8888 from your local computer to the same port on `localhost` on the remote computer (the Onyx node).
You need to change 8888 and `onyxnode03` to match your port number and Onyx node.

??? tip "Direct MobaXterm Tunnel"

    If you are using MobaXterm directly with the VPN, use the *Tunneling* tool in the toolbar (if you are using MobaXterm as a command-line terminal to run the `ssh` command, this will not work; instead use the command-line instructions).
    Create a new tunnel with the following settings:

    - Forwarded port: port number (e.g. 8888)
    - SSH server: the node (e.g. `onxnode03.boisestate.edu`)
    - SSH login: your username
    - SSH port: 22
    - Remote server: `localhost`
    - Remote port: port number (e.g. 8888)

The forwarded port (in `ssh -L`, the first port number) does not have to match the remote port.
If you have something else running on your computer using port 888, you can forward any port you want.

Once you have the port forward or tunnel set up, go to the URL indicated in the Jupyter Notebook output in your web browser.
The tunnel makes `localhost:8888` on your computer route to `localhost:8888` on the Onyx node, and everything works.

## Video

{{ media.video('8e280072-b2c3-4cb3-a629-ac210160137f') | trim }}
