from django.shortcuts import render_to_response
def cookiebeleid(request):
	return render_to_response('cookiebeleid.html')

def disclaimer(request):
	return render_to_response('disclaimer.html')
