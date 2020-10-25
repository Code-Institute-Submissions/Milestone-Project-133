from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfiles
from .forms import UserProfilesForm

from payment.models import DrinkOrder


def user_profiles(request):
    # displays user profiles
    profile = get_object_or_404(UserProfiles, user=request.user)
    if request.method == 'POST':
        form = UserProfilesForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has successfully updated!")

    form = UserProfilesForm(instance=profile)
    drink_orders = profile.drink_orders.all()
    print(drink_orders)
    template = "user_profiles/user_profiles.html"
    context = {
        "form": form,
        "drink_orders": drink_orders,
    }

    return render(request, template, context)


def drink_order_history(request, drink_order_number):
    drink_order = get_object_or_404(
        DrinkOrder, drink_order_number=drink_order_number)

    messages.info(
        request, (f"This is a past confirmation for drink order number {drink_order_number}. \
            A confirmation email was sent on the order date."))

    template = "payment/payment_success.html"
    context = {
        "drink_order": drink_order,
        "taken_from_user_profiles": True,
    }

    return render(request, template, context)
