# Setting up your environment

Before you begin, 
download VirtualBox from <a href="https://www.virtualbox.org/wiki/Downloads">here</a>, and
download Vagrant from <a href="https://www.vagrantup.com/downloads.html">here</a>.

* Clone this repo and cd into the directory. Run ```cd django-predix```
* Run ```vagrant up```. This will create a Virtual Machine with the tools you will need to run this application.
You can see what we're installing in the Vagrantfile.
* Once the machine starts, log in to it by running ```vagrant ssh```
* Although not necessary, it's a good practice to create a virtual environment for every project so that your package versions don't clash.
* To create a new python virtual env, run ```mkvirtualenv <your-virtual-env-name>```
* To start working in the virtual env, run ```workon <your-virtual-env-name>```.

    * The virtual env you are working on will be displayed before the prompt like this.
      <img src="https://i.imgur.com/t4L4kmI.png"/>
    * In the above screenshot, the virtual env is called predix.
    * Remember to run this every time to start working on your project.

* Run ```/vagrant/```. This will bring you to the directory you launched the VM from. You will have access to the files on your host machine.
Any change you make to the files on your host machine will be applied in the VM and vice versa.
* We will use the VM to run the application only. We will use the host machine to write and edit code.
