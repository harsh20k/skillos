---
title: Hide div with class
category: Academic
priority: Medium
starred: None
created: 2024-06-23T11:05:22.149677
updated: 2024-06-23T11:05:45.326388
dg-publish: true
---
# Hide div with class

**Priority:** Medium

## Conversation

### Assistant

To hide a `div` with a specific class, you can use CSS or JavaScript. Here are examples for both methods:

### Using CSS

You can use CSS to hide a `div` with a specific class by setting its `display` property to `none`. Add the following CSS rule to your stylesheet or within a `<style>` tag in your HTML:

```css
.hidden-class {
  display: none;
}
```

Then, apply the class `hidden-class` to the `div` you want to hide:

```html
<div class="hidden-class">
  This content is hidden.
</div>
```

### Using JavaScript

You can also hide a `div` using JavaScript by changing its `style.display` property. Here's how you can do it:

#### With Vanilla JavaScript

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hide Div Example</title>
</head>
<body>
  <div class="my-div">
    This content will be hidden by JavaScript.
  </div>

  <script>
    document.addEventListener("DOMContentLoaded", function() {
      var div = document.querySelector(".my-div");
      if (div) {
        div.style.display = "none";
      }
    });
  </script>
</body>
</html>
```

#### With jQuery (if you have jQuery included in your project)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hide Div Example</title>
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
  <div class="my-div">
    This content will be hidden by jQuery.
  </div>

  <script>
    $(document).ready(function() {
      $(".my-div").hide();
    });
  </script>
</body>
</html>
```

Choose the method that best fits your needs and project setup.

---

