# პროექტის მოდელი

## მონაცემთა ბაზა

მონაცემთა ბაზასთან სამუშაოდ ჯანგო იყენებს ORM ტექნოლოგიას, ეს საშუალებას გვაძლევს არ ვიყოთ დამოკიდებული რომელიმე კონკრეტული ბაზის ენაზე, ჯანგოში არსად არ ვიყენებთ SQL შეკვეთებს

ჯანგოს პროექტის შექმნის მერე გასაკეთებელია მონაცემთა ბაზის მიგრაცია. ახალ პროექტს სხვადასხვა ამოცანებისათივის მოყვება მოდელების ბევრი კლასი, რომელთა მიგრაიის შედეგად მონაცემთა ბაზაში იქმნება რამოდენიმე ცრილი.


```Bash
    python manage.py migrate
```

ცრილები აღიწერება მოდელების სახით ფაილში models.py კლასის სახით

ამ პროექტში პირველი ცრილი SiteMenu იქმნება აპლიკაცია main-ის models.py ფაილში. შექმნილ ცრილში შევინახავთ საიტის მენიუს

რაიმე მოდელის შექმნის შემდეგ საჭიროა ბაზაში მიგრაცია:

```Bash
    python manage.py makemigrations
```


ამის შემდეგ ხდება ბაზასთან მუშაობა

ამ პროექტში პირველი მაგალითი არის ფაილში wiews.py

```python
    menu = SiteMenu.objects.all()
```  

ამ ბრძანებით მივიღებთ საიტზე გამოსაყენებელი მენიუს და მის შესაბამის URL-ებს, რომლებსაც `'menu': menu` სახით ვუგზავნით შაბლონ html ფაილებს

შაბლონებში გასარკვევად საჭიროა გადავხედოთ Jinja2 სპეციფიკაციას, თუმცა ამ მაგალითების ნახვითაც შეიძლება გარკვევაც

აქ არის ერთი ძირითადი ფაილი - base.html, რომელშიც ძირითადი HTML ფორმირდება, მასში არის მენიუს შესაქმნელი ციკლიც, და რამდენიმე ბლოკი არის ცარიელი

ამ საბაზო ფაილის გაფართოება ხდება სხვა ფაილებში და დარჩენილ ცარიელა ბლოკებში ყველა მათგანი თავის საკუთარ კონტენტს ჩაამატებს

ამდაგვარად ვაღწევთ იმას, რომ ყველა ფაილში კოდს აღარ ვიმეორებთ, ის რაც გამეორებადია და საერთო ყველასთვის, ვწერთ საბაზო ფაილში და მას ვაფართოებთ ყველა დანარჩენ ფალიში

### URL მისამართები

განმარტების თანახმად URL არ უნდა წარმოვიდგინოთ საიტის მისამართად, ის განსაზღვრავს საიტზე განთავსეული რესურსების მდებარეობას. ამიტომ მნიშვნელოვანია მისი სწორად გაწერა
ამისათვის ჯანგოს აქვს მდიდარი არსენალი, ამისათვის კი გარკვეულ წესებს უნდა დავექმემდებაროთ

URL შეესაბამება მარშრუტები, რომელიც გაწერილია urls.py ფაილში შემდეგი სახით

```python
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('reg/', reg, name='reg'),
```  

ცარიელი `''` მასშრუტი მიუთითებს საიტის ძირითად მისამართზე, ყველა დანარჩენი მარშრუტი ეწყობა მასზე დამატებით. ამ აღწერაში მნიშვნელოვანია პარამეტრი `name`. მარშრუტები პროექტში შეიძლება შეიცვალოს სხვადასხვა საჭიროების გამო, მაგრამ `name` მარშრუტთან კავშირს ყოველთვის ინარჩუნებს, ამიტომ თუ შაბლონში URL-ად გადავცემთ `name`-ს, შემდგომში შაბლონებში URL-ების ცვლილება აღარ დაგვჭირდება, როგორც არ უნდა შეიცვალოს კოდი და რესურსები. ეს კი ძალიან მოსახერხებელი რამაა ნებისმიერი პროექტის შემხვევაში

ამ შემთხვევაში ამოცანა მარტივდება და დაიყვანება შემდეგ სახეზ, რომ საიტის დაგეგმარების დროს, როცა ვწერთ მარშრუტებს, ყველა მარშრუტს დავარქმევთ თავის სახელს და ამ სახელის გამოყენებით ავაწყობთ შაბლონს, შემდგომში თუ მარშრუტი შეიცვალა, ანუ რესურსი გადაადგილდა სადმე, სახელი რჩება იგივე და შარლონი ამ მარშრუტს მაინც მიაგნებს და გამოიყენებს. სხვანაირად, მარშრუტის შეცვლის შემთხვევაში, იძულებული ვიქნებოდით, მისი შესაბამისი URL შეგვეცვალა შაბლონშიც

`name` შაბლონში გადაეცემა `{% url '<name>' %}` სახით, ჩვენ კონკრეტულ მაგალითში:  `{% url 'home' %}` და ა. შ.  ჩვენ ეს სახელები შეტანილი გვაქვს ცრილში url სვეტში და `menu' ლექსიკონში მოხვდება menu.url-სახით, რომელსაც ციკლით ვალაგებთ (იხ. base.html)