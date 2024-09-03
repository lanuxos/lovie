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

    class Meta:
        ordering = ['-createdDate', 'title']
        # constraints = [
        #     models.UniqueConstraint(
        #         fields=['title', 'year'], name='uniqueDB')
        # ]
    
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        return self.title + " [" + str(self.year) + "]"


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
