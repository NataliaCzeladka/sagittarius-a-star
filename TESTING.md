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

[JSHint](https://jshint.com/), a static code analysis tool, was used to check if JavaScript source code complies with coding rules. No errors were found in this area.

### HTML Validation

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files. No errors or warnings were found. Django allauth templates were not tested. Pages that required user authentication were validated by direct input.

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsagittarius-a-star-ab236042b163.herokuapp.com%2F) | ![home page validation](static/docs/validate_html_home.png) | Pass: No Errors |
| Products | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsagittarius-a-star-ab236042b163.herokuapp.com%2Fproducts%2F) | ![products page validation](static/docs/validate_html_products.png) | Pass: No Errors |
| Product Detail | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsagittarius-a-star-ab236042b163.herokuapp.com%2Fproducts%2F2%2F) | ![product detail page validation](static/docs/validate_html_product_detail.png) | Pass: No Errors |
| Add Product | [W3C](https://validator.w3.org/nu/#textarea) | ![add product page validation](static/docs/validate_html_add_product.png) | Pass: No Errors |
| Edit Product | [W3C](https://validator.w3.org/nu/#textarea) | ![edit product page validation](static/docs/validate_html_edit_product.png) | Pass: No Errors |
| Bag | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsagittarius-a-star-ab236042b163.herokuapp.com%2Fbag%2F) | ![shopping bag page validation](static/docs/validate_html_bag.png) | Pass: No Errors |
| Checkout | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsagittarius-a-star-ab236042b163.herokuapp.com%2Fcheckout%2F) | ![checkout page validation](static/docs/validate_html_checkout.png) | Pass: No Errors |
| Checkout Success | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsagittarius-a-star-ab236042b163.herokuapp.com%2Fcheckout%2Fcheckout_success%2F2541D772F60543C38B84B7BA09FCA42B) | ![checkout success page validation](static/docs/validate_html_checkout_success.png) | Pass: No Errors |
| User Profile | [W3C](https://validator.w3.org/nu/#textarea) | ![user profile page validation](static/docs/validate_html_profile.png) | Pass: No Errors |
| Contact | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsagittarius-a-star-ab236042b163.herokuapp.com%2Fcontact%2F) | ![contact page validation](static/docs/validate_html_contact.png) | Pass: No Errors |

### CSS Validation

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate my CSS files. No errors were found.

| File | Screenshot | Notes |
| --- | --- | --- |
| base.css | ![base.css validation](static/docs/validate_css_base.png) | Pass: No Errors |
| checkout.css | ![checkout.css validation](static/docs/validate_css_checkout.png) | Pass: No Errors |
| profile.css | ![profile.css validation](static/docs/validate_css_profile.png) | Pass: No Errors |

### JS Hint Testing

I have used [JSHint](https://jshint.com/) to identify potential errors in my JavaScript file. No errors were found.

| File | Screenshot | Notes |
| --- | --- | --- |
| stripe_elements.js | ![script.js](static/docs/validate_js_stripe_elements.png) | Undefined Stripe element |
| countryfields.js | ![script.js](static/docs/validate_js_country_fields.png) | Pass : No Errors |
| script from bag.html | ![script.js](static/docs/validate_js_bag.png) | Pass: No Errors |
| script from product.html | ![script.js](static/docs/validate_js_product.png) | Pass: No Errors |
| script from add/edit_product.html | ![script.js](static/docs/validate_js_add_edit_product.png) | Pass: No Errors |
| script from quantity_input_script.html | ![script.js](static/docs/validate_js_quantity_input.png) | Pass: No Errors |

### Python Testing

## Browser Compatibility

## Responsiveness

## Lighthouse Audit

## User Stories Testing

## Fixed Bugs

## Unfixed Bugs
