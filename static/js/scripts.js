$(document).ready(function () {

    // smooth scroll to screen top using arrow
    $(".back-to-top-link").click(function () {
        window.scrollTo({
            top: 0,
            behavior: "smooth",
        });
    });

    // shows or hides back to top arrow
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $(".fixed-arrow").show();
        } else {
            $(".fixed-arrow").hide();
        }
    });

    // to update drink quantity
    $(".edit-btn").click(function () {
        let editForm = $(this).parent();
        editForm.submit();
    });

    // stripe elements
    let stripePublicKey = $("#id_stripe_public_key").text().slice(1, -1);
    let clientSecret = $("#id_client_secret").text().slice(1, -1);
    let stripe = Stripe(stripePublicKey);
    let elements = stripe.elements();
    let style = {
        base: {
            color: "#212529",
            fontFamily: "sans-serif",
            src: "local('Montserrat Regular'), local('Montserrat-Regular'), url(https://fonts.gstatic.com/s/montserrat/v15/JTUSjIg1_i6t8kCHKm459WRhyyTh89ZNpQ.woff2) format('woff2')", //delete if not used
            fontSmoothing: "antialiased",
            fontSize: "16px",
            "::placeholder": {
                color: "#495057",
            },
        },
        invalid: {
            color: "red",
            iconColor: "red",
        },
    };

    let card = elements.create("card", { style: style });
    card.mount("#stripeCard");

    // deals with card validation errors 
    card.addEventListener("change", function (event) {
        let errorDiv = document.getElementById("stripeCardErrors");
            if (event.error) {
                let html = `
                    <span>
                        <i class="fas fa-times"></i>
                    </span>
                    <span>${event.error.message}</span>`;
                $(errorDiv).html(html);
            } else {
                errorDiv.textContent = "";
            }
    });

    // deals with card form submit
    let form = document.getElementById("paymentForm");

    form.addEventListener("submit", function (ev) {
        ev.preventDefault();
        card.update({ "disabled": true });
        $("#stripeFormSubmit").attr("disabled", true);
         $("#paymentForm").fadeToggle(100);
         $("#loadingOverlay").fadeToggle(100);

        let saveInfo = Boolean($("#saveInfo").attr("checked"));
        // from using {% csrf_token %} in the form
        let csrfToken = $("input[name='csrfmiddlewaretoken']").val();
        let postData = {
            "csrfmiddlewaretoken": csrfToken,
            "client_secret": clientSecret,
            "save_info": saveInfo,
        };

        let url = "/payment/cache_payment_data/";

        $.post(url, postData).done(function () {
            stripe.confirmCardPayment(clientSecret, {
                payment_method: {
                    card: card,
                    billing_details: {
                        name: $.trim(form.full_name.value),
                        email: $.trim(form.email.value),
                        phone: $.trim(form.phone_number.value),
                        address:{
                            line1: $.trim(form.street_address1.value),
                            line2: $.trim(form.street_address2.value),
                            country: $.trim(form.country.value),
                        }
                    }
                },
                shipping:{
                        name: $.trim(form.full_name.value),
                        phone: $.trim(form.phone_number.value),
                        address:{
                            line1: $.trim(form.street_address1.value),
                            line2: $.trim(form.street_address2.value),
                            postal_code: $.trim(form.postcode.value),
                            country: $.trim(form.country.value),
                        }
                    },                
                }).then(function (result) {
                    if (result.error) {            
                        let errorDiv = document.getElementById("stripeCardErrors");
                        let html = `<span>
                                        <i class="fas fa-times"></i>
                                    </span>
                                    <span>${result.error.message}</span>`;
                        $(errorDiv).html(html);
                        $("#paymentForm").fadeToggle(100);
                        $("#loadingOverlay").fadeToggle(100);
                        card.update({ "disabled": false });
                        $("#stripeFormSubmit").attr("disabled", false);
                    } else {
                        if (result.paymentIntent.status === "succeeded") {
                                form.submit();
                            }
                        }
                    });
                }).fail(function () {      
                    // just reload the page, the error will be in django messages
                    location.reload();
                })
    });

});
