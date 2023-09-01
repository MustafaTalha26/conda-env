import subprocess

# Conda ortam kurulumundan sonra pip kurulmalı.
# pip kullanarak yüklenecek paketler ortamın pip scriptini kullanmalı.
env_name = 'Env'
pip_path = "c:/Users/mtmert/anaconda3/envs/Env/Scripts/pip"

# matplotlib=3.7.1, matplotlib<=3.7.1, matplotlib>=3.7.1 gibi kullanımlar mümkündür.
# .whl uzantılı paketleri directory vererek yükleyebiliriz.
conda_package_list = ['numpy','matplotlib=3.7.1']
pip_package_list   = ['seaborn']
whl_package_list   = ['c:/Users/mtmert/Desktop/scikit_learn-1.3.0-cp311-cp311-win_amd64.whl']

# Tek seferlik log tutuyoruz.
f=open("log.txt", "w+")

# Conda ortam oluşturuyor.
c = subprocess.run('powershell "conda create -n {} -y"'
                    .format(env_name), 
                    capture_output=True, shell=True, text=True)
f.write(c.stdout)
print(c.stdout)

# Conda ortamına pip kuruyor
c = subprocess.run('powershell "conda install {} -n {} -y"'
                    .format('pip',env_name), 
                    capture_output=True, shell=True, text=True)
f.write(c.stdout) 
print(c.stdout)

# Conda ortamına conda paketlerini yüklüyor.
for package_name in conda_package_list:
    c = subprocess.run('powershell "conda install {} -n {} -y"'
                    .format(package_name,env_name), 
                    capture_output=True, shell=True, text=True)
    f.write(c.stdout)   
    print(c.stdout)

# Conda ortamına pip paketlerini yüklüyor.
for package_name in pip_package_list:
    c = subprocess.run('powershell "{} install {}"'
                    .format(pip_path,package_name), 
                    capture_output=True, shell=True, text=True)
    f.write("\n")
    f.write(c.stdout)
    print(c.stdout)

# Conda ortamına whl paketlerini yüklüyor.    
for package_name in whl_package_list:
    c = subprocess.run('powershell "{} install {}"'
                    .format(pip_path,package_name),
                    capture_output=True, shell=True, text=True)
    f.write("\n")
    f.write(c.stdout)
    print(c.stdout)  

# Conda ortamına kurulan paketleri ve bilgilerini gösteriyor.
c = subprocess.run('powershell "conda list -n {}"'
                    .format(env_name), 
                    capture_output=True, shell=True, text=True)
f.write("\n")
f.write(c.stdout)
print(c.stdout)

# log.txt dosyasını kapatıyor.
f.close()