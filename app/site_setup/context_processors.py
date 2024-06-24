from site_setup.models import SiteSetup

#def site_setup_test(request):
#    return {
#        'exemple': 'exemple de merda'
#    }

def site_setup(request):
    site_setup = SiteSetup.objects.order_by('-id').first()
    return {
        'site_setup': site_setup
    }