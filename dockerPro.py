import os  
print("\t\t\t Docker World Welcomes You")
print("this TUI application helps understand Docker world")


c=0

while True:
    os.system("clear")
    print(""" 
    
                              DOCKER COMMAND USING TUI IN EASY WAY 
                             ======================================

  Enter the Number to perform the task alloted :
  1. Basic Yum Configuration                 
  2. Docker Installation 
  3. Launching New OS in Docker 
  4. WordPress Site Installation     
  5. Reconstruct Infrastruture          (In Case website crashes within seconds)
  6. Centos:7 yum Error Solution        < first watch tutorial video

Note : First visit tutorial video as in video directory.

  9. Exit
            
            
  Enter your option : """,end='')

    ch = input()

    if(choice==1):
        yum_configure()
        continue
    elif(choice==2):
        docker_installation()
        continue
    elif(choice==3):
        if c==1:
            launch()
        else:
            print(" Docker Not Found ")
        continue
    elif(choice==4):
        infra_setup(choice)
        continue

    elif(choice==5):
        infra_setup(choice)
        continue
    elif(choice==6):
        infra_setup(choice)
        continue

    elif(choice==9):
        exit(0)
    else:
        print("Invalid Input")
	print("Enter Valid INPUT")
        x=input("Press Enter to continue...")

def launch():
    os1=input("Enter the Name of the OS image which you want")
    os.system("docker run -it {}".format(os1)) 

def yum_configure():
    os.system("cp epel.repo dock.repo  epel-playground.repo epel-testing.repo root.repo rpmfusion-free-updates.repo rpmfusion-free-updates-testing.repo /etc/yum.repos.d/ ")
    print("Your yum is configured now check it by 'yum repolist' command. ")
    c=input("Press Enter to continue...")

    
def docker_installation():
    os.system("yum install docker-ce --nobest -y")
    print("Docker sucessfully installed....")
    c=input("Press Enter to continue...")
    c=c+1
    

def infra_setup(a):
    if a==4:
        flag=0
        try:
            os.system(' curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
            os.system("chmod +x /usr/local/bin/docker-compose")
            os.system("cp docker-compose.yml /") 
            os.system("cd / ")
            os.system("mkdir /my_infrastructure")
            os.system("cd /my_infrastructure/")
            os.system("pwd")
            os.system("mv ../docker-compose.yml .")
            os.system("docker-compose up -d")
        except ValueError:
            print("Error .... Watch tutorial .... to solve this.")
            x=input("Press Enter to continue....")
            flag=1
        if flag == 0 :
            print("\n\n     Now you can access your wordpress site by redhat IP:7081  < eg:- 123.456.789.12:7081 > in your redhat firefox.")
            x=input("Press Enter to continue...")

    elif a==5:
        os.system("docker-compose up -d")
        print("\n\n     Now you can access your wordpress site by redhat IP:7081  < eg:- 123.456.789.12:7081 > in your redhat firefox.\n    or visit tutorial videos")
        x=input("Press Enter to continue...")

    
    elif a==6:
        os.system("docker pull centos:7")
        os.system("firewall-cmd --zone=public --add-masquerade --permanent")
        os.system("firewall-cmd --zone=public --add-port=80/tcp")
        os.system("firewall-cmd --zone=public --add-port=443/tcp")
        os.system("firewall-cmd --reload")
        os.system("systemctl restart docker")
        print("\n\n Problem Resolved. Enjoy ......")
        x=input("Press Enter to continue...")



        



    
 

