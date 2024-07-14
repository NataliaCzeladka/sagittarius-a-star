# TESTING

Return back to the [README.md](README.md) file.

## Introduction

Software testing is a common practice and a crucial step in the development process that ensures the quality, functionality and reliability of a web application. There are two primary approaches to testing - manual and automated. They both play vital roles in the process.

Both manual and automated testing have their strengths and limitations, but let's focus on the strengths. Manual testing offers flexibility and human insight, while automated testing provides efficiency and repeatability. Combining these two approaches can help achieve comprehensive test coverage.

### Manual Testing

Manual Testing involves human testers who interact with the software and assess its behavior against predefined criteria. This method relies on the tester's intuition, experience, and creativity to identify defects, making it particularly effective in exploratory testing and scenarios where user interaction is complex or subjective. 

"Sagittarius A-Star: A Supermassive Book Store" has been tested manually to check if the project works according to the user stories, to check its performance in different browsers and to check its responsiveness at different resolutions. Some friends and family members were invited to test the app on their devices and to check for potential functionality issues.

### Automated Testing

Automated Testing, on the other hand, employs specialized testing tools and scripts to automate the execution of test cases and verification of results. It excels in repetitive, time-consuming, and regression testing scenarios, where the same tests need to be run repeatedly to ensure new code changes do not introduce defects. 

All tests described and documented in the Code Validation and the Lighthouse Audit sections are automated tests.

## Code Validation

[The W3C Markup Validation Service](https://validator.w3.org/) and [The W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) were used to validate every page of the project to ensure there were no syntax errors. The results clearly showed that the website stays in compliance with the standards and recommendations set by the World Wide Web Consortium.

[JSHint](https://jshint.com/), a static code analysis tool, was used to check if JavaScript source code complies with coding rules. No errors were found in this area. And finally, I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate my Python file.

### HTML Validation

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files. No errors or warnings were found. Django allauth templates were not tested. Pages that required user authentication were validated by direct input.

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsagittarius-a-star-ab236042b163.herokuapp.com%2F) | ![home page validation](docs/validation/validate_html_home.png) | Pass: No Errors |
| Products | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsagittarius-a-star-ab236042b163.herokuapp.com%2Fproducts%2F) | ![products page validation](docs/validation/validate_html_products.png) | Pass: No Errors |
| Product Detail | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsagittarius-a-star-ab236042b163.herokuapp.com%2Fproducts%2F2%2F) | ![product detail page validation](docs/validation/validate_html_product_detail.png) | Pass: No Errors |
| Add Product | [W3C](https://validator.w3.org/nu/#textarea) | ![add product page validation](docs/validation/validate_html_add_product.png) | Pass: No Errors |
| Edit Product | [W3C](https://validator.w3.org/nu/#textarea) | ![edit product page validation](docs/validation/validate_html_edit_product.png) | Pass: No Errors |
| Bag | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsagittarius-a-star-ab236042b163.herokuapp.com%2Fbag%2F) | ![shopping bag page validation](docs/validation/validate_html_bag.png) | Pass: No Errors |
| Checkout | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsagittarius-a-star-ab236042b163.herokuapp.com%2Fcheckout%2F) | ![checkout page validation](docs/validation/validate_html_checkout.png) | Pass: No Errors |
| Checkout Success | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsagittarius-a-star-ab236042b163.herokuapp.com%2Fcheckout%2Fcheckout_success%2F2541D772F60543C38B84B7BA09FCA42B) | ![checkout success page validation](docs/validation/validate_html_checkout_success.png) | Pass: No Errors |
| User Profile | [W3C](https://validator.w3.org/nu/#textarea) | ![user profile page validation](docs/validation/validate_html_profile.png) | Pass: No Errors |
| Contact | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsagittarius-a-star-ab236042b163.herokuapp.com%2Fcontact%2F) | ![contact page validation](docs/validation/validate_html_contact.png) | Pass: No Errors |

### CSS Validation

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate my CSS files. No errors were found.

| File | Screenshot | Notes |
| --- | --- | --- |
| base.css | ![base.css validation](docs/validation/validate_css_base.png) | Pass: No Errors |
| checkout.css | ![checkout.css validation](docs/validation/validate_css_checkout.png) | Pass: No Errors |
| profile.css | ![profile.css validation](docs/validation/validate_css_profile.png) | Pass: No Errors |

### JS Hint Testing

I have used [JSHint](https://jshint.com/) to identify potential errors in my JavaScript file. No errors were found.

| File | Screenshot | Notes |
| --- | --- | --- |
| stripe_elements.js | ![script.js](docs/validation/validate_js_stripe_elements.png) | Undefined Stripe element |
| countryfields.js | ![script.js](docs/validation/validate_js_country_fields.png) | Pass : No Errors |
| script from bag.html | ![script.js](docs/validation/validate_js_bag.png) | Pass: No Errors |
| script from product.html | ![script.js](docs/validation/validate_js_product.png) | Pass: No Errors |
| script from add/edit_product.html | ![script.js](docs/validation/validate_js_add_edit_product.png) | Pass: No Errors |
| script from quantity_input_script.html | ![script.js](docs/validation/validate_js_quantity_input.png) | Pass: No Errors |

### Python Testing

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate my Python file.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| bag | contexts.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NataliaCzeladka/sagittarius-a-star/main/bag/contexts.py) | ![screenshot](docs/validation/validate_python_bag_context.png) | No Errors Found |
| bag | bag_tools.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NataliaCzeladka/sagittarius-a-star/main/bag/templatetags/bag_tools.py) | ![screenshot](docs/validation/validate_python_bag_tools.png) | No Errors Found |
| bag | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NataliaCzeladka/sagittarius-a-star/main/bag/urls.py) | ![screenshot](docs/validation/validate_python_bag_urls.png) | No Errors Found |
| bag | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NataliaCzeladka/sagittarius-a-star/main/bag/views.py) | ![screenshot](docs/validation/validate_python_bag_views.png) | No Errors Found |
| checkout | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NataliaCzeladka/sagittarius-a-star/main/checkout/admin.py) | ![screenshot](docs/validation/validate_python_checkout_admin.png) | No Errors Found |
| checkout | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NataliaCzeladka/sagittarius-a-star/main/checkout/forms.py) | ![screenshot](docs/validation/validate_python_checkout_forms.png) | No Errors Found |
| checkout | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NataliaCzeladka/sagittarius-a-star/main/checkout/models.py) | ![screenshot](docs/validation/validate_python_checkout_models.png) | No Errors Found |
| checkout | signals.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NataliaCzeladka/sagittarius-a-star/main/checkout/signals.py) | ![screenshot](docs/validation/validate_python_checkout_signals.png) | No Errors Found |
| checkout | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NataliaCzeladka/sagittarius-a-star/main/checkout/urls.py) | ![screenshot](docs/validation/validate_python_checkout_urls.png) | No Errors Found |
| checkout | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NataliaCzeladka/sagittarius-a-star/main/checkout/views.py) | ![screenshot](docs/validation/validate_python_checkout_views.png) | No Errors Found |
| contact | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NataliaCzeladka/sagittarius-a-star/main/contact/admin.py) | ![screenshot](docs/validation/validate_python_contact_admin.png) | No Errors Found |
| contact | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NataliaCzeladka/sagittarius-a-star/main/contact/forms.py) | ![screenshot](docs/validation/validate_python_contact_forms.png) | No Errors Found |
| contact | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NataliaCzeladka/sagittarius-a-star/main/contact/models.py) | ![screenshot](docs/validation/validate_python_contact_models.png) | No Errors Found |
| contact | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NataliaCzeladka/sagittarius-a-star/main/contact/urls.py) | ![screenshot](docs/validation/validate_python_contact_urls.png) | No Errors Found |
| contact | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NataliaCzeladka/sagittarius-a-star/main/contact/views.py) | ![screenshot](docs/validation/validate_python_contact_views.png) | No Errors Found |
| home | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NataliaCzeladka/sagittarius-a-star/main/home/urls.py) | ![screenshot](docs/validation/validate_python_home_urls.png) | No Errors Found |
| home | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NataliaCzeladka/sagittarius-a-star/main/home/views.py) | ![screenshot](docs/validation/validate_python_home_views.png) | No Errors Found |
| newsletter | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NataliaCzeladka/sagittarius-a-star/main/newsletter/admin.py) | ![screenshot](docs/validation/validate_python_newsletter_admin.png) | No Errors Found |
| newsletter | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NataliaCzeladka/sagittarius-a-star/main/newsletter/forms.py) | ![screenshot](docs/validation/validate_python_newsletter_forms.png) | No Errors Found |
| newsletter | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NataliaCzeladka/sagittarius-a-star/main/newsletter/models.py) | ![screenshot](docs/validation/validate_python_newsletter_models.png) | No Errors Found |
| newsletter | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NataliaCzeladka/sagittarius-a-star/main/newsletter/urls.py) | ![screenshot](docs/validation/validate_python_newsletter_urls.png) | No Errors Found |
| newsletter | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NataliaCzeladka/sagittarius-a-star/main/newsletter/views.py) | ![screenshot](docs/validation/validate_python_newsletter_views.png) | No Errors Found |
| products | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NataliaCzeladka/sagittarius-a-star/main/products/admin.py) | ![screenshot](docs/validation/validate_python_products_admin.png) | No Errors Found |
| products | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NataliaCzeladka/sagittarius-a-star/main/products/forms.py) | ![screenshot](docs/validation/validate_python_products_forms.png) | No Errors Found |
| products | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NataliaCzeladka/sagittarius-a-star/main/products/models.py) | ![screenshot](docs/validation/validate_python_products_models.png) | No Errors Found |
| products | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NataliaCzeladka/sagittarius-a-star/main/products/urls.py) | ![screenshot](docs/validation/validate_python_products_urls.png) | No Errors Found |
| products | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NataliaCzeladka/sagittarius-a-star/main/products/views.py) | ![screenshot](docs/validation/validate_python_products_views.png) | No Errors Found |
| products | widgets.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NataliaCzeladka/sagittarius-a-star/main/products/widgets.py) | ![screenshot](docs/validation/validate_python_products_widgets.png) | No Errors Found |
| profiles | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NataliaCzeladka/sagittarius-a-star/main/profiles/forms.py) | ![screenshot](docs/validation/validate_python_profiles_forms.png) | No Errors Found |
| profiles | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NataliaCzeladka/sagittarius-a-star/main/profiles/models.py) | ![screenshot](docs/validation/validate_python_profiles_models.png) | No Errors Found |
| profiles | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NataliaCzeladka/sagittarius-a-star/main/profiles/urls.py) | ![screenshot](docs/validation/validate_python_profiles_urls.png) | No Errors Found |
| profiles | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NataliaCzeladka/sagittarius-a-star/main/profiles/views.py) | ![screenshot](docs/validation/validate_python_profiles_views.png) | No Errors Found |

## Browser Compatibility

## Responsiveness

## Lighthouse Audit

## User Stories Testing

## Fixed Bugs

## Unfixed Bugs
