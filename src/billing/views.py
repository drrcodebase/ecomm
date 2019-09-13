from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from billing.models import BillingProfile, Card

# Create your views here.
import stripe

STRIPE_SECRET_KEY =  getattr(settings, "STRIPE_SECRET_KEY", "sk_test_1DmqaYwt3fedT3KaMyYdk5sC0000Dy4w1y")
STRIPE_PUB_KEY =  getattr(settings, "STRIPE_PUB_KEY", "pk_test_EDCTIuVjYC158QsPGshh2AGZ00SCgAQHBk")
stripe.api_key = STRIPE_SECRET_KEY


def payment_method_view(request):

    # if request.user.is_authenticated():
    #     billing_profile = request.user.billingprofile
    #     my_customer_id = billing_profile.customer_id

    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    if not billing_profile:
        return redirect("/cart")
    next_url = None
    next_ = request.GET.get('next')
    if is_safe_url(next_, request.get_host()):
        next_url =next_
    return render(request, 'billing/payment-method.html', {"publish_key": STRIPE_PUB_KEY, "next_url":next_url })

def payment_method_createview(request):
    print("create view called")
    if request.method == "POST" and request.is_ajax():
        billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
        if not billing_profile:
            return HttpResponse({"message":" Can not find this User "}, status_code=401)
        token = request.POST.get("token")
        if token is not None:
            # customer = stripe.Customer.retrieve(billing_profile.customer_id)
            # card_response = customer.sources.create(source=token)
            # # new_card_object = Card.objects.add_new(billing_profile, card_response)
            new_card_object = Card.objects.add_new(billing_profile, token)
        return JsonResponse({"message": "Success ! your card as added ."})
    return HttpResponse("error", status_code=401)
