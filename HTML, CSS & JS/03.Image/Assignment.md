**1.** Create an image tag that displays an image named `flower.jpg` which is in the **same folder** as your HTML file. Add proper `alt` text.

**2.** Display an image named `logo.png` that is stored inside a folder called `images`. Your HTML file is outside the `images` folder.  
Also give the image a width of `200px`.

**3.** An image named `banner.jpg` is inside a folder called `assets/images`. Your HTML file is in the root folder. Write the correct `src` path and add `alt` text.

**4.** Your HTML file is inside a folder called `pages`. The image `photo.jpg` is in the root folder. Write the correct path to display the image.

**5.** Display an image with:
- `src` = `images/nature.jpg`
- `alt` = "Beautiful nature view"
- `width` = 300
- `height` = 200

**6.** Add a `title` attribute to an image so that when the user hovers over it, the text “Click to view full size” appears.

**7.** Create an image that should load **only when the user scrolls near it** (lazy loading). Use an image from the `images` folder.

**8.** Create a hero image that should load **immediately** when the page opens (eager loading).

**9.** Write an image tag using `loading="auto"` and explain in one line what the browser will decide.

**10.** Create a responsive image using `srcset` with three versions:
- `small.jpg` (400w)
- `medium.jpg` (800w)
- `large.jpg` (1200w)

Also add a normal `src` as fallback.

**11.** Create a complete image tag that includes all these attributes:
- Image is inside `images/` folder
- `alt` text
- `width` and `height`
- `loading="lazy"`
- `title`
- `srcset` with two sizes

**12.** Create two images side by side:
- First image loads immediately (`eager`) and is a logo from `assets/logo.png`
- Second image loads lazily and is a product photo from `images/products/shoe.jpg`
Both should have proper `alt` text and width of 250px.


---

**Answers**

---

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Assignment</title>
</head>
<body>

        <h1 align="center">Assignment 01</h1>
    <br>

    <H3>Question-01</H3>

    <img src="flower.jpg" alt="A pink rose flower in full bloom">
    <br>

    <H3>Question-02</H3>

    <img src="image/logo.png" alt="Company Logo" width="200">
    <br>    

    <H3>Question-03</H3>

    <img src="assests/images01/banner.jpg" alt="Website promotional banner">
    <br>

    <H3>Question-04</H3>

    <img src="../photo.jpg" alt="A photo from root directory">
    <br>

    <H3>Question-05</H3>

    <img src="image/nature.jpg" alt="Beautiful nature view" width="300" height="200">
    <br>

    <H3>Question-06</H3>

    <img src="image/sample.jpg" alt="Sample picture preview" title="Click to view full size">
    <br>

    <H3>Question-07</H3>

    <img src="image/scenery.jpg" alt="Scenic landscape" loading="lazy">
    <br>
    
    <H3>Question-08</H3>

    <img src="image/hero-banner.jpg" alt="Main hero banner" loading="eager">
    <br>

    <H3>Question-09</H3>

    <img src="image/hero-banner.jpg" alt="Promotional banner" loading="auto">
    <br>

    <H3>Question-10</H3>

    <img 
    src="image/medium.jpg" 
    srcset="image/small.jpg 400w, image/medium.jpg 800w, image/large.jpg 1200w" 
    alt="A responsive landscape view">
    <br>

    <H3>Question-11</H3>

    <img 
    src="image/nature.jpg" 
    alt="Detailed description of the image" 
    width="600" 
    height="400" 
    loading="lazy" 
    title="Click or hover to learn more" 
    srcset="image/small.jpg 500w, image/nature.jpg 1000w">
    <br>

    <H3>Question-12</H3>

    <img 
    src="assests/logo.png" 
    alt="Company Logo" 
    loading="eager" 
    width="250">
    <br>

    <H3>Question-13</H3>

    <img 
    src="image/product/shoes.jpg" 
    alt="Running Shoe" 
    loading="lazy" 
    width="250">  
    <br> 


</body>
</html>
