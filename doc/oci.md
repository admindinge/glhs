
OCI-ს ეგზემპლიარის შექნისას გასავლელია რამოდენიმე პროცედურა, მათ შორის მნიშვნელოვანია `ssh` გასაღებების შექმნა. ასეთი გასაღები მე უქვე მაქვს და რეპოზიტორში არის დირექტორიაში key

> [!Important] გასაღებეს გადავარქვი სახელები `oci.key` და `oci.key.pub`
> შეერთებისათვის გვჭირდება `oci.key`
> `.pub` გასაღებები, როგორც წესი `ssh` სერვერზე იტვირთება `ssh-copy-id` ბძანებით, მაგრამ მანამდე ამ სერვერზე უნდა გქონდეს პაროლით შესვლის საშუალება. `OCI`-ზე ამის საშუალება არაა, ამიტომ გასაღებს ყველა ახალ მომხმარებელს ვუკოპირებ ძირეული მომხმარებლიდან (`ubuntu`) ბრძანება `rsync`-ის საშუალებით, იხ. ქვემოთ

`OCI` ეგზემპლიარის შექმნისას საიტზე არის საშუალება, რომ მან შექმნას გასაღების წყვილი, ასევე გაძლევს საშუალებას, აუტვირთო საკუთარი. როცა რამოდენიმე ეგზემპლიართან იგეგმება მუშაობა, პროცედურის გამარტივების მიზნით, მე მაქვს ჩემი გასაღების წყვილი და ვირჩევ ამ გასაღებების ატვირთვას, ამით ყველა ეგზეპლიარისთვის მაქვს ერთი წყვილი და აღარ ვიხლართები

შემდეგ ეგზეპლიარზე დაშვება ტერმინალიდან არის ამ დახურული გასაღების მითითებით

```Bash 
ssh -i .ssh/key_filename ubuntu@server_ip

```

ubuntu ავტომატური იუზერია ეგზემპლიარისა დაყენების შემდეგ და ასევე არის ადმინისტრატორი (`sudoer`)

მე როგორც წესი მჭირდება ჩემი მომხმარებლები, მათ შორის ადმინისტრატორის ფუნქციებითაც, ამიტომ ავტორიზაციის შემდეგ,  ჩვეულებრივად 

```Bash
sudo su
adduser avto
usermod -aG sudo avto
rsync --archive --chown=avto:avto ~/.ssh /home/avto
```
`sudo su` არის ბრძანება, რომელსაც `sudoer`-ი მომხმარებელი გადაყავს `root`-ში, თუ ყოველ ჯერზე არ გვინდა ბრძანების წინ ვწეროთ `sudo`

მე ლოკალ ტერმინალშიც მომხმარებელი მყავს `avto`, ამიტომ სერვერსაც ვაწყობ `avto`-თვის, რომ შემდეგ ავტორიზაციისთვის დიდი სტრიქონები არ ვწერო

ამ ბრძანებებით შევქმენი `avto`, მივეცი ადმინისტრატორის პრივილეგიები და `ubunu` მომხმარებლის `home` დირექტორიიდან `rsync` საშულებით დავაკოპირე ღია გასაღები

ამის მერე ლოკალში, ჩემთან უნდა გავაღვიძო `ssh-agent` და მას დავამახსოვრებინო სად მაქვს დახურული გასაღები


```Bash
eval "$(ssh-agent -s)"
ssh-add .ssh/private_key

```

ამის მერე სერვერის დავუკავშირდები მარტივად `ssh din.ge` რაც ტოლფასია `ssh -i .ssh/private_key avto@din.ge

`wsl`-ი ამას ვერ იმახსოვრებს, ამიტომ `~/.bashrc`  ფაილის ბოლოში ვამატებთ

```Bash
# მოწმდება SSH_AUTH_SOCK ცვლადის არსებობა
if [ -z "$SSH_AUTH_SOCK" ]; then 
# თუ არ არის გაეშვება ssh-agent
eval $(ssh-agent) > /dev/null 2>&1
# ვამაებთ გასაღებს ssh-agent-ში
ssh-add .ssh/private_key > /dev/null 2>&1
fi
```


OCI-ზე დაყენებული `Ubuntu` სერვერის სესია ძალიან მცირე დროში ეკიდება, მისი დროის გასახანგრლივებლად ადმინისტრატოით გავხსნით `/etc/ssh/sshs_config`
ფაილს და მოვუხსნით კომენტარებს და დავაყენებ შემდეგ მნიშვნელობებს `ClientAliveInterval 300` და `ClientAliveCountMax 3`  

300 წამის, ანუ 5 წუთის შემდეგ გასინჯავს კონექტს, ამას გაიმეორებს სამჯერ და მერე დაკიდებს შეერთებას, ანუ 5 წუთი შეიძლება არ გქონდეს აქტივობა ტერმინალში და არ გაგეთიშება. ეს ნორმალური დროა, თუ არა და პარამეტრებს დაარედაქტირებ




