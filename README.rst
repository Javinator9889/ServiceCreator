ServiceCreator
==============

Create init.d services at your Debian-based distribution easily with
this automatic tool.

How it works
------------

This tool will allow you to *easily create* **init.d** scripts
(*functions that will start on computer boot*) on your Debian based
distributions (such as **Ubuntu**, **Raspbian**, etc).

The functionality of this tool is simple: *ask the user for some
information about the service and create it with no more user
interaction*.

The tool works as follows:

1. **Ask for service folder** if not found: the script will try to
   search *"/etc/init.d/"* folder. If not found, then will request user
   for giving a **new folder** where scripts are installed.

2. **Request a service name**, which is necessary for installation. If
   the provided service name exists, a *new name for the service will be
   asked* (as **there can not be two services** with the same name).

3. **Ask for a command** that will execute your service. At this option,
   you are able to **load the command** from a file (if the command you
   would like to add has multiple lines) If load option is chosen, the
   file *will be modified* and stored in *"/usr/local/bin/"* in order to
   be able to execute \| see `"Why
   root?" <https://github.com/Javinator9889/ServiceCreator#why-root>`__

4. **Request a short and a long description** for the service. The
   installation and execution process needs, at least, a *short
   description*, and not necessary a long description. If you do not
   specify the long one, it will be a copy of the short description.

5. **Install and register** the service into the system. For this
   process, the tool *copies* and *registers* the new script into the
   system, and enables it for running on boot.

If you want to know more about that services and process, see *`"Why
root?" <https://github.com/Javinator9889/ServiceCreator#why-root>`__*

How to install
--------------

You have some methods in order to install this tool (all need *root
access - get it by typing ``su`` or using ``sudo``*):

-  Using ``pip``:

   If you only have Python 3 installed:

   .. code:: bash

       pip install ServiceCreator
       # If "pip" not found:
       pip3 install ServiceCreator
       # If none of the above works:
       python3 -m pip install ServiceCreator 
       # If "python3" not present, try with "python"
       python -m pip install ServiceCreator

   If the above commands *are not present on your system*:

   .. code:: bash

       apt-get install pip3
       # If Python 3 not installed
       apt-get install python3 pip3

   Then run the commands listed with ``pip``
-  Using the ``setup.py`` method:

   -  First, **download the file**:

      (Using ``wget`` and ``unzip``):

      .. code:: bash

          wget https://github.com/Javinator9889/ServiceCreator/archive/master.zip
          unzip master.zip
          cd master/

      If the above commands *are not present on your system*:

      .. code:: bash

          apt-get install wget unzip

      (Using ``git``):

      .. code:: bash

          git clone https://github.com/Javinator9889/ServiceCreator.git
          cd ServiceCreator/

      If the above commands *are not present on your system*:

      .. code:: bash

          apt-get install git

   -  Then, **install it** to your system:
      ``bash     python3 setup.py install     # If the above does not work     python setup.py install``
      If *commands not found*, you must install ``Python 3`` on your
      system: ``bash     apt-get install python3``

This will install **the application** and **all its dependencies** to
your system.

How to update
-------------

As in the `installation
method <https://github.com/Javinator9889/ServiceCreator#how-to-install>`__,
to update you have two options:

1. If you installed via ``pip``:
   ``bash     pip install -U ServiceCreator     # If "pip" not found:     pip3 install -U ServiceCreator     # If none of the above works:     python3 -m pip -U install ServiceCreator      # If "python3" not present, try with "python"     python -m pip -U install ServiceCreator``

2. If you installed via ``setup.py``:

   First, you have to *download the new version available* following the
   steps described at the *`installation
   method. <https://github.com/Javinator9889/ServiceCreator#how-to-install>`__*

   Then, what you have to do is:

   .. code:: bash

       python setup.py install
       # If the above does not work
       python3 setup.py install

How to use it
-------------

Once the application *is installed on your system*, you will be able to
run it by typing the following command:

.. code:: bash

    service_creator 
    # or with sudo
    sudo service_creator

Why root?
---------

This application requires root for the following commands: \* In
***/usr/local/bin/*** for creating an executable file. If not, you can
create that file by yourself with:
``bash     nano your_script.sh     # Add your config here     chmod +x your_script.sh     sudo mv your_script.sh /usr/local/bin/your_script.sh``
\* In ***/etc/init.d/*** for moving your created service and registering
it for running on boot. To perform this manually:
``bash     service_creator -e /home/YOUR_USER/your_script.sh     # Create your service     sudo mv /home/YOUR_USER/your_script.sh /etc/init.d/your_script.sh     sudo update-rc.d your_script.sh defaults``

Also you can give the application *root* permissions so it will be able
to do that by itself.

I found an error or I want to contribute
----------------------------------------

I would *love* to see how my application grows up, so feel free to
create your **own version** of this app. Just *fork it* and make all the
changes you want 😄

Also if you want to *add a new functionality* or *solve a bug*, you are
free to open a **pull request** so I can merge the changes you have
done.

How can I help?
---------------

-  Feel free to *follow me at GitHub* 👥: I create a lot of projects and
   maybe you find someone interesting.
-  *Start* ⭐ this project if you find it helpful 😄
-  *Share it* with the people you think they will find interesting my
   job 🗣

License
-------

This project is under *GNU General Public License v3.0*. You can read
all **permissions**, **limitations** and **conditions** by `clicking
here <https://github.com/Javinator9889/ServiceCreator/blob/master/LICENSE>`__
