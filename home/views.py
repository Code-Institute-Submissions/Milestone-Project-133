from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Drink, About_us
from .forms import DrinkForm, AboutUsForm


def home(request):

    new_drinks = Drink.objects.filter(drink_type=1)
    juices = Drink.objects.filter(drink_type=2)
    milkshakes = Drink.objects.filter(drink_type=3)
    main_mission = About_us.objects.filter(section=1)
    sub_mission = About_us.objects.filter(section=2)

    searched_drinks = Drink.objects.exclude(drink_type=1)
    drink_search = None
    drink_search_results = ""

    sort = None
    direction = None

    if request.GET:

        if "sort" in request.GET:
            sort_key = request.GET["sort"]
            sort = sort_key
            sort_key == "price"

            if sort_key == "drink_name":
                sort_key == "lower_case_name"
                new_drinks = new_drinks.annotate(
                    lower_case_name=Lower("drink_name"))
                juices = juices.annotate(lower_case_name=Lower("drink_name"))
                milkshakes = milkshakes.annotate(
                    lower_case_name=Lower("drink_name"))
                searched_drinks = searched_drinks.annotate(
                    lower_case_name=Lower("drink_name"))

            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sort_key = f"-{sort_key}"
            new_drinks = new_drinks.order_by(sort_key)
            juices = juices.order_by(sort_key)
            milkshakes = milkshakes.order_by(sort_key)
            searched_drinks = searched_drinks.order_by(sort_key)

        if "search" in request.GET:
            drink_search = request.GET["search"]
            drink_search_results = searched_drinks.filter(
                Q(drink_name__icontains=drink_search))

    drink_sorting = f"{sort}_{direction}"

    context = {
        "new_drinks": new_drinks,
        "juices": juices,
        "milkshakes": milkshakes,
        "main_mission": main_mission,
        "sub_mission": sub_mission,
        "drink_search_results": drink_search_results,
        "typed_in_search": drink_search,
        "drink_sorting": drink_sorting,
        "this_is_the_homepage":  True,
    }

    # shows homepage
    return render(request, "home/index.html", context)


@login_required
def add_drink(request):
    # adds drinks to shop
    if not request.user.is_superuser:
        messages.error(
            request, "Access Denied. \
                Access restricted to administrators only.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = DrinkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Drink successfully added!")
            return redirect(reverse("add_drink"))
        else:
            messages.error(request,
                           "Failed to add drink. Please \
                                ensure the form is valid.")
    else:
        form = DrinkForm()

    template = "home/add_drink.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def edit_drink(request, drink_id):
    # edits drinks in shop
    if not request.user.is_superuser:
        messages.error(
            request, "Access Denied. \
                Access restricted to administrators only.")
        return redirect(reverse("home"))

    drink = get_object_or_404(Drink, pk=drink_id)
    if request.method == "POST":
        form = DrinkForm(request.POST, request.FILES, instance=drink)
        if form.is_valid():
            form.save()
            messages.success(request, "Drink successfully edited!")
            return redirect(reverse("home"))
        else:
            messages.error(request, "Failed to edit drink. \
                 Please ensure the form is valid.")
    else:
        form = DrinkForm(instance=drink)
        messages.info(request, f"You are editing \
             {drink.drink_name.capitalize()}.")

    template = "home/edit_drink.html"
    context = {
        "form": form,
        "drink": drink,
    }

    return render(request, template, context)


@login_required
def delete_drink(request, drink_id):
    # deletes drinks from shop
    if not request.user.is_superuser:
        messages.error(
            request, "Access Denied. \
                Access restricted to administrators only.")
        return redirect(reverse("home"))

    drink = get_object_or_404(Drink, pk=drink_id)
    drink.delete()
    messages.success(request, "Drink deleted!")

    return redirect(reverse("home"))


@login_required
def append_about_us(request):
    # adds about us section
    if not request.user.is_superuser:
        messages.error(
            request, "Access Denied. \
                Access restricted to administrators only.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = AboutUsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Mission statement section successfully added!")
            return redirect(reverse("append_about_us"))
        else:
            messages.error(request,
                           "Failed to add mission statement section. Please \
                                ensure the form is valid.")
    else:
        form = AboutUsForm()

    template = "home/append_about_us.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def change_about_us(request, about_us_id):
    # edits about us section
    if not request.user.is_superuser:
        messages.error(
            request, "Access Denied. \
                Access restricted to administrators only.")
        return redirect(reverse("home"))

    about_us = get_object_or_404(About_us, pk=about_us_id)
    if request.method == "POST":
        form = AboutUsForm(
            request.POST, request.FILES, instance=about_us)
        if form.is_valid():
            form.save()
            messages.success(request,
                             "Mission statement section successfully updated!")
            return redirect(reverse("home"))
        else:
            messages.error(request, f'Failed to update the: "{about_us.title}" section. \
                 Please ensure the form is valid.')
    else:
        form = AboutUsForm(instance=about_us)
        messages.info(
            request, f'You are editing the: "{about_us.title}" \
            section.')

    template = "home/edit_about_us.html"
    context = {
        "form": form,
        "about_us": about_us,
    }

    return render(request, template, context)


@login_required
def remove_about_us(request, about_us_id):
    # deletes about us section
    if not request.user.is_superuser:
        messages.error(
            request, "Access Denied. \
                Access restricted to administrators only.")
        return redirect(reverse("home"))

    about_us = get_object_or_404(About_us, pk=about_us_id)
    about_us.delete()
    messages.success(request, "Mission statement section deleted!")

    return redirect(reverse("home"))
