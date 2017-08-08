import os
import re
import django
from django.core.wsgi import get_wsgi_application
from django.utils import timezone


os.environ['DJANGO_SETTINGS_MODULE'] = 'Tr.settings'
application = get_wsgi_application()


from TrDisplay.models import TrClass

if __name__ == '__main__':
<<<<<<< HEAD
    
=======
>>>>>>> efe4ad104ff3535595cc075654c5eceef38656d4
    Tr = TrClass()
    EmailData = open('/mnt/c/Users/knoah/Desktop/EmailEx.txt', 'r').read()
    TR_NUMB = re.search('TR NUMBER:\s+([0-9]+)', EmailData).group(1)
    From_Team = re.search('FROM TEAM:\s+(.*)', EmailData).group(1)
    print(TR_NUMB)

    Tr.Tr_NO = TR_NUMB
    Tr.FromTeam = From_Team
    Tr.Pub_date = timezone.now()

    Tr.save()

