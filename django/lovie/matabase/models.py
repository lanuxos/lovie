from fileinput import filename
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User, Group, Permission, AbstractUser, AbstractBaseUser, BaseUserManager
from PIL import Image
from time import timezone
import os
from uuid import uuid4


# class UserManager(BaseUserManager):
#     def _create_user(self, username, password):
#         if not username:
#             raise ValueError('username requered')
#         now = timezone.now()
class UserProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, help_text="ຊື່ຜູ້ໃຊ້")
    genderChoices = {
        "m": "ຊາຍ",
        "f": "ຍິງ",
        "o": "ອື່ນໆ",
    }
    gender = models.CharField(max_length=10, choices=genderChoices, blank=True, null=True, help_text="ເພດ")
    firstname = models.CharField(max_length=100, blank=True, null=True, help_text="ຊື່")
    lastname = models.CharField(max_length=100, blank=True, null=True, help_text="ນາມສະກຸນ")
    idCardNo = models.CharField(max_length=15, blank=True, null=True, help_text="ເລກບັດປະຊາຊົນ")
    passportNo = models.CharField(max_length=15, blank=True, null=True, help_text="ເລກໜັງສືເດີນທາງ")
    dateOfBirth = models.DateField(blank=True, null=True, help_text="ວັນເດືອນປີເກີດ")
    email = models.EmailField(blank=True, null=True, help_text="ອີເມວ")
    tel = models.CharField(max_length=15, blank=True, null=True, help_text="ເບີໂທ")
    villageOfBirth = models.CharField(max_length=100, blank=True, null=True, help_text="ບ້ານເກີດ")
    districtOfBirth = models.CharField(max_length=100, blank=True, null=True, help_text="ເມືອງເກີດ")
    provinceOfBirth = models.CharField(max_length=100, blank=True, null=True, help_text="ແຂວງເກີດ")
    height = models.FloatField(blank=True, null=True, help_text="ລວງສູງ (cm)")
    weight = models.FloatField(blank=True, null=True, help_text="ນ້ຳໜັກ (kg)")
    color = models.CharField(max_length=100, blank=True, null=True, help_text="ສີຜິວ")
    mark = models.CharField(max_length=100, blank=True, null=True, help_text="ຮ່ອງຮອຍພິເສດ")
    blood = models.CharField(max_length=100, blank=True, null=True, help_text="ກຸ່ມເລືອດ")
    allergies = models.CharField(max_length=100, blank=True, null=True, help_text="ອາການແພ້")
    congenitalDisease = models.CharField(max_length=100, blank=True, null=True, help_text="ພະຍາດປະຈຳຕົວ")
    rank = models.CharField(max_length=100, blank=True, null=True, help_text="ຊັ້ນ / ຂັ້ນ")
    jobTitle = models.CharField(max_length=100, blank=True, null=True, help_text="ຕຳແໜ່ງ")
    dateOfStartCurrentJob = models.DateField(blank=True, null=True, help_text="ວັນເດືອນປີເຂົ້າເຮັດວຽກປັດຈຸບັນ")
    dateOfRetired = models.DateField(blank=True, null=True, help_text="ວັນເດືອນປີເຂົ້າຮັບເບ້ຍບຳນານ")
    employeeNo = models.CharField(max_length=100, blank=True, null=True, help_text="ເລກລະຫັດປະຈຳຕົວ")
    employeePersonalNo = models.CharField(max_length=100, blank=True, null=True, help_text="ເລກລະຫັດປະຈຳຕົວພະນັກງານ")
    employeeIdCardNo = models.CharField(max_length=100, blank=True, null=True, help_text="ເລກລະຫັດບັດພະນັກງານ")
    socialIdNo = models.CharField(max_length=100, blank=True, null=True, help_text="ເລກປະກັນສັງຄົມ")
    statusChoices = {
        "single": "ໂສດ",
        "married": "ແຕ່ງງານແລ້ວ",
        "divorced": "ໝ້າຍ",
        "widow": "ຢ່າຮ້າງ"
    }
    status = models.CharField(max_length=10, choices=statusChoices, blank=True, null=True, help_text="ສະຖານະ", verbose_name="ສະຖານະ")
    company = models.CharField(max_length=100, blank=True, null=True, help_text="ກົມກອງປະຈຳ", verbose_name="ກົມກອງປະຈຳ")
    dateOfStartRevolution = models.DateField(blank=True, null=True, help_text="ວັນເດືອນປີເຂົ້າການປະຕິວັດ", verbose_name="ວັນເດືອນປີເຂົ້າການປະຕິວັດ")
    dateOfStartJob = models.DateField(blank=True, null=True, help_text="ວັນເດືອນປີເຂົ້າເຮັດວຽກ", verbose_name="ວັນເດືອນປີເຂົ້າເຮັດວຽກ")
    placeOfStartJob = models.CharField(max_length=100, blank=True, null=True, help_text="ກົມກອງເຂົ້າເຮັດວຽກ", verbose_name="ກົມກອງເຂົ້າເຮັດວຽກ")
    dateOfTemporaryParty = models.DateField(blank=True, null=True, help_text="ວັນເດືອນປີເຂົ້າພັກສຳຮອງ", verbose_name="ວັນເດືອນປີເຂົ້າພັກສຳຮອງ")
    dateOfParty = models.DateField(blank=True, null=True, help_text="ວັນເດືອນປີເຂົ້າພັກສົມບູນ", verbose_name="ວັນເດືອນປີເຂົ້າພັກສົມບູນ")
    partyTitle = models.CharField(max_length=100, blank=True, null=True, help_text="ຕຳແໜ່ງສາຍພັກ", verbose_name="ຕຳແໜ່ງສາຍພັກ")
    currentAddress = models.CharField(max_length=100, blank=True, null=True, help_text="ທີ່ຢູ່ປັດຈຸບັນ", verbose_name="ທີ່ຢູ່ປັດຈຸບັນ")
    currentVillage = models.CharField(max_length=100, blank=True, null=True, help_text="ບ້ານຢູ່ປັດຈຸບັນ", verbose_name="ບ້ານຢູ່ປັດຈຸບັນ")
    currentDistrict = models.CharField(max_length=100, blank=True, null=True, help_text="ເມືອງຢູ່ປັດຈຸບັນ", verbose_name="ເມືອງຢູ່ປັດຈຸບັນ")
    currentProvince = models.CharField(max_length=100, blank=True, null=True, help_text="ແຂວງຢູ່ປັດຈຸບັນ", verbose_name="ແຂວງຢູ່ປັດຈຸບັນ")
    dateOfWomenUnion = models.DateField(blank=True, null=True, help_text="ວັນເດືອນປີເຂົ້າສະຫະພັນແມ່ຍິງ", verbose_name="ວັນເດືອນປີເຂົ້າສະຫະພັນແມ່ຍິງ")
    dateOfYouth = models.DateField(blank=True, null=True, help_text="ວັນເດືອນປີເຂົ້າຊາວໜຸ່ມ", verbose_name="ວັນເດືອນປີເຂົ້າຊາວໜຸ່ມ")
    dateOfLabour = models.DateField(blank=True, null=True, help_text="ວັນເດືອນປີເຂົ້າກຳມະບານ", verbose_name="ວັນເດືອນປີເຂົ້າກຳມະບານ")
    ethnic = models.CharField(max_length=100, blank=True, null=True, help_text="ຊົນເຜົ່າ", verbose_name="ຊົນເຜົ່າ")
    religion = models.CharField(max_length=100, blank=True, null=True, help_text="ສາສະໜາ", verbose_name="ສາສະໜາ")
    father = models.CharField(max_length=100, blank=True, null=True, help_text="ຊື່ ແລະ ນາມສະກຸນພໍ່", verbose_name="ຊື່ ແລະ ນາມສະກຸນພໍ່")
    mother = models.CharField(max_length=100, blank=True, null=True, help_text="ຊື່ ແລະ ນາມສະກຸນແມ່", verbose_name="ຊື່ ແລະ ນາມສະກຸນແມ່")
    partner = models.CharField(max_length=100, blank=True, null=True, help_text="ຊື່ ແລະ ນາມສະກຸນ ຜົວ ຫຼື ເມຍ", verbose_name="ຊື່ ແລະ ນາມສະກຸນ ຜົວ ຫຼື ເມຍ")
    partnerJob = models.CharField(max_length=100, blank=True, null=True, help_text="ອາຊີບ ຜົວ ຫຼື ເມຍ", verbose_name="ອາຊີບ ຜົວ ຫຼື ເມຍ")
    emergencyContact = models.CharField(max_length=100, blank=True, null=True, help_text="ລາຍຊື່ຕິດຕໍ່ສຸກເສີນ", verbose_name="ລາຍຊື່ຕິດຕໍ່ສຸກເສີນ")
    emergencyContactTel = models.CharField(max_length=15, blank=True, null=True, help_text="ເບີໂທຕິດຕໍ່ສຸກເສີນ", verbose_name="ເບີໂທຕິດຕໍ່ສຸກເສີນ")
    generalSchool = models.CharField(max_length=100, blank=True, null=True, help_text="ລະດັບວັດທະນະທຳ", verbose_name="ລະດັບວັດທະນະທຳ")
    highestEducation = models.CharField(max_length=100, blank=True, null=True, help_text="ລະດັບການສຶກສາສູງສຸດ", verbose_name="ລະດັບການສຶກສາສູງສຸດ")
    highestEducationField = models.CharField(max_length=100, blank=True, null=True, help_text="ສາຂາວິຊີການສຶກສາສູງສຸດ", verbose_name="ສາຂາວິຊີການສຶກສາສູງສຸດ")
    highestEducationInstitution = models.CharField(max_length=100, blank=True, null=True, help_text="ສະຖາບັນທີ່ຈົບການສຶກສາສູງສຸດ", verbose_name="ສະຖາບັນທີ່ຈົບການສຶກສາສູງສຸດ")
    highestTheory = models.CharField(max_length=100, blank=True, null=True, help_text="ລະດັບທິດສະດີສູງສຸດ", verbose_name="ລະດັບທິດສະດີສູງສຸດ")
    highestTheoryInstitution = models.CharField(max_length=100, blank=True, null=True, help_text="ສະຖາບັນທີ່ຈົບທິດສະດີສູງສຸດ", verbose_name="ສະຖາບັນທີ່ຈົບທິດສະດີສູງສຸດ")
    foreignLanguage = models.CharField(max_length=100, blank=True, null=True, help_text="ພາສາຕ່າງປະເທດ", verbose_name="ພາສາຕ່າງປະເທດ")

    # for renamee the image's name using uuid randomly
    def pathAndName(instance, filename):
        upload_to = 'images/userProfile'
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)

    photo = models.ImageField(upload_to=pathAndName, default="default.png", blank=True, null=True, help_text="ຮູບພາບ", verbose_name="ຮູບພາບ")

    # for resizeing the image before saving
    def save(self, *args, **kwargs):
        super().save()
        if self.photo:
            img = Image.open(self.photo.path)
            if img.height > 400 or img.width > 300:
                outputSize = (400, 300)
                img.thumbnail(outputSize)
                img.save(self.photo.path)

    upload = models.FileField(upload_to="uploads/%Y-%m/", default="", blank=True, null=True, help_text="ອັບໂຫຼດໄຟລ໌")

    def __str__(self):
        title = ""
        if self.gender == "f":
            title = "Ms"
        elif self.gender == 'm':
            # title = "Mr"
            title = ""
        else:
            title = ""
        # return f"{title}.{self.firstname} {self.lastname}"
        return f"{self.rank} {title} {self.username} {self.firstname}"


class Matabase(models.Model):
    title = models.CharField(max_length=200, help_text="Enter movies' title")
    year = models.CharField(max_length=4, help_text="Enter released year, eg: xxxx")
    choices = (
        ('d', 'Downloaded'),
        ('w', 'Watched'),
        ('r', 'Removed'),
    )
    status = models.CharField(max_length=10, choices=choices, default='d', help_text="d: Downloaded, w: Watched, r: Removed")
    createdDate = models.DateField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    createdUser = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, default=1, related_name="createUser")
    updatedUser = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, default=1, related_name="updateUser")

    class Meta:
        ordering = ['-createdDate', 'title']
        # constraints = [
        #     models.UniqueConstraint(
        #         fields=['title', 'year'], name='uniqueDB')
        # ]
    
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        return self.title + " [" + str(self.year) + "]-[" + self.createdUser.username + "]"


"""
[
    {
        "model": "matabase.matabase",
        "pk": 1,
        "fields": {
            "title": "007 Spectre 007 องค์กรลับ ดับพยัคฆ์ร้าย",
            "year": "2005",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-09T07:33:52.467Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 2,
        "fields": {
            "title": "11 14 Eleven Fourteen",
            "year": "2003",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:04:08Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 3,
        "fields": {
            "title": "127 Hours",
            "year": "2010",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:07:16Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 4,
        "fields": {
            "title": "13 Sins",
            "year": "2014",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:09:50Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 5,
        "fields": {
            "title": "13 Hours The Secret Soldiers Of Benghazi",
            "year": "2016",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:09:50Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 6,
        "fields": {
            "title": "1BR",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:09:50Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 7,
        "fields": {
            "title": "2 Guns",
            "year": "2013",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:09:50Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 8,
        "fields": {
            "title": "The Old Guard",
            "year": "2020",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:15:51Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 9,
        "fields": {
            "title": "21 Bridges",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:16:15Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 10,
        "fields": {
            "title": "211",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:16:15Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 11,
        "fields": {
            "title": "24 Hours To Live",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:16:44Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 12,
        "fields": {
            "title": "24 Redemption",
            "year": "2008",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:16:44Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 13,
        "fields": {
            "title": "3096 Days",
            "year": "2013",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:16:44Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 14,
        "fields": {
            "title": "Meters Down",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:16:44Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 15,
        "fields": {
            "title": "500 Days of Summer",
            "year": "2009",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:16:44Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 16,
        "fields": {
            "title": "6 Underground",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:16:44Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 17,
        "fields": {
            "title": "A Perfect Getaway",
            "year": "2009",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:16:44Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 18,
        "fields": {
            "title": "A Quiet Place",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:16:44Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 19,
        "fields": {
            "title": "A Simple Favor",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:16:44Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 20,
        "fields": {
            "title": "Abraham Lincoln Vampire Hunter",
            "year": "2012",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:16:44Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 21,
        "fields": {
            "title": "Accident Man",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:16:44Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 22,
        "fields": {
            "title": "Act of Valor",
            "year": "2012",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:16:44Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 23,
        "fields": {
            "title": "Adventures of A Boy Genius",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:16:44Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 24,
        "fields": {
            "title": "After The Sunset",
            "year": "2004",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:16:44Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 25,
        "fields": {
            "title": "Alita Battle Angel",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:16:44Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 26,
        "fields": {
            "title": "Allied",
            "year": "2016",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:16:44Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 27,
        "fields": {
            "title": "American Made",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:16:44Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 28,
        "fields": {
            "title": "An Inconvenient Sequel Truth to Power",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:16:44Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 29,
        "fields": {
            "title": "Angel Has Fallen ผ่ายุทธการ ดับแผนอหังการ์",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:16:44Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 30,
        "fields": {
            "title": "Anna",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:16:44Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 31,
        "fields": {
            "title": "Annabelle Comes Home",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:16:44Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 32,
        "fields": {
            "title": "Annabelle Creation",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:16:44Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 33,
        "fields": {
            "title": "Anon",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:16:44Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 34,
        "fields": {
            "title": "Ant Man and the Wasp",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:17:17Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 35,
        "fields": {
            "title": "Arctic",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:17:17Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 36,
        "fields": {
            "title": "Argo",
            "year": "2012",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:17:17Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 37,
        "fields": {
            "title": "Asher",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:17:17Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 38,
        "fields": {
            "title": "Attraction 2 Invasion",
            "year": "2020",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:17:17Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 39,
        "fields": {
            "title": "Ava",
            "year": "2020",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:17:17Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 40,
        "fields": {
            "title": "Baby Driver",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:17:17Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 41,
        "fields": {
            "title": "Bad Boys คู่หูขวางนรก",
            "year": "1995",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:17:17Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 42,
        "fields": {
            "title": "Bad Boys คู่หูขวางนรก",
            "year": "2003",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:17:17Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 43,
        "fields": {
            "title": "Bad company",
            "year": "2002",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:17:17Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 44,
        "fields": {
            "title": "Bad Boys for Life",
            "year": "2020",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:17:17Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 45,
        "fields": {
            "title": "Bad Genius",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:17:17Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 46,
        "fields": {
            "title": "Barely Lethal",
            "year": "2015",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:17:17Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 47,
        "fields": {
            "title": "Batman Bad Blood",
            "year": "2016",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:17:17Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 48,
        "fields": {
            "title": "Batman Begins บีกินส์",
            "year": "2005",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:17:17Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 49,
        "fields": {
            "title": "Batman The Dark Knight",
            "year": "2008",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:17:17Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 50,
        "fields": {
            "title": "Batman The Dark Knight Rises",
            "year": "2012",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:17:17Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 51,
        "fields": {
            "title": "Battleship",
            "year": "2012",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:17:17Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 52,
        "fields": {
            "title": "Belleville Cop",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:17:17Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 53,
        "fields": {
            "title": "Better days",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:17:17Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 54,
        "fields": {
            "title": "Beyond the คนพลังเหนือโลก",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:17:17Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 55,
        "fields": {
            "title": "Beyond the Edge",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:17:17Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 56,
        "fields": {
            "title": "Birds of Prey",
            "year": "2020",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:17:17Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 57,
        "fields": {
            "title": "Black Christmas",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:17:17Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 58,
        "fields": {
            "title": "Bleeding Steel",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:17:17Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 59,
        "fields": {
            "title": "Bloodshot",
            "year": "2020",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:17:17Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 60,
        "fields": {
            "title": "Blue Miracle",
            "year": "2021",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:17:17Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 61,
        "fields": {
            "title": "Body บอดี้ ศพ#19",
            "year": "2007",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:17:17Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 62,
        "fields": {
            "title": "Bumblebee",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:17:17Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 63,
        "fields": {
            "title": "CRADLE 2 THE GRAVE คู่อริ ถล่มยกเมือง",
            "year": "2003",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:20:36Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 64,
        "fields": {
            "title": "Can You Keep A Secret",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:20:36Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 65,
        "fields": {
            "title": "Cashback",
            "year": "2006",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:20:36Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 66,
        "fields": {
            "title": "Cats And Peachtopia",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:20:36Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 67,
        "fields": {
            "title": "Charlies Angels",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:20:36Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 68,
        "fields": {
            "title": "Child's Play",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:20:36Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 69,
        "fields": {
            "title": "Chinese Zodiac",
            "year": "2012",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:20:36Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 70,
        "fields": {
            "title": "Chips",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:20:36Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 71,
        "fields": {
            "title": "City Hunter",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:20:36Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 72,
        "fields": {
            "title": "Classmates Minus",
            "year": "2020",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:20:36Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 73,
        "fields": {
            "title": "Cold Pursuit",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:20:36Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 74,
        "fields": {
            "title": "Company of Heroes",
            "year": "2013",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:20:36Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 75,
        "fields": {
            "title": "Con Air",
            "year": "1997",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:20:36Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 76,
        "fields": {
            "title": "Coidential Assignment",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:20:36Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 77,
        "fields": {
            "title": "Contagion สัมผัสล้างโลก",
            "year": "2011",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:20:36Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 78,
        "fields": {
            "title": "Crawl",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:20:36Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 79,
        "fields": {
            "title": "Crazy , Stupid , Love",
            "year": "2011",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:20:36Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 80,
        "fields": {
            "title": "Criminal",
            "year": "2016",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:20:36Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 81,
        "fields": {
            "title": "Crooked House",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:20:36Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 82,
        "fields": {
            "title": "Day's Home",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 83,
        "fields": {
            "title": "Danger Close The Battle of Long Tan",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 84,
        "fields": {
            "title": "Dark Waters",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 85,
        "fields": {
            "title": "Death wish",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 86,
        "fields": {
            "title": "Deception",
            "year": "2008",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 88,
        "fields": {
            "title": "Den of Thieves",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 89,
        "fields": {
            "title": "Derailed",
            "year": "2005",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 90,
        "fields": {
            "title": "Die Hard",
            "year": "1988",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 91,
        "fields": {
            "title": "Die Hard",
            "year": "1990",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 92,
        "fields": {
            "title": "Die Hard 3 With a Vengeance",
            "year": "1995",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 93,
        "fields": {
            "title": "Die Hard 4 Live Free or Die Harde",
            "year": "2007",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 94,
        "fields": {
            "title": "Die Hard 5 A Good Day to Die Hard",
            "year": "2013",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 95,
        "fields": {
            "title": "Dolittle",
            "year": "2020",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 96,
        "fields": {
            "title": "Don't Breathe",
            "year": "2016",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 97,
        "fields": {
            "title": "Doomsday",
            "year": "2008",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-25T15:46:09.568Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 98,
        "fields": {
            "title": "Drive Angry",
            "year": "2011",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 99,
        "fields": {
            "title": "Eagle Eye แผนสังหารพลิกนรก",
            "year": "2008",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 100,
        "fields": {
            "title": "Edge of ซูเปอร์นักรบดับทัพอสูร",
            "year": "2014",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 101,
        "fields": {
            "title": "Elektra",
            "year": "2005",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 103,
        "fields": {
            "title": "Enemy at Gates",
            "year": "2001",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 104,
        "fields": {
            "title": "Escape Room",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 105,
        "fields": {
            "title": "Evidence",
            "year": "2013",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 106,
        "fields": {
            "title": "Extraction",
            "year": "2020",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 107,
        "fields": {
            "title": "FRIEND ZONE",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 108,
        "fields": {
            "title": "Fanday",
            "year": "2016",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 109,
        "fields": {
            "title": "Faster",
            "year": "2010",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 110,
        "fields": {
            "title": "Fatima",
            "year": "2020",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 111,
        "fields": {
            "title": "Femme Fatale",
            "year": "2002",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 112,
        "fields": {
            "title": "Ferdinand",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 113,
        "fields": {
            "title": "Final Score",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 114,
        "fields": {
            "title": "Firewall หักดิบระห่ำ แผนจารกรรมพันล้าน",
            "year": "2006",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 115,
        "fields": {
            "title": "First Kill",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 116,
        "fields": {
            "title": "First Man",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 117,
        "fields": {
            "title": "Five Feet Apart",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 118,
        "fields": {
            "title": "Four Brothers",
            "year": "2005",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 119,
        "fields": {
            "title": "Fractured",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 120,
        "fields": {
            "title": "Freaky",
            "year": "2020",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 121,
        "fields": {
            "title": "Friend Request",
            "year": "2016",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 122,
        "fields": {
            "title": "Frozen II",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 123,
        "fields": {
            "title": "Furry Vengeance",
            "year": "2010",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 124,
        "fields": {
            "title": "G I Joe Retaliation",
            "year": "2013",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 125,
        "fields": {
            "title": "G I Joe The Rise Of Cobra",
            "year": "2009",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 126,
        "fields": {
            "title": "Game Night",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 127,
        "fields": {
            "title": "Gemini Man",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 128,
        "fields": {
            "title": "Geostorm",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 129,
        "fields": {
            "title": "Get Out ลวงร่างจิตหลอน",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 130,
        "fields": {
            "title": "Get the คนมหากาฬระอุ",
            "year": "2012",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 131,
        "fields": {
            "title": "Ghost Rider Spirit Of Vengeance",
            "year": "2011",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 132,
        "fields": {
            "title": "Ghost Wife",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 133,
        "fields": {
            "title": "Girl House",
            "year": "2014",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 134,
        "fields": {
            "title": "Goal II Living the Dream",
            "year": "2007",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 135,
        "fields": {
            "title": "Goal The Dream Begins",
            "year": "2005",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 136,
        "fields": {
            "title": "Goal! 3 Taking on the World",
            "year": "2009",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 137,
        "fields": {
            "title": "Golden Job",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 138,
        "fields": {
            "title": "Gone Girl เล่นซ่อนหาย",
            "year": "2014",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 139,
        "fields": {
            "title": "Gone In Sixty Seconds",
            "year": "2000",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 140,
        "fields": {
            "title": "Goosebumps 2 Haunted Halloween",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 141,
        "fields": {
            "title": "Green Lantern",
            "year": "2011",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 142,
        "fields": {
            "title": "Green Zone",
            "year": "2010",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 143,
        "fields": {
            "title": "Green Book",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 144,
        "fields": {
            "title": "Greta",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 145,
        "fields": {
            "title": "Gridlocked",
            "year": "2015",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 146,
        "fields": {
            "title": "Gullivers Travels",
            "year": "2010",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 147,
        "fields": {
            "title": "Guns Akimbo มือพี่ไม่ว่าง",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 148,
        "fields": {
            "title": "HOMESTAY",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 149,
        "fields": {
            "title": "Happy Death Day",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 150,
        "fields": {
            "title": "Happy Old Year",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 151,
        "fields": {
            "title": "Headhunters",
            "year": "2011",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 152,
        "fields": {
            "title": "Hitman Agent สายลับ",
            "year": "2015",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 153,
        "fields": {
            "title": "Hitmans Bodyguard",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 154,
        "fields": {
            "title": "Hot Fuzz",
            "year": "2007",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 155,
        "fields": {
            "title": "Hotel Mumbai",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 156,
        "fields": {
            "title": "Hotel Transylvania 3 Summer Vacation",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 157,
        "fields": {
            "title": "House of Fury",
            "year": "2005",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 158,
        "fields": {
            "title": "I Am Legend",
            "year": "2007",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 159,
        "fields": {
            "title": "I Saw the Devil",
            "year": "2010",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 160,
        "fields": {
            "title": "I Split On Your Grave 2",
            "year": "2013",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 161,
        "fields": {
            "title": "I Split On Your Grave 3 Vengeance Is Mine",
            "year": "2015",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 162,
        "fields": {
            "title": "Ice Age Collision Course",
            "year": "2016",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 163,
        "fields": {
            "title": "If Only เอ่ยคำว่ารัก",
            "year": "2004",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 164,
        "fields": {
            "title": "Inception",
            "year": "2010",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 165,
        "fields": {
            "title": "Instant Family",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 166,
        "fields": {
            "title": "Into the ฉกมหาภัย",
            "year": "2005",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 167,
        "fields": {
            "title": "Ip Man 4 The Finale ยิปมัน 4",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 168,
        "fields": {
            "title": "It Chapter Two",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 169,
        "fields": {
            "title": "Jack Reacher ยอดคนสืบระห่ำ",
            "year": "2012",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 170,
        "fields": {
            "title": "Jason Bourne",
            "year": "2016",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 171,
        "fields": {
            "title": "Jeepers Creepers 1",
            "year": "2001",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 172,
        "fields": {
            "title": "Jeepers Creepers 2",
            "year": "2003",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 173,
        "fields": {
            "title": "Jeepers Creepers",
            "year": "2001",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 174,
        "fields": {
            "title": "Jeepers Creepers 3",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 175,
        "fields": {
            "title": "Jexi",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 176,
        "fields": {
            "title": "Jigsaw",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 177,
        "fields": {
            "title": "John Wick",
            "year": "2014",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 178,
        "fields": {
            "title": "John Wick 2",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 179,
        "fields": {
            "title": "John Wick 3 Parabellum",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 180,
        "fields": {
            "title": "Joker",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 181,
        "fields": {
            "title": "Jom Kamang Weth",
            "year": "2020",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 182,
        "fields": {
            "title": "Jumanji The Next Level",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 183,
        "fields": {
            "title": "Jungle",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 184,
        "fields": {
            "title": "Kick Ass 1 เกรียนโคตรมหาประลัย",
            "year": "2010",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 185,
        "fields": {
            "title": "Kick Ass 2 เกรียนโคตรมหาประลัย",
            "year": "2013",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 186,
        "fields": {
            "title": "Killing Ground",
            "year": "2016",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 187,
        "fields": {
            "title": "Kingsman The Golden Circle",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 188,
        "fields": {
            "title": "Kiss of ล่าข้ามโลก",
            "year": "2001",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 189,
        "fields": {
            "title": "Knight and day",
            "year": "2010",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 190,
        "fields": {
            "title": "Knock Knock",
            "year": "2015",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 191,
        "fields": {
            "title": "Knowing",
            "year": "2009",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 192,
        "fields": {
            "title": "Latitude 6",
            "year": "2015",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 193,
        "fields": {
            "title": "Leap Year",
            "year": "2010",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 194,
        "fields": {
            "title": "Lockout (แหกคุกกลางอวกาศ)",
            "year": "2012",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 195,
        "fields": {
            "title": "Logan Lucky",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 196,
        "fields": {
            "title": "Lone Survivor",
            "year": "2014",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 197,
        "fields": {
            "title": "Lost Bullet",
            "year": "2020",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 198,
        "fields": {
            "title": "Low Season",
            "year": "2020",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 199,
        "fields": {
            "title": "Lucky Number Slevin",
            "year": "2006",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 200,
        "fields": {
            "title": "Lucy ลูซี่ สวยพิฆาต",
            "year": "2014",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 201,
        "fields": {
            "title": "Madagascar 3 Europe s Most Wanted มาดากัสการ์ 3 ข้ามป่าไปซ่ายุโรป",
            "year": "2012",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 202,
        "fields": {
            "title": "Malavita พันธุ์แสบยกตระกูล",
            "year": "2013",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 203,
        "fields": {
            "title": "Man Of Steel",
            "year": "2013",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 204,
        "fields": {
            "title": "Marvel 21 Captain Marvel กัปตันมาร์เวล",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 205,
        "fields": {
            "title": "Mechanic Resurrection",
            "year": "2016",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 206,
        "fields": {
            "title": "Men in Black 1 หน่วยจารชนพิทักษ์โลก 1",
            "year": "1997",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 207,
        "fields": {
            "title": "Men in Black 2 หน่วยจารชนพิทักษ์โลก 2",
            "year": "2002",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 208,
        "fields": {
            "title": "Men in Black 3 หน่วยจารชนพิทักษ์โลก 3",
            "year": "2012",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 209,
        "fields": {
            "title": "Men in Black International",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 210,
        "fields": {
            "title": "Miami Vice คู่เดือดไมอามี่่",
            "year": "2006",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 211,
        "fields": {
            "title": "Miss Congeniality",
            "year": "2000",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 212,
        "fields": {
            "title": "Miss Congeniality 2",
            "year": "2005",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 213,
        "fields": {
            "title": "Mission Impossible 1 ผ่าปฎิบัติการสะท้านโลก 1",
            "year": "1996",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 214,
        "fields": {
            "title": "Mission Impossible 2 ผ่าปฎิบัติการสะท้านโลก 2",
            "year": "2000",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 215,
        "fields": {
            "title": "Mission Impossible 3 ผ่าปฎิบัติการสะท้านโลก 3",
            "year": "2006",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 216,
        "fields": {
            "title": "Mission Impossible 4 ปฎิบัติการไร้เงา 4",
            "year": "2011",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 217,
        "fields": {
            "title": "Mission Impossible 5 Rogue Nation มิชชั่น อิมพอสซิเบิ้ล ปฏิบัติการรัฐอำพราง",
            "year": "2015",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 218,
        "fields": {
            "title": "Mission Impossible 6 Fallout",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 219,
        "fields": {
            "title": "Monster Hunter",
            "year": "2020",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 220,
        "fields": {
            "title": "Mr & Mrs Smith",
            "year": "2005",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 221,
        "fields": {
            "title": "Mr Hurt มือวางอันดับเจ็บ",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 222,
        "fields": {
            "title": "Murder on the Orient Express",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 223,
        "fields": {
            "title": "National Treasure",
            "year": "2004",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 224,
        "fields": {
            "title": "National Treasure 2 Book of Secrets",
            "year": "2007",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 225,
        "fields": {
            "title": "Need For Speed",
            "year": "2014",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 226,
        "fields": {
            "title": "Neighbors",
            "year": "2014",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 227,
        "fields": {
            "title": "Neighbors 2",
            "year": "2016",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 228,
        "fields": {
            "title": "Night at พิพิธภัณฑ์มันส์ทะลุโลก",
            "year": "2006",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 229,
        "fields": {
            "title": "Night at the Museum Battle of the Smithsonian",
            "year": "2009",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 230,
        "fields": {
            "title": "Night Hunter",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 231,
        "fields": {
            "title": "No Country for Old Men",
            "year": "2007",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 232,
        "fields": {
            "title": "Non Stop ยึดเหนือฟ้า",
            "year": "2014",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 234,
        "fields": {
            "title": "Oblivion",
            "year": "2013",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 235,
        "fields": {
            "title": "Ocean's 8",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 236,
        "fields": {
            "title": "Official Secrets",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 237,
        "fields": {
            "title": "Only the Brave",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 238,
        "fields": {
            "title": "Orphan",
            "year": "2009",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 239,
        "fields": {
            "title": "Our Kind of Traitor",
            "year": "2016",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 240,
        "fields": {
            "title": "Our House",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 241,
        "fields": {
            "title": "Overdrive",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 242,
        "fields": {
            "title": "Overlord",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 243,
        "fields": {
            "title": "P2",
            "year": "2007",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 244,
        "fields": {
            "title": "Pacific Rim Uprising",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 245,
        "fields": {
            "title": "Pan",
            "year": "2015",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 246,
        "fields": {
            "title": "Panic Room ห้องเช่านิรภัยท้านรก",
            "year": "2002",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 247,
        "fields": {
            "title": "Papillon",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 248,
        "fields": {
            "title": "Pawn Shop Chronicles",
            "year": "2013",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 249,
        "fields": {
            "title": "Paycheck แกะรอยอดีต ล่าปมปริศนา",
            "year": "2003",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 250,
        "fields": {
            "title": "Peppermint",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 251,
        "fields": {
            "title": "Phone Booth",
            "year": "2003",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 252,
        "fields": {
            "title": "Pirates of the Caribbean 1 The Curse of the Black Pearl",
            "year": "2003",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 253,
        "fields": {
            "title": "Pirates of the Caribbean 2",
            "year": "2006",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 254,
        "fields": {
            "title": "Pirates of the Caribbean 3 At World's End",
            "year": "2007",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 255,
        "fields": {
            "title": "Pirates of the Caribbean 4 on stranger tides",
            "year": "2011",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 256,
        "fields": {
            "title": "Pirates of the Caribbean Dead Men Tell No Tales",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 257,
        "fields": {
            "title": "Polaroid",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 258,
        "fields": {
            "title": "Poseidon มหาวิบัติเรือยักษ์",
            "year": "2006",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 259,
        "fields": {
            "title": "Primal",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 260,
        "fields": {
            "title": "Primeval",
            "year": "2007",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 261,
        "fields": {
            "title": "Prisoners",
            "year": "2013",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 262,
        "fields": {
            "title": "Professor Marston and the Wonder Women",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 263,
        "fields": {
            "title": "Rambo Last Blood",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 264,
        "fields": {
            "title": "Ramona and Beezus",
            "year": "2010",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 265,
        "fields": {
            "title": "Rampant",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 266,
        "fields": {
            "title": "Ready Player One",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 267,
        "fields": {
            "title": "Red",
            "year": "2010",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 268,
        "fields": {
            "title": "Red 2",
            "year": "2013",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 269,
        "fields": {
            "title": "Replicas",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 270,
        "fields": {
            "title": "Rescue Dawn",
            "year": "2006",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 271,
        "fields": {
            "title": "Robin Hood",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 272,
        "fields": {
            "title": "Rogue",
            "year": "2007",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 273,
        "fields": {
            "title": "Room 1408",
            "year": "2007",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 274,
        "fields": {
            "title": "Rush Hour คู่ใหญ่ฟัดเต็มสปีด",
            "year": "1998",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 275,
        "fields": {
            "title": "Rush Hour คู่ใหญ่ฟัดเต็มสปีด",
            "year": "2001",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 276,
        "fields": {
            "title": "Rush Hour คู่ใหญ่ฟัดเต็มสปีด",
            "year": "2007",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 277,
        "fields": {
            "title": "SOLACE",
            "year": "2015",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 278,
        "fields": {
            "title": "Sabotage",
            "year": "2014",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 279,
        "fields": {
            "title": "Safe โครตระห่ำ ทะลุรหัส",
            "year": "2012",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 280,
        "fields": {
            "title": "Safe House ภารกิจเดือดฝ่าตาย",
            "year": "2012",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 281,
        "fields": {
            "title": "Sahara พิชิตขุมทรัพย์หมื่นฟาเรนไฮต์",
            "year": "2005",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 282,
        "fields": {
            "title": "Salt",
            "year": "2010",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 283,
        "fields": {
            "title": "San Andreas มหาวินาศแผ่นดินแยก",
            "year": "2015",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 284,
        "fields": {
            "title": "Snake eyes",
            "year": "2021",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 285,
        "fields": {
            "title": "Save Yourselves!",
            "year": "2020",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 286,
        "fields": {
            "title": "Searching",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 287,
        "fields": {
            "title": "Sherlock Holmes ดับแผนพิฆาตโลก",
            "year": "2009",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 288,
        "fields": {
            "title": "Sherlock Holmes 2 A Game Of Shadows",
            "year": "2011",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 289,
        "fields": {
            "title": "Shooter คนระห่ำปืนดือด",
            "year": "2007",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 290,
        "fields": {
            "title": "Show Dogs",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 291,
        "fields": {
            "title": "Shutter Island",
            "year": "2010",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 292,
        "fields": {
            "title": "Sicario Day of the Soldado",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 293,
        "fields": {
            "title": "Signs",
            "year": "2002",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 295,
        "fields": {
            "title": "Skyscraper",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 296,
        "fields": {
            "title": "Sleepless",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 297,
        "fields": {
            "title": "Smurfs The Lost Village",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 298,
        "fields": {
            "title": "Snatch",
            "year": "2000",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 299,
        "fields": {
            "title": "Sniper Ultimate Kill",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 300,
        "fields": {
            "title": "Snow Dogs",
            "year": "2002",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 301,
        "fields": {
            "title": "Snowden",
            "year": "2016",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 302,
        "fields": {
            "title": "Snowpiercer สโนว์เพียซเซอร์ MKV",
            "year": "2013",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 303,
        "fields": {
            "title": "Spenser Coidential",
            "year": "2020",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 304,
        "fields": {
            "title": "Spies in Disguise",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 305,
        "fields": {
            "title": "Steal My Heart",
            "year": "2013",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 306,
        "fields": {
            "title": "Stealth",
            "year": "2005",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 307,
        "fields": {
            "title": "Stratton แผนแค้น ถล่มลอนดอน",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 308,
        "fields": {
            "title": "StreetKings",
            "year": "2008",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 309,
        "fields": {
            "title": "Submergence",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 310,
        "fields": {
            "title": "Suburbicon",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 311,
        "fields": {
            "title": "Suicide Squad",
            "year": "2016",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 312,
        "fields": {
            "title": "Superman Return ซุปเปอร์แมนรีเทริ์น",
            "year": "2006",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 313,
        "fields": {
            "title": "Swordfish",
            "year": "2001",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 314,
        "fields": {
            "title": "Taken 1",
            "year": "2008",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 315,
        "fields": {
            "title": "Taken 2",
            "year": "2012",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 316,
        "fields": {
            "title": "Taken 3",
            "year": "2014",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 317,
        "fields": {
            "title": "Taking Lives",
            "year": "2004",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 318,
        "fields": {
            "title": "Tears of the Sun ฝ่ายุทธกรสุริยะทมิฬ",
            "year": "2003",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-13T09:53:54.429Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 319,
        "fields": {
            "title": "Ted",
            "year": "2012",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 320,
        "fields": {
            "title": "Ted 2",
            "year": "2015",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 321,
        "fields": {
            "title": "Tenet",
            "year": "2020",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 322,
        "fields": {
            "title": "Terminator 1 ฅนเหล็ก (2029) ภาต",
            "year": "1984",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 323,
        "fields": {
            "title": "Terminator 2 Judgment Day ฅนเหล็ก",
            "year": "1991",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 324,
        "fields": {
            "title": "Terminator 3 Rise Of The Machines ฅนเหล็ก",
            "year": "2003",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 325,
        "fields": {
            "title": "Terminator Genisys มหาวิบัติจักรกลยึดโลก",
            "year": "2015",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 326,
        "fields": {
            "title": "Terminator Salvation 4 Director's cut ฅนเหล็ก",
            "year": "2009",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 327,
        "fields": {
            "title": "Terminator Dark Fate",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 328,
        "fields": {
            "title": "The A Team",
            "year": "2010",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 329,
        "fields": {
            "title": "The Accidental Spy วิ่งระเบิดฟัด",
            "year": "2001",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 330,
        "fields": {
            "title": "The Amazing Spider Man 1",
            "year": "2012",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 331,
        "fields": {
            "title": "The Amazing Spider Man 2",
            "year": "2014",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 332,
        "fields": {
            "title": "The Angry Birds Movie",
            "year": "2016",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 333,
        "fields": {
            "title": "The Bank Job เปิดตำนานปล้นบันลือโลก",
            "year": "2008",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 334,
        "fields": {
            "title": "The Blind Side",
            "year": "2009",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-24T12:42:02.161Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 335,
        "fields": {
            "title": "The Bourne 1 Identity",
            "year": "2002",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 336,
        "fields": {
            "title": "The Bourne 2 Supremacy",
            "year": "2004",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 337,
        "fields": {
            "title": "The Bourne 3 Ultimatum",
            "year": "2007",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 338,
        "fields": {
            "title": "The Bourne 4 Legacy",
            "year": "2012",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 339,
        "fields": {
            "title": "The Boy Next Door",
            "year": "2015",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 340,
        "fields": {
            "title": "The Boy ตุ๊กตาซ่อนผี",
            "year": "2016",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 341,
        "fields": {
            "title": "The Collector",
            "year": "2009",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 342,
        "fields": {
            "title": "The Contractor",
            "year": "2007",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 343,
        "fields": {
            "title": "The Day After Tomorrow",
            "year": "2004",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 344,
        "fields": {
            "title": "The Day the Earth Stood Still",
            "year": "2008",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 345,
        "fields": {
            "title": "The Dictator",
            "year": "2012",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 346,
        "fields": {
            "title": "The Equalizer 2",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-20T04:05:48.287Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 347,
        "fields": {
            "title": "The Expendables โครตคนทีมมหากาฬ",
            "year": "2010",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 348,
        "fields": {
            "title": "The Expendables โครตคนทีมมหากาฬ",
            "year": "2012",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 349,
        "fields": {
            "title": "The Expendables ทีมเอ็กซ์เพนเดเบิ้ล",
            "year": "2014",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 350,
        "fields": {
            "title": "The Girl in the Spiders",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 351,
        "fields": {
            "title": "The Green Hornet",
            "year": "2011",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 352,
        "fields": {
            "title": "The Intouchables พิชิตทุกสิ่ง",
            "year": "2011",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 353,
        "fields": {
            "title": "The Kingdom ล่าข้ามแผ่นดิน",
            "year": "2007",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 354,
        "fields": {
            "title": "The Last Stand",
            "year": "2013",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 355,
        "fields": {
            "title": "The Mexican",
            "year": "2001",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 356,
        "fields": {
            "title": "The Next ee Days",
            "year": "2010",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 357,
        "fields": {
            "title": "The Night Before",
            "year": "2015",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 358,
        "fields": {
            "title": "The November Man พลิกเกมส์ฆ่า ล่าพยัคฆ์ร้าย",
            "year": "2014",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 359,
        "fields": {
            "title": "The Other Guys",
            "year": "2010",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 360,
        "fields": {
            "title": "The Possession of Hannah Grace",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 361,
        "fields": {
            "title": "The Promise",
            "year": "2005",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 362,
        "fields": {
            "title": "The Punisher เพชฌฆาตมหากาฬ",
            "year": "2004",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 363,
        "fields": {
            "title": "The Punisher เพชฌฆาตมหากาฬ",
            "year": "2008",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 364,
        "fields": {
            "title": "The Ring 1",
            "year": "2002",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 365,
        "fields": {
            "title": "The Ring 2",
            "year": "2005",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 366,
        "fields": {
            "title": "The Ring 3",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 367,
        "fields": {
            "title": "The Rock ยึดนรกป้อมทมิฬ",
            "year": "1996",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 368,
        "fields": {
            "title": "The Rundown โคตรคนล่าขุมทรัพย์",
            "year": "2003",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 369,
        "fields": {
            "title": "The Samaritan ลวงทรชนปล้นล้างมือ",
            "year": "2012",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 370,
        "fields": {
            "title": "The Scorpion King 1 ศึกราชันย์แผ่นดินเดือด 1",
            "year": "2002",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 371,
        "fields": {
            "title": "The Scorpion King 2 ศึกราชันย์แผ่นดินเดือด 2",
            "year": "2008",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 372,
        "fields": {
            "title": "The Scorpion King 3 ศึกราชันย์แผ่นดินเดือด 3",
            "year": "2012",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 373,
        "fields": {
            "title": "The Social Dilemma",
            "year": "2020",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 374,
        "fields": {
            "title": "The Stepfather (UNRATED) พ่อเลี้ยงโหดโคตรอำมหิต",
            "year": "2009",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 375,
        "fields": {
            "title": "The Sum of All Fears วิกฤตนิวเคลียร์ถล่มโลก",
            "year": "2002",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 376,
        "fields": {
            "title": "The Thieves ดาวโจรปล้นโคตรเพชร",
            "year": "2012",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 377,
        "fields": {
            "title": "The Tourist",
            "year": "2010",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 378,
        "fields": {
            "title": "The Town",
            "year": "2010",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 379,
        "fields": {
            "title": "The Woman In Black",
            "year": "2012",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 380,
        "fields": {
            "title": "The Woman in Black 2 Angel of Death",
            "year": "2014",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 381,
        "fields": {
            "title": "The Last Recipe สูตรลับเมนูยอดเชฟ",
            "year": "2017",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-29T02:24:17.688Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 382,
        "fields": {
            "title": "The last samurai",
            "year": "2003",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 383,
        "fields": {
            "title": "The peacemaker หยุดนิวเคลีย์มหาภัยถล่มโลก",
            "year": "1997",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 384,
        "fields": {
            "title": "The Accountant",
            "year": "2016",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 385,
        "fields": {
            "title": "The Aams Family",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 386,
        "fields": {
            "title": "The Amityville Horror",
            "year": "2005",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 388,
        "fields": {
            "title": "The Best Offer",
            "year": "2013",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 389,
        "fields": {
            "title": "The Big Short",
            "year": "2015",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 390,
        "fields": {
            "title": "The Commuter",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 391,
        "fields": {
            "title": "The Current War Director's Cut",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 392,
        "fields": {
            "title": "The Curse Of La Llorona",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 393,
        "fields": {
            "title": "The Foreigner",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 394,
        "fields": {
            "title": "The General's Daughter",
            "year": "1999",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 395,
        "fields": {
            "title": "The Guest",
            "year": "2014",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 396,
        "fields": {
            "title": "The Hummingbird Project",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 397,
        "fields": {
            "title": "The Hurricane Heist",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 398,
        "fields": {
            "title": "The Hustle",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 399,
        "fields": {
            "title": "The Interpreter",
            "year": "2005",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 400,
        "fields": {
            "title": "The Invisible Man",
            "year": "2020",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 401,
        "fields": {
            "title": "The Last Castle",
            "year": "2001",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 402,
        "fields": {
            "title": "The Last Days of American Crime",
            "year": "2020",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 403,
        "fields": {
            "title": "The Lion King",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 404,
        "fields": {
            "title": "The Meg",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 405,
        "fields": {
            "title": "The Mummy",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 406,
        "fields": {
            "title": "The New Mutants",
            "year": "2020",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 407,
        "fields": {
            "title": "The Pool",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 408,
        "fields": {
            "title": "The Post",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 409,
        "fields": {
            "title": "The Prodigy",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 410,
        "fields": {
            "title": "The Queens Corgi",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 411,
        "fields": {
            "title": "The Rhy Section",
            "year": "2020",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 412,
        "fields": {
            "title": "The Score",
            "year": "2001",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 413,
        "fields": {
            "title": "The Secret Life of Pets 2",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 414,
        "fields": {
            "title": "The Strangers Prey at Night",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 415,
        "fields": {
            "title": "The Taking of Pelham 123",
            "year": "2009",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 416,
        "fields": {
            "title": "The Unity of Heroes",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 417,
        "fields": {
            "title": "Thor Ragnarok",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 418,
        "fields": {
            "title": "Tom And Jerry",
            "year": "2021",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 419,
        "fields": {
            "title": "Tomb Raider Lara Croft 1",
            "year": "2001",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 420,
        "fields": {
            "title": "Tomb Raider Lara Croft 2",
            "year": "2003",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 421,
        "fields": {
            "title": "Tomb Raider",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 422,
        "fields": {
            "title": "Tomorrowland",
            "year": "2015",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 423,
        "fields": {
            "title": "Torque",
            "year": "2004",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 424,
        "fields": {
            "title": "Total Recall",
            "year": "2012",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 425,
        "fields": {
            "title": "Toy Story",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 426,
        "fields": {
            "title": "Transformers 1",
            "year": "2007",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 427,
        "fields": {
            "title": "Transformers 2 Revenge of the Fallen",
            "year": "2009",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 428,
        "fields": {
            "title": "Transformers 3 Dark of the Moon",
            "year": "2011",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 429,
        "fields": {
            "title": "Transformers 4 Age of Extinction",
            "year": "2014",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 430,
        "fields": {
            "title": "Transformers The Last Knight",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 431,
        "fields": {
            "title": "Trespass",
            "year": "2011",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 432,
        "fields": {
            "title": "True Legend ตำนานหมัดเมา",
            "year": "2010",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 433,
        "fields": {
            "title": "Truth or Dare",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 434,
        "fields": {
            "title": "Undercover Punch and Gun",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 435,
        "fields": {
            "title": "Unleashed",
            "year": "2005",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 436,
        "fields": {
            "title": "Unlocked",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 437,
        "fields": {
            "title": "Unthinkable",
            "year": "2010",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 438,
        "fields": {
            "title": "Upgrade",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 439,
        "fields": {
            "title": "Vanguard",
            "year": "2020",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 440,
        "fields": {
            "title": "Vanguard",
            "year": "2020",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 442,
        "fields": {
            "title": "Wanted",
            "year": "2008",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 443,
        "fields": {
            "title": "War",
            "year": "2007",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 444,
        "fields": {
            "title": "We Can Be Heroes",
            "year": "2020",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 445,
        "fields": {
            "title": "We Own the Night",
            "year": "2007",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 446,
        "fields": {
            "title": "Welcome to Jungle",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 447,
        "fields": {
            "title": "When a Stranger Calls",
            "year": "2006",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 448,
        "fields": {
            "title": "Whered You Go Bernadette",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 449,
        "fields": {
            "title": "White House Down",
            "year": "2013",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 450,
        "fields": {
            "title": "Whiteout",
            "year": "2009",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 451,
        "fields": {
            "title": "Wicker Park",
            "year": "2004",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 452,
        "fields": {
            "title": "Wild card มือฆ่าเอโพดำ",
            "year": "2015",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 453,
        "fields": {
            "title": "Wolf Creek",
            "year": "2013",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 454,
        "fields": {
            "title": "Wonder Woman",
            "year": "2020",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 455,
        "fields": {
            "title": "Wrong Turn",
            "year": "2003",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 456,
        "fields": {
            "title": "Wrong Turn 2 Dead End",
            "year": "2007",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 457,
        "fields": {
            "title": "Wrong Turn 3 Left for Dead",
            "year": "2009",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 458,
        "fields": {
            "title": "Wrong Turn 4 Bloody Beginnings",
            "year": "2011",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 459,
        "fields": {
            "title": "Wrong Turn 5 Bloodlines",
            "year": "2012",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 460,
        "fields": {
            "title": "Wrong Turn 6 Last Resort",
            "year": "2014",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 461,
        "fields": {
            "title": "Wu Xia แขนเดียว",
            "year": "2011",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 462,
        "fields": {
            "title": "X Men ศึกพลังมนุษย์เหนือโลก",
            "year": "2000",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 463,
        "fields": {
            "title": "X Men ศึกมนุษย์พลังเหนือโลก",
            "year": "2003",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 464,
        "fields": {
            "title": "X Men รวมพลังประจัญบาน",
            "year": "2006",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 465,
        "fields": {
            "title": "X Men 4 First Class",
            "year": "2011",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 466,
        "fields": {
            "title": "X Men 5 The Wolverine",
            "year": "2013",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 467,
        "fields": {
            "title": "X Men 6 Days of Future Past",
            "year": "2014",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 468,
        "fields": {
            "title": "X Men Dark Phoenix",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 469,
        "fields": {
            "title": "ZERO DARK THIRTY",
            "year": "2012",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 470,
        "fields": {
            "title": "Zombieland Double Tap",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 471,
        "fields": {
            "title": "xXx 1",
            "year": "2002",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 472,
        "fields": {
            "title": "xXx 2",
            "year": "2005",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 473,
        "fields": {
            "title": "อ้าย คนหล่อลวง",
            "year": "2020",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 474,
        "fields": {
            "title": "เร็วแรงทะลุนรก 1 The Fast and the Furious 1",
            "year": "2001",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 475,
        "fields": {
            "title": "เร็วแรงทะลุนรก 2 2 Fast 2 Furious",
            "year": "2003",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 476,
        "fields": {
            "title": "เร็วแรงทะลุนรก 3 The Fast & Furious 3 the Furious Tokyo Drift",
            "year": "2006",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 477,
        "fields": {
            "title": "เร็วแรงทะลุนรก 4 Fast Furious 4",
            "year": "2009",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 478,
        "fields": {
            "title": "เร็วแรงทะลุนรก 5 Fast Five 5",
            "year": "2011",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 479,
        "fields": {
            "title": "เร็วแรงทะลุนรก 6 The Fast & Furious 6",
            "year": "2013",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 480,
        "fields": {
            "title": "เร็วแรงทะลุนรก 7 Fast Furious 7",
            "year": "2015",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 481,
        "fields": {
            "title": "ຫົງຫາມເຕົ່າ Swan Lifts Turtle",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 482,
        "fields": {
            "title": "ຮັກອ່ຳຫຼ່ຳ Huk Aum Lum ฮักอ่ำหล่ำ",
            "year": "2013",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-08-08T07:38:06Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 483,
        "fields": {
            "title": "Fantastic Beasts The Secrets of Dumbledore",
            "year": "2022",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-04-25T14:43:22.075Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 484,
        "fields": {
            "title": "12 Years a Slave",
            "year": "2013",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-27T13:46:15.626Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 485,
        "fields": {
            "title": "Outside the Wire สมรภูมินอกลวดหนาม",
            "year": "2021",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-20T14:15:08.859Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 486,
        "fields": {
            "title": "A Dog's Journey",
            "year": "2019",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-07T13:17:40.820Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 487,
        "fields": {
            "title": "A Dog's Purpose",
            "year": "2017",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-07T14:59:55.148Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 488,
        "fields": {
            "title": "AGENT TOBY BARKS SPY DOG",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-14T01:52:22.030Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 489,
        "fields": {
            "title": "Above Suspicion ระห่ำชีวิต",
            "year": "2019",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-06T16:05:34.791Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 490,
        "fields": {
            "title": "Adrift",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-03-15T13:17:22.089Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 491,
        "fields": {
            "title": "Alien Covenant",
            "year": "2017",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-12T16:00:33.891Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 492,
        "fields": {
            "title": "All the Money in the World",
            "year": "2017",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-03-15T15:43:20.421Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 493,
        "fields": {
            "title": "Ambulance",
            "year": "2022",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-03-31T15:05:56.037Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 494,
        "fields": {
            "title": "Ammonite",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-21T22:57:35.358Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 495,
        "fields": {
            "title": "And Tomorrow the Entire World",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-14T08:58:51.321Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 496,
        "fields": {
            "title": "Antebellum",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-04-15T02:56:16.287Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 497,
        "fields": {
            "title": "Antitrust",
            "year": "2001",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-14T15:26:56.564Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 498,
        "fields": {
            "title": "Army of Dead",
            "year": "2021",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-25T15:59:43.973Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 499,
        "fields": {
            "title": "Assassination Nation",
            "year": "2018",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-12T16:01:03.064Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 500,
        "fields": {
            "title": "Awake",
            "year": "2021",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-04-15T04:43:23.069Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 501,
        "fields": {
            "title": "BIG FREAKING RAT",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-04-15T13:32:20.721Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 502,
        "fields": {
            "title": "Becky",
            "year": "2020",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-04-15T08:43:54.198Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 503,
        "fields": {
            "title": "Bedtime Stories",
            "year": "2008",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-03-29T14:19:56.627Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 504,
        "fields": {
            "title": "Black Beauty",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-04-17T11:05:52.654Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 505,
        "fields": {
            "title": "Blasted",
            "year": "2022",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-04-18T03:16:34.837Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 506,
        "fields": {
            "title": "Breach",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-04-18T05:48:22.713Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 508,
        "fields": {
            "title": "COVID 21 LETHAL VIRUS",
            "year": "2021",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-04-22T00:01:26.459Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 510,
        "fields": {
            "title": "Contraband",
            "year": "2012",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-04-15T16:02:44.816Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 511,
        "fields": {
            "title": "Copshop",
            "year": "2021",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-04-22T00:02:29.381Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 512,
        "fields": {
            "title": "Cracked",
            "year": "2022",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-04-22T08:08:26.767Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 513,
        "fields": {
            "title": "Daeng Phra Khanong",
            "year": "2022",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-04-22T14:23:11.091Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 514,
        "fields": {
            "title": "Detective Dee and The Red Eye",
            "year": "2021",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-04-05T15:28:34.661Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 515,
        "fields": {
            "title": "Doctor Strange in the Multiverse of Madness",
            "year": "2022",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-04-22T14:23:34.139Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 516,
        "fields": {
            "title": "Eraser Reborn รีบอร์น",
            "year": "2022",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-04-24T12:07:18.263Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 517,
        "fields": {
            "title": "Fast and Furious F9 The Fast Saga",
            "year": "2021",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-29T03:57:12.435Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 519,
        "fields": {
            "title": "Freaks",
            "year": "2018",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-30T13:42:17.077Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 520,
        "fields": {
            "title": "Greenland",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-05T14:53:34.854Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 521,
        "fields": {
            "title": "HOUSE OF THE DEAD 2",
            "year": "2005",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-31T07:49:59.662Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 522,
        "fields": {
            "title": "Hackers",
            "year": "1995",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-13T14:56:52.641Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 523,
        "fields": {
            "title": "Hard Kill",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-19T13:13:13.772Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 525,
        "fields": {
            "title": "Hooking Up",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-06T08:09:35.438Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 526,
        "fields": {
            "title": "I Remember",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-22T13:55:17.956Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 527,
        "fields": {
            "title": "Incantation",
            "year": "2022",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-09T13:09:02.968Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 528,
        "fields": {
            "title": "Interceptor",
            "year": "2022",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-14T06:28:54.335Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 529,
        "fields": {
            "title": "Killer Cheerleader",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-13T15:39:42.152Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 530,
        "fields": {
            "title": "L Storm คนคมโค่นพายุ",
            "year": "2018",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-12T14:09:48.577Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 532,
        "fields": {
            "title": "Love and Other Drugs",
            "year": "2010",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-20T09:09:57.759Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 533,
        "fields": {
            "title": "Man on a Ledge",
            "year": "2012",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-13T04:30:56.338Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 534,
        "fields": {
            "title": "Meet The Fockers",
            "year": "2004",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-10T00:35:55.036Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 535,
        "fields": {
            "title": "Meet the Parents",
            "year": "2000",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-10T00:36:02.841Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 536,
        "fields": {
            "title": "Memories of The Sword",
            "year": "2015",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-18T09:33:40.749Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 537,
        "fields": {
            "title": "Mirror Mirror",
            "year": "2012",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-18T12:42:03.743Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 538,
        "fields": {
            "title": "Moh Pla Wan",
            "year": "2022",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-13T14:19:45.642Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 539,
        "fields": {
            "title": "Mother Gamer",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-08T13:41:00.140Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 540,
        "fields": {
            "title": "My Cousin Rachel",
            "year": "2017",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-11T03:03:51.361Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 541,
        "fields": {
            "title": "My Spy",
            "year": "2020",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-25T14:31:11.346Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 542,
        "fields": {
            "title": "News of World",
            "year": "2021",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-13T03:08:37.585Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 544,
        "fields": {
            "title": "No Mercy",
            "year": "2010",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-31T03:04:53.946Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 545,
        "fields": {
            "title": "No Strings Attached",
            "year": "2011",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-06T14:01:42.233Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 546,
        "fields": {
            "title": "Nomadland",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-20T20:18:21.557Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 547,
        "fields": {
            "title": "Notes on A Scandal",
            "year": "2006",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-15T13:26:29.067Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 548,
        "fields": {
            "title": "One for Road",
            "year": "2021",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-12T06:35:19.732Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 549,
        "fields": {
            "title": "Pets United ขนปุยรวมพลัง",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-22T15:21:00.065Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 550,
        "fields": {
            "title": "Playing with Fire",
            "year": "2019",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-10T02:16:02.686Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 551,
        "fields": {
            "title": "Point Blank ชนแหลก",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-26T15:37:34.616Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 553,
        "fields": {
            "title": "QUAN DAO THE JOURNEY OF A BOXER",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-29T13:32:34.979Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 554,
        "fields": {
            "title": "REDEMPTION DAY",
            "year": "2021",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-28T03:06:43.190Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 555,
        "fields": {
            "title": "ROGUE WARFARE 3 DEATH OF A NATION",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-14T13:49:01.877Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 556,
        "fields": {
            "title": "Radioactive",
            "year": "2019",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-28T01:31:02.094Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 557,
        "fields": {
            "title": "Red Riding Hood",
            "year": "2011",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-05T13:11:22.851Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 558,
        "fields": {
            "title": "Revenge Ride",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-28T13:05:15.663Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 559,
        "fields": {
            "title": "Rogue Warfare 3 Death of a Nation",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-14T13:48:39.779Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 560,
        "fields": {
            "title": "Room in ในห้องรักโรมรำลึก",
            "year": "2010",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-15T14:28:25.312Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 562,
        "fields": {
            "title": "Sentinelle",
            "year": "2021",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-14T15:04:07.219Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 563,
        "fields": {
            "title": "Sinister Stalker",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-30T15:45:39.647Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 564,
        "fields": {
            "title": "Skater Girl",
            "year": "2021",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-30T13:27:09.754Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 565,
        "fields": {
            "title": "Special Actors ใจเกินร้อย",
            "year": "2019",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-18T02:29:15.568Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 566,
        "fields": {
            "title": "Spiderhead",
            "year": "2022",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-02T14:11:01.547Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 567,
        "fields": {
            "title": "Stronger",
            "year": "2017",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-03T13:33:08.563Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 568,
        "fields": {
            "title": "Sully",
            "year": "2016",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-11T14:35:53.111Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 569,
        "fields": {
            "title": "T2 Trainspotting",
            "year": "2017",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-03-28T15:46:32.745Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 570,
        "fields": {
            "title": "THE SALTON SEA",
            "year": "2002",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-03-24T14:56:57.351Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 571,
        "fields": {
            "title": "TINKER TAILOR SOLDIER SPY",
            "year": "2011",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-31T07:48:58.987Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 573,
        "fields": {
            "title": "Target Number One",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-25T14:22:44.364Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 574,
        "fields": {
            "title": "Tesla เทสลา คนล่าอนาคต",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-30T23:12:10.559Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 576,
        "fields": {
            "title": "The Captive Nanny",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-03T08:07:52.464Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 578,
        "fields": {
            "title": "The Craft Legacy",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-16T12:27:09.284Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 579,
        "fields": {
            "title": "The Disappearance of Alice Creed",
            "year": "2009",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-20T09:07:45.273Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 580,
        "fields": {
            "title": "The Exorcist(1)",
            "year": "1973",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-13T14:00:56.028Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 581,
        "fields": {
            "title": "The Exorcist(2) The Heretic",
            "year": "1977",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-13T14:01:05.128Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 582,
        "fields": {
            "title": "The Exorcist(3)",
            "year": "1990",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-13T14:01:10.918Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 583,
        "fields": {
            "title": "The Exorcist(4) The Beginning",
            "year": "2004",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-13T14:01:19.089Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 584,
        "fields": {
            "title": "The Exorcist(5) Dominion Prequel to the Exocist",
            "year": "2005",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-13T14:01:24.588Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 585,
        "fields": {
            "title": "The Ides Of March",
            "year": "2011",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-20T09:07:15.753Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 587,
        "fields": {
            "title": "The Mystic Nine Qing Shan Hai Tang",
            "year": "2022",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-06T13:00:31.908Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 588,
        "fields": {
            "title": "The Postcard Killings",
            "year": "2020",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-07T15:43:47.965Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 590,
        "fields": {
            "title": "The Secret",
            "year": "2016",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-11T04:22:58.656Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 591,
        "fields": {
            "title": "The Sentinel",
            "year": "2006",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-20T12:54:40.390Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 592,
        "fields": {
            "title": "The Way Back",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-08T15:44:09.244Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 593,
        "fields": {
            "title": "The Black Phone",
            "year": "2022",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-10T13:44:25.635Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 594,
        "fields": {
            "title": "The Broken Hearts Gallery",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-11T14:35:40.949Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 595,
        "fields": {
            "title": "The Father",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-03-19T05:27:21.546Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 596,
        "fields": {
            "title": "The First Myth Clash of Gods",
            "year": "2021",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-26T13:13:51.306Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 597,
        "fields": {
            "title": "The Gray Man",
            "year": "2022",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-11T02:21:16.348Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 598,
        "fields": {
            "title": "The Green Knight",
            "year": "2021",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-11T04:14:21.369Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 599,
        "fields": {
            "title": "The Half of It",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-18T15:08:17.186Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 600,
        "fields": {
            "title": "The Hitmans Wifes Bodyguard",
            "year": "2021",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-11T08:26:24.862Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 601,
        "fields": {
            "title": "The House",
            "year": "2017",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-05T09:51:14.235Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 602,
        "fields": {
            "title": "The Larva Island Movie",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-08T14:48:45.051Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 603,
        "fields": {
            "title": "The Last Vermeer",
            "year": "2019",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-03T06:48:06.453Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 604,
        "fields": {
            "title": "The Librarian Quest For The Spear",
            "year": "2004",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-08T15:00:30.924Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 605,
        "fields": {
            "title": "The Librarian Return To King Solomons Mines",
            "year": "2006",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-08T15:00:51.261Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 606,
        "fields": {
            "title": "The Little Things",
            "year": "2021",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-29T14:54:30.913Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 609,
        "fields": {
            "title": "The Santa Clause 3 The Escape Clause",
            "year": "2006",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-18T09:33:01.461Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 610,
        "fields": {
            "title": "The Secret Garden",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-26T15:28:44.965Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 611,
        "fields": {
            "title": "The Thomas Crown Affair",
            "year": "1999",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-07T12:16:31.715Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 612,
        "fields": {
            "title": "Thunder Force",
            "year": "2021",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-15T13:27:31.224Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 613,
        "fields": {
            "title": "Till Death",
            "year": "2021",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-11T15:43:48.673Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 614,
        "fields": {
            "title": "Tom Clancy's Without Remorse",
            "year": "2021",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-10T06:31:22.603Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 615,
        "fields": {
            "title": "Toys of Terror",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-14T13:44:37.631Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 616,
        "fields": {
            "title": "Tragic Jungle",
            "year": "2021",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-10T02:51:03.022Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 617,
        "fields": {
            "title": "Training Day",
            "year": "2001",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-15T13:48:49.236Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 618,
        "fields": {
            "title": "Two Weeks Notice",
            "year": "2002",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-07T15:40:44.867Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 619,
        "fields": {
            "title": "Unhinged",
            "year": "2020",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-12T13:37:01.593Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 620,
        "fields": {
            "title": "V I P",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-20T09:06:01.404Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 622,
        "fields": {
            "title": "Wrath of Man",
            "year": "2021",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-13T14:18:44.630Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 623,
        "fields": {
            "title": "You're Next",
            "year": "2011",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-30T11:38:07.403Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 625,
        "fields": {
            "title": "mortal kombat legends scorpions revenge",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-19T13:36:00.468Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 626,
        "fields": {
            "title": "บักแตงโม",
            "year": "2022",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-11T09:04:03.907Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 627,
        "fields": {
            "title": "รักข้ามคาน",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-11T15:58:53.872Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 628,
        "fields": {
            "title": "ฮักมะย๋อมมะแย๋ม",
            "year": "2019",
            "status": "r",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-11T09:03:18.977Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 629,
        "fields": {
            "title": "เร็วโหด เหมือนโกรธเธอ",
            "year": "2022",
            "status": "w",
            "createdDate": "2022-08-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-11T15:59:50.226Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 631,
        "fields": {
            "title": "Begin Again",
            "year": "2013",
            "status": "r",
            "createdDate": "2022-08-11",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-03-31T14:08:30.741Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 632,
        "fields": {
            "title": "Carter",
            "year": "2022",
            "status": "w",
            "createdDate": "2022-08-11",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-04-20T15:47:34.953Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 634,
        "fields": {
            "title": "Father Stu",
            "year": "2022",
            "status": "r",
            "createdDate": "2022-08-11",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-04-27T15:49:21.262Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 635,
        "fields": {
            "title": "My True Friends The Beginning (16 ห้าว 19 เดือด)",
            "year": "2022",
            "status": "r",
            "createdDate": "2022-08-11",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-15T13:58:10.410Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 636,
        "fields": {
            "title": "Pee Nak 3",
            "year": "2022",
            "status": "r",
            "createdDate": "2022-08-11",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-12T15:42:18.601Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 638,
        "fields": {
            "title": "Imperium",
            "year": "2016",
            "status": "r",
            "createdDate": "2022-08-24",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-03-14T13:49:45.967Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 639,
        "fields": {
            "title": "Panama",
            "year": "2022",
            "status": "r",
            "createdDate": "2022-08-24",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-26T12:17:23.276Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 641,
        "fields": {
            "title": "Queenpins",
            "year": "2021",
            "status": "w",
            "createdDate": "2022-08-24",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-26T13:44:44.546Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 642,
        "fields": {
            "title": "The missing",
            "year": "2003",
            "status": "r",
            "createdDate": "2022-08-24",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-12T14:00:04.884Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 643,
        "fields": {
            "title": "SLR กล้อง ติด ตาย",
            "year": "2022",
            "status": "w",
            "createdDate": "2022-08-24",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-04-05T15:28:06.423Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 644,
        "fields": {
            "title": "The Long Walk",
            "year": "2019",
            "status": "r",
            "createdDate": "2022-08-24",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-09T14:11:48.433Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 645,
        "fields": {
            "title": "Pickled Love Potion ฮักล้นไห หัวใจนายเกิบคีบ",
            "year": "2022",
            "status": "r",
            "createdDate": "2022-08-24",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-12T13:44:28.213Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 646,
        "fields": {
            "title": "Look both ways",
            "year": "2022",
            "status": "r",
            "createdDate": "2022-08-24",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-14T14:22:07.193Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 647,
        "fields": {
            "title": "Royalteen",
            "year": "2022",
            "status": "r",
            "createdDate": "2022-08-24",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-29T13:29:18.620Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 648,
        "fields": {
            "title": "Last Looks คดีป่วนพลิกฮอลลีวู้ด",
            "year": "2021",
            "status": "w",
            "createdDate": "2022-09-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-03T13:52:25.397Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 649,
        "fields": {
            "title": "kidnap",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-09-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-03-14T14:55:06.150Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 650,
        "fields": {
            "title": "Me Time",
            "year": "2022",
            "status": "w",
            "createdDate": "2022-09-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-07T13:38:24.687Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 652,
        "fields": {
            "title": "Top Gun Maverick",
            "year": "2022",
            "status": "w",
            "createdDate": "2022-09-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-13T12:28:26.174Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 653,
        "fields": {
            "title": "Watch Out, We're Mad คู่บ้า อย่าให้เดือด",
            "year": "2022",
            "status": "r",
            "createdDate": "2022-09-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-14T14:34:24.847Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 654,
        "fields": {
            "title": "Scary Movie 1",
            "year": "2000",
            "status": "r",
            "createdDate": "2022-09-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-25T12:51:46.872Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 655,
        "fields": {
            "title": "Scary Movie 2",
            "year": "2001",
            "status": "r",
            "createdDate": "2022-09-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-25T12:52:01.293Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 656,
        "fields": {
            "title": "Scary Movie 3",
            "year": "2003",
            "status": "r",
            "createdDate": "2022-09-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-25T12:52:08.973Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 657,
        "fields": {
            "title": "Scary Movie 4",
            "year": "2006",
            "status": "r",
            "createdDate": "2022-09-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-25T12:52:14.217Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 658,
        "fields": {
            "title": "Scary Movie 5",
            "year": "2013",
            "status": "r",
            "createdDate": "2022-09-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-25T12:52:19.633Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 659,
        "fields": {
            "title": "The Shack",
            "year": "2017",
            "status": "r",
            "createdDate": "2022-09-05",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-21T15:14:50.733Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 660,
        "fields": {
            "title": "War Pigs",
            "year": "2015",
            "status": "r",
            "createdDate": "2022-09-05",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-21T13:42:48.368Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 661,
        "fields": {
            "title": "Painted Skin ตำนานรักปีศาจสาว",
            "year": "2022",
            "status": "r",
            "createdDate": "2022-09-05",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-22T13:22:41.628Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 662,
        "fields": {
            "title": "oxygen ออกซิเจน",
            "year": "2021",
            "status": "r",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-07T13:49:56.304Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 663,
        "fields": {
            "title": "State of Play",
            "year": "2009",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-03T09:57:32.984Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 664,
        "fields": {
            "title": "Burn After Reading",
            "year": "2008",
            "status": "r",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-03-27T13:16:30.963Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 665,
        "fields": {
            "title": "Everything Everywhere All At Once",
            "year": "2022",
            "status": "r",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-21T16:02:39.029Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 666,
        "fields": {
            "title": "Hereafter",
            "year": "2010",
            "status": "r",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-06T06:27:09.003Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 667,
        "fields": {
            "title": "Luckiest Girl Alive",
            "year": "2022",
            "status": "r",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-14T07:51:40.431Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 668,
        "fields": {
            "title": "Paranormal Activity Next of Kin",
            "year": "2021",
            "status": "r",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-23T13:29:45.551Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 669,
        "fields": {
            "title": "Predestination",
            "year": "2014",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-20T09:01:56.542Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 670,
        "fields": {
            "title": "Anatomy of Time",
            "year": "2021",
            "status": "r",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-04-07T14:08:17.675Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 671,
        "fields": {
            "title": "AGEFIGHTER WORLDS COLLIDE",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-23T12:41:55.300Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 672,
        "fields": {
            "title": "Baggio - The Divine Ponytail",
            "year": "2021",
            "status": "r",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-04-15T13:11:23.850Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 673,
        "fields": {
            "title": "Cook Up a Storm",
            "year": "2017",
            "status": "r",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-04-20T15:47:48.328Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 674,
        "fields": {
            "title": "EASTERN PROMISES บันทึกบาปสัญญาเลือด",
            "year": "2017",
            "status": "r",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-03-20T13:55:53.063Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 675,
        "fields": {
            "title": "Ferry",
            "year": "2021",
            "status": "r",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-25T10:45:22.263Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 676,
        "fields": {
            "title": "Free State of Jones",
            "year": "2016",
            "status": "r",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-04-29T03:20:10.983Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 677,
        "fields": {
            "title": "Infinite",
            "year": "2021",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-13T06:50:50.302Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 678,
        "fields": {
            "title": "OUT FOR JUSTICE ทวงหนี้แบบยมบาล",
            "year": "1991",
            "status": "r",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-04-12T15:17:49.260Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 680,
        "fields": {
            "title": "Red Cliff",
            "year": "2008",
            "status": "r",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-07T13:49:17.692Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 681,
        "fields": {
            "title": "Red Cliff II",
            "year": "2009",
            "status": "r",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-07T13:49:24.590Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 682,
        "fields": {
            "title": "State of Play ซ่อนปมฆ่า ล่าซ้อนแผน",
            "year": "2009",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-03T09:57:18.237Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 683,
        "fields": {
            "title": "The Autopsy of Jane Doe สืบศพหลอน ซ่อนระทึก",
            "year": "2016",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-08T08:41:16.501Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 684,
        "fields": {
            "title": "The Four",
            "year": "2012",
            "status": "r",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-26T15:05:26.402Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 685,
        "fields": {
            "title": "The Four 2",
            "year": "2013",
            "status": "r",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-26T15:05:34.410Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 686,
        "fields": {
            "title": "The Four 3 Final Battle",
            "year": "2014",
            "status": "r",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-26T15:05:42.501Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 688,
        "fields": {
            "title": "รักหวานอมเปรี้ยว Sweet & Sour",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-09T16:02:28.912Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 689,
        "fields": {
            "title": "The Woman in the Window ส่องปมมรณะ",
            "year": "2021",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-18T01:16:27.896Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 690,
        "fields": {
            "title": "12 Strong",
            "year": "2016",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-13T14:50:24.812Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 691,
        "fields": {
            "title": "Amusement",
            "year": "2008",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-13T14:50:36.780Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 692,
        "fields": {
            "title": "Countdown เคาท์ดาวน์ตาย",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-13T14:50:53.348Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 693,
        "fields": {
            "title": "Red Eye",
            "year": "2005",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-20T09:02:19.096Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 694,
        "fields": {
            "title": "Sabaidee Luang Prabang",
            "year": "2008",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-13T14:52:19.919Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 695,
        "fields": {
            "title": "From Pakse With Love",
            "year": "2010",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-13T14:51:11.255Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 696,
        "fields": {
            "title": "[Hannibal 1] The Silence of the Lambs",
            "year": "1991",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-20T09:03:08.974Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 697,
        "fields": {
            "title": "[Hannibal 2]",
            "year": "2001",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-20T09:03:10.278Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 698,
        "fields": {
            "title": "[Hannibal 3] Red Dragon",
            "year": "2022",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-20T09:03:11.239Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 699,
        "fields": {
            "title": "[Hannibal 4] Hannibal Rising",
            "year": "2007",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-20T09:03:12.111Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 700,
        "fields": {
            "title": "[The Da Vinci Code] The Da Vinci Code",
            "year": "2006",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-13T14:52:52.154Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 701,
        "fields": {
            "title": "[The Da Vinci Code] Angels & Demons",
            "year": "2009",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-13T14:53:10.755Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 702,
        "fields": {
            "title": "[The Da Vinci Code] Inferno",
            "year": "2015",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-13T14:53:25.202Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 703,
        "fields": {
            "title": "[Minions] Despicable Me",
            "year": "2010",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-13T14:25:08.883Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 704,
        "fields": {
            "title": "[Minions] Despicable Me 2",
            "year": "2013",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-13T14:25:19.568Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 705,
        "fields": {
            "title": "[Minions] Minions",
            "year": "2016",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-13T14:24:34.213Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 706,
        "fields": {
            "title": "[Minions] Despicable Me 3",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-13T14:24:57.993Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 707,
        "fields": {
            "title": "เดี่ยว 1",
            "year": "1995",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-13T14:54:17.855Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 708,
        "fields": {
            "title": "เดี่ยว 2",
            "year": "1996",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-13T14:55:04.833Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 709,
        "fields": {
            "title": "เดี่ยว 3",
            "year": "1997",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-13T14:55:09.853Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 710,
        "fields": {
            "title": "เดี่ยว 4",
            "year": "1999",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-13T14:55:15.041Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 711,
        "fields": {
            "title": "เดี่ยว 5",
            "year": "2002",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-13T14:55:19.633Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 712,
        "fields": {
            "title": "เดี่ยว 6",
            "year": "2003",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-13T14:55:25.343Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 713,
        "fields": {
            "title": "เดี่ยว 7",
            "year": "2008",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-13T14:55:30.925Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 714,
        "fields": {
            "title": "เดี่ยว 7.5",
            "year": "2008",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-13T14:55:36.874Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 715,
        "fields": {
            "title": "เดี่ยว 8",
            "year": "2010",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-13T14:55:43.259Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 716,
        "fields": {
            "title": "เดี่ยว 9",
            "year": "2011",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-13T14:55:49.184Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 717,
        "fields": {
            "title": "เดี่ยว 9.5",
            "year": "2011",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-13T14:55:53.542Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 718,
        "fields": {
            "title": "เดี่ยว 10",
            "year": "2013",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-13T14:54:42.134Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 719,
        "fields": {
            "title": "เดี่ยว 11",
            "year": "2015",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-13T14:54:55.068Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 720,
        "fields": {
            "title": "หมู่ วาไรตี้โชว์ อุดมและผองเพื่อน",
            "year": "2016",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-13T14:53:48.464Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 721,
        "fields": {
            "title": "เดี่ยว 12",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-10-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-13T14:54:59.862Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 722,
        "fields": {
            "title": "Ant Man",
            "year": "2015",
            "status": "w",
            "createdDate": "2022-10-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-17T07:24:23.605Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 723,
        "fields": {
            "title": "Avengers Age of Ultron อเวนเจอร์ส  มหาศึกอัลตรอนถล่มโลก",
            "year": "2015",
            "status": "w",
            "createdDate": "2022-10-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-17T07:24:44.110Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 724,
        "fields": {
            "title": "Avengers Endgame",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-10-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-17T07:24:56.143Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 725,
        "fields": {
            "title": "Avengers Infinity War ",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-10-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-17T07:25:06.748Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 726,
        "fields": {
            "title": "Black Panther",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-10-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-17T07:25:19.671Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 727,
        "fields": {
            "title": "Captain America Civil War",
            "year": "2016",
            "status": "w",
            "createdDate": "2022-10-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-17T07:25:48.074Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 728,
        "fields": {
            "title": "Captain America The First Avenger Avenger",
            "year": "2011",
            "status": "w",
            "createdDate": "2022-10-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-17T07:26:00.149Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 729,
        "fields": {
            "title": "Captain America The Winter Soldier Soldier กัปคันอเมริกา มัชจุราชอพังกา 2",
            "year": "2014",
            "status": "w",
            "createdDate": "2022-10-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-17T07:26:10.716Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 730,
        "fields": {
            "title": "Deadpool",
            "year": "2016",
            "status": "w",
            "createdDate": "2022-10-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-17T07:26:22.387Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 731,
        "fields": {
            "title": "Deadpool 2",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-10-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-17T07:26:28.695Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 732,
        "fields": {
            "title": "Guardians of the Galaxy รวมพันธุ์นักสู้พิทักษ์จักรวาล",
            "year": "2014",
            "status": "w",
            "createdDate": "2022-10-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-17T07:26:43.760Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 733,
        "fields": {
            "title": "Iron Man 1 มหาประลัย คนเกราะเหล็ก 1",
            "year": "2008",
            "status": "w",
            "createdDate": "2022-10-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-17T07:26:52.293Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 734,
        "fields": {
            "title": "Iron Man 2 มหาประลัย คนเกราะเหล็ก 2",
            "year": "2010",
            "status": "w",
            "createdDate": "2022-10-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-17T07:27:01.013Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 735,
        "fields": {
            "title": "Iron Man 3 มหาประลัย คนเกราะเหล็ก 3",
            "year": "2013",
            "status": "w",
            "createdDate": "2022-10-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-17T07:27:08.619Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 736,
        "fields": {
            "title": "Justice League",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-10-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-17T07:27:22.132Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 737,
        "fields": {
            "title": "Spider-Man Far From Home",
            "year": "2019",
            "status": "w",
            "createdDate": "2022-10-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-17T07:27:30.584Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 738,
        "fields": {
            "title": "Spider-Man Homecoming",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-10-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-17T07:27:38.858Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 739,
        "fields": {
            "title": "Star Trek สตาร์เทค",
            "year": "2009",
            "status": "w",
            "createdDate": "2022-10-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-17T07:27:47.696Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 740,
        "fields": {
            "title": "Star Trek Into Darkness สตาร์ เทรค ทะยานสู่ห้วงมืด",
            "year": "2013",
            "status": "w",
            "createdDate": "2022-10-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-17T07:27:57.290Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 741,
        "fields": {
            "title": "The Avengers ศึกอีโร่รวมการเฉพาะกิจ",
            "year": "2012",
            "status": "w",
            "createdDate": "2022-10-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-17T07:28:08.100Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 742,
        "fields": {
            "title": "The Hulk ฮัค",
            "year": "2003",
            "status": "w",
            "createdDate": "2022-10-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-17T07:28:16.496Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 743,
        "fields": {
            "title": "The Incredible Hulk  มนุษย์ตัวเขียวจอมพลัง 2",
            "year": "2008",
            "status": "w",
            "createdDate": "2022-10-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-17T07:28:25.132Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 744,
        "fields": {
            "title": "Thor",
            "year": "2016",
            "status": "w",
            "createdDate": "2022-10-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-17T07:28:33.523Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 745,
        "fields": {
            "title": "Thor The Dark  World เทพเจ้าสายฟ้าโลกาทมิฬ",
            "year": "2013",
            "status": "w",
            "createdDate": "2022-10-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-17T07:28:43.548Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 746,
        "fields": {
            "title": "Wonder Woman",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-10-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-17T07:28:52.467Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 747,
        "fields": {
            "title": "The BFG",
            "year": "2016",
            "status": "r",
            "createdDate": "2022-10-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-19T12:52:14.475Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 748,
        "fields": {
            "title": "Eye for an Eye ยอดกระบี่ไร้เทียมทาน",
            "year": "2022",
            "status": "w",
            "createdDate": "2022-10-21",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-21T13:48:15.008Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 749,
        "fields": {
            "title": "Forbidden Legend of Sex and Chopsticks",
            "year": "2008",
            "status": "r",
            "createdDate": "2022-10-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-25T16:05:42.282Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 750,
        "fields": {
            "title": "Forbidden Legend of Sex and Chopsticks II",
            "year": "2009",
            "status": "r",
            "createdDate": "2022-10-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-25T16:05:59.041Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 751,
        "fields": {
            "title": "The Killing of a Sacred Deer",
            "year": "2017",
            "status": "r",
            "createdDate": "2022-10-26",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-26T15:32:23.739Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 752,
        "fields": {
            "title": "The Age of Shadow",
            "year": "2016",
            "status": "w",
            "createdDate": "2022-10-28",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-27T21:47:30.548Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 753,
        "fields": {
            "title": "Heist ด่วนอันตราย 657",
            "year": "2015",
            "status": "w",
            "createdDate": "2022-10-31",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-31T14:27:53.182Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 754,
        "fields": {
            "title": "The School for Good and Evil ",
            "year": "2022",
            "status": "r",
            "createdDate": "2022-10-31",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-10-31T14:48:02.614Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 755,
        "fields": {
            "title": "Passengers ",
            "year": "2016",
            "status": "r",
            "createdDate": "2022-11-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-01T14:19:52.106Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 756,
        "fields": {
            "title": "The Curse of Bridge Hollow",
            "year": "2022",
            "status": "r",
            "createdDate": "2022-11-03",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-03T14:19:33.731Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 757,
        "fields": {
            "title": "Barbarian ",
            "year": "2022",
            "status": "w",
            "createdDate": "2022-11-05",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-05T03:13:00.630Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 758,
        "fields": {
            "title": "Fortress: Sniper's Eye",
            "year": "2022",
            "status": "r",
            "createdDate": "2022-11-05",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-05T03:14:08.267Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 759,
        "fields": {
            "title": "Fortress ",
            "year": "2021",
            "status": "r",
            "createdDate": "2022-11-05",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-05T03:15:44.425Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 760,
        "fields": {
            "title": "20th Century Girl",
            "year": "2022",
            "status": "w",
            "createdDate": "2022-11-05",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-05T12:11:07.359Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 761,
        "fields": {
            "title": "Red cliff ",
            "year": "2008",
            "status": "r",
            "createdDate": "2022-11-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-06T12:45:06.507Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 762,
        "fields": {
            "title": "Red cliff II",
            "year": "2009",
            "status": "r",
            "createdDate": "2022-11-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-06T12:45:21.049Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 763,
        "fields": {
            "title": "Leio ไลโอโคตรแย้ยักษ์ ",
            "year": "2022",
            "status": "r",
            "createdDate": "2022-11-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-06T13:00:06.849Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 764,
        "fields": {
            "title": "Bullet Train",
            "year": "2022",
            "status": "w",
            "createdDate": "2022-11-09",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-04-18T14:39:47.427Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 765,
        "fields": {
            "title": "Emergency Declaration",
            "year": "2021",
            "status": "r",
            "createdDate": "2022-11-09",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-04-23T10:18:48.290Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 766,
        "fields": {
            "title": "Hellhole",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-11-14",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-06T06:25:59.358Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 767,
        "fields": {
            "title": "Robbing Mussolini",
            "year": "2022",
            "status": "w",
            "createdDate": "2022-11-14",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-20T09:01:43.788Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 768,
        "fields": {
            "title": "All Quiet on the Western Front",
            "year": "2022",
            "status": "r",
            "createdDate": "2022-11-14",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-03-29T22:18:31.875Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 769,
        "fields": {
            "title": "The Hidden Town",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-11-14",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-04T14:21:51.178Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 770,
        "fields": {
            "title": "Fearless Love ทวงคืน",
            "year": "2022",
            "status": "r",
            "createdDate": "2022-11-15",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-11T08:36:33.491Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 771,
        "fields": {
            "title": "Lost Bullet 2",
            "year": "2022",
            "status": "w",
            "createdDate": "2022-11-15",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-15T12:58:22.677Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 772,
        "fields": {
            "title": "Pan's Labyrinth อัศจรรย์แดนฝัน มหัศจรรย์เขาวงกต",
            "year": "2006",
            "status": "r",
            "createdDate": "2022-11-16",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-16T13:49:09.852Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 773,
        "fields": {
            "title": "Enola Holmes 2",
            "year": "2022",
            "status": "w",
            "createdDate": "2022-11-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-04-23T14:45:07.723Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 774,
        "fields": {
            "title": "Hereditary",
            "year": "2018",
            "status": "r",
            "createdDate": "2022-11-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-03-17T15:06:13.625Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 775,
        "fields": {
            "title": "The Invitation",
            "year": "2022",
            "status": "w",
            "createdDate": "2022-11-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-11T14:19:38.617Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 776,
        "fields": {
            "title": "The Up Rank อาชญาเกม",
            "year": "2022",
            "status": "r",
            "createdDate": "2022-11-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-08T13:41:59.229Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 777,
        "fields": {
            "title": "House of Flying Daggers",
            "year": "2004",
            "status": "r",
            "createdDate": "2022-11-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-17T14:09:35.657Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 778,
        "fields": {
            "title": "Let Him Go",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-11-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-03-05T03:03:54.137Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 779,
        "fields": {
            "title": "Lights Out",
            "year": "2016",
            "status": "w",
            "createdDate": "2022-11-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-02-11T14:30:47.630Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 780,
        "fields": {
            "title": "Run",
            "year": "2020",
            "status": "w",
            "createdDate": "2022-11-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-02-19T06:03:37.556Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 781,
        "fields": {
            "title": "Marley & Me จอมป่วนหน้าซื่อ",
            "year": "2008",
            "status": "w",
            "createdDate": "2022-11-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-28T03:52:41.264Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 783,
        "fields": {
            "title": "The Princess Switch เดอะ พริ้นเซส สวิตช์ สลับตัวไม่สลับหัวใจ",
            "year": "2018",
            "status": "r",
            "createdDate": "2022-11-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-02-12T03:47:21.663Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 784,
        "fields": {
            "title": "The Princess Switch 2 Switched Again เดอะ พริ้นเซส สวิตช์ สลับแล้วสลับอีก",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-11-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-02-12T03:47:39.784Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 785,
        "fields": {
            "title": "The Princess Switch 3 Romancing the Star เดอะ พริ้นเซส สวิตช์ 3 ไขว่คว้าหาดาว",
            "year": "2021",
            "status": "r",
            "createdDate": "2022-11-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-02-12T03:47:34.221Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 786,
        "fields": {
            "title": "Lost In Translation",
            "year": "2003",
            "status": "r",
            "createdDate": "2022-11-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-19T08:18:07.954Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 787,
        "fields": {
            "title": "Mr. Brooks",
            "year": "2007",
            "status": "w",
            "createdDate": "2022-11-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-19T15:32:22.977Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 788,
        "fields": {
            "title": "Zhong Kui Exorcism จงขุย ตำนานเทพอสูร",
            "year": "2022",
            "status": "r",
            "createdDate": "2022-11-22",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-22T14:14:59.771Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 789,
        "fields": {
            "title": "Stray (Tvar)",
            "year": "2019",
            "status": "r",
            "createdDate": "2022-11-23",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-23T13:20:16.124Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 790,
        "fields": {
            "title": "The Protégé",
            "year": "2021",
            "status": "w",
            "createdDate": "2022-11-23",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-23T13:28:36.434Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 791,
        "fields": {
            "title": "Black Panther Wakanda Forever",
            "year": "2022",
            "status": "w",
            "createdDate": "2022-11-26",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-04-17T12:32:30.820Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 792,
        "fields": {
            "title": "The Guardians of The Galaxy Holiday",
            "year": "2022",
            "status": "w",
            "createdDate": "2022-11-26",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-20T09:03:24.435Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 793,
        "fields": {
            "title": "Happy Ending ใจฟู สตอรี่",
            "year": "2022",
            "status": "w",
            "createdDate": "2022-11-26",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-06T08:09:51.477Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 794,
        "fields": {
            "title": "THE VANISHED MURDERER แหกนรกดับแค้น",
            "year": "2015",
            "status": "w",
            "createdDate": "2022-11-26",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-10T14:11:45.393Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 795,
        "fields": {
            "title": "Serenity",
            "year": "2019",
            "status": "r",
            "createdDate": "2022-11-26",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-30T09:49:22.830Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 796,
        "fields": {
            "title": "Escape Room Tournament of Champions",
            "year": "2021",
            "status": "w",
            "createdDate": "2022-11-26",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-20T09:01:10.299Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 797,
        "fields": {
            "title": "The Matrix",
            "year": "1990",
            "status": "w",
            "createdDate": "2022-11-26",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-29T10:50:47.739Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 798,
        "fields": {
            "title": "The Matrix Reloaded",
            "year": "2003",
            "status": "w",
            "createdDate": "2022-11-26",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-29T10:50:57.610Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 799,
        "fields": {
            "title": "The Matrix Revolutions",
            "year": "2003",
            "status": "w",
            "createdDate": "2022-11-26",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-30T23:34:32.511Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 800,
        "fields": {
            "title": "The Matrix Resurrections",
            "year": "2021",
            "status": "w",
            "createdDate": "2022-11-26",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-29T10:51:00.118Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 801,
        "fields": {
            "title": "Escape from Alcatraz",
            "year": "1979",
            "status": "r",
            "createdDate": "2022-11-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-28T23:04:57.289Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 802,
        "fields": {
            "title": "The Swimmers",
            "year": "2022",
            "status": "r",
            "createdDate": "2022-11-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-29T14:09:07.583Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 803,
        "fields": {
            "title": "Enchanted",
            "year": "2007",
            "status": "r",
            "createdDate": "2022-11-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-11-29T15:12:21.089Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 804,
        "fields": {
            "title": "Call Me Daddy รักหนูมั้ย",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-12-05",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-05T10:03:03.353Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 806,
        "fields": {
            "title": "Drive",
            "year": "2021",
            "status": "w",
            "createdDate": "2022-12-09",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-04-07T14:36:31.871Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 807,
        "fields": {
            "title": "The Lake",
            "year": "2022",
            "status": "r",
            "createdDate": "2022-12-09",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-03T13:21:29.112Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 809,
        "fields": {
            "title": "The Father",
            "year": "2020",
            "status": "r",
            "createdDate": "2022-12-09",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-03-19T05:26:59.328Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 810,
        "fields": {
            "title": "Warriors of Future",
            "year": "2022",
            "status": "r",
            "createdDate": "2022-12-09",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-13T14:43:24.510Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 811,
        "fields": {
            "title": "The Girl with the Dragon Tattoo",
            "year": "2011",
            "status": "w",
            "createdDate": "2022-12-09",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-16T15:28:30.711Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 812,
        "fields": {
            "title": "The Girl Who Kicked The Hornest Nest",
            "year": "2009",
            "status": "w",
            "createdDate": "2022-12-09",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-16T15:28:37.638Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 813,
        "fields": {
            "title": "The Girl Who Played With Fire",
            "year": "209",
            "status": "w",
            "createdDate": "2022-12-09",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-16T15:28:41.529Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 814,
        "fields": {
            "title": "The Girl With The Dragon Tattoo",
            "year": "2009",
            "status": "w",
            "createdDate": "2022-12-09",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-16T15:28:48.140Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 815,
        "fields": {
            "title": "Little Forkers",
            "year": "2010",
            "status": "w",
            "createdDate": "2022-12-10",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-10T00:36:56.235Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 816,
        "fields": {
            "title": "V.I.P",
            "year": "2017",
            "status": "w",
            "createdDate": "2022-12-10",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-10T04:21:58.603Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 817,
        "fields": {
            "title": "The 100 ๑oo ขา",
            "year": "2022",
            "status": "r",
            "createdDate": "2022-12-11",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-06T11:21:24.912Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 818,
        "fields": {
            "title": "Desire",
            "year": "2011",
            "status": "r",
            "createdDate": "2022-12-11",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-03-19T05:28:27.497Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 819,
        "fields": {
            "title": "The Contractor",
            "year": "2022",
            "status": "w",
            "createdDate": "2022-12-11",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-11T00:08:28.811Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 820,
        "fields": {
            "title": "Pixels",
            "year": "2015",
            "status": "w",
            "createdDate": "2022-12-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-03-22T13:05:50.393Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 821,
        "fields": {
            "title": "Black Book",
            "year": "2006",
            "status": "r",
            "createdDate": "2022-12-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-09T14:44:42.412Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 822,
        "fields": {
            "title": "First man",
            "year": "2018",
            "status": "w",
            "createdDate": "2022-12-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-03-16T14:24:52.571Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 823,
        "fields": {
            "title": "Road to Perdition",
            "year": "2002",
            "status": "w",
            "createdDate": "2022-12-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-03-26T01:35:21.731Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 824,
        "fields": {
            "title": "The Electrical Life of Louis Wain",
            "year": "2021",
            "status": "r",
            "createdDate": "2022-12-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-03T06:41:05.452Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 825,
        "fields": {
            "title": "The Pursuit of Happyness",
            "year": "2006",
            "status": "w",
            "createdDate": "2022-12-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-19T13:32:44.809Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 826,
        "fields": {
            "title": "The Roundup",
            "year": "2022",
            "status": "w",
            "createdDate": "2022-12-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-07T13:32:53.193Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 827,
        "fields": {
            "title": "I Believe in Santa ซานต้ามีจริงนะ",
            "year": "2022",
            "status": "r",
            "createdDate": "2022-12-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-03T15:27:53.612Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 828,
        "fields": {
            "title": "Bad Trip",
            "year": "2021",
            "status": "r",
            "createdDate": "2022-12-27",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2022-12-27T13:06:46.007Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 829,
        "fields": {
            "title": "Amsterdam",
            "year": "2022",
            "status": "w",
            "createdDate": "2022-12-31",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-04-07T14:07:54.649Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 830,
        "fields": {
            "title": "Asfall",
            "year": "2019",
            "status": "r",
            "createdDate": "2022-12-31",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-03-19T14:00:43.394Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 831,
        "fields": {
            "title": "Lou",
            "year": "2022",
            "status": "w",
            "createdDate": "2022-12-31",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-12T08:42:39.673Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 832,
        "fields": {
            "title": "Public Enemies",
            "year": "2009",
            "status": "w",
            "createdDate": "2022-12-31",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-03-24T13:21:34.494Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 833,
        "fields": {
            "title": "Showtime โชว์ไทม์ ตำรวจจอทีวี",
            "year": "2002",
            "status": "w",
            "createdDate": "2022-12-31",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-30T09:51:29.416Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 834,
        "fields": {
            "title": "Spy Game",
            "year": "2001",
            "status": "w",
            "createdDate": "2022-12-31",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-03-12T04:45:04.701Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 835,
        "fields": {
            "title": "The Hateful Eight 8 พิโรธ โกรธแล้วฆ่า",
            "year": "2015",
            "status": "r",
            "createdDate": "2022-12-31",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-08T08:22:42.622Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 836,
        "fields": {
            "title": "The Lost Hero Of Ayodhya ขุนแหย",
            "year": "2022",
            "status": "r",
            "createdDate": "2022-12-31",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-03T04:25:23.544Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 837,
        "fields": {
            "title": "The Flue",
            "year": "2013",
            "status": "r",
            "createdDate": "2022-12-31",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-11T14:06:15.635Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 838,
        "fields": {
            "title": "Toxin ฝ่าวิกฤติไวรัสมฤตยู",
            "year": "2014",
            "status": "r",
            "createdDate": "2022-12-31",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-14T14:21:30.995Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 839,
        "fields": {
            "title": "Bad Guys The Movie",
            "year": "2019",
            "status": "w",
            "createdDate": "2023-01-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-03-28T14:10:51.427Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 840,
        "fields": {
            "title": "Equilibrium",
            "year": "2022",
            "status": "w",
            "createdDate": "2023-01-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-03-07T14:07:47.518Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 841,
        "fields": {
            "title": "Love Destiny The Movie",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-01-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-12T10:52:20.979Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 842,
        "fields": {
            "title": "Romeo Must Die",
            "year": "2000",
            "status": "w",
            "createdDate": "2023-01-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-03-12T04:45:30.523Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 843,
        "fields": {
            "title": "Love 101",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-01-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-06T08:26:00.087Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 844,
        "fields": {
            "title": "Six Characters",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-01-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-03T03:19:48.128Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 845,
        "fields": {
            "title": "Motherless Brooklyn",
            "year": "2019",
            "status": "r",
            "createdDate": "2023-01-07",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-19T15:52:14.319Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 846,
        "fields": {
            "title": "Voyagers",
            "year": "2021",
            "status": "r",
            "createdDate": "2023-01-07",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-10T02:50:16.946Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 847,
        "fields": {
            "title": "The Ghost Writer",
            "year": "2010",
            "status": "r",
            "createdDate": "2023-01-07",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-03T13:41:17.769Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 848,
        "fields": {
            "title": "Survivor",
            "year": "2015",
            "status": "w",
            "createdDate": "2023-01-07",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-12T15:27:40.815Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 849,
        "fields": {
            "title": "The Legend of Fong Sai Yuk",
            "year": "1992",
            "status": "r",
            "createdDate": "2023-01-07",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-08T09:56:22.293Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 850,
        "fields": {
            "title": "Moonfall",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-01-07",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-15T16:10:05.477Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 851,
        "fields": {
            "title": "7 Women and a Murder 7 สตรี 1 ฆาตกรรม",
            "year": "2022",
            "status": "w",
            "createdDate": "2023-01-07",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-14T08:58:30.258Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 852,
        "fields": {
            "title": "Bad Teacher",
            "year": "2011",
            "status": "r",
            "createdDate": "2023-01-07",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-03-19T03:21:17.945Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 853,
        "fields": {
            "title": "Closer",
            "year": "2004",
            "status": "r",
            "createdDate": "2023-01-07",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-12T14:06:32.038Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 854,
        "fields": {
            "title": "Cold Mountain",
            "year": "2003",
            "status": "r",
            "createdDate": "2023-01-07",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-03-06T13:36:03.393Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 855,
        "fields": {
            "title": "Collateral",
            "year": "2004",
            "status": "w",
            "createdDate": "2023-01-07",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-03-07T14:19:51.971Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 857,
        "fields": {
            "title": "Thirteen Days",
            "year": "2000",
            "status": "w",
            "createdDate": "2023-01-07",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-20T09:00:46.850Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 858,
        "fields": {
            "title": "Along with the Gods 1",
            "year": "2017",
            "status": "r",
            "createdDate": "2023-01-09",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-10T16:48:21.728Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 859,
        "fields": {
            "title": "Along with the Gods 2",
            "year": "2018",
            "status": "r",
            "createdDate": "2023-01-09",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-10T16:48:33.521Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 860,
        "fields": {
            "title": "Inside Man",
            "year": "2006",
            "status": "w",
            "createdDate": "2023-01-09",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-03-09T13:01:29.176Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 861,
        "fields": {
            "title": "Nightmare Alley",
            "year": "2021",
            "status": "w",
            "createdDate": "2023-01-09",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-19T15:52:32.419Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 862,
        "fields": {
            "title": "Extremely Loud & Incredibly Close ปริศนารักจากพ่อ ไม่ไกลเกินใจเอื้อม",
            "year": "2011",
            "status": "r",
            "createdDate": "2023-01-10",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-04-25T14:42:55.581Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 863,
        "fields": {
            "title": "A History of Violence",
            "year": "2005",
            "status": "r",
            "createdDate": "2023-01-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-13T13:57:39.070Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 864,
        "fields": {
            "title": "The Banquet",
            "year": "2006",
            "status": "r",
            "createdDate": "2023-01-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-16T15:28:01.956Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 865,
        "fields": {
            "title": "Do Revenge",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-01-18",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-18T14:21:04.229Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 866,
        "fields": {
            "title": "Extreme Job",
            "year": "2019",
            "status": "w",
            "createdDate": "2023-01-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-19T15:58:17.835Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 867,
        "fields": {
            "title": "Last Night in Soho",
            "year": "2021",
            "status": "r",
            "createdDate": "2023-01-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-20T14:36:08.219Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 868,
        "fields": {
            "title": "Ivy + Bean",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-01-21",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-21T02:38:12.749Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 869,
        "fields": {
            "title": "Ivy + Bean and the Ghost that Had to Go",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-01-21",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-21T02:39:17.322Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 870,
        "fields": {
            "title": "Ivy + Bean: Doomed to Dance",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-01-21",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-21T02:39:57.648Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 871,
        "fields": {
            "title": "Detective Dee and the Mystery of the Phantom Flame",
            "year": "2010",
            "status": "r",
            "createdDate": "2023-01-23",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-23T13:21:17.234Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 872,
        "fields": {
            "title": "Young Detective Dee: Rise of the Sea Dragon",
            "year": "2013",
            "status": "r",
            "createdDate": "2023-01-23",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-23T13:22:15.665Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 873,
        "fields": {
            "title": "R.I.P.D.",
            "year": "2013",
            "status": "w",
            "createdDate": "2023-01-23",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-23T13:25:15.800Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 874,
        "fields": {
            "title": "Premika-Parab",
            "year": "2017",
            "status": "r",
            "createdDate": "2023-01-24",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-24T12:28:31.736Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 875,
        "fields": {
            "title": "I Came By",
            "year": "2022",
            "status": "w",
            "createdDate": "2023-01-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-25T13:59:17.376Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 876,
        "fields": {
            "title": "Journey of East",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-01-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-25T14:45:38.712Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 877,
        "fields": {
            "title": "Dog Gone หมาหลง",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-01-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-02-14T15:35:28.757Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 878,
        "fields": {
            "title": "Narvik นาร์วิค",
            "year": "2022",
            "status": "w",
            "createdDate": "2023-01-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-02-25T01:37:02.544Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 879,
        "fields": {
            "title": "Demonic",
            "year": "2015",
            "status": "w",
            "createdDate": "2023-01-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-02-07T16:30:53.718Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 880,
        "fields": {
            "title": "Faces of Anne",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-01-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-03-01T16:57:21.607Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 883,
        "fields": {
            "title": "That's Amor นี่แหละความรัก",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-01-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-02-26T09:06:57.754Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 884,
        "fields": {
            "title": "The Perfumier กลิ่นฆาตกร",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-01-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-02-19T13:53:31.664Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 885,
        "fields": {
            "title": "Suspiria กลัว",
            "year": "2018",
            "status": "r",
            "createdDate": "2023-01-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-02-13T23:29:14.985Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 886,
        "fields": {
            "title": "Nights in Rodanthe",
            "year": "2008",
            "status": "r",
            "createdDate": "2023-01-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-01-30T23:02:16.236Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 887,
        "fields": {
            "title": "Love in the Villa รักในวิลล่า",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-01-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-03-05T04:52:33.787Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 888,
        "fields": {
            "title": "The Imaginarium of Doctor Parnassus",
            "year": "2009",
            "status": "r",
            "createdDate": "2023-01-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-02-05T15:51:08.670Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 889,
        "fields": {
            "title": "Thor Love and Thunder",
            "year": "2022",
            "status": "w",
            "createdDate": "2023-01-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-03-05T07:26:38.590Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 890,
        "fields": {
            "title": "The Protege",
            "year": "2021",
            "status": "w",
            "createdDate": "2023-01-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-02-19T13:53:50.018Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 891,
        "fields": {
            "title": "The Final Blade",
            "year": "2018",
            "status": "r",
            "createdDate": "2023-01-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-02-25T03:23:39.437Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 892,
        "fields": {
            "title": "Spell",
            "year": "2020",
            "status": "r",
            "createdDate": "2023-01-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-02-19T02:45:15.260Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 893,
        "fields": {
            "title": "Reincarnation Land",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-01-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-28T04:07:15.419Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 894,
        "fields": {
            "title": "THE TOURNAMENT เลือดล้างสังเวียนนักฆ่า",
            "year": "2009",
            "status": "r",
            "createdDate": "2023-01-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-02-05T16:48:47.962Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 895,
        "fields": {
            "title": "Love You My Arrogance สปาร์คใจนายจอมหยิ่ง เดอะ มูฟวี่",
            "year": "2020",
            "status": "r",
            "createdDate": "2023-01-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-02-08T12:34:28.773Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 896,
        "fields": {
            "title": "Love You My Arrogance 2 สปาร์คใจนายจอมหยิ่ง เดอะ มูฟวี่ 2",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-01-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-02-08T12:34:42.093Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 897,
        "fields": {
            "title": "Atonement",
            "year": "2007",
            "status": "r",
            "createdDate": "2023-02-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-02-05T10:06:21.512Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 898,
        "fields": {
            "title": "Munich",
            "year": "2005",
            "status": "w",
            "createdDate": "2023-02-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-02-14T15:35:35.755Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 899,
        "fields": {
            "title": "Race to Witch Mountain",
            "year": "2009",
            "status": "w",
            "createdDate": "2023-02-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-02-12T14:02:05.662Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 900,
        "fields": {
            "title": "Bodies Bodies Bodies เพื่อนซี้ ปาร์ตี้ หนีตาย",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-02-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-02-14T13:47:32.967Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 904,
        "fields": {
            "title": "Ouija",
            "year": "2014",
            "status": "r",
            "createdDate": "2023-02-03",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-02-09T15:27:33.454Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 905,
        "fields": {
            "title": "Flight",
            "year": "2012",
            "status": "r",
            "createdDate": "2023-02-03",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-03-01T16:57:11.734Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 906,
        "fields": {
            "title": "Texas Rangers",
            "year": "2001",
            "status": "r",
            "createdDate": "2023-02-09",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-02-09T15:29:06.411Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 907,
        "fields": {
            "title": "The Little Comedian บ้านฉัน..ตลกไว้ก่อน(พ่อสอนไว้)",
            "year": "2010",
            "status": "r",
            "createdDate": "2023-02-15",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-02-15T14:15:28.021Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 908,
        "fields": {
            "title": "The Perfect Storm",
            "year": "2000",
            "status": "r",
            "createdDate": "2023-02-15",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-02-15T15:57:48.993Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 909,
        "fields": {
            "title": "Willard",
            "year": "2003",
            "status": "r",
            "createdDate": "2023-02-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-02-17T13:21:08.951Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 910,
        "fields": {
            "title": "22 Bullets",
            "year": "2010",
            "status": "w",
            "createdDate": "2023-02-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-02-17T14:58:39.334Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 911,
        "fields": {
            "title": "The Other Woman",
            "year": "2014",
            "status": "r",
            "createdDate": "2023-02-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-02-19T05:06:47.077Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 912,
        "fields": {
            "title": "Drafon Sword To Be Immortal",
            "year": "2018",
            "status": "r",
            "createdDate": "2023-02-21",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-02-21T14:20:59.687Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 913,
        "fields": {
            "title": "Dragon Sword Outlander",
            "year": "2021",
            "status": "r",
            "createdDate": "2023-02-21",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-02-21T14:21:29.856Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 914,
        "fields": {
            "title": "Drafon Sword Ancient Battlefield",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-02-21",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-02-21T14:21:53.971Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 915,
        "fields": {
            "title": "Brother",
            "year": "2009",
            "status": "r",
            "createdDate": "2023-02-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-02-25T02:29:27.242Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 916,
        "fields": {
            "title": "Shaolin vs. Evil Dead",
            "year": "2004",
            "status": "r",
            "createdDate": "2023-02-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-02-25T03:18:18.822Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 917,
        "fields": {
            "title": "Shaolin vs. Evil Dead: Ultimate Power",
            "year": "2007",
            "status": "r",
            "createdDate": "2023-02-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-02-25T03:18:50.757Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 918,
        "fields": {
            "title": "Dien Bien Phu",
            "year": "1992",
            "status": "r",
            "createdDate": "2023-03-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-03-25T02:56:14.685Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 919,
        "fields": {
            "title": "Dark Places",
            "year": "2015",
            "status": "w",
            "createdDate": "2023-04-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-04-17T11:05:08.016Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 920,
        "fields": {
            "title": "Hunt",
            "year": "2022",
            "status": "w",
            "createdDate": "2023-05-09",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-09T13:11:58.181Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 921,
        "fields": {
            "title": "Space Cowboys",
            "year": "2000",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-05-29T10:47:20.298Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 922,
        "fields": {
            "title": "21 Jump Street",
            "year": "2021",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-20T08:56:19.204Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 923,
        "fields": {
            "title": "22 Jump Street",
            "year": "2014",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-20T08:56:22.113Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 924,
        "fields": {
            "title": "65",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-16T13:35:06.959Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 925,
        "fields": {
            "title": "A Girl at My Door",
            "year": "2014",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-07T02:37:12.239Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 926,
        "fields": {
            "title": "A Tourist's Guide to Love คู่มือรักฉบับนักท่องเที่ยว",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-11T13:37:43.964Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 927,
        "fields": {
            "title": "Alpha ผจญนรกแดนทมิฬ 20,000 ปี",
            "year": "2018",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-16T03:12:47.998Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 928,
        "fields": {
            "title": "Blacklight โคตรระห่ำ ล้างบางนรก",
            "year": "2022",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-14T08:57:07.662Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 929,
        "fields": {
            "title": "Blair Witch แบลร์ วิทช์ ตำนานผีดุ",
            "year": "2016",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-11T15:44:05.012Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 930,
        "fields": {
            "title": "Breath",
            "year": "2017",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-29T14:10:17.182Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 931,
        "fields": {
            "title": "By the Time It Gets Dark ดาวคะนอง",
            "year": "2016",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-01T05:00:41.425Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 932,
        "fields": {
            "title": "Chrismas Carol",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-12T16:54:13.621Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 933,
        "fields": {
            "title": "Come Here ใจจำลอง",
            "year": "2021",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-01T03:35:59.823Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 934,
        "fields": {
            "title": "Easy A อีนี่...แร๊งงงส์",
            "year": "2010",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-28T15:31:45.458Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 935,
        "fields": {
            "title": "Evil Dead Rise",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-24T12:59:02.005Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 936,
        "fields": {
            "title": "Golden Escape แผนกล้าล่าแหกสมบัติ",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-11T13:38:42.155Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 937,
        "fields": {
            "title": "Heatwave คลื่นร้อน",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-26T12:29:18.666Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 938,
        "fields": {
            "title": "Honest Thief ทรชน ปล้นชั่ว",
            "year": "2020",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-14T14:02:54.432Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 939,
        "fields": {
            "title": "Horrible Bosses",
            "year": "2011",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-02T07:06:20.026Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 940,
        "fields": {
            "title": "Horrible Bosses 2",
            "year": "2014",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-02T07:06:36.012Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 941,
        "fields": {
            "title": "I Am Not Madame Bovary อย่าคิดหลอกเจ้",
            "year": "2016",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-25T14:20:49.292Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 942,
        "fields": {
            "title": "In His Shadow ราชาเงา",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-19T13:40:43.447Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 943,
        "fields": {
            "title": "Kill Boksoon คิลบกซุน",
            "year": "2023",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-30T14:52:39.880Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 944,
        "fields": {
            "title": "King of The New Beggars ยาจกซูกับบัญชาสวรรค์",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-21T12:26:27.758Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 946,
        "fields": {
            "title": "Murder Mystery ปริศนาฮันนีมูนอลวน",
            "year": "2019",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-28T13:38:23.996Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 947,
        "fields": {
            "title": "Murder Mystery 2 ปริศนาฮันนีมูนอลวน 2",
            "year": "2023",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-28T13:38:36.389Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 948,
        "fields": {
            "title": "Now You See Me",
            "year": "2013",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-31T12:39:56.046Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 949,
        "fields": {
            "title": "Now You See Mee 2",
            "year": "2016",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-31T12:40:09.138Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 950,
        "fields": {
            "title": "Pepermint",
            "year": "2018",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-15T12:26:02.979Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 951,
        "fields": {
            "title": "ReMember ตามล่าศพสยอง",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-11T13:18:54.377Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 952,
        "fields": {
            "title": "Secret Headquarters กองบัญชาการลับ",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-06T15:11:56.833Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 953,
        "fields": {
            "title": "Sinister เห็นแล้วต้องตาย",
            "year": "2012",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-16T03:12:29.840Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 954,
        "fields": {
            "title": "Slumdog Millionaire คำตอบสุดท้าย...อยู่ที่หัวใจ",
            "year": "2008",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-26T14:02:46.768Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 955,
        "fields": {
            "title": "The Antique Shop ร้านของเก่า",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-13T15:35:45.206Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 956,
        "fields": {
            "title": "The Enforcer",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-14T13:25:20.860Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 957,
        "fields": {
            "title": "The Hunger Games",
            "year": "2012",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-04T15:50:15.508Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 958,
        "fields": {
            "title": "The Hunger Games Catching Fire",
            "year": "2013",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-04T15:50:37.793Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 959,
        "fields": {
            "title": "The Hunger Games Mockingjay Part 1",
            "year": "2014",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-04T15:50:28.299Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 960,
        "fields": {
            "title": "The Hunger Games Mockingjay Part 2",
            "year": "2015",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-04T15:50:29.933Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 961,
        "fields": {
            "title": "The Last Kingdom Seven Kings Must Die เจ็ดกษัตริย์จักวายชนม์",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-07T13:43:29.031Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 962,
        "fields": {
            "title": "The Maze Runner",
            "year": "2014",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-17T15:11:31.833Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 963,
        "fields": {
            "title": "The Maze Runner The Scorch Trails",
            "year": "2015",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-17T15:11:45.541Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 964,
        "fields": {
            "title": "The Maze Runner The Death Cure",
            "year": "2018",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-17T15:11:59.972Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 965,
        "fields": {
            "title": "The Offering มันสิงอยู่ในร่าง",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-15T08:36:59.460Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 966,
        "fields": {
            "title": "The Third Murder กับดักฆาตกรรมครั้งที่ 3",
            "year": "2017",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-09T13:48:16.411Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 967,
        "fields": {
            "title": "The Vault หยุดโลกปล้น",
            "year": "2021",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-20T08:57:21.436Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 968,
        "fields": {
            "title": "True Spirit ทรู สปิริต",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-07T11:09:55.957Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 969,
        "fields": {
            "title": "Unlocked แค่ทำโทรศัพท์มือถือหาย ทำไมต้องกลายเป็นศพ",
            "year": "2023",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-11T15:13:41.345Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 970,
        "fields": {
            "title": "Urban Myths ผีดุสุดโซล",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-16T14:03:27.881Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 971,
        "fields": {
            "title": "V for Vengeance แผนแก้แค้น",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-23T15:41:55.013Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 972,
        "fields": {
            "title": "Warm Bodies",
            "year": "2013",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-23T13:09:40.703Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 973,
        "fields": {
            "title": "We Have a Ghost บ้านนี้มีผีป่วน",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-15T13:09:18.748Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 974,
        "fields": {
            "title": "What Happened to Monday 7 เป็น 7 ตาย",
            "year": "2017",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-18T14:29:29.761Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 975,
        "fields": {
            "title": "Willy's Wonderland หุ่นนรก VS ภารโรงคลั่ง",
            "year": "2021",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-16T05:01:33.156Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 976,
        "fields": {
            "title": "50 First Dates",
            "year": "2004",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-16T14:30:15.380Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 977,
        "fields": {
            "title": "2046",
            "year": "2004",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-19T13:50:03.183Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 978,
        "fields": {
            "title": "A Man Called Otto",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-16T15:40:22.805Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 979,
        "fields": {
            "title": "Ai Khai Dek Wat Chedi",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-29T09:10:51.616Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 980,
        "fields": {
            "title": "Alive",
            "year": "2020",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-19T14:23:48.229Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 981,
        "fields": {
            "title": "All About My Wife แผนลับ สลัดเมียเลิฟ",
            "year": "2012",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-07T14:12:54.003Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 982,
        "fields": {
            "title": "Ant-Man and the Wasp - Quantumania",
            "year": "2023",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-26T13:27:20.890Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 983,
        "fields": {
            "title": "Bad Lieutenant Port of Call New Orleans",
            "year": "2009",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-19T23:38:40.942Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 984,
        "fields": {
            "title": "Bad Times at the El Royale",
            "year": "2018",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-20T14:55:51.956Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 985,
        "fields": {
            "title": "Billionaire Boys Club",
            "year": "2018",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-20T08:57:30.529Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 986,
        "fields": {
            "title": "Black Panther - Wakanda Forever",
            "year": "2022",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-20T08:57:36.529Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 987,
        "fields": {
            "title": "Blood and Wine ขบวนคนปล้นไม่เลือก",
            "year": "1996",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-17T14:47:04.420Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 988,
        "fields": {
            "title": "Bordello of Blood คืนนรกแตก 2",
            "year": "1996",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-17T22:22:31.340Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 989,
        "fields": {
            "title": "Brokeback Mountain",
            "year": "2005",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-24T14:40:37.102Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 990,
        "fields": {
            "title": "Broken Trail สิงห์เหี้ยมเสือห้าว",
            "year": "2006",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-03T15:05:27.721Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 991,
        "fields": {
            "title": "Brothers By Blood",
            "year": "2020",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-08T14:54:18.824Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 992,
        "fields": {
            "title": "Brutal Imprisonment",
            "year": "2014",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-11T15:14:33.049Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 993,
        "fields": {
            "title": "Bua Pun Fun Yup",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-14T06:37:42.241Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 994,
        "fields": {
            "title": "Buried",
            "year": "2010",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-06T07:46:03.573Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 995,
        "fields": {
            "title": "Click",
            "year": "2006",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-29T07:46:35.788Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 996,
        "fields": {
            "title": "Come Play",
            "year": "2020",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-08T12:39:35.650Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 997,
        "fields": {
            "title": "Confessions of a Shopaholic",
            "year": "2009",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-26T15:41:58.544Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 998,
        "fields": {
            "title": "Cube",
            "year": "2021",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-25T13:45:51.062Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 999,
        "fields": {
            "title": "Dawn of the Death",
            "year": "2004",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-19T16:17:37.925Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1000,
        "fields": {
            "title": "Decision to Leave",
            "year": "2022",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-01T03:10:09.204Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1001,
        "fields": {
            "title": "Definitely Maybe",
            "year": "2008",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-28T14:56:06.895Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1002,
        "fields": {
            "title": "Don't Worry Darling",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-16T09:50:09.440Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1003,
        "fields": {
            "title": "Downton Abbey A New Era",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-03T13:44:40.751Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1004,
        "fields": {
            "title": "Dumbo",
            "year": "2019",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-02T13:29:01.236Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1005,
        "fields": {
            "title": "Dungeons & Dragons: Honour Among Thieves",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-29T08:27:46.900Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1006,
        "fields": {
            "title": "Evil Dead",
            "year": "2013",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-28T13:27:46.717Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1007,
        "fields": {
            "title": "Fidelity เลน่า มโนนัก.รักติดหล่ม",
            "year": "2019",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-19T15:04:58.919Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1008,
        "fields": {
            "title": "Firestarter",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-01T15:07:25.884Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1009,
        "fields": {
            "title": "Flatliners",
            "year": "2017",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-08T09:59:26.989Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1011,
        "fields": {
            "title": "Gone Baby Gone",
            "year": "2007",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-29T15:21:33.438Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1012,
        "fields": {
            "title": "Hell or High Water",
            "year": "2016",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-02T15:53:39.818Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1013,
        "fields": {
            "title": "Her",
            "year": "2013",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-04T14:12:05.336Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1014,
        "fields": {
            "title": "Home Sweet Hell",
            "year": "2015",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-07T15:37:53.675Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1015,
        "fields": {
            "title": "I Still See You",
            "year": "2018",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-09T04:08:47.115Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1016,
        "fields": {
            "title": "Lyle Lyle Crocodile",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-27T13:55:09.109Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1017,
        "fields": {
            "title": "Manchester by the Sea",
            "year": "2016",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-03T15:02:20.461Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1018,
        "fields": {
            "title": "Max Manus Man Of War แม็กซ์ มานัส ขบวนการล้างนาซี",
            "year": "2008",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-22T03:17:07.572Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1019,
        "fields": {
            "title": "Missing",
            "year": "2023",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-29T06:00:53.173Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1020,
        "fields": {
            "title": "Mother's Day",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-30T07:50:08.816Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1021,
        "fields": {
            "title": "Ode to My Father",
            "year": "2014",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-06T04:31:38.841Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1022,
        "fields": {
            "title": "OMG Oh My Girl",
            "year": "2022",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-13T14:11:04.761Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1023,
        "fields": {
            "title": "Paradise City",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-30T06:04:23.016Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1024,
        "fields": {
            "title": "Patriots Day",
            "year": "2016",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-07T16:05:02.994Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1025,
        "fields": {
            "title": "Peter Pan & Wendy",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-15T04:49:58.593Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1026,
        "fields": {
            "title": "Pride and Prejudice",
            "year": "2005",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-01T12:28:56.566Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1028,
        "fields": {
            "title": "Russian Raid",
            "year": "2020",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-16T14:51:28.328Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1029,
        "fields": {
            "title": "Saving Mr Wu",
            "year": "2015",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-20T09:33:06.302Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1030,
        "fields": {
            "title": "Scream VI หวีดสุดขีด",
            "year": "2023",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-22T01:28:25.865Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1031,
        "fields": {
            "title": "Separation",
            "year": "2021",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-11T00:00:54.975Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1032,
        "fields": {
            "title": "Sing Street",
            "year": "2016",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-06T13:48:27.732Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1033,
        "fields": {
            "title": "Snitch",
            "year": "2013",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-07T14:21:24.278Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1034,
        "fields": {
            "title": "Source Code",
            "year": "2011",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-29T01:17:04.541Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1036,
        "fields": {
            "title": "Super Heros Malgre Lui",
            "year": "2021",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-29T04:10:08.689Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1037,
        "fields": {
            "title": "Thank You For Smoking",
            "year": "2005",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-29T16:06:21.239Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1038,
        "fields": {
            "title": "The Intern",
            "year": "2015",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-15T02:45:13.817Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1039,
        "fields": {
            "title": "The Life of David Gale",
            "year": "2003",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-02T14:08:59.409Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1042,
        "fields": {
            "title": "The Anchor",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-07T04:19:01.567Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1044,
        "fields": {
            "title": "The Imitation Game",
            "year": "2014",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-12T15:47:21.890Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1045,
        "fields": {
            "title": "The Man From U.N.C.L.E",
            "year": "2015",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-11T00:01:10.909Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1046,
        "fields": {
            "title": "The Point Men",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-30T13:10:31.212Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1047,
        "fields": {
            "title": "The Social Network",
            "year": "2010",
            "status": "w",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-07T12:54:25.927Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1048,
        "fields": {
            "title": "The Vanishin",
            "year": "2018",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-09T08:24:39.603Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1049,
        "fields": {
            "title": "The Woman King",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-31T12:32:47.983Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1050,
        "fields": {
            "title": "Tid Noii ทิดน้อย",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-30T08:27:49.860Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1051,
        "fields": {
            "title": "True Grit",
            "year": "2010",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-07T08:01:35.616Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1053,
        "fields": {
            "title": "You Don't Mess with the Zohan",
            "year": "2008",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-25T04:06:19.429Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1054,
        "fields": {
            "title": "Lust Caution เล่ห์ราคะ",
            "year": "2007",
            "status": "r",
            "createdDate": "2023-05-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-22T12:18:42.479Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1055,
        "fields": {
            "title": "Blood & Gold",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-05-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-30T15:04:20.787Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1056,
        "fields": {
            "title": "Juno",
            "year": "2007",
            "status": "r",
            "createdDate": "2023-05-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-02T03:26:00.460Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1057,
        "fields": {
            "title": "Spotlight",
            "year": "2015",
            "status": "r",
            "createdDate": "2023-05-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-07T14:39:37.693Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1058,
        "fields": {
            "title": "Charlie Chaplin: A Dog's Life ชาลี แชปลิน ตอน บุญตกทับ",
            "year": "1918",
            "status": "r",
            "createdDate": "2023-05-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-20T08:55:56.722Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1059,
        "fields": {
            "title": "The Fabric ผ้าผีบอก",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-06-04",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-03T23:48:10.451Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1060,
        "fields": {
            "title": "The Noel Diary",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-06-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-06T13:58:09.678Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1062,
        "fields": {
            "title": "Lincoln",
            "year": "2012",
            "status": "r",
            "createdDate": "2023-06-07",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-05T15:17:18.409Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1063,
        "fields": {
            "title": "SPECIES I สายพันธุ์มฤตยู...สวยสูบนรก 1",
            "year": "1995",
            "status": "r",
            "createdDate": "2023-06-07",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-19T11:23:14.724Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1064,
        "fields": {
            "title": "SPECIES II สายพันธุ์มฤตยู...สวยสูบนรก 2",
            "year": "1998",
            "status": "r",
            "createdDate": "2023-06-07",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-19T11:23:25.159Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1065,
        "fields": {
            "title": "SPECIES III สายพันธุ์มฤตยู...สวยสูบนรก 3",
            "year": "2004",
            "status": "r",
            "createdDate": "2023-06-07",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-19T11:23:33.225Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1066,
        "fields": {
            "title": "SPECIES IV สายพันธุ์มฤตยู...สวยสูบนรก 4",
            "year": "2007",
            "status": "r",
            "createdDate": "2023-06-07",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-19T11:23:40.643Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1067,
        "fields": {
            "title": "The Seduction Game",
            "year": "2011",
            "status": "r",
            "createdDate": "2023-06-07",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-04T03:31:30.391Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1068,
        "fields": {
            "title": "10 Cloverfield Lane",
            "year": "2016",
            "status": "w",
            "createdDate": "2023-06-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-20T08:55:36.911Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1069,
        "fields": {
            "title": "Gothika",
            "year": "2003",
            "status": "w",
            "createdDate": "2023-06-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-04T23:50:58.004Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1070,
        "fields": {
            "title": "Jade Dynasty",
            "year": "2019",
            "status": "r",
            "createdDate": "2023-06-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-11T15:31:46.099Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1071,
        "fields": {
            "title": "Wimbledon",
            "year": "2004",
            "status": "r",
            "createdDate": "2023-06-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-25T14:11:13.097Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1072,
        "fields": {
            "title": "Sin City",
            "year": "2005",
            "status": "r",
            "createdDate": "2023-06-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-09T06:16:33.832Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1073,
        "fields": {
            "title": "Sin City 2 - A Dame to Kill For",
            "year": "2014",
            "status": "r",
            "createdDate": "2023-06-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-09T06:16:45.552Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1074,
        "fields": {
            "title": "Trouble with the Curve",
            "year": "2012",
            "status": "r",
            "createdDate": "2023-06-10",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-05T11:42:53.472Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1075,
        "fields": {
            "title": "True Crime วิกฤติแดนประหาร",
            "year": "1999",
            "status": "r",
            "createdDate": "2023-06-10",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-08T07:08:45.236Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1076,
        "fields": {
            "title": "Cocoon",
            "year": "1995",
            "status": "r",
            "createdDate": "2023-06-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-24T14:06:57.478Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1077,
        "fields": {
            "title": "Cocoon The Return",
            "year": "1998",
            "status": "r",
            "createdDate": "2023-06-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-24T14:07:11.888Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1078,
        "fields": {
            "title": "Extraction 2 คนระห่ำภารกิจเดือด 2",
            "year": "2023",
            "status": "w",
            "createdDate": "2023-06-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-09T15:00:56.575Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1079,
        "fields": {
            "title": "Girl",
            "year": "2018",
            "status": "r",
            "createdDate": "2023-06-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-06T13:04:40.460Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1080,
        "fields": {
            "title": "The Eight Hundred นักรบ 800",
            "year": "2020",
            "status": "r",
            "createdDate": "2023-06-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-03T06:22:35.914Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1081,
        "fields": {
            "title": "The Popes Exorcist",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-06-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-08T12:56:41.497Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1082,
        "fields": {
            "title": "Yara",
            "year": "2021",
            "status": "r",
            "createdDate": "2023-06-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-05T07:21:04.390Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1083,
        "fields": {
            "title": "Ma",
            "year": "2019",
            "status": "w",
            "createdDate": "2023-06-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-20T08:51:37.002Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1084,
        "fields": {
            "title": "Molly's Game",
            "year": "2017",
            "status": "w",
            "createdDate": "2023-06-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-09T16:20:34.382Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1085,
        "fields": {
            "title": "The Legend of Bagger Vance",
            "year": "2000",
            "status": "r",
            "createdDate": "2023-06-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-09T14:33:45.173Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1086,
        "fields": {
            "title": "The Three Burials of Melquiades Estrada พลิกปมฆ่า ผ่าคดีสังหาร",
            "year": "2005",
            "status": "r",
            "createdDate": "2023-06-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-09T23:11:26.228Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1087,
        "fields": {
            "title": "The Vow",
            "year": "2012",
            "status": "r",
            "createdDate": "2023-06-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-05T04:27:40.845Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1088,
        "fields": {
            "title": "The Help",
            "year": "2011",
            "status": "r",
            "createdDate": "2023-06-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-07T16:45:49.230Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1089,
        "fields": {
            "title": "Blood Work ดับชีพจรล่านรก",
            "year": "2002",
            "status": "r",
            "createdDate": "2023-06-23",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-05T06:39:16.934Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1090,
        "fields": {
            "title": "Cocaine Bear หมีคลั่ง",
            "year": "2023",
            "status": "w",
            "createdDate": "2023-06-23",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-12T07:58:49.935Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1091,
        "fields": {
            "title": "Doctor Sleep",
            "year": "2019",
            "status": "r",
            "createdDate": "2023-06-23",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-12T01:36:48.384Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1092,
        "fields": {
            "title": "Don't Say a Word",
            "year": "2001",
            "status": "w",
            "createdDate": "2023-06-23",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-02T09:09:28.426Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1093,
        "fields": {
            "title": "Ghosts of Girlfriends Past",
            "year": "2009",
            "status": "r",
            "createdDate": "2023-06-23",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-04T12:51:06.384Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1094,
        "fields": {
            "title": "Gran Torino",
            "year": "2008",
            "status": "r",
            "createdDate": "2023-06-23",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-27T15:34:14.924Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1095,
        "fields": {
            "title": "Sunshine",
            "year": "2007",
            "status": "r",
            "createdDate": "2023-06-23",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-06-27T14:41:27.963Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1096,
        "fields": {
            "title": "Zombieland",
            "year": "2009",
            "status": "w",
            "createdDate": "2023-06-23",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-11T15:31:07.690Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1097,
        "fields": {
            "title": "Unknown",
            "year": "2011",
            "status": "w",
            "createdDate": "2023-06-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-11T14:19:28.757Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1098,
        "fields": {
            "title": "The Perfect Find",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-06-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-12T15:04:51.245Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1099,
        "fields": {
            "title": "iNumber Number",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-06-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-13T14:09:45.464Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1100,
        "fields": {
            "title": "The Burning Sea",
            "year": "2021",
            "status": "r",
            "createdDate": "2023-06-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-12T14:21:05.080Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1101,
        "fields": {
            "title": "Fall",
            "year": "2022",
            "status": "w",
            "createdDate": "2023-06-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-12T12:18:50.986Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1102,
        "fields": {
            "title": "Inhuman Kiss 2 - The Last Breath แสงกระสือ",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-07-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-15T14:22:18.286Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1103,
        "fields": {
            "title": "Notre-Dame on Fire",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-07-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-14T13:44:54.761Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1104,
        "fields": {
            "title": "Run Rabbit Run",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-07-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-14T14:38:55.548Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1105,
        "fields": {
            "title": "American Psycho",
            "year": "2000",
            "status": "r",
            "createdDate": "2023-07-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-12T06:18:52.318Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1106,
        "fields": {
            "title": "Collateral Damage",
            "year": "2002",
            "status": "w",
            "createdDate": "2023-07-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-12T16:14:43.942Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1107,
        "fields": {
            "title": "In the Valley of Elah",
            "year": "2007",
            "status": "r",
            "createdDate": "2023-07-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-12T04:59:54.444Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1108,
        "fields": {
            "title": "Ditto",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-07-03",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-15T15:48:01.491Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1109,
        "fields": {
            "title": "Enola Holmes",
            "year": "2020",
            "status": "w",
            "createdDate": "2023-07-03",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-06T01:23:01.908Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1110,
        "fields": {
            "title": "Django Unchained",
            "year": "2012",
            "status": "r",
            "createdDate": "2023-07-05",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-05T12:13:58.367Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1111,
        "fields": {
            "title": "It",
            "year": "2017",
            "status": "r",
            "createdDate": "2023-07-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-16T03:08:44.942Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1112,
        "fields": {
            "title": "It Chapter Two",
            "year": "2019",
            "status": "r",
            "createdDate": "2023-07-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-16T03:08:54.737Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1113,
        "fields": {
            "title": "City of God",
            "year": "2002",
            "status": "r",
            "createdDate": "2023-07-07",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-12T16:24:56.981Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1114,
        "fields": {
            "title": "The Proposal",
            "year": "2009",
            "status": "w",
            "createdDate": "2023-07-07",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-12T16:14:59.855Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1115,
        "fields": {
            "title": "Transsiberian",
            "year": "2008",
            "status": "r",
            "createdDate": "2023-07-15",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-23T16:12:39.973Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1116,
        "fields": {
            "title": "The Ghoul Mansion คฤหาสน์ผีปอบ",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-07-15",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-24T12:06:14.035Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1117,
        "fields": {
            "title": "Race ต้อง กล้า วิ่ง",
            "year": "2016",
            "status": "r",
            "createdDate": "2023-07-15",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-21T12:59:08.734Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1118,
        "fields": {
            "title": "Millennium เธอ...ถามใจหารัก",
            "year": "2001",
            "status": "r",
            "createdDate": "2023-07-15",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-18T12:26:18.445Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1119,
        "fields": {
            "title": "Shutter",
            "year": "2004",
            "status": "r",
            "createdDate": "2023-07-15",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-16T03:08:33.983Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1120,
        "fields": {
            "title": "Red Dog",
            "year": "2011",
            "status": "r",
            "createdDate": "2023-07-15",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-16T03:37:10.482Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1121,
        "fields": {
            "title": "The Girl on the Train",
            "year": "2016",
            "status": "w",
            "createdDate": "2023-07-15",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-16T11:59:03.715Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1122,
        "fields": {
            "title": "The Ruins",
            "year": "2008",
            "status": "w",
            "createdDate": "2023-07-15",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-18T14:12:00.162Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1123,
        "fields": {
            "title": "The Way Of The Househusband The Movie พ่อบ้านสุดเก๋า เดอะมูฟวี่",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-07-18",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-26T06:30:20.948Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1124,
        "fields": {
            "title": "Pook Payon ปลุกพยนต์",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-07-18",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-24T14:49:31.551Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1125,
        "fields": {
            "title": "Bird Box Barcelona มอง อย่าให้เห็น (บาร์เซโลนา)",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-07-18",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-26T04:47:27.223Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1127,
        "fields": {
            "title": "A Beatiful Mind",
            "year": "2001",
            "status": "r",
            "createdDate": "2023-07-18",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-26T23:27:04.553Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1128,
        "fields": {
            "title": "21",
            "year": "2008",
            "status": "w",
            "createdDate": "2023-07-18",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-15T14:16:15.302Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1129,
        "fields": {
            "title": "Fatale",
            "year": "2020",
            "status": "r",
            "createdDate": "2023-07-18",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-15T12:37:01.907Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1130,
        "fields": {
            "title": "Breakthrough",
            "year": "2019",
            "status": "r",
            "createdDate": "2023-07-18",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-14T13:41:27.097Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1131,
        "fields": {
            "title": "They Cloned โคลนนิ่งลวง ลับ ล่อ",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-07-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-28T12:18:33.316Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1132,
        "fields": {
            "title": "The American ล่าเด็ดหัวมือสังหารหนีสุดโลก",
            "year": "2010",
            "status": "w",
            "createdDate": "2023-07-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-27T13:05:54.810Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1133,
        "fields": {
            "title": "Knigths of the Zodiac",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-07-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-01T07:15:22.323Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1134,
        "fields": {
            "title": "The Call",
            "year": "2013",
            "status": "w",
            "createdDate": "2023-07-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-31T12:03:51.576Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1135,
        "fields": {
            "title": "The Grey",
            "year": "2011",
            "status": "r",
            "createdDate": "2023-07-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-30T15:35:54.946Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1136,
        "fields": {
            "title": "We Need to Talk About Kevin",
            "year": "2011",
            "status": "r",
            "createdDate": "2023-07-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-30T13:49:48.709Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1137,
        "fields": {
            "title": "The Happening",
            "year": "2008",
            "status": "r",
            "createdDate": "2023-07-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-29T05:34:28.428Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1138,
        "fields": {
            "title": "Pan's Labyrinth",
            "year": "2006",
            "status": "r",
            "createdDate": "2023-07-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-29T02:02:09.263Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1139,
        "fields": {
            "title": "Jupiter Ascending",
            "year": "2015",
            "status": "r",
            "createdDate": "2023-07-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-07-31T14:56:57.334Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1140,
        "fields": {
            "title": "Shin Kamen Rider",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-08-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-02T01:16:42.746Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1141,
        "fields": {
            "title": "JCVD ฌอง คล็อด แวน แดมม์ ข้านี่แหละคนมหาประลัย",
            "year": "2008",
            "status": "r",
            "createdDate": "2023-08-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-01T12:35:45.937Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1142,
        "fields": {
            "title": "Dream",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-08-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-01T16:59:00.191Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1143,
        "fields": {
            "title": "Paradise",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-08-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-01T08:58:04.293Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1144,
        "fields": {
            "title": "The Murderer",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-08-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-01T13:49:36.082Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1145,
        "fields": {
            "title": "Ticket to Paradise",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-08-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-03T12:08:19.337Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1146,
        "fields": {
            "title": "Guardians of the Galaxy Vol 3",
            "year": "2023",
            "status": "w",
            "createdDate": "2023-08-04",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-14T14:21:13.743Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1147,
        "fields": {
            "title": "Winnie the Pooh - Blood and Honey",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-08-04",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-17T02:58:52.553Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1148,
        "fields": {
            "title": "Pig",
            "year": "2021",
            "status": "r",
            "createdDate": "2023-08-04",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-11T13:50:04.582Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1149,
        "fields": {
            "title": "Keanu",
            "year": "2016",
            "status": "r",
            "createdDate": "2023-08-04",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-18T12:20:35.527Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1150,
        "fields": {
            "title": "The Unforgivable",
            "year": "2021",
            "status": "r",
            "createdDate": "2023-08-04",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-18T15:46:31.481Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1151,
        "fields": {
            "title": "Nine Lives",
            "year": "2016",
            "status": "w",
            "createdDate": "2023-08-04",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-16T13:44:47.902Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1152,
        "fields": {
            "title": "Cosmic Sin",
            "year": "2021",
            "status": "r",
            "createdDate": "2023-08-04",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-15T14:15:43.903Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1153,
        "fields": {
            "title": "Khun Pan 3",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-08-07",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-19T15:42:00.867Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1154,
        "fields": {
            "title": "Wish Me Luck",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-08-07",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-13T12:25:04.845Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1155,
        "fields": {
            "title": "Home for Rent",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-08-07",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-17T06:00:56.564Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1156,
        "fields": {
            "title": "The Adjustment Bureau",
            "year": "2011",
            "status": "r",
            "createdDate": "2023-08-07",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-18T15:46:17.321Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1157,
        "fields": {
            "title": "Sisu",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-08-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-21T14:55:53.234Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1158,
        "fields": {
            "title": "Creed",
            "year": "2015",
            "status": "r",
            "createdDate": "2023-08-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-13T13:33:33.621Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1159,
        "fields": {
            "title": "Creed II",
            "year": "2018",
            "status": "r",
            "createdDate": "2023-08-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-13T13:33:39.339Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1160,
        "fields": {
            "title": "Marry My Dead Body",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-08-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-17T09:20:02.821Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1161,
        "fields": {
            "title": "Vesper",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-08-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-17T11:26:20.960Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1162,
        "fields": {
            "title": "Tazza The Hidden Card",
            "year": "2014",
            "status": "r",
            "createdDate": "2023-08-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-22T14:35:31.731Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1163,
        "fields": {
            "title": "Commitment",
            "year": "2013",
            "status": "w",
            "createdDate": "2023-08-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-21T17:31:08.182Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1164,
        "fields": {
            "title": "A Street Cat Named Bob",
            "year": "2016",
            "status": "w",
            "createdDate": "2023-08-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-21T16:23:50.160Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1165,
        "fields": {
            "title": "Gravity",
            "year": "2013",
            "status": "r",
            "createdDate": "2023-08-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-20T07:40:31.231Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1166,
        "fields": {
            "title": "Wood Job",
            "year": "2014",
            "status": "r",
            "createdDate": "2023-08-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-20T03:02:58.143Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1167,
        "fields": {
            "title": "Just Mercy",
            "year": "2019",
            "status": "r",
            "createdDate": "2023-08-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-20T06:12:27.159Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1168,
        "fields": {
            "title": "Ironclad",
            "year": "2011",
            "status": "r",
            "createdDate": "2023-08-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-18T23:18:26.398Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1169,
        "fields": {
            "title": "Heart of Stone",
            "year": "2023",
            "status": "w",
            "createdDate": "2023-08-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-22T13:32:09.430Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1170,
        "fields": {
            "title": "Red, White & Royal Blue เรด ไวท์ & รอยัล บลู รักของผมกับเจ้าชาย",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-08-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-17T06:52:05.895Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1171,
        "fields": {
            "title": "Money Monster",
            "year": "2016",
            "status": "r",
            "createdDate": "2023-08-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-26T03:16:58.577Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1172,
        "fields": {
            "title": "Just Go with It",
            "year": "2011",
            "status": "w",
            "createdDate": "2023-08-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-25T14:25:07.073Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1173,
        "fields": {
            "title": "Kiss Kiss Bang Bang",
            "year": "2005",
            "status": "r",
            "createdDate": "2023-08-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-24T15:51:09.588Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1174,
        "fields": {
            "title": "Looper",
            "year": "2012",
            "status": "w",
            "createdDate": "2023-08-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-21T14:05:15.396Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1175,
        "fields": {
            "title": "Be With You",
            "year": "2004",
            "status": "r",
            "createdDate": "2023-08-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-24T12:42:27.798Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1176,
        "fields": {
            "title": "The Blind Side",
            "year": "2009",
            "status": "r",
            "createdDate": "2023-08-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-24T12:42:13.219Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1177,
        "fields": {
            "title": "Room",
            "year": "2015",
            "status": "r",
            "createdDate": "2023-08-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-22T16:28:56.334Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1178,
        "fields": {
            "title": "The Princess Diaries",
            "year": "2001",
            "status": "r",
            "createdDate": "2023-08-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-20T13:11:30.574Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1179,
        "fields": {
            "title": "The Princess Diaries 2 Royal Engagement",
            "year": "2004",
            "status": "r",
            "createdDate": "2023-08-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-20T13:11:53.563Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1180,
        "fields": {
            "title": "Lost in Blue ระหว่างเราครั้งก่อน",
            "year": "2016",
            "status": "r",
            "createdDate": "2023-08-21",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-25T12:58:29.395Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1181,
        "fields": {
            "title": "Fear Street Part 1 1994",
            "year": "2021",
            "status": "r",
            "createdDate": "2023-08-21",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-31T05:23:23.856Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1182,
        "fields": {
            "title": "Fear Street Part 2 1978",
            "year": "2021",
            "status": "r",
            "createdDate": "2023-08-21",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-31T05:23:38.182Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1183,
        "fields": {
            "title": "Fear Street Part 3 1666",
            "year": "2021",
            "status": "r",
            "createdDate": "2023-08-21",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-31T05:24:48.476Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1184,
        "fields": {
            "title": "Viking Woof",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-08-21",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-26T13:33:20.974Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1185,
        "fields": {
            "title": "Dearest Sister ນ້ອງຮັກ",
            "year": "2016",
            "status": "r",
            "createdDate": "2023-08-21",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-19T12:13:04.046Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1186,
        "fields": {
            "title": "Take Shelter",
            "year": "2011",
            "status": "r",
            "createdDate": "2023-08-21",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-27T10:00:24.134Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1187,
        "fields": {
            "title": "Get Smart",
            "year": "2008",
            "status": "w",
            "createdDate": "2023-08-21",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-27T03:06:15.951Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1188,
        "fields": {
            "title": "The Fighter",
            "year": "2010",
            "status": "r",
            "createdDate": "2023-08-21",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-26T03:40:14.517Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1189,
        "fields": {
            "title": "Surrogates",
            "year": "2009",
            "status": "r",
            "createdDate": "2023-08-22",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-28T14:08:53.153Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1190,
        "fields": {
            "title": "The Devil Wears Prada",
            "year": "2006",
            "status": "r",
            "createdDate": "2023-08-22",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-27T13:26:28.540Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1191,
        "fields": {
            "title": "I Care a Lot",
            "year": "2020",
            "status": "w",
            "createdDate": "2023-08-22",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-27T12:15:07.877Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1192,
        "fields": {
            "title": "Little Women",
            "year": "2019",
            "status": "r",
            "createdDate": "2023-08-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-30T13:50:58.779Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1193,
        "fields": {
            "title": "The Courier",
            "year": "2019",
            "status": "r",
            "createdDate": "2023-08-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-29T15:33:37.888Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1194,
        "fields": {
            "title": "Beirut",
            "year": "2018",
            "status": "r",
            "createdDate": "2023-08-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-08-29T14:08:03.129Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1195,
        "fields": {
            "title": "Prince of Persia The Sands of Time",
            "year": "2010",
            "status": "w",
            "createdDate": "2023-08-26",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-20T08:54:41.907Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1196,
        "fields": {
            "title": "Guy Ritchie's The Covenant เดอะ โคเวแนนท์ โดย กาย ริชชี่",
            "year": "2023",
            "status": "w",
            "createdDate": "2023-08-26",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-20T08:54:50.937Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1197,
        "fields": {
            "title": "Killer Book Club ชมรมหนังสือฆาตกร",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-08-31",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-15T07:57:59.571Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1198,
        "fields": {
            "title": "The Only Mom มาร-ดา",
            "year": "2019",
            "status": "r",
            "createdDate": "2023-08-31",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-01T04:18:30.112Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1199,
        "fields": {
            "title": "Kumanthong กุมารทอง ราคะ เฮี้ยน",
            "year": "2019",
            "status": "r",
            "createdDate": "2023-08-31",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-01T03:07:54.555Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1200,
        "fields": {
            "title": "Summit Fever",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-08-31",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-27T12:02:38.511Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1201,
        "fields": {
            "title": "Unstoppable",
            "year": "2010",
            "status": "r",
            "createdDate": "2023-08-31",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-04T15:50:00.292Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1202,
        "fields": {
            "title": "The Lighthouse",
            "year": "2019",
            "status": "r",
            "createdDate": "2023-08-31",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-05T15:48:31.320Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1203,
        "fields": {
            "title": "Richard Jewell",
            "year": "2019",
            "status": "r",
            "createdDate": "2023-08-31",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-05T14:20:34.464Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1204,
        "fields": {
            "title": "Lucy in the Sky",
            "year": "2019",
            "status": "r",
            "createdDate": "2023-08-31",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-04T15:49:51.497Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1205,
        "fields": {
            "title": "Revolver",
            "year": "2005",
            "status": "r",
            "createdDate": "2023-09-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-09T02:42:57.148Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1206,
        "fields": {
            "title": "Good Luck Chuck [Unrated]",
            "year": "2007",
            "status": "r",
            "createdDate": "2023-09-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-08T13:41:37.225Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1207,
        "fields": {
            "title": "The Last 10 Years",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-09-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-03T13:02:51.662Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1208,
        "fields": {
            "title": "No Hard Feelings",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-09-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-02T14:51:57.174Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1209,
        "fields": {
            "title": "Transformers 6 Rise of the Beasts",
            "year": "2023",
            "status": "w",
            "createdDate": "2023-09-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-04T12:29:32.951Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1210,
        "fields": {
            "title": "John Wick Chapter 4",
            "year": "2023",
            "status": "w",
            "createdDate": "2023-09-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-15T08:00:28.723Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1211,
        "fields": {
            "title": "Meg 2 The Trench",
            "year": "2023",
            "status": "w",
            "createdDate": "2023-09-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-03T14:37:41.120Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1212,
        "fields": {
            "title": "Nakornsawan นคร-สวรรค์  นครแห่งความจริง สวรรค์แห่งเรื่องเล่า",
            "year": "2018",
            "status": "r",
            "createdDate": "2023-09-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-01T06:28:54.810Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1213,
        "fields": {
            "title": "The Condemned",
            "year": "2007",
            "status": "r",
            "createdDate": "2023-09-09",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-08T23:14:35.951Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1214,
        "fields": {
            "title": "Cyborg Girl ยัยนี่น่ารักจัง",
            "year": "2008",
            "status": "r",
            "createdDate": "2023-09-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-04T12:27:50.402Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1215,
        "fields": {
            "title": "Seabiscuit",
            "year": "2003",
            "status": "r",
            "createdDate": "2023-09-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-12T13:38:40.062Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1216,
        "fields": {
            "title": "Once Upon a Crime",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-09-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-10T12:47:41.194Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1217,
        "fields": {
            "title": "Thunder Monk",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-09-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-08T13:46:08.743Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1218,
        "fields": {
            "title": "Love at First Sight",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-09-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-08T13:11:24.107Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1220,
        "fields": {
            "title": "The Triangle Part 1",
            "year": "2005",
            "status": "r",
            "createdDate": "2023-09-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-08T13:10:53.650Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1221,
        "fields": {
            "title": "Brightburn",
            "year": "2019",
            "status": "r",
            "createdDate": "2023-09-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-23T09:40:20.845Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1222,
        "fields": {
            "title": "The Ledge",
            "year": "2011",
            "status": "r",
            "createdDate": "2023-09-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-20T14:49:29.672Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1223,
        "fields": {
            "title": "The Shamer's Daughter",
            "year": "2015",
            "status": "r",
            "createdDate": "2023-09-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-20T13:07:12.612Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1224,
        "fields": {
            "title": "Spy Kids Armageddon พยัคฆ์จิ๋วไฮเทค วันสิ้นโลก",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-09-28",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-12T03:19:48.047Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1225,
        "fields": {
            "title": "The Equalizer",
            "year": "2014",
            "status": "w",
            "createdDate": "2023-09-28",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-20T08:54:14.684Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1226,
        "fields": {
            "title": "Shaun of the Dead",
            "year": "2004",
            "status": "r",
            "createdDate": "2023-09-28",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-30T03:59:58.190Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1227,
        "fields": {
            "title": "The Wondering Earth",
            "year": "2019",
            "status": "r",
            "createdDate": "2023-09-28",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-30T05:36:49.582Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1228,
        "fields": {
            "title": "Tropic Thunder",
            "year": "2008",
            "status": "r",
            "createdDate": "2023-09-28",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-09-30T04:00:19.548Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1229,
        "fields": {
            "title": "Love is in the Air",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-10-03",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-12T08:16:24.270Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1230,
        "fields": {
            "title": "The Ice Road เหยียบระห่ำ ฝ่านรกเยือกแข็ง",
            "year": "2021",
            "status": "r",
            "createdDate": "2023-10-03",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-12T07:08:11.687Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1231,
        "fields": {
            "title": "Overhaul ซิ่งแรงแซงตาย",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-10-03",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-12T09:25:19.458Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1232,
        "fields": {
            "title": "Legend of The Demon Cat ตำนานอสูรล่าวิญญาณ",
            "year": "2017",
            "status": "r",
            "createdDate": "2023-10-03",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-04T13:31:19.544Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1233,
        "fields": {
            "title": "Insidious The Red Door",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-10-03",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-12T04:58:59.694Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1234,
        "fields": {
            "title": "Ex Machina",
            "year": "2015",
            "status": "r",
            "createdDate": "2023-10-03",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-11T06:58:45.183Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1235,
        "fields": {
            "title": "Gangster Squad",
            "year": "2013",
            "status": "w",
            "createdDate": "2023-10-03",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-04T15:38:23.085Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1236,
        "fields": {
            "title": "Shock Wave",
            "year": "2017",
            "status": "r",
            "createdDate": "2023-10-03",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-05T18:06:18.149Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1237,
        "fields": {
            "title": "Shock Wave 2",
            "year": "2020",
            "status": "r",
            "createdDate": "2023-10-03",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-05T18:06:28.343Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1238,
        "fields": {
            "title": "Haunted Hotel 1174 ห้องผีจองเวร",
            "year": "2018",
            "status": "r",
            "createdDate": "2023-10-04",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-06T16:03:31.753Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1239,
        "fields": {
            "title": "Gangnam Zombie คังนัมซอมบี้",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-10-04",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-13T06:03:05.108Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1240,
        "fields": {
            "title": "Gran Turismo",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-10-09",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-19T09:06:28.370Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1241,
        "fields": {
            "title": "Ballerina",
            "year": "2023",
            "status": "w",
            "createdDate": "2023-10-09",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-13T15:50:37.092Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1242,
        "fields": {
            "title": "Haunted Mansion บ้านชวนเฮี้ยน ผีชวนฮา",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-10-09",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-13T13:35:01.419Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1243,
        "fields": {
            "title": "Nowhere",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-10-09",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-13T12:00:31.942Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1244,
        "fields": {
            "title": "From Vegas to Macau โคตรเซียนมาเก๊า เขย่าเวกัส",
            "year": "2014",
            "status": "r",
            "createdDate": "2023-10-09",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-10T14:33:57.734Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1245,
        "fields": {
            "title": "From Vegas to Macau II โคตรเซียนมาเก๊า เขย่าเวกัส 2",
            "year": "2015",
            "status": "r",
            "createdDate": "2023-10-09",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-10T14:34:16.179Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1247,
        "fields": {
            "title": "Kitty The Killer อีหนูอันตราย",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-10-09",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-13T07:43:36.859Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1248,
        "fields": {
            "title": "Nobody",
            "year": "2021",
            "status": "w",
            "createdDate": "2023-10-09",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-09T14:40:00.543Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1249,
        "fields": {
            "title": "Land",
            "year": "2021",
            "status": "r",
            "createdDate": "2023-10-14",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-14T06:23:04.115Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1250,
        "fields": {
            "title": "Unbroken",
            "year": "2014",
            "status": "r",
            "createdDate": "2023-10-14",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-14T13:22:56.868Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1251,
        "fields": {
            "title": "Jigen Daisuke ไดสุเกะ จิเก็น",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-10-15",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-14T06:20:34.190Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1252,
        "fields": {
            "title": "The Conference สัมมนาเลือด",
            "year": "2023",
            "status": "w",
            "createdDate": "2023-10-15",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-14T14:36:36.481Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1253,
        "fields": {
            "title": "Once Upon a Star มนต์รักนักพากย์",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-10-15",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-14T15:52:40.779Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1254,
        "fields": {
            "title": "Zien Lang Best Friends Forever",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-10-15",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-17T13:20:17.719Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1255,
        "fields": {
            "title": "Dark World เกมล่าฆ่ารอด",
            "year": "2021",
            "status": "r",
            "createdDate": "2023-10-15",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-15T08:46:41.497Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1256,
        "fields": {
            "title": "Mission Impossible Dead Reckoning Part 1",
            "year": "2023",
            "status": "w",
            "createdDate": "2023-10-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-17T13:20:49.188Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1257,
        "fields": {
            "title": "The House Eif บ้านนี้เอลฟ์ดุ",
            "year": "2019",
            "status": "r",
            "createdDate": "2023-10-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-19T13:48:57.351Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1258,
        "fields": {
            "title": "The Concubine",
            "year": "2012",
            "status": "r",
            "createdDate": "2023-10-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-24T13:39:54.238Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1259,
        "fields": {
            "title": "The Equalizer 3",
            "year": "2023",
            "status": "w",
            "createdDate": "2023-10-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-19T14:16:53.220Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1260,
        "fields": {
            "title": "Homefront",
            "year": "2013",
            "status": "w",
            "createdDate": "2023-10-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-25T14:35:52.753Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1261,
        "fields": {
            "title": "Hotel Artemis",
            "year": "2018",
            "status": "w",
            "createdDate": "2023-10-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-25T12:10:38.140Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1262,
        "fields": {
            "title": "Killers",
            "year": "2010",
            "status": "w",
            "createdDate": "2023-10-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-29T01:45:45.063Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1263,
        "fields": {
            "title": "From Paris with Love คู่ระห่ำ ฝรั่งแสบ",
            "year": "2010",
            "status": "w",
            "createdDate": "2023-10-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-29T08:31:48.745Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1264,
        "fields": {
            "title": "Alone ฝ่ามหันตภัยเมืองร้าง",
            "year": "2017",
            "status": "r",
            "createdDate": "2023-10-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-25T14:55:52.527Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1265,
        "fields": {
            "title": "Ghost College of Fine Arts เพื่อนกันเฉพาะวันพระ",
            "year": "2008",
            "status": "r",
            "createdDate": "2023-10-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-27T06:43:56.717Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1267,
        "fields": {
            "title": "M3GAN",
            "year": "2023",
            "status": "w",
            "createdDate": "2023-10-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-29T10:15:00.875Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1268,
        "fields": {
            "title": "Crypto Boy",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-10-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-29T13:42:04.246Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1269,
        "fields": {
            "title": "The Devil's Deal ดีลนรกคนกินชาติ",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-10-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-25T13:49:31.862Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1270,
        "fields": {
            "title": "Pain Threshold ทริประทึก",
            "year": "2019",
            "status": "r",
            "createdDate": "2023-10-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-29T15:18:16.530Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1271,
        "fields": {
            "title": "Infection เชื้อนรก คนคลั่งสยองโลก",
            "year": "2019",
            "status": "r",
            "createdDate": "2023-10-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-30T02:10:23.215Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1272,
        "fields": {
            "title": "Werewolf by Night in Color แวร์วูล์ฟ บาย ไนท์ คืนหอน อสูรโหด อิน คัลเลอร์",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-10-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-30T04:23:41.515Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1273,
        "fields": {
            "title": "Always",
            "year": "2011",
            "status": "r",
            "createdDate": "2023-10-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-10-31T12:49:08.094Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1274,
        "fields": {
            "title": "Tolkien",
            "year": "2019",
            "status": "r",
            "createdDate": "2023-10-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-01T12:51:00.817Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1275,
        "fields": {
            "title": "Ghost Ship",
            "year": "2002",
            "status": "r",
            "createdDate": "2023-11-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-12T03:06:37.850Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1277,
        "fields": {
            "title": "Armageddon Time",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-11-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-29T01:43:28.404Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1278,
        "fields": {
            "title": "In the Heart of the Sea",
            "year": "2015",
            "status": "r",
            "createdDate": "2023-11-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-03T12:42:36.750Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1279,
        "fields": {
            "title": "Pet Sematary",
            "year": "2019",
            "status": "r",
            "createdDate": "2023-11-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-03T15:12:14.729Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1280,
        "fields": {
            "title": "Guardians of the Galaxy Vol 2",
            "year": "2017",
            "status": "w",
            "createdDate": "2023-11-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-06T11:58:14.221Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1281,
        "fields": {
            "title": "OK Baytong โอเค เบตง",
            "year": "2003",
            "status": "r",
            "createdDate": "2023-11-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-12T03:06:20.312Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1282,
        "fields": {
            "title": "A Haunting in Venice",
            "year": "2023",
            "status": "w",
            "createdDate": "2023-11-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-28T05:46:40.538Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1283,
        "fields": {
            "title": "Blue Beetle",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-11-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-28T11:26:03.841Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1284,
        "fields": {
            "title": "The Silenced โรงเรียนสยดสัญญาณสยอง",
            "year": "2015",
            "status": "r",
            "createdDate": "2023-11-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-09T13:26:57.836Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1285,
        "fields": {
            "title": "Wingwomen ร่วมด้วยช่วยกัน...ปล้น",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-11-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-28T09:02:29.567Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1286,
        "fields": {
            "title": "Sister Death",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-11-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-28T06:46:12.330Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1287,
        "fields": {
            "title": "Shambhala",
            "year": "2012",
            "status": "r",
            "createdDate": "2023-11-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-08T16:46:00.256Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1288,
        "fields": {
            "title": "What Women Want",
            "year": "2000",
            "status": "r",
            "createdDate": "2023-11-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-08T14:59:43.852Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1289,
        "fields": {
            "title": "The Nun II",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-11-15",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-31T09:17:31.422Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1290,
        "fields": {
            "title": "Hypnotic",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-11-15",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-27T11:03:13.266Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1291,
        "fields": {
            "title": "My Precious",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-11-15",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-27T11:15:47.092Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1292,
        "fields": {
            "title": "Accross the Universe",
            "year": "2007",
            "status": "r",
            "createdDate": "2023-11-15",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-27T14:35:33.746Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1293,
        "fields": {
            "title": "The Upside",
            "year": "2017",
            "status": "r",
            "createdDate": "2023-11-15",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-16T16:06:08.175Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1294,
        "fields": {
            "title": "The Phantom of the Opera",
            "year": "2004",
            "status": "r",
            "createdDate": "2023-11-15",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-16T14:07:25.214Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1295,
        "fields": {
            "title": "Stillwater",
            "year": "2021",
            "status": "r",
            "createdDate": "2023-11-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-31T13:28:00.110Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1296,
        "fields": {
            "title": "80 for Brady",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-11-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-30T05:33:55.429Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1297,
        "fields": {
            "title": "Changeling",
            "year": "2008",
            "status": "r",
            "createdDate": "2023-11-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-23T14:31:21.815Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1298,
        "fields": {
            "title": "The Boy in the Striped Pajamas",
            "year": "2008",
            "status": "r",
            "createdDate": "2023-11-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-21T15:17:22.231Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1299,
        "fields": {
            "title": "The Legend of Zu  ซูซัน ศึกเทพยุทธถล่มฟ้า.mkv",
            "year": "2001",
            "status": "r",
            "createdDate": "2023-11-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-30T12:29:11.509Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1300,
        "fields": {
            "title": "It Gets Better",
            "year": "2012",
            "status": "r",
            "createdDate": "2023-11-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-01T08:16:42.546Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1301,
        "fields": {
            "title": "Believer",
            "year": "2018",
            "status": "w",
            "createdDate": "2023-11-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-31T06:53:19.845Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1302,
        "fields": {
            "title": "Legend of the Tsunami Warrior",
            "year": "2008",
            "status": "r",
            "createdDate": "2023-11-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-26T04:03:11.289Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1303,
        "fields": {
            "title": "Rustin",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-11-27",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-01T15:01:08.642Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1304,
        "fields": {
            "title": "Best Christmas Ever",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-11-27",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-01T12:24:00.816Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1305,
        "fields": {
            "title": "Doi Boy",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-11-27",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-01T14:31:15.201Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1306,
        "fields": {
            "title": "The Raid Redemption",
            "year": "2012",
            "status": "w",
            "createdDate": "2023-11-27",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-30T23:30:50.097Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1307,
        "fields": {
            "title": "The Raid 2",
            "year": "2014",
            "status": "w",
            "createdDate": "2023-11-27",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-30T23:30:34.062Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1308,
        "fields": {
            "title": "Congrats My Ex! ลุ้นรักป่วน ก๊วนแฟนเก่า",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-11-27",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-30T06:58:12.978Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1309,
        "fields": {
            "title": "Super Salaryman",
            "year": "2012",
            "status": "r",
            "createdDate": "2023-11-27",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-11-28T14:44:55.866Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1310,
        "fields": {
            "title": "Architecture 101",
            "year": "2012",
            "status": "w",
            "createdDate": "2023-11-27",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-20T08:53:05.600Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1311,
        "fields": {
            "title": "Indiana Jones and the Dail of Destiny",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-12-03",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-02T14:44:40.287Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1312,
        "fields": {
            "title": "3 Idiot Heroes ฮีโร่ต้มแซ่บ",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-12-03",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-02T03:26:54.534Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1313,
        "fields": {
            "title": "47 Ronin 47 โรนิน มหาศึกซามูไร",
            "year": "2013",
            "status": "w",
            "createdDate": "2023-12-03",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-09T15:12:37.336Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1314,
        "fields": {
            "title": "Hidden Figures",
            "year": "2016",
            "status": "r",
            "createdDate": "2023-12-03",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-09T04:02:05.339Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1315,
        "fields": {
            "title": "Assassination",
            "year": "2015",
            "status": "w",
            "createdDate": "2023-12-03",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-10T02:15:18.847Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1316,
        "fields": {
            "title": "Artemis Fowl",
            "year": "2020",
            "status": "r",
            "createdDate": "2023-12-03",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-08T08:04:25.574Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1317,
        "fields": {
            "title": "The Theory of Everything",
            "year": "2014",
            "status": "r",
            "createdDate": "2023-12-03",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-07T14:34:07.927Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1318,
        "fields": {
            "title": "After The Rain",
            "year": "2018",
            "status": "r",
            "createdDate": "2023-12-03",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-05T13:40:18.443Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1319,
        "fields": {
            "title": "Savages",
            "year": "2012",
            "status": "r",
            "createdDate": "2023-12-03",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-05T13:11:45.294Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1320,
        "fields": {
            "title": "The Rite",
            "year": "2011",
            "status": "r",
            "createdDate": "2023-12-03",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-05T09:32:37.056Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1321,
        "fields": {
            "title": "Let Me In",
            "year": "2010",
            "status": "r",
            "createdDate": "2023-12-03",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-03T03:35:33.379Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1322,
        "fields": {
            "title": "The Lazarus Effect",
            "year": "2015",
            "status": "r",
            "createdDate": "2023-12-03",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-02T10:10:04.740Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1323,
        "fields": {
            "title": "Devil",
            "year": "2010",
            "status": "w",
            "createdDate": "2023-12-03",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-02T13:39:53.162Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1324,
        "fields": {
            "title": "Family Switch",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-12-03",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-02T06:19:04.628Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1325,
        "fields": {
            "title": "Hard Days",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-12-03",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-02T08:42:20.415Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1326,
        "fields": {
            "title": "The Unbearable Weight of Massive Talent ข้านี่แหละ นิค “ฟักกลิ้ง” เคจ",
            "year": "2022",
            "status": "w",
            "createdDate": "2023-12-10",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-05T06:08:26.848Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1327,
        "fields": {
            "title": "Knock at the Cabin",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-12-10",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-05T08:18:00.246Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1328,
        "fields": {
            "title": "Uncle Drew",
            "year": "2018",
            "status": "r",
            "createdDate": "2023-12-10",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-05T02:10:36.440Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1329,
        "fields": {
            "title": "Slice",
            "year": "2009",
            "status": "r",
            "createdDate": "2023-12-10",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-02T02:39:30.682Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1330,
        "fields": {
            "title": "Mile 22",
            "year": "2018",
            "status": "w",
            "createdDate": "2023-12-10",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-11T14:27:48.838Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1331,
        "fields": {
            "title": "Hostage",
            "year": "2005",
            "status": "w",
            "createdDate": "2023-12-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-14T14:21:33.826Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1332,
        "fields": {
            "title": "Mank",
            "year": "2020",
            "status": "r",
            "createdDate": "2023-12-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-15T13:23:14.196Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1333,
        "fields": {
            "title": "Bedevilled",
            "year": "2010",
            "status": "r",
            "createdDate": "2023-12-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-04T14:06:35.095Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1334,
        "fields": {
            "title": "Leave the World Behide",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-12-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-04T16:52:55.271Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1335,
        "fields": {
            "title": "Violent Night",
            "year": "2022",
            "status": "w",
            "createdDate": "2023-12-18",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-04T10:17:39.564Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1336,
        "fields": {
            "title": "American Assassin",
            "year": "2017",
            "status": "w",
            "createdDate": "2023-12-18",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-20T08:53:31.607Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1337,
        "fields": {
            "title": "Lawless",
            "year": "2012",
            "status": "r",
            "createdDate": "2023-12-18",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-21T12:45:40.391Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1338,
        "fields": {
            "title": "Minority Report",
            "year": "2002",
            "status": "w",
            "createdDate": "2023-12-18",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-21T12:46:07.502Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1339,
        "fields": {
            "title": "8MM",
            "year": "1999",
            "status": "w",
            "createdDate": "2023-12-22",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-25T13:02:15.099Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1340,
        "fields": {
            "title": "The Creator",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-12-27",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-09T03:34:26.551Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1341,
        "fields": {
            "title": "Rebel Moon Part One A Child of Fire ภาค 1 บุตรแห่งเปลวไฟ",
            "year": "2023",
            "status": "r",
            "createdDate": "2023-12-27",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-03T08:45:17.558Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1342,
        "fields": {
            "title": "The Lair",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-12-27",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-03T12:55:57.339Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1343,
        "fields": {
            "title": "The Thing",
            "year": "2011",
            "status": "r",
            "createdDate": "2023-12-27",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-09T05:35:25.890Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1344,
        "fields": {
            "title": "The Gunman",
            "year": "2015",
            "status": "r",
            "createdDate": "2023-12-27",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-03T08:31:11.654Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1345,
        "fields": {
            "title": "Decibel",
            "year": "2022",
            "status": "r",
            "createdDate": "2023-12-27",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-03T15:14:56.000Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1346,
        "fields": {
            "title": "Seventh Son",
            "year": "2014",
            "status": "r",
            "createdDate": "2023-12-27",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-04T02:23:16.724Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1347,
        "fields": {
            "title": "A Beautiful Day in the Neighborhood",
            "year": "2019",
            "status": "r",
            "createdDate": "2023-12-27",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-04T05:01:05.612Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1348,
        "fields": {
            "title": "The Finest Hours",
            "year": "2016",
            "status": "r",
            "createdDate": "2023-12-27",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-31T09:37:11.438Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1349,
        "fields": {
            "title": "Into the Woods",
            "year": "2014",
            "status": "r",
            "createdDate": "2023-12-27",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2023-12-31T13:53:31.293Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1350,
        "fields": {
            "title": "Mondo",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-01-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-06T15:55:19.318Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1351,
        "fields": {
            "title": "My Happy Marriage",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-01-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-07T01:43:29.297Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1352,
        "fields": {
            "title": "Miss  Shampoo",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-01-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-07T03:28:06.172Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1353,
        "fields": {
            "title": "The Adventures",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-01-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-08T09:41:10.182Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1354,
        "fields": {
            "title": "The Ghost Station",
            "year": "2022",
            "status": "r",
            "createdDate": "2024-01-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-08T07:49:50.851Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1355,
        "fields": {
            "title": "The Last Christmas",
            "year": "2019",
            "status": "r",
            "createdDate": "2024-01-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-07T08:07:37.340Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1356,
        "fields": {
            "title": "The Alamo",
            "year": "2004",
            "status": "r",
            "createdDate": "2024-01-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-08T03:39:28.325Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1357,
        "fields": {
            "title": "Bait",
            "year": "2012",
            "status": "r",
            "createdDate": "2024-01-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-08T13:46:38.547Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1358,
        "fields": {
            "title": "Focus",
            "year": "2015",
            "status": "w",
            "createdDate": "2024-01-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-08T14:23:27.902Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1359,
        "fields": {
            "title": "The Exorcist Believer",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-01-11",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-01-29T03:40:15.879Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1362,
        "fields": {
            "title": "Lemony Snickets A Series of Unfortunate Events",
            "year": "2004",
            "status": "r",
            "createdDate": "2024-01-11",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-06T08:42:07.733Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1363,
        "fields": {
            "title": "Unforgiven",
            "year": "1992",
            "status": "r",
            "createdDate": "2024-01-11",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-06T12:41:30.920Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1364,
        "fields": {
            "title": "Moloch อย่าขุดมันขึ้นมา",
            "year": "2022",
            "status": "r",
            "createdDate": "2024-01-11",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-11T10:22:11.581Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1365,
        "fields": {
            "title": "Society of the Snow หิมะโหด คนทรหด",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-01-11",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-11T07:01:07.500Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1366,
        "fields": {
            "title": "My Super Ex-Girlfriend กิ๊กเก่าผม เธอเป็นยอดมนุษย์",
            "year": "2006",
            "status": "r",
            "createdDate": "2024-01-11",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-06T14:53:38.345Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1367,
        "fields": {
            "title": "Phases of the Moon เกิดกี่ครั้งก็ยังเป็นเธอ",
            "year": "2022",
            "status": "r",
            "createdDate": "2024-01-11",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-08T01:51:30.327Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1368,
        "fields": {
            "title": "Blade",
            "year": "1998",
            "status": "w",
            "createdDate": "2024-01-11",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-09T12:57:20.368Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1369,
        "fields": {
            "title": "Blade II",
            "year": "2002",
            "status": "w",
            "createdDate": "2024-01-11",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-09T12:57:28.206Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1370,
        "fields": {
            "title": "Blade Trinity",
            "year": "2004",
            "status": "w",
            "createdDate": "2024-01-11",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-09T12:57:38.713Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1371,
        "fields": {
            "title": "You Are Not My Mother มาร(ดา)จำแลง",
            "year": "2022",
            "status": "r",
            "createdDate": "2024-01-11",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-08T07:21:52.896Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1372,
        "fields": {
            "title": "Gunpowder Milkshake นรกเรียกแม่",
            "year": "2021",
            "status": "w",
            "createdDate": "2024-01-11",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-06T06:53:41.793Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1373,
        "fields": {
            "title": "Garfield การ์ฟิลด์ เดอะ มูฟวี่",
            "year": "2004",
            "status": "w",
            "createdDate": "2024-01-11",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-04T10:17:59.333Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1374,
        "fields": {
            "title": "Garfield A Tail of Two Kitties การ์ฟิลด์ 2 ตอน อลเวงเจ้าชายบัลลังก์เหมียว",
            "year": "2006",
            "status": "w",
            "createdDate": "2024-01-11",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-04T07:14:20.550Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1375,
        "fields": {
            "title": "Always Be with You สัมผัสมรณะ",
            "year": "2017",
            "status": "r",
            "createdDate": "2024-01-11",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-06T01:52:43.942Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1376,
        "fields": {
            "title": "Flight 7500 ไฟลท์ 7500 ไม่ตกก็ตาย",
            "year": "2014",
            "status": "r",
            "createdDate": "2024-01-11",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-04T08:29:11.797Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1377,
        "fields": {
            "title": "The Marvels",
            "year": "2023",
            "status": "w",
            "createdDate": "2024-01-24",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-12T15:32:37.530Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1378,
        "fields": {
            "title": "Miss You Again อนึ่ง คิดถึงเป็นอย่างยิ่ง",
            "year": "2009",
            "status": "r",
            "createdDate": "2024-01-24",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-12T02:23:59.034Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1379,
        "fields": {
            "title": "Napoleon",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-01-24",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-12T07:49:34.634Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1380,
        "fields": {
            "title": "I MISS YOU อนึ่ง คิดถึงพอสังเขป",
            "year": "1992",
            "status": "r",
            "createdDate": "2024-01-24",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-12T02:23:10.203Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1381,
        "fields": {
            "title": "I MISS YOU 2 อนึ่ง คิดถึงพอสังเขป รุ่น 2",
            "year": "1996",
            "status": "r",
            "createdDate": "2024-01-24",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-12T02:23:31.074Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1382,
        "fields": {
            "title": "After Sundown ดับแสงรวี",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-01-24",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-11T14:34:46.421Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1383,
        "fields": {
            "title": "The Legend Of Monkey หนุมานคลุกฝุ่น",
            "year": "2008",
            "status": "r",
            "createdDate": "2024-02-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-14T04:11:02.227Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1384,
        "fields": {
            "title": "The Exchange โจรปล้นโจร",
            "year": "2019",
            "status": "r",
            "createdDate": "2024-02-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-16T08:21:50.303Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1385,
        "fields": {
            "title": "Still Missing พราก",
            "year": "2020",
            "status": "r",
            "createdDate": "2024-02-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-16T07:52:06.885Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1386,
        "fields": {
            "title": "My Sexdoll พร้อมรุก ยัยตุ๊กตาซ้อมรัก",
            "year": "2020",
            "status": "r",
            "createdDate": "2024-02-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-13T14:06:46.191Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1387,
        "fields": {
            "title": "Man of ma year คนปีมะ",
            "year": "2003",
            "status": "r",
            "createdDate": "2024-02-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-16T09:25:51.844Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1388,
        "fields": {
            "title": "Ghost Mother ผีเลี้ยงลูกคน",
            "year": "2007",
            "status": "r",
            "createdDate": "2024-02-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-14T16:35:42.990Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1389,
        "fields": {
            "title": "Evil Phone ต่อติดตาย",
            "year": "2002",
            "status": "r",
            "createdDate": "2024-02-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-14T12:48:42.158Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1390,
        "fields": {
            "title": "Wonka",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-02-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-13T05:34:30.568Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1391,
        "fields": {
            "title": "We're The Millers",
            "year": "2013",
            "status": "r",
            "createdDate": "2024-02-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-11T05:29:02.588Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1392,
        "fields": {
            "title": "Up In The Air",
            "year": "2009",
            "status": "r",
            "createdDate": "2024-02-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-13T14:02:29.606Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1393,
        "fields": {
            "title": "The Beekeeper",
            "year": "2024",
            "status": "w",
            "createdDate": "2024-02-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-17T03:55:07.566Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1394,
        "fields": {
            "title": "The 33",
            "year": "2015",
            "status": "r",
            "createdDate": "2024-02-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-10T12:33:31.032Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1395,
        "fields": {
            "title": "Reign Of Fire",
            "year": "2002",
            "status": "r",
            "createdDate": "2024-02-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-10T13:55:55.149Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1396,
        "fields": {
            "title": "Open Range",
            "year": "2003",
            "status": "r",
            "createdDate": "2024-02-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-16T13:46:26.460Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1398,
        "fields": {
            "title": "Downtown Abbey A New Era",
            "year": "2022",
            "status": "r",
            "createdDate": "2024-02-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-11T02:35:54.182Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1399,
        "fields": {
            "title": "Absolute Power",
            "year": "1997",
            "status": "w",
            "createdDate": "2024-02-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-10T16:03:28.070Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1400,
        "fields": {
            "title": "18 Rin",
            "year": "2009",
            "status": "r",
            "createdDate": "2024-02-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-12T01:25:39.159Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1401,
        "fields": {
            "title": "Quicksand ดูดไปลงนรก",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-02-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-14T02:42:02.724Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1402,
        "fields": {
            "title": "Postman ไปรษณีย์ 4 โลก",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-02-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-13T03:43:50.579Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1403,
        "fields": {
            "title": "Lift ปล้นเหนือเมฆ",
            "year": "2024",
            "status": "w",
            "createdDate": "2024-02-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-12T15:32:52.469Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1404,
        "fields": {
            "title": "Home ความรัก ความสุข ความทรงจำ",
            "year": "2012",
            "status": "r",
            "createdDate": "2024-02-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-14T12:22:01.619Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1405,
        "fields": {
            "title": "Headless Hero 1 ผีหัวขาด 1",
            "year": "2002",
            "status": "r",
            "createdDate": "2024-02-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-14T14:07:34.215Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1406,
        "fields": {
            "title": "Headless Hero 2 ผีหัวขาด 2",
            "year": "2004",
            "status": "r",
            "createdDate": "2024-02-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-14T14:07:44.902Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1407,
        "fields": {
            "title": "From The Ashes จากเถ้าถ่าน",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-02-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-13T10:11:46.341Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1408,
        "fields": {
            "title": "Formalin Man ฟอร์มาลินแมน รักเธอเท่าฟ้า",
            "year": "2004",
            "status": "r",
            "createdDate": "2024-02-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-12T15:58:04.359Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1409,
        "fields": {
            "title": "Equals ฝ่ากฎล้ำ โลกห้ามรัก",
            "year": "2015",
            "status": "r",
            "createdDate": "2024-02-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-13T07:41:09.593Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1410,
        "fields": {
            "title": "Rahtree: Flower Of The Night บุปผาราตรี 1",
            "year": "2003",
            "status": "r",
            "createdDate": "2024-02-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-14T06:37:02.263Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1411,
        "fields": {
            "title": "Rahtree Returns บุปผาราตรี เฟส 2",
            "year": "2005",
            "status": "r",
            "createdDate": "2024-02-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-14T06:37:14.814Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1412,
        "fields": {
            "title": "6/45 Lucky Lotto ลอตโต้วุ่น ลุ้นโชคอลเวงกลางเขตแดนทหาร",
            "year": "2022",
            "status": "r",
            "createdDate": "2024-02-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-15T03:52:08.027Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1413,
        "fields": {
            "title": "Thibaan The Series ไทบ้านเดอะซีรีส์",
            "year": "2017",
            "status": "r",
            "createdDate": "2024-02-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-09T18:05:21.342Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1414,
        "fields": {
            "title": "Thibaan The Series 2.1 ไทบ้านเดอะซีรีส์ 2.1",
            "year": "2018",
            "status": "r",
            "createdDate": "2024-02-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-10T03:20:35.633Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1415,
        "fields": {
            "title": "Thibaan The Series 2.2 ไทบ้านเดอะซีรีส์ 2.2",
            "year": "2018",
            "status": "r",
            "createdDate": "2024-02-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-10T03:20:50.684Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1416,
        "fields": {
            "title": "Thibaan × BNK48 ไทบ้าน × BNK48 จากใจผู้สาวคนนี้",
            "year": "2020",
            "status": "r",
            "createdDate": "2024-02-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-10T03:21:02.282Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1417,
        "fields": {
            "title": "Thibaan × BNK48 ไทบ้าน × BNK48 จากใจผู้สาวคนนี้",
            "year": "2020",
            "status": "r",
            "createdDate": "2024-02-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-10T03:21:17.790Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1418,
        "fields": {
            "title": "Teng's Angel เทวดาท่าจะเท่ง",
            "year": "2008",
            "status": "r",
            "createdDate": "2024-02-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-15T04:18:00.047Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1419,
        "fields": {
            "title": "Bone Tomahawk",
            "year": "2015",
            "status": "r",
            "createdDate": "2024-02-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-09T16:00:04.644Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1420,
        "fields": {
            "title": "Longkhong 1 ลองของ 1",
            "year": "2005",
            "status": "w",
            "createdDate": "2024-02-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-15T07:56:20.137Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1421,
        "fields": {
            "title": "Longkhong 2 ลองของ 2",
            "year": "2008",
            "status": "w",
            "createdDate": "2024-02-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-15T07:56:26.500Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1422,
        "fields": {
            "title": "The Witch Part 2 - The Other One แม่มดมือสังหาร",
            "year": "2022",
            "status": "w",
            "createdDate": "2024-02-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-15T16:06:09.627Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1424,
        "fields": {
            "title": "The Last House on the Left วิมานนรกล่าเดนคน",
            "year": "2009",
            "status": "w",
            "createdDate": "2024-02-14",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-19T07:41:56.097Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1425,
        "fields": {
            "title": "The Gentlemen สุภาพบุรุษมาหากัญ",
            "year": "2020",
            "status": "w",
            "createdDate": "2024-02-14",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-15T16:05:54.607Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1426,
        "fields": {
            "title": "Haunting of the Queen Mary เรือปีศาจ",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-02-14",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-16T06:09:36.666Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1427,
        "fields": {
            "title": "The Undertaker สัปเหร่อ",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-02-14",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-15T08:52:44.096Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1428,
        "fields": {
            "title": "Don't Look at the Demon ฝรั่งเซ่นผี",
            "year": "2022",
            "status": "r",
            "createdDate": "2024-02-16",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-19T03:15:19.062Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1429,
        "fields": {
            "title": "Red Rest",
            "year": "2022",
            "status": "r",
            "createdDate": "2024-02-16",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-19T04:06:31.277Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1430,
        "fields": {
            "title": "The Classic",
            "year": "2003",
            "status": "r",
            "createdDate": "2024-02-16",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-19T05:17:27.831Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1431,
        "fields": {
            "title": "Windstruck",
            "year": "2004",
            "status": "r",
            "createdDate": "2024-02-16",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-19T12:13:02.132Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1432,
        "fields": {
            "title": "Tae Guk Gi The Brotherhood of War เท กึก กี เลือดเนื้อเพื่อฝัน วันสิ้นสงคราม",
            "year": "2004",
            "status": "r",
            "createdDate": "2024-02-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-20T03:44:27.092Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1433,
        "fields": {
            "title": "71 Into The Fire สมรภูมิไฟล้างแผ่นดิน",
            "year": "2010",
            "status": "r",
            "createdDate": "2024-02-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-20T06:30:23.283Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1434,
        "fields": {
            "title": "Kill Me If You Dare ถ้ากล้า ก็ฆ่าเลย",
            "year": "2024",
            "status": "w",
            "createdDate": "2024-02-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-19T15:22:07.848Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1435,
        "fields": {
            "title": "Season of the Witch",
            "year": "2011",
            "status": "r",
            "createdDate": "2024-02-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-20T03:45:11.534Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1436,
        "fields": {
            "title": "G-Force จี-ฟอร์ซ หน่วยจารพันธุ์พิทักษ์โลก",
            "year": "2009",
            "status": "w",
            "createdDate": "2024-02-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-19T14:30:56.573Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1437,
        "fields": {
            "title": "Harry Potter 1 - And The Sorcerer's Stone",
            "year": "2001",
            "status": "w",
            "createdDate": "2024-02-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-19T04:18:05.588Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1438,
        "fields": {
            "title": "Harry Potter 2 - And The Chamber of Secrets",
            "year": "2002",
            "status": "w",
            "createdDate": "2024-02-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-19T04:18:42.468Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1439,
        "fields": {
            "title": "Harry Potter 3 - And The Prisoner of Azkaban",
            "year": "2004",
            "status": "w",
            "createdDate": "2024-02-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-19T04:19:12.125Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1440,
        "fields": {
            "title": "Harry Potter 4 - And The Goblet of Fire",
            "year": "2005",
            "status": "w",
            "createdDate": "2024-02-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-19T04:19:51.165Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1441,
        "fields": {
            "title": "Harry Potter 5 - And The Order of The Phoenix",
            "year": "2007",
            "status": "w",
            "createdDate": "2024-02-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-19T04:20:28.415Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1442,
        "fields": {
            "title": "Harry Potter 6 - And The Half-Blood Prince",
            "year": "2009",
            "status": "w",
            "createdDate": "2024-02-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-19T04:21:06.133Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1443,
        "fields": {
            "title": "Harry Potter 7 - And The Deathly Hallows Part.1",
            "year": "2010",
            "status": "w",
            "createdDate": "2024-02-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-19T04:21:46.114Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1444,
        "fields": {
            "title": "Harry Potter 8 - And The Deathly Hallows Part.2",
            "year": "2011",
            "status": "w",
            "createdDate": "2024-02-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-19T04:22:23.747Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1445,
        "fields": {
            "title": "Malignant มาลิกแนนท์ ชั่วโคตรร้าย",
            "year": "2021",
            "status": "r",
            "createdDate": "2024-02-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-20T14:02:29.353Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1446,
        "fields": {
            "title": "The Abandoned",
            "year": "2006",
            "status": "r",
            "createdDate": "2024-02-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-20T07:36:56.690Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1447,
        "fields": {
            "title": "E-Sarn Tootsie - Part 1 อีสานตุ๊ดซี่",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-02-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-21T14:35:13.706Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1448,
        "fields": {
            "title": "E-Sarn Tootsie - Part 2 อีสานตุ๊ดซี่ ภาค 2",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-02-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-21T14:35:20.580Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1449,
        "fields": {
            "title": "Thirst",
            "year": "2009",
            "status": "r",
            "createdDate": "2024-02-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-22T13:01:01.078Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1450,
        "fields": {
            "title": "Valentine's Day",
            "year": "2010",
            "status": "r",
            "createdDate": "2024-02-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-22T16:13:16.360Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1451,
        "fields": {
            "title": "The Heartbreak Agency คลินิกบำบัดไข้ใจ",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-02-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-23T14:11:40.806Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1452,
        "fields": {
            "title": "Thanksgiving คืนเดือดเชือดขาช็อป",
            "year": "2023",
            "status": "w",
            "createdDate": "2024-02-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-23T13:33:28.329Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1453,
        "fields": {
            "title": "The Bridge Curse Ritual โรงเรียนผีเฮี้ยน",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-02-21",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-23T02:23:37.221Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1454,
        "fields": {
            "title": "The Killer นักฆ่า",
            "year": "2023",
            "status": "w",
            "createdDate": "2024-02-21",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-24T00:16:46.093Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1455,
        "fields": {
            "title": "Special ID",
            "year": "2013",
            "status": "r",
            "createdDate": "2024-02-21",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-24T08:01:34.502Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1456,
        "fields": {
            "title": "Holiday",
            "year": "2016",
            "status": "r",
            "createdDate": "2024-02-21",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-24T04:00:05.321Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1457,
        "fields": {
            "title": "30+ Single on Sale 30+ โสด ON SALE",
            "year": "2011",
            "status": "r",
            "createdDate": "2024-02-21",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-22T04:50:16.261Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1458,
        "fields": {
            "title": "Super Me ยอดมนุษย์สุดโต่ง",
            "year": "2021",
            "status": "r",
            "createdDate": "2024-02-21",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-23T09:21:18.133Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1459,
        "fields": {
            "title": "Mortal Engines",
            "year": "2018",
            "status": "r",
            "createdDate": "2024-02-22",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-24T03:26:23.783Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1460,
        "fields": {
            "title": "Flight of the Phoenix",
            "year": "2004",
            "status": "r",
            "createdDate": "2024-02-23",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-25T08:35:51.341Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1461,
        "fields": {
            "title": "White Tiger เบลียติกร์ สงครามรถถังประจัญบาน",
            "year": "2012",
            "status": "r",
            "createdDate": "2024-02-23",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-24T09:04:51.120Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1462,
        "fields": {
            "title": "Battle Royale เกมนรก โรงเรียนพันธุ์โหด",
            "year": "2000",
            "status": "r",
            "createdDate": "2024-02-23",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-23T03:31:16.586Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1463,
        "fields": {
            "title": "Infernal Affairs 1",
            "year": "2002",
            "status": "r",
            "createdDate": "2024-02-23",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-25T06:29:17.270Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1464,
        "fields": {
            "title": "Infernal Affairs 2",
            "year": "2003",
            "status": "r",
            "createdDate": "2024-02-23",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-25T06:29:22.801Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1465,
        "fields": {
            "title": "Infernal Affairs 3",
            "year": "2003",
            "status": "r",
            "createdDate": "2024-02-23",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-25T06:29:29.424Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1466,
        "fields": {
            "title": "Outlander ไวกิ้ง ปีศาจมังกรไฟ",
            "year": "2008",
            "status": "r",
            "createdDate": "2024-02-23",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-25T06:29:58.203Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1467,
        "fields": {
            "title": "Burn Out ซิ่งท้าทรชน",
            "year": "2017",
            "status": "r",
            "createdDate": "2024-02-24",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-26T04:02:42.358Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1468,
        "fields": {
            "title": "The Art of Raing in the Rain",
            "year": "2019",
            "status": "w",
            "createdDate": "2024-02-24",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-28T14:45:53.036Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1469,
        "fields": {
            "title": "Satan's Slaves",
            "year": "2017",
            "status": "r",
            "createdDate": "2024-02-24",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-28T05:28:08.362Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1470,
        "fields": {
            "title": "Jumper จัมพ์เปอร์ ฅนโดดกระชากมิติ",
            "year": "2008",
            "status": "r",
            "createdDate": "2024-02-24",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-28T02:21:16.297Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1471,
        "fields": {
            "title": "A Tale of Two Sisters ตู้ซ่อนผี ปวดร้าวจนเกินทน",
            "year": "2003",
            "status": "r",
            "createdDate": "2024-02-24",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-27T02:22:34.528Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1472,
        "fields": {
            "title": "The Cave",
            "year": "2005",
            "status": "r",
            "createdDate": "2024-02-24",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-28T14:09:23.067Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1473,
        "fields": {
            "title": "Antichrist",
            "year": "2009",
            "status": "r",
            "createdDate": "2024-02-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-26T13:58:59.097Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1474,
        "fields": {
            "title": "Sniper: Reloaded",
            "year": "2011",
            "status": "r",
            "createdDate": "2024-02-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-28T09:18:04.710Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1475,
        "fields": {
            "title": "Hello Stranger กวน มึน โฮ",
            "year": "2010",
            "status": "w",
            "createdDate": "2024-02-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-26T08:24:53.822Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1476,
        "fields": {
            "title": "Dallas Buyers Club",
            "year": "2013",
            "status": "r",
            "createdDate": "2024-02-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-27T14:56:48.881Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1477,
        "fields": {
            "title": "Black Water",
            "year": "2007",
            "status": "r",
            "createdDate": "2024-02-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-27T09:54:51.224Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1478,
        "fields": {
            "title": "Beneath Still Waters",
            "year": "2005",
            "status": "r",
            "createdDate": "2024-02-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-27T08:04:42.991Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1479,
        "fields": {
            "title": "Mortdecai",
            "year": "2015",
            "status": "w",
            "createdDate": "2024-02-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-28T02:47:47.188Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1480,
        "fields": {
            "title": "I.T.",
            "year": "2016",
            "status": "w",
            "createdDate": "2024-02-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-27T15:43:12.471Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1481,
        "fields": {
            "title": "Let Me Eat Your Pancreas",
            "year": "2017",
            "status": "r",
            "createdDate": "2024-02-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-25T12:45:18.898Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1482,
        "fields": {
            "title": "Mea Culpa ทนายคดีฆ่า",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-02-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-26T05:39:56.895Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1483,
        "fields": {
            "title": "The Sisters ผีช่องแอร์",
            "year": "2004",
            "status": "r",
            "createdDate": "2024-02-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-26T00:48:36.682Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1484,
        "fields": {
            "title": "The Lunchbox เมนูต้องมนต์รัก",
            "year": "2013",
            "status": "r",
            "createdDate": "2024-02-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-26T12:04:00.238Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1485,
        "fields": {
            "title": "Chef เชฟ เติมรสให้เต็มรถ",
            "year": "2014",
            "status": "r",
            "createdDate": "2024-02-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-26T12:03:52.139Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1486,
        "fields": {
            "title": "Burnt เบิร์นท รสชาติความเป็นเชฟ",
            "year": "2015",
            "status": "r",
            "createdDate": "2024-02-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-27T13:33:47.117Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1487,
        "fields": {
            "title": "The Art of Getting By",
            "year": "2011",
            "status": "r",
            "createdDate": "2024-02-26",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-29T12:39:36.148Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1488,
        "fields": {
            "title": "The Devil on Trial พิพากษาปีศาจ",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-02-26",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-29T13:33:00.058Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1489,
        "fields": {
            "title": "Absolutely Anything พลังเพี้ยนเอเลี่ยนส่งข้ามโลก",
            "year": "2015",
            "status": "r",
            "createdDate": "2024-02-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-29T07:49:30.155Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1490,
        "fields": {
            "title": "TAG อวสาน โมเอะ",
            "year": "2015",
            "status": "r",
            "createdDate": "2024-02-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-29T05:32:54.321Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1491,
        "fields": {
            "title": "Luther: The Fallen Sun",
            "year": "2023",
            "status": "w",
            "createdDate": "2024-02-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-29T09:12:02.610Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1492,
        "fields": {
            "title": "Uncharted ผจญภัยล่าขุมทรัพย์สุดขอบโลก",
            "year": "2022",
            "status": "r",
            "createdDate": "2024-02-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-02-29T16:20:39.627Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1493,
        "fields": {
            "title": "A Dog's Way Home เพื่อนรักผจญภัยสี่ร้อยไมล์",
            "year": "2019",
            "status": "r",
            "createdDate": "2024-03-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-18T13:49:11.899Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1495,
        "fields": {
            "title": "Code 8 Part II ล่าคนโคตรพลัง ภาค 2",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-03-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-21T06:12:29.713Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1496,
        "fields": {
            "title": "แมนสรวง Man Suang",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-03-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-21T07:36:59.098Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1497,
        "fields": {
            "title": "Ajoomma คุณป้าซารางเฮ",
            "year": "2022",
            "status": "r",
            "createdDate": "2024-03-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-04T15:11:16.098Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1498,
        "fields": {
            "title": "Love Like the Falling Petals ใบไม้ผลิที่ไม่มีเธอเป็นซากุระ",
            "year": "2022",
            "status": "r",
            "createdDate": "2024-03-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-02T14:56:56.863Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1499,
        "fields": {
            "title": "Destiny The Tale of Kamakura",
            "year": "2017",
            "status": "r",
            "createdDate": "2024-03-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-03T13:10:29.951Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1500,
        "fields": {
            "title": "Drag Me to Hell",
            "year": "2009",
            "status": "r",
            "createdDate": "2024-03-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-03T12:42:43.354Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1502,
        "fields": {
            "title": "Warcraft",
            "year": "2016",
            "status": "r",
            "createdDate": "2024-03-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-01T14:22:57.208Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1503,
        "fields": {
            "title": "14 Blades 8 ดาบทรมาน 6 ดาบสังหาร",
            "year": "2010",
            "status": "r",
            "createdDate": "2024-03-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-04T15:11:00.380Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1504,
        "fields": {
            "title": "Solo: A Star Wars Story",
            "year": "2018",
            "status": "r",
            "createdDate": "2024-03-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-18T15:06:39.214Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1505,
        "fields": {
            "title": "House of Wax บ้านหุ่นผี",
            "year": "2005",
            "status": "w",
            "createdDate": "2024-03-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-03T08:05:43.329Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1506,
        "fields": {
            "title": "The Wall สมรภูมิกำแพงนรก",
            "year": "2017",
            "status": "r",
            "createdDate": "2024-03-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-15T16:16:22.631Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1507,
        "fields": {
            "title": "The Pink Panther 1 มือปราบ เป๋อ ป่วน ฮา",
            "year": "2006",
            "status": "w",
            "createdDate": "2024-03-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-19T13:55:53.213Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1508,
        "fields": {
            "title": "The Pink Panther 2 มือปราบ เป๋อ ป่วน ฮา",
            "year": "2009",
            "status": "w",
            "createdDate": "2024-03-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-19T13:56:07.686Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1509,
        "fields": {
            "title": "The Main Event หนุ่มน้อยเจ้าสังเวียน WWE",
            "year": "2020",
            "status": "r",
            "createdDate": "2024-03-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-21T09:40:42.110Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1510,
        "fields": {
            "title": "Troll",
            "year": "2022",
            "status": "r",
            "createdDate": "2024-03-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-02T13:58:18.710Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1511,
        "fields": {
            "title": "Hostel I นรกรอชำแหละ ภาค 1",
            "year": "2005",
            "status": "w",
            "createdDate": "2024-03-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-03T01:44:59.567Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1512,
        "fields": {
            "title": "Hostel II นรกรอชำแหละ ภาค 2",
            "year": "2007",
            "status": "w",
            "createdDate": "2024-03-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-03T01:45:11.340Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1513,
        "fields": {
            "title": "Hostel III นรกรอชำแหละ ภาค 3",
            "year": "2011",
            "status": "w",
            "createdDate": "2024-03-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-03T01:45:23.957Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1514,
        "fields": {
            "title": "Shoot Em Up ยิงแม่งเลย",
            "year": "2007",
            "status": "r",
            "createdDate": "2024-03-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-19T09:34:45.677Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1515,
        "fields": {
            "title": "300 ขุนศึกพันธุ์สะท้านโลก  ภาค 1",
            "year": "2006",
            "status": "r",
            "createdDate": "2024-03-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-15T06:39:45.579Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1516,
        "fields": {
            "title": "300 Rise Of An Empire มหาศึกกำเนิดอาณาจักร  ภาค 2",
            "year": "2014",
            "status": "r",
            "createdDate": "2024-03-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-15T06:39:58.916Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1517,
        "fields": {
            "title": "Farewell Song เพลงรักเราสามคน",
            "year": "2019",
            "status": "r",
            "createdDate": "2024-03-03",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-10T05:13:24.101Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1518,
        "fields": {
            "title": "The Green Inferno หวีดสุดนรก",
            "year": "2013",
            "status": "r",
            "createdDate": "2024-03-04",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-17T00:56:09.170Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1519,
        "fields": {
            "title": "Martyrs ฝังแค้นรออาฆาต",
            "year": "2008",
            "status": "r",
            "createdDate": "2024-03-04",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-06T13:21:10.604Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1520,
        "fields": {
            "title": "No One Livesโหด...ล่าเหี้ยม",
            "year": "2012",
            "status": "w",
            "createdDate": "2024-03-04",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-19T15:00:54.038Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1521,
        "fields": {
            "title": "Below",
            "year": "2002",
            "status": "r",
            "createdDate": "2024-03-04",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-10T05:04:23.920Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1522,
        "fields": {
            "title": "Scouts Guide To The Zombie Apocalypse",
            "year": "2015",
            "status": "r",
            "createdDate": "2024-03-04",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-19T13:42:34.617Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1523,
        "fields": {
            "title": "Saand Ki Aankh",
            "year": "2019",
            "status": "r",
            "createdDate": "2024-03-04",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-05T12:21:20.441Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1524,
        "fields": {
            "title": "Abduction",
            "year": "2011",
            "status": "r",
            "createdDate": "2024-03-04",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-10T12:11:11.522Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1525,
        "fields": {
            "title": "The Bone Collector",
            "year": "1999",
            "status": "w",
            "createdDate": "2024-03-04",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-05T15:11:11.019Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1526,
        "fields": {
            "title": "Good Kill โดรนพิฆาต ล่าพลิกโลก",
            "year": "2014",
            "status": "r",
            "createdDate": "2024-03-05",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-31T07:13:59.723Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1527,
        "fields": {
            "title": "Lupin the 3rd ลูแปง ยอดโจรกรรมอัจฉริยะ",
            "year": "2014",
            "status": "r",
            "createdDate": "2024-03-05",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-07T14:08:47.581Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1528,
        "fields": {
            "title": "Hunter Killer",
            "year": "2018",
            "status": "r",
            "createdDate": "2024-03-05",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-30T15:25:07.485Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1529,
        "fields": {
            "title": "Our 30 Minute Sessions",
            "year": "2020",
            "status": "r",
            "createdDate": "2024-03-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-06T13:50:30.410Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1530,
        "fields": {
            "title": "John Carter",
            "year": "2012",
            "status": "r",
            "createdDate": "2024-03-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-11T14:33:23.707Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1531,
        "fields": {
            "title": "Life",
            "year": "2017",
            "status": "r",
            "createdDate": "2024-03-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-11T13:36:56.046Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1532,
        "fields": {
            "title": "Before I Fall ตื่นมา ทุกวัน ฉันตาย",
            "year": "2017",
            "status": "r",
            "createdDate": "2024-03-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-10T02:55:55.170Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1533,
        "fields": {
            "title": "How It Ends หายนะวันสิ้นโลก",
            "year": "2018",
            "status": "r",
            "createdDate": "2024-03-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-31T02:57:00.874Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1534,
        "fields": {
            "title": "The Man From Nowhere นักฆ่าฉายาเงียบ",
            "year": "2010",
            "status": "w",
            "createdDate": "2024-03-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-16T15:14:46.436Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1535,
        "fields": {
            "title": "The Guardian วีรบุรุษพันธุ์อึด ฝ่าทะเลเดือด",
            "year": "2006",
            "status": "r",
            "createdDate": "2024-03-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-06T09:35:52.205Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1536,
        "fields": {
            "title": "Beethoven 1 บีโธเฟน ชื่อหมาแต่ไม่ใช่หมา 1",
            "year": "1992",
            "status": "r",
            "createdDate": "2024-03-07",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-09T23:48:29.855Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1537,
        "fields": {
            "title": "Beethoven's 2nd บีโธเฟน ชื่อหมาแต่ไม่ใช่หมา 2",
            "year": "1993",
            "status": "r",
            "createdDate": "2024-03-07",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-09T23:48:35.639Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1538,
        "fields": {
            "title": "Ghost of War",
            "year": "2020",
            "status": "r",
            "createdDate": "2024-03-07",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-31T14:24:30.103Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1539,
        "fields": {
            "title": "The Best of Me",
            "year": "2014",
            "status": "r",
            "createdDate": "2024-03-07",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-17T12:57:47.612Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1540,
        "fields": {
            "title": "Room in Rome",
            "year": "2010",
            "status": "r",
            "createdDate": "2024-03-07",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-08T23:52:23.683Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1541,
        "fields": {
            "title": "Lolita",
            "year": "1997",
            "status": "r",
            "createdDate": "2024-03-07",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-08T14:51:10.245Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1542,
        "fields": {
            "title": "Prometheus",
            "year": "2012",
            "status": "r",
            "createdDate": "2024-03-07",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-07T15:00:15.427Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1543,
        "fields": {
            "title": "Valerian and the City of a Thousand Planets วาเลเรียน พลิกจักรวาล",
            "year": "2017",
            "status": "r",
            "createdDate": "2024-03-09",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-09T15:11:46.699Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1544,
        "fields": {
            "title": "Deliver Us From Evil",
            "year": "2014",
            "status": "r",
            "createdDate": "2024-03-09",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-10T07:55:10.682Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1545,
        "fields": {
            "title": "Spy",
            "year": "2015",
            "status": "w",
            "createdDate": "2024-03-09",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-09T15:13:00.012Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1546,
        "fields": {
            "title": "7 Guardians of the Tomb",
            "year": "2018",
            "status": "r",
            "createdDate": "2024-03-09",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-31T04:12:13.343Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1547,
        "fields": {
            "title": "Push พุช โคตรคนเหนือมนุษย์",
            "year": "2009",
            "status": "r",
            "createdDate": "2024-03-09",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-10T14:03:37.723Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1548,
        "fields": {
            "title": "The Unholy เทวาอาถรรพณ์",
            "year": "2021",
            "status": "r",
            "createdDate": "2024-03-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-18T13:07:09.162Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1549,
        "fields": {
            "title": "Damsel ดรุณีผู้พิชิต",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-03-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-05-07T14:10:42.526Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1550,
        "fields": {
            "title": "Ricky Stanicky ริคกี้ สแตนนิคกี้ เพื่อนซี้กำมะลอ",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-03-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-05-08T12:46:58.926Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1551,
        "fields": {
            "title": "Death is All Around อยากตาย อย่าตาย มรณาคาเฟ่",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-03-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-05-08T14:09:18.950Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1552,
        "fields": {
            "title": "Into the Deep สามซั่มหวีด",
            "year": "2022",
            "status": "r",
            "createdDate": "2024-03-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-05-09T14:31:55.731Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1553,
        "fields": {
            "title": "Ladda Land ลัดดาแลนด์",
            "year": "2011",
            "status": "r",
            "createdDate": "2024-03-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-20T15:35:58.236Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1554,
        "fields": {
            "title": "Day of the Dead วันนรก กัดไม่เหลือซาก",
            "year": "2008",
            "status": "r",
            "createdDate": "2024-03-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-07T13:51:37.336Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1555,
        "fields": {
            "title": "Black Sea ยุทธการฉกขุมทรัพย์ดิ่งนรก",
            "year": "2014",
            "status": "r",
            "createdDate": "2024-03-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-18T13:19:26.473Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1556,
        "fields": {
            "title": "Robin Hood จอมโจรกู้แผ่นดินเดือด",
            "year": "2010",
            "status": "r",
            "createdDate": "2024-03-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-13T14:22:55.007Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1557,
        "fields": {
            "title": "Marrowbone ตระกูลปีศาจ",
            "year": "2017",
            "status": "r",
            "createdDate": "2024-03-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-14T13:23:44.033Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1558,
        "fields": {
            "title": "The Wrath นางอาฆาต",
            "year": "2018",
            "status": "r",
            "createdDate": "2024-03-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-15T13:50:20.548Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1559,
        "fields": {
            "title": "LEGEND OF THE ANCIENT SWORD อภินิหารแหวนครองพิภพสยบฟ้า",
            "year": "2018",
            "status": "r",
            "createdDate": "2024-03-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-19T15:06:48.608Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1560,
        "fields": {
            "title": "The Others คฤหาสน์ สัมผัสผวา",
            "year": "2001",
            "status": "r",
            "createdDate": "2024-03-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-12T15:11:00.446Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1561,
        "fields": {
            "title": "Stolen คนโคตรระห่ำ",
            "year": "2012",
            "status": "w",
            "createdDate": "2024-03-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-13T12:50:34.708Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1562,
        "fields": {
            "title": "Hummingbird คนโคตรระห่ำ",
            "year": "2013",
            "status": "r",
            "createdDate": "2024-03-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-31T02:02:55.302Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1563,
        "fields": {
            "title": "Cirque du Freak The Vampire's Assistant ผจญโลกแวมไพร์มรณะ",
            "year": "2009",
            "status": "r",
            "createdDate": "2024-03-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-13T00:26:02.301Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1564,
        "fields": {
            "title": "DEJA VU เดจา วู ภารกิจเดือด ล่าทะลุเวลา",
            "year": "2006",
            "status": "w",
            "createdDate": "2024-03-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-06T13:01:24.282Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1565,
        "fields": {
            "title": "King Arthur: Legen of the Sword คิงอาร์เธอร์ ตำนานแห่งดาบราชันย์",
            "year": "2017",
            "status": "r",
            "createdDate": "2024-03-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-25T14:04:20.827Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1566,
        "fields": {
            "title": "Mr Jones",
            "year": "2019",
            "status": "r",
            "createdDate": "2024-03-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-15T12:53:56.801Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1567,
        "fields": {
            "title": "Skiptrace คู่ใหญ่สั่งมาฟัด",
            "year": "2016",
            "status": "w",
            "createdDate": "2024-03-15",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-15T13:04:05.371Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1568,
        "fields": {
            "title": "The Collection จับคนมาเชือด",
            "year": "2012",
            "status": "w",
            "createdDate": "2024-03-15",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-15T13:14:56.984Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1569,
        "fields": {
            "title": "Nightcrawler เหยี่ยวข่าวคลั่ง ล่าข่าวโหด",
            "year": "2014",
            "status": "w",
            "createdDate": "2024-03-15",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-15T13:18:45.506Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1570,
        "fields": {
            "title": "Dead Silence อาถรรพ์ผีใบ้",
            "year": "2007",
            "status": "r",
            "createdDate": "2024-03-15",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-07T06:29:17.165Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1571,
        "fields": {
            "title": "Mirrors มันอยู่ในกระจก",
            "year": "2008",
            "status": "r",
            "createdDate": "2024-03-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-29T04:14:36.392Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1572,
        "fields": {
            "title": "Mirrors 2 มันอยู่ในกระจก 2",
            "year": "2010",
            "status": "r",
            "createdDate": "2024-03-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-29T04:14:44.816Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1573,
        "fields": {
            "title": "Not Friends เพื่อน(ไม่)สนิท",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-03-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-05-05T13:50:32.148Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1574,
        "fields": {
            "title": "24 Hours with Gaspar",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-03-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-05-05T15:55:15.408Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1575,
        "fields": {
            "title": "Operation Bangkok เย้ยนรกฉกตัวประกัน",
            "year": "2021",
            "status": "r",
            "createdDate": "2024-03-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-19T06:38:04.645Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1576,
        "fields": {
            "title": "Glass คนเหนือมนุษย์",
            "year": "2019",
            "status": "r",
            "createdDate": "2024-03-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-31T08:16:47.224Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1577,
        "fields": {
            "title": "Vampire Academy มัธยม มหาเวทย์",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-03-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-21T13:28:22.075Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1578,
        "fields": {
            "title": "Furry Vengeance ม็อบหน้าขน ซนซ่าป่วนเมือง",
            "year": "2010",
            "status": "r",
            "createdDate": "2024-03-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-31T15:45:35.328Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1579,
        "fields": {
            "title": "Journey to the West Conquering the Demons ไซอิ๋ว คนเล็กอิทธิฤทธิ์หญ่าย",
            "year": "2013",
            "status": "r",
            "createdDate": "2024-03-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-30T01:30:34.290Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1580,
        "fields": {
            "title": "The Remaining หายนะสูบโลก",
            "year": "2014",
            "status": "r",
            "createdDate": "2024-03-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-26T15:39:59.227Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1581,
        "fields": {
            "title": "Rogue นางสิงห์ระห่ำล่า",
            "year": "2020",
            "status": "r",
            "createdDate": "2024-03-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-27T13:44:53.859Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1582,
        "fields": {
            "title": "The Admiral Roaring Currents ยีซุนชิน ขุนพลคลื่นคำราม",
            "year": "2014",
            "status": "r",
            "createdDate": "2024-03-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-24T09:25:25.007Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1583,
        "fields": {
            "title": "Aftershock 1976 มหาภิบัติสิ้นแผ่นดิน",
            "year": "2010",
            "status": "r",
            "createdDate": "2024-03-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-14T13:43:37.634Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1584,
        "fields": {
            "title": "Ender's Game สงครามพลิกจักรวาล",
            "year": "2013",
            "status": "w",
            "createdDate": "2024-03-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-06T12:59:45.772Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1585,
        "fields": {
            "title": "Death Proof โชเฟอร์บากพญายม",
            "year": "2007",
            "status": "r",
            "createdDate": "2024-03-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-06T13:42:01.257Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1586,
        "fields": {
            "title": "The Ladykillers แผนปล้นมั่ว มุดเหนือเมฆ",
            "year": "2004",
            "status": "r",
            "createdDate": "2024-03-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-24T06:35:16.669Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1587,
        "fields": {
            "title": "Stand Up Guys ไม่อยากเจ็บตัว อย่าหัวเราะปู่",
            "year": "2013",
            "status": "r",
            "createdDate": "2024-03-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-24T08:04:16.755Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1588,
        "fields": {
            "title": "Before I Go to Sleep หลับ ลืม ตื่น ตาย",
            "year": "2014",
            "status": "r",
            "createdDate": "2024-03-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-14T23:24:00.520Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1589,
        "fields": {
            "title": "The Ritual สัมผัสอาฆาต วิญญาณสยอง",
            "year": "2017",
            "status": "r",
            "createdDate": "2024-03-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-26T14:43:18.626Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1590,
        "fields": {
            "title": "The Hunt จับ ล่า ฆ่าโหด",
            "year": "2020",
            "status": "r",
            "createdDate": "2024-03-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-26T13:35:51.890Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1591,
        "fields": {
            "title": "Wish Upon พร-ขอ-ตาย",
            "year": "2017",
            "status": "r",
            "createdDate": "2024-03-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-21T15:18:23.365Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1592,
        "fields": {
            "title": "The Messengers คนเห็นโคตรผี",
            "year": "2007",
            "status": "r",
            "createdDate": "2024-03-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-25T13:52:36.303Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1593,
        "fields": {
            "title": "Day of the Dead: Bloodline วันนรกเดือด มฤตยูซอมบี้สยอง",
            "year": "2018",
            "status": "r",
            "createdDate": "2024-03-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-07T13:51:47.070Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1594,
        "fields": {
            "title": "Timeline ข้ามมิติเวลา ฝ่าวิกฤติอันตราย",
            "year": "2003",
            "status": "r",
            "createdDate": "2024-03-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-23T10:31:36.991Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1595,
        "fields": {
            "title": "Kill the Messenger คนข่าว โค่นทำเนียบ",
            "year": "2014",
            "status": "r",
            "createdDate": "2024-03-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-29T07:55:14.506Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1597,
        "fields": {
            "title": "Boss Level บอสมหากาฬ ฝ่าด่านนรก",
            "year": "2020",
            "status": "r",
            "createdDate": "2024-03-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-17T08:26:39.192Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1598,
        "fields": {
            "title": "Repo Men UNRATED หน่วยนรก ล่าผ่าแหลก",
            "year": "2010",
            "status": "r",
            "createdDate": "2024-03-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-28T12:38:08.146Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1599,
        "fields": {
            "title": "Identity เพชฌฆาตไร้เงา",
            "year": "2003",
            "status": "w",
            "createdDate": "2024-03-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-20T11:17:52.427Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1600,
        "fields": {
            "title": "Assassin's Creed อัสแซสซินส์ ครีด",
            "year": "2016",
            "status": "r",
            "createdDate": "2024-03-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-17T09:07:21.471Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1601,
        "fields": {
            "title": "The Art of the Steal ขบวนการโจรปล้นเหนือเมฆ",
            "year": "2013",
            "status": "r",
            "createdDate": "2024-03-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-24T14:00:21.037Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1602,
        "fields": {
            "title": "Jungle Cruise ผจญภัยล่องป่ามหัศจรรย์",
            "year": "2021",
            "status": "d",
            "createdDate": "2024-03-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-20T11:18:59.377Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1603,
        "fields": {
            "title": "JFK Revisited: Through the Looking Glass",
            "year": "2021",
            "status": "d",
            "createdDate": "2024-03-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-20T11:19:52.565Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1604,
        "fields": {
            "title": "Argylle อาร์ไกล์ ยอดสายลับ",
            "year": "2024",
            "status": "w",
            "createdDate": "2024-03-26",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-05-01T03:31:45.074Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1605,
        "fields": {
            "title": "Dog",
            "year": "2022",
            "status": "r",
            "createdDate": "2024-03-26",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-05-01T09:38:01.607Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1606,
        "fields": {
            "title": "Naked Weapon ผู้หญิงกล้าแกร่งเกินพิกัด",
            "year": "2002",
            "status": "r",
            "createdDate": "2024-03-26",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-28T13:37:46.887Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1607,
        "fields": {
            "title": "Let The Bullet Fly คนท้าใหญ่",
            "year": "2010",
            "status": "r",
            "createdDate": "2024-03-26",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-29T00:19:09.367Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1608,
        "fields": {
            "title": "Kung Fu Monster ยุทธจักรอสูรยักษ์สะท้านฟ้า",
            "year": "2018",
            "status": "r",
            "createdDate": "2024-03-26",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-29T05:36:45.112Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1609,
        "fields": {
            "title": "League of Gods สงครามเทพเจ้า",
            "year": "2016",
            "status": "r",
            "createdDate": "2024-03-26",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-29T08:45:29.809Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1610,
        "fields": {
            "title": "Boat Trip เรือสวรรค์ วุ่นสยิว",
            "year": "2002",
            "status": "r",
            "createdDate": "2024-03-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-25T22:56:15.438Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1611,
        "fields": {
            "title": "400 Days ภารกิจลับมฤตยูใต้โลก",
            "year": "2015",
            "status": "r",
            "createdDate": "2024-03-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-14T06:58:30.017Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1612,
        "fields": {
            "title": "MADAME WEB มาดามเว็บ",
            "year": "2024",
            "status": "w",
            "createdDate": "2024-03-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-28T04:39:23.658Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1613,
        "fields": {
            "title": "Monk Comes Down The Mountain คนเล็กหมัดอรหันต์ ",
            "year": "2015",
            "status": "r",
            "createdDate": "2024-03-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-30T03:55:26.341Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1614,
        "fields": {
            "title": "Xuan Zang เสวียนจ้าง บุรุษพุทธานุภาพ",
            "year": "2016",
            "status": "r",
            "createdDate": "2024-03-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-03-30T05:43:00.714Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1615,
        "fields": {
            "title": "Babylon บาบิลอน",
            "year": "2022",
            "status": "r",
            "createdDate": "2024-03-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-14T08:15:24.312Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1616,
        "fields": {
            "title": "Colonia โคโลเนีย หนีตาย",
            "year": "2016",
            "status": "w",
            "createdDate": "2024-03-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-07T14:45:56.344Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1617,
        "fields": {
            "title": "Concrete Utopia คอนกรีต ยูโทเปีย วิมานกลางนรก",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-04-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-22T12:21:37.555Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1618,
        "fields": {
            "title": "A Chinese Torture Chamber Story 10 เครื่องสังเวยรัก ภาค 1",
            "year": "1994",
            "status": "r",
            "createdDate": "2024-04-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-01T14:46:00.609Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1619,
        "fields": {
            "title": "Daredevil แดร์เดวิล มนุษย์อหังการ์",
            "year": "2003",
            "status": "d",
            "createdDate": "2024-04-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-01T09:47:12.759Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1620,
        "fields": {
            "title": "Cloud Atlas คลาวด์ แอตลาส หยุดโลกข้ามเวลา",
            "year": "2012",
            "status": "r",
            "createdDate": "2024-04-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-10T14:25:12.689Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1621,
        "fields": {
            "title": "Craft Legacy วัยร้าย ร่ายเวทย์",
            "year": "2020",
            "status": "r",
            "createdDate": "2024-04-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-07T23:42:40.140Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1622,
        "fields": {
            "title": "CHAOS หักแผนจารกรรม สะท้านโลก",
            "year": "2005",
            "status": "w",
            "createdDate": "2024-04-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-14T03:06:01.225Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1623,
        "fields": {
            "title": "Arrow The Ultimate Weapon สงครามธนูพิฆาต",
            "year": "2011",
            "status": "r",
            "createdDate": "2024-04-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-14T04:23:04.267Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1624,
        "fields": {
            "title": "The Girl with all the Gifts เชื้อนรกล้างซอมบี้",
            "year": "2016",
            "status": "r",
            "createdDate": "2024-04-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-02T13:06:52.336Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1625,
        "fields": {
            "title": "Hidden Blade โค่นคมพยัคฆ์",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-04-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-05T15:18:40.235Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1628,
        "fields": {
            "title": "Chinese Torture Chamber Story 2 10 เครื่องสังเวยรัก ภาค 2",
            "year": "1998",
            "status": "r",
            "createdDate": "2024-04-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-03T11:57:42.055Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1629,
        "fields": {
            "title": "Chinese Torture Chamber Story 3 10 เครื่องสังเวยรัก ภาค 3",
            "year": "2000",
            "status": "r",
            "createdDate": "2024-04-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-03T11:58:07.282Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1630,
        "fields": {
            "title": "Arnold Is a Model Student อานนเป็นนักเรียนตัวอย่าง",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-04-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-01T12:26:30.023Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1631,
        "fields": {
            "title": "Renfield เรนฟิลด์",
            "year": "2023",
            "status": "w",
            "createdDate": "2024-04-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-21T22:48:38.470Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1632,
        "fields": {
            "title": "Five Nights at Freddy's 5 คืนสยองที่ร้านเฟรดดี้",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-04-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-24T15:22:30.621Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1633,
        "fields": {
            "title": "Thick as Thieves ผ่าแผนปล้น คนเหนือเมฆ",
            "year": "2009",
            "status": "r",
            "createdDate": "2024-04-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-08T15:46:20.627Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1634,
        "fields": {
            "title": "Security โคตรยามอันตราย",
            "year": "2017",
            "status": "r",
            "createdDate": "2024-04-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-09T14:53:44.810Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1635,
        "fields": {
            "title": "The Trust คู่ปล้นตำรวจแสบ",
            "year": "2016",
            "status": "r",
            "createdDate": "2024-04-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-09T13:26:35.857Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1636,
        "fields": {
            "title": "The Legend of Hercules โคตรคน พลังเทพ",
            "year": "2014",
            "status": "r",
            "createdDate": "2024-04-10",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-10T12:48:09.036Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1637,
        "fields": {
            "title": "A Walk Among the Tombstones พลิกเกมนรกล่าสุดโลก",
            "year": "2014",
            "status": "w",
            "createdDate": "2024-04-14",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-15T15:58:49.087Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1638,
        "fields": {
            "title": "Better Watch Out",
            "year": "2016",
            "status": "w",
            "createdDate": "2024-04-14",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-16T04:51:09.336Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1639,
        "fields": {
            "title": "Scoop สกู๊ปสะเทือนโลก",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-04-14",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-06-05T09:57:56.172Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1640,
        "fields": {
            "title": "Huesera The Bone Woman สิงร่างหักกระดูก",
            "year": "2022",
            "status": "r",
            "createdDate": "2024-04-14",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-06-24T14:47:38.766Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1641,
        "fields": {
            "title": "Goosebumps คืนอัศจรรย์ขนหัวลุก 1",
            "year": "2015",
            "status": "w",
            "createdDate": "2024-04-14",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-17T06:27:20.191Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1642,
        "fields": {
            "title": "Ghost Book อัศจรรย์หนังสือดูดวิญญาณ",
            "year": "2022",
            "status": "r",
            "createdDate": "2024-04-14",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-05-28T14:44:53.271Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1643,
        "fields": {
            "title": "Kung Fu Yoga โยคะสู้ฟัด",
            "year": "2017",
            "status": "r",
            "createdDate": "2024-04-14",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-10T13:37:20.733Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1644,
        "fields": {
            "title": "Death Whisperer",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-04-14",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-06-30T14:23:59.558Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1645,
        "fields": {
            "title": "Black and White The Dawn of Assault คู่มหาประลัย อุบัติการณ์ถล่มเมือง",
            "year": "2012",
            "status": "r",
            "createdDate": "2024-04-14",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-09T13:50:02.630Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1646,
        "fields": {
            "title": "Body Cam กล้องซ่อนคดีหลอน",
            "year": "2020",
            "status": "r",
            "createdDate": "2024-04-14",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-16T03:25:57.244Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1647,
        "fields": {
            "title": "City Hunter ใหญ่ไม่ใหญ่ข้าก็ใหญ่",
            "year": "1993",
            "status": "r",
            "createdDate": "2024-04-14",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-05-02T13:56:37.347Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1648,
        "fields": {
            "title": "Duplicity สายลับคู่พิฆาต หักเหลี่ยมจารกรรม",
            "year": "2009",
            "status": "w",
            "createdDate": "2024-04-14",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-15T14:37:20.067Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1649,
        "fields": {
            "title": "No Escape หนีตายฝ่านรกข้ามแดน",
            "year": "2015",
            "status": "w",
            "createdDate": "2024-04-14",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-16T07:46:24.640Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1650,
        "fields": {
            "title": "Once Upon a Time in Shanghai อึ้ง ทึ่ง สู้",
            "year": "2014",
            "status": "w",
            "createdDate": "2024-04-14",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-17T04:41:13.841Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1651,
        "fields": {
            "title": "Winchester",
            "year": "2018",
            "status": "r",
            "createdDate": "2024-04-14",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-17T02:36:06.790Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1652,
        "fields": {
            "title": "Honey Sweet รักโคตรจี๊ดของนายโคตรจืด",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-04-18",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-05-20T15:05:08.192Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1653,
        "fields": {
            "title": "The Secret Kingdom ผจญภัยอาณาจักรมังกร",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-04-18",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-05-21T15:19:58.276Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1654,
        "fields": {
            "title": "Woody Woodpecker Goes to Camp วู้ดดี้ เจ้านกหัวขวาน ไปค่าย",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-04-18",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-05-19T12:07:03.591Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1655,
        "fields": {
            "title": "The Warlords 3 อหังการ์ เจ้าสุริยา",
            "year": "2007",
            "status": "r",
            "createdDate": "2024-04-18",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-18T22:17:53.446Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1656,
        "fields": {
            "title": "Triple Frontier ปล้น ล่า ท้านรก",
            "year": "2019",
            "status": "r",
            "createdDate": "2024-04-18",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-19T04:08:42.845Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1657,
        "fields": {
            "title": "House Party เฮาส์ ปาร์ตี้",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-04-18",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-05-19T14:09:17.571Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1658,
        "fields": {
            "title": "Warriors of Heaven and Earth ขุนพลจ้าวปฐพี",
            "year": "2003",
            "status": "r",
            "createdDate": "2024-04-18",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-19T04:14:36.716Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1659,
        "fields": {
            "title": "Dune Part Two ดูน ภาคสอง",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-04-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-05-12T02:51:05.305Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1660,
        "fields": {
            "title": "Dora and the Lost City of Gold ดอร่า และเมืองทองคำที่สาบสูญ",
            "year": "2019",
            "status": "r",
            "createdDate": "2024-04-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-20T14:28:13.222Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1661,
        "fields": {
            "title": "Rebel Moon - Part Two: The Scargiver ภาค 2: นักรบผู้ตีตรา",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-04-26",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-05-09T14:39:33.753Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1662,
        "fields": {
            "title": "Ghostbusters: Afterlife โกสต์บัสเตอร์ ปลุกพลังล่าท้าผี",
            "year": "2021",
            "status": "r",
            "createdDate": "2024-04-26",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-05-05T09:05:14.357Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1663,
        "fields": {
            "title": "Undercover Punch and Gun ทลายแผนอาชญกรรมระห่ำโลก",
            "year": "2019",
            "status": "r",
            "createdDate": "2024-04-26",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-27T07:52:59.045Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1664,
        "fields": {
            "title": "Teeth กลีบเขมือบ",
            "year": "2007",
            "status": "r",
            "createdDate": "2024-04-29",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-04-29T15:53:15.975Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1665,
        "fields": {
            "title": "Ghostbusters บริษัทกำจัดผี",
            "year": "2016",
            "status": "r",
            "createdDate": "2024-05-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-05-05T09:05:19.507Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1666,
        "fields": {
            "title": "Talk to Me จับ มือ ผี",
            "year": "2022",
            "status": "r",
            "createdDate": "2024-05-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-05-18T15:44:34.947Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1667,
        "fields": {
            "title": "Book Club ก๊วนลับฉบับสาวแซ่บ",
            "year": "2018",
            "status": "r",
            "createdDate": "2024-05-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-05-04T14:50:03.708Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1668,
        "fields": {
            "title": "The Floating Landscape ผู้ชายคนนี้ ที่หัวใจไม่อยากลืม",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-05-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-05-04T13:45:34.498Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1669,
        "fields": {
            "title": "Unfrosted ศึกป๊อปทาร์ต",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-05-05",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-08T15:47:09.813Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1670,
        "fields": {
            "title": "Asteriod City แอสเทอรอยด์ ซิตี้",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-05-05",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-05-13T12:27:26.767Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1671,
        "fields": {
            "title": "It Lives Inside ขังปีศาจคลั่ง",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-05-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-07T14:42:02.322Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1672,
        "fields": {
            "title": "Slyth The Hunt Saga สลิธ โปรเจกต์ล่า",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-05-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-07T12:52:43.409Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1673,
        "fields": {
            "title": "Bad Guy โคตรเลวในดวงใจ",
            "year": "2001",
            "status": "r",
            "createdDate": "2024-05-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-05-14T14:44:55.199Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1674,
        "fields": {
            "title": "Elevator Game ลิฟต์ซ่อนผี",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-05-16",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-07T08:22:29.352Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1675,
        "fields": {
            "title": "Mother of the Bride แม่เจ้าสาว",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-05-16",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-07T06:22:07.797Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1676,
        "fields": {
            "title": "Troy ทรอย",
            "year": "2004",
            "status": "r",
            "createdDate": "2024-05-16",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-05-18T14:12:20.937Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1677,
        "fields": {
            "title": "Sleep หลับ ลึก หลอน",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-05-19",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-07T05:15:06.082Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1678,
        "fields": {
            "title": "Disturbia จ้อง หลอน...ซ่อนเงื่อนผวา",
            "year": "2007",
            "status": "w",
            "createdDate": "2024-05-21",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-06T15:19:56.130Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1679,
        "fields": {
            "title": "Ministry of Ungentlemanly Warfare",
            "year": "2024",
            "status": "w",
            "createdDate": "2024-05-21",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-06T16:20:43.338Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1680,
        "fields": {
            "title": "Kandahar",
            "year": "2023",
            "status": "w",
            "createdDate": "2024-05-21",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-06T13:53:42.753Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1681,
        "fields": {
            "title": "Cyber Heist ล่าอาชญากรไซเบอร์",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-05-21",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-07T01:43:40.907Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1682,
        "fields": {
            "title": "Atlas ล่าข้ามจักรวาล",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-05-28",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-05T14:47:17.229Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1683,
        "fields": {
            "title": "The Adam Project ย้อนเวลาหาอดัม",
            "year": "2022",
            "status": "w",
            "createdDate": "2024-05-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-06-21T15:07:10.743Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1684,
        "fields": {
            "title": "Civil War",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-05-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-05T13:37:13.785Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1685,
        "fields": {
            "title": "The Promise เพื่อนที่ระลึก",
            "year": "2017",
            "status": "w",
            "createdDate": "2024-05-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-06-20T11:21:30.416Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1686,
        "fields": {
            "title": "As the Light Goes Out ทีมดับเพลิงมหากาฬ",
            "year": "2014",
            "status": "r",
            "createdDate": "2024-05-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-06-02T01:56:18.141Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1687,
        "fields": {
            "title": "Great White ฉลามขาว เพชฌฆาต",
            "year": "2021",
            "status": "r",
            "createdDate": "2024-05-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-06-02T00:15:48.633Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1688,
        "fields": {
            "title": "The Outlaws เถื่อน เหนือกฏหมาย",
            "year": "2017",
            "status": "r",
            "createdDate": "2024-06-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-06-12T15:44:39.138Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1689,
        "fields": {
            "title": "Switch คนคมล่าคม",
            "year": "2013",
            "status": "r",
            "createdDate": "2024-06-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-06-12T15:46:00.971Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1690,
        "fields": {
            "title": "Ice Soldiers ไอซ์โซลด์เยอร์ส นักรบเหนือมนุษย์ ",
            "year": "2013",
            "status": "r",
            "createdDate": "2024-06-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-04T15:55:00.371Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1692,
        "fields": {
            "title": "A Part of You ส่วนหนึ่งของเธอ",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-06-05",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-04T12:59:45.123Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1693,
        "fields": {
            "title": "The Blackening เดอะ แบล็คเคนิ่ง",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-06-05",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-03T09:37:01.003Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1694,
        "fields": {
            "title": "The Medallion ฟัดอมตะ",
            "year": "2003",
            "status": "r",
            "createdDate": "2024-06-05",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-06-09T23:09:13.943Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1695,
        "fields": {
            "title": "Wu Kong หงอคง กำเนิดเทพเจ้าวานร",
            "year": "2017",
            "status": "r",
            "createdDate": "2024-06-05",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-06-07T13:18:22.237Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1696,
        "fields": {
            "title": "Body of Lies",
            "year": "2008",
            "status": "w",
            "createdDate": "2024-06-09",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-02T08:50:51.561Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1697,
        "fields": {
            "title": "Our Brand Is Crisis",
            "year": "2015",
            "status": "r",
            "createdDate": "2024-06-09",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-31T12:59:22.780Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1698,
        "fields": {
            "title": "The Price of Nonna's Inheritance มรดกคุณยาย",
            "year": "2024",
            "status": "w",
            "createdDate": "2024-06-09",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-03T08:18:33.633Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1699,
        "fields": {
            "title": "E-Sarn Zombie อีสานซอมบี้",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-06-09",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-31T13:42:11.929Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1700,
        "fields": {
            "title": "Live By Night ลีฟ บาย ไนท์",
            "year": "2016",
            "status": "r",
            "createdDate": "2024-06-09",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-06-10T22:57:12.220Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1701,
        "fields": {
            "title": "The First Omen",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-06-09",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-01T14:35:16.305Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1702,
        "fields": {
            "title": "Big Eyes ติสท์ลวงตา",
            "year": "2014",
            "status": "r",
            "createdDate": "2024-06-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-06-16T10:31:37.055Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1703,
        "fields": {
            "title": "Line Walker ล่าจารชน",
            "year": "2016",
            "status": "r",
            "createdDate": "2024-06-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-06-16T13:15:44.055Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1704,
        "fields": {
            "title": "Villains บ้านซ่อนเพี้ยน",
            "year": "2019",
            "status": "w",
            "createdDate": "2024-06-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-01T13:00:50.262Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1705,
        "fields": {
            "title": "Kill Switch วันหายนะพลิกโลก",
            "year": "2017",
            "status": "r",
            "createdDate": "2024-06-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-06-16T13:05:17.623Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1706,
        "fields": {
            "title": "The Omen อาถรรพณ์กำเนิดซาตานล้างโลก",
            "year": "2006",
            "status": "r",
            "createdDate": "2024-06-18",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-06-20T14:35:57.108Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1707,
        "fields": {
            "title": "Blair Witch ตำนานผีดุ",
            "year": "2016",
            "status": "r",
            "createdDate": "2024-06-18",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-06-20T13:06:24.116Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1708,
        "fields": {
            "title": "How to Have Sex",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-06-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-30T14:13:34.342Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1709,
        "fields": {
            "title": "The Underdoggs ดิ อันเดอร์ด็อกส์ สานฝันตัวกระจอก",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-06-20",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-30T12:17:54.346Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1710,
        "fields": {
            "title": "China Town Cha Cha ไชน่าทาวน์ ชะช่า",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-06-26",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-29T14:00:08.704Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1711,
        "fields": {
            "title": "Flags of Our Fathers สมรภูมิศักดิ์ศรี ปฐพีวีรบุรุษ",
            "year": "2006",
            "status": "r",
            "createdDate": "2024-06-26",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-06-30T08:16:12.738Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1712,
        "fields": {
            "title": "Operation Avalanche ปฏิบัติการลวงโลก",
            "year": "2016",
            "status": "r",
            "createdDate": "2024-06-26",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-06-26T12:54:37.534Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1713,
        "fields": {
            "title": "500 Days of Summer ซัมเมอร์ของฉัน 500 วัน ไม่ลืมเธอ",
            "year": "2009",
            "status": "r",
            "createdDate": "2024-06-26",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-06-30T07:50:21.427Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1714,
        "fields": {
            "title": "Odd Thomas อ็อด โทมัส เห็นความตาย",
            "year": "2013",
            "status": "r",
            "createdDate": "2024-06-26",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-06-29T13:48:35.351Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1715,
        "fields": {
            "title": "Crawlspace คลานระห่ำปะทะเดือด",
            "year": "2022",
            "status": "r",
            "createdDate": "2024-06-27",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-28T15:05:47.811Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1716,
        "fields": {
            "title": "The Last Voyage of the Demeter",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-06-27",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-24T14:30:16.836Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1717,
        "fields": {
            "title": "Gohostbusters: Frozen Empire โกสต์บัสเตอร์ส มหันตภัยเมืองเยือกแข็ง",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-06-27",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-09T00:09:15.715Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1718,
        "fields": {
            "title": "Furiosa: A Mad Max Saga ฟูริโอซ่า : มหากาพย์แมดแม็กซ์",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-06-27",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-15T12:44:18.936Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1719,
        "fields": {
            "title": "Challengers",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-06-27",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-28T12:46:45.569Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1720,
        "fields": {
            "title": "The Loft ห้องเร้นรัก",
            "year": "2014",
            "status": "r",
            "createdDate": "2024-06-27",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-06-28T13:53:39.121Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1721,
        "fields": {
            "title": "Mustang ม้าป่าแสนพยศ",
            "year": "2019",
            "status": "r",
            "createdDate": "2024-06-27",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-06-28T14:49:13.527Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1722,
        "fields": {
            "title": "Metamorphosis",
            "year": "2019",
            "status": "r",
            "createdDate": "2024-06-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-13T09:10:06.925Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1723,
        "fields": {
            "title": "Tarot",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-06-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-13T08:05:18.188Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1724,
        "fields": {
            "title": "A Family Affair",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-06-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-12T14:17:06.471Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1725,
        "fields": {
            "title": "The Watchers",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-07-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-12T13:19:00.184Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1726,
        "fields": {
            "title": "Badland Hunter",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-07-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-13T08:05:23.596Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1727,
        "fields": {
            "title": "The Secret We Keep ขัง แค้น บริสุทธิ์",
            "year": "2020",
            "status": "r",
            "createdDate": "2024-07-01",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-04T10:15:58.024Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1728,
        "fields": {
            "title": "Love Reset 30 วันโคตร(เกลียด)เธอเลย",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-07-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-08T13:43:32.884Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1729,
        "fields": {
            "title": "The Roudup 4 Punishment",
            "year": "2024",
            "status": "w",
            "createdDate": "2024-07-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-09T01:30:47.683Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1730,
        "fields": {
            "title": "Pattaya Heat ปิดเมืองล่า",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-07-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-09T03:35:36.132Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1731,
        "fields": {
            "title": "The Fall Guy",
            "year": "2024",
            "status": "w",
            "createdDate": "2024-07-08",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-15T10:37:15.066Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1732,
        "fields": {
            "title": "Fury วันปฐพีเดือด",
            "year": "2014",
            "status": "r",
            "createdDate": "2024-07-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-12T11:24:37.146Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1733,
        "fields": {
            "title": "Tyler Perry's Divorce in the Black รัก ร้าง ร้าว เรื่องราวของไทเลอ",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-07-15",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-05T12:56:36.904Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1734,
        "fields": {
            "title": "Project Almanac กล้า ซ่าส์ ท้าเวลา",
            "year": "2015",
            "status": "r",
            "createdDate": "2024-07-15",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-24T12:35:23.491Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1735,
        "fields": {
            "title": "Freelance",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-07-15",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-05T15:53:10.321Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1736,
        "fields": {
            "title": "Happy Death Day 2U สุขสันต์วันตาย 2U",
            "year": "2019",
            "status": "r",
            "createdDate": "2024-07-15",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-16T13:54:41.187Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1737,
        "fields": {
            "title": "IF",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-07-15",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-08T15:39:18.857Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1738,
        "fields": {
            "title": "Blame the Game",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-07-15",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-04T15:05:05.748Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1739,
        "fields": {
            "title": "Project Gutenberg เกมหักเหลี่ยม เฉือนคม",
            "year": "2018",
            "status": "r",
            "createdDate": "2024-07-15",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-23T15:08:56.632Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1740,
        "fields": {
            "title": "Dredd เดร็ด คนหน้ากากทมิฬ",
            "year": "2012",
            "status": "r",
            "createdDate": "2024-07-15",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-16T14:01:05.645Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1741,
        "fields": {
            "title": "Deepwater Horizon ฝ่าวิบัติเพลิงนรก",
            "year": "2016",
            "status": "r",
            "createdDate": "2024-07-24",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-24T10:46:38.204Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1742,
        "fields": {
            "title": "Shaolin เส้าหลิน สองใหญ่",
            "year": "2011",
            "status": "r",
            "createdDate": "2024-07-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-25T15:51:57.515Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1743,
        "fields": {
            "title": "My Spy The Eternal City พยัคฆ์ร้าย สปายแสบ:คู่ป่วนตะลุยเมืองศักดิ์สิทธ์",
            "year": "2024",
            "status": "w",
            "createdDate": "2024-07-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-04T05:15:34.709Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1744,
        "fields": {
            "title": "Anyone But You",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-07-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-04T03:06:43.769Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1745,
        "fields": {
            "title": "Bad Boys : Ride or Die",
            "year": "2024",
            "status": "w",
            "createdDate": "2024-07-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-04T07:01:50.931Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1746,
        "fields": {
            "title": "Shinjuku Incident",
            "year": "2009",
            "status": "r",
            "createdDate": "2024-07-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-03T16:43:43.596Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1747,
        "fields": {
            "title": "Under Paris มฤตยูใต้ปารีส",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-07-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-04T08:54:59.644Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1748,
        "fields": {
            "title": "Invisible Target อึด ฟัด อัด ถล่มเมืองตำรวจ",
            "year": "2007",
            "status": "r",
            "createdDate": "2024-07-25",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-28T06:00:23.576Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1749,
        "fields": {
            "title": "Ghostbusters: Frozen Empire",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-07-28",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-07-28T09:57:43.334Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1750,
        "fields": {
            "title": "Die Hart 2 Die Harter",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-07-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-03T15:08:57.801Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1751,
        "fields": {
            "title": "End of the Road สุดปลายถนน",
            "year": "2022",
            "status": "r",
            "createdDate": "2024-07-30",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-04T13:37:52.280Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1752,
        "fields": {
            "title": "The Blade of Wind ดาบตัดวายุ",
            "year": "2020",
            "status": "r",
            "createdDate": "2024-07-31",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-02T12:09:38.328Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1753,
        "fields": {
            "title": "Failure to Launch",
            "year": "2006",
            "status": "r",
            "createdDate": "2024-08-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-04T02:06:48.642Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1754,
        "fields": {
            "title": "Antigang aka The Squad หน่วยตำรวจระห่ำ",
            "year": "2015",
            "status": "r",
            "createdDate": "2024-08-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-03T13:43:58.177Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1755,
        "fields": {
            "title": "The Greate Wall เดอะ เกรท วอลล์",
            "year": "2016",
            "status": "r",
            "createdDate": "2024-08-02",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-02T13:43:42.737Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1756,
        "fields": {
            "title": "A Quiet Place Day One",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-08-04",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-09T14:59:48.646Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1757,
        "fields": {
            "title": "The Unseeable เปนชู้กับผี",
            "year": "2006",
            "status": "r",
            "createdDate": "2024-08-04",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-10T03:16:21.551Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1758,
        "fields": {
            "title": "Moei the Promised เหมรฺย",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-08-04",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-10T05:18:05.431Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1759,
        "fields": {
            "title": "Are You There God? It's Me, Margaret วันนั้น ของมาร์กาเร็ต",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-08-04",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-09T13:51:07.871Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1760,
        "fields": {
            "title": "The Bricklayer จารชนคนพันธุ์เดือด",
            "year": "2023",
            "status": "w",
            "createdDate": "2024-08-05",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-09T08:37:16.565Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1761,
        "fields": {
            "title": "The White Storm 3 Heaven Or Hell คนอันตรายล่าข้ามโลก 3",
            "year": "2023",
            "status": "r",
            "createdDate": "2024-08-06",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-09T05:07:09.875Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1762,
        "fields": {
            "title": "Alice, Darling",
            "year": "2022",
            "status": "r",
            "createdDate": "2024-08-10",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-10T07:11:56.794Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1763,
        "fields": {
            "title": "One Fast Move วันฟาสต์มูฟ",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-08-10",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-10T14:22:38.727Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1764,
        "fields": {
            "title": "Double Trouble พ่อสั่งมาฟัด",
            "year": "2012",
            "status": "r",
            "createdDate": "2024-08-10",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-10T15:02:30.365Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1765,
        "fields": {
            "title": "Wonderland",
            "year": "2024",
            "status": "r",
            "createdDate": "2024-08-10",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-11T03:34:39.346Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1766,
        "fields": {
            "title": "Kill Chain โคตรโจรอันตราย",
            "year": "2019",
            "status": "r",
            "createdDate": "2024-08-11",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-11T12:54:26.793Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1767,
        "fields": {
            "title": "Cashback คืนฝันมหัศจรรย์จินตนาการ",
            "year": "2006",
            "status": "r",
            "createdDate": "2024-08-11",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-11T02:04:56.571Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1769,
        "fields": {
            "title": "Sweet Girl สวีทเกิร์ล",
            "year": "2021",
            "status": "r",
            "createdDate": "2024-08-12",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-12T23:59:20.210Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1770,
        "fields": {
            "title": "Road to Paloma ถนนคนแค้น",
            "year": "2014",
            "status": "w",
            "createdDate": "2024-08-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-13T00:05:27.452Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1771,
        "fields": {
            "title": "Red Down หน่วยรบพันธุ์สายฟ้า",
            "year": "2012",
            "status": "r",
            "createdDate": "2024-08-13",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-13T00:05:35.636Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1772,
        "fields": {
            "title": "Road to Paloma",
            "year": "2014",
            "status": "r",
            "createdDate": "2024-08-14",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-14T13:24:28.407Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1773,
        "fields": {
            "title": "The Roundup 3 No Way Out",
            "year": "2023",
            "status": "d",
            "createdDate": "2024-08-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-17T01:58:31.454Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1774,
        "fields": {
            "title": "Fly Me to the Moon",
            "year": "2024",
            "status": "d",
            "createdDate": "2024-08-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-17T01:58:44.095Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1775,
        "fields": {
            "title": "Bullet Head หักโหดชะตากรรมสยอง",
            "year": "2017",
            "status": "d",
            "createdDate": "2024-08-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-17T01:58:55.366Z"
        }
    },
    {
        "model": "matabase.matabase",
        "pk": 1776,
        "fields": {
            "title": "The Illusionist มายากลเขย่าบัลลังก์",
            "year": "2006",
            "status": "d",
            "createdDate": "2024-08-17",
            "createdUser": 1,
            "updatedUser": 1,
            "updatedDate": "2024-08-17T01:59:07.949Z"
        }
    }
]
"""

class Footer(models.Model):
    footerCategory = [('stack', 'stack'), ('links', 'links'), ('developer', 'developer')]
    category = models.CharField(max_length=25, choices=footerCategory)
    title = models.CharField(max_length=25)
    icon = models.CharField(max_length=100, null=True, blank=True)
    link = models.URLField(max_length=255, null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['category', 'title', 'link'], name='uniqueFooter')
        ]

    def __str__(self):
        return self.title

"""
[{"model": "matabase.footer", "pk": 1, "fields": {"category": "stack", "title": "Django", "icon": "browser-chrome", "link": "https://www.djangoproject.com/"}}, {"model": "matabase.footer", "pk": 2, "fields": {"category": "stack", "title": "Bootstrap", "icon": "bootstrap", "link": "https://getbootstrap.com/"}}, {"model": "matabase.footer", "pk": 3, "fields": {"category": "stack", "title": "Sqlite", "icon": "database", "link": "https://www.sqlite.org/index.html"}}, {"model": "matabase.footer", "pk": 4, "fields": {"category": "stack", "title": "PythonAnywhere", "icon": "filetype-py", "link": "https://www.pythonanywhere.com/"}}, {"model": "matabase.footer", "pk": 5, "fields": {"category": "links", "title": "lanuxos", "icon": "link", "link": "https://lanuxos.github.io/"}}, {"model": "matabase.footer", "pk": 6, "fields": {"category": "developer", "title": "Email", "icon": "envelope-at", "link": "http://lanuxos@gmail.com"}}, {"model": "matabase.footer", "pk": 7, "fields": {"category": "developer", "title": "Github", "icon": "github", "link": "https://github.com/lanuxos"}}]
"""

# class Mag(models.Model):
#     '''
#     action, adventure, animated,
#     comedy, crime,
#     drama, detective, documentary,
#     epics,
#     fantasy,
#     gangster,
#     historical, horror,
#     musical, mystery,
#     noir,
#     period,
#     romance,
#     science fiction, superhero, supernatural
#     thriller,
#     war, western,
#     zombie,
#     '''
#     magReference = models.ForeignKey(Matabase, on_delete= models.CASCADE)
#     mag = models.CharField(max_length=50)

#     class Meta:
#         ordering = ['magReference']

#     def __str__(self):
#         return f'{self.magReference.title} [{self.mag}]'
