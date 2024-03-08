---
layout: break
title: "Course Evaluation"
break: 60
---

<!-- Container for the image gallery -->
<div class="container">

  <!-- Full-width images with number text -->
  <div class="mySlides">
    <div class="numbertext">1 / 6</div>
      <img src="{{ '/assets/img/evaluation/eval1.png' | relative_url }}" style="width:100%">
  </div>

  <div class="mySlides">
    <div class="numbertext">2 / 6</div>
      <img src="{{ '/assets/img/evaluation/eval2.png' | relative_url }}" style="width:100%">
  </div>

  <div class="mySlides">
    <div class="numbertext">3 / 6</div>
      <img src="{{ '/assets/img/evaluation/eval3.png' | relative_url }}" style="width:100%">
  </div>

  <div class="mySlides">
    <div class="numbertext">4 / 6</div>
      <img src="{{ '/assets/img/evaluation/eval4.png' | relative_url }}" style="width:100%">
  </div>

  <div class="mySlides">
    <div class="numbertext">5 / 6</div>
      <img src="{{ '/assets/img/evaluation/eval5.png' | relative_url }}" style="width:100%">
  </div>

  <div class="mySlides">
    <div class="numbertext">6 / 6</div>
      <img src="{{ '/assets/img/evaluation/eval6.png' | relative_url }}" style="width:100%">
  </div>

  <!-- Next and previous buttons -->
  <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
  <a class="next" onclick="plusSlides(1)">&#10095;</a>

  <!-- Image text -->
  <div class="caption-container">
    <p id="caption"></p>
  </div>

  <!-- Thumbnail images -->
  <div class="row">
    <div class="column">
      <img class="demo cursor" src="{{ '/assets/img/evaluation/eval1.png' | relative_url }}" style="width:100%" onclick="currentSlide(1)" alt="The Woods">
    </div>
    <div class="column">
      <img class="demo cursor" src="{{ '/assets/img/evaluation/eval2.png' | relative_url }}" style="width:100%" onclick="currentSlide(2)" alt="Cinque Terre">
    </div>
    <div class="column">
      <img class="demo cursor" src="{{ '/assets/img/evaluation/eval3.png' | relative_url }}" style="width:100%" onclick="currentSlide(3)" alt="Mountains and fjords">
    </div>
    <div class="column">
      <img class="demo cursor" src="{{ '/assets/img/evaluation/eval4.png' | relative_url }}" style="width:100%" onclick="currentSlide(4)" alt="Northern Lights">
    </div>
    <div class="column">
      <img class="demo cursor" src="{{ '/assets/img/evaluation/eval5.png' | relative_url }}" style="width:100%" onclick="currentSlide(5)" alt="Nature and sunrise">
    </div>
    <div class="column">
      <img class="demo cursor" src="{{ '/assets/img/evaluation/eval6.png' | relative_url }}" style="width:100%" onclick="currentSlide(6)" alt="Snowy Mountains">
    </div>
  </div>
</div>

* {
  box-sizing: border-box;
}

/* Position the image container (needed to position the left and right arrows) */
.container {
  position: relative;
}

/* Hide the images by default */
.mySlides {
  display: none;
}

/* Add a pointer when hovering over the thumbnail images */
.cursor {
  cursor: pointer;
}

/* Next & previous buttons */
.prev,
.next {
  cursor: pointer;
  position: absolute;
  top: 40%;
  width: auto;
  padding: 16px;
  margin-top: -50px;
  color: white;
  font-weight: bold;
  font-size: 20px;
  border-radius: 0 3px 3px 0;
  user-select: none;
  -webkit-user-select: none;
}

/* Position the "next button" to the right */
.next {
  right: 0;
  border-radius: 3px 0 0 3px;
}

/* On hover, add a black background color with a little bit see-through */
.prev:hover,
.next:hover {
  background-color: rgba(0, 0, 0, 0.8);
}

/* Number text (1/3 etc) */
.numbertext {
  color: #f2f2f2;
  font-size: 12px;
  padding: 8px 12px;
  position: absolute;
  top: 0;
}

/* Container for image text */
.caption-container {
  text-align: center;
  background-color: #222;
  padding: 2px 16px;
  color: white;
}

.row:after {
  content: "";
  display: table;
  clear: both;
}

/* Six columns side by side */
.column {
  float: left;
  width: 16.66%;
}

/* Add a transparency effect for thumnbail images */
.demo {
  opacity: 0.6;
}

.active,
.demo:hover {
  opacity: 1;
}

<p class="d-flex justify-content-around align-items-center">
  <a>
  <img src="{{ '/assets/img/evaluation/eval1.png' | relative_url }}" alt="evaluation" width="250">
  </a>
  <a>
  <img src="{{ '/assets/img/evaluation/eval2.png' | relative_url }}" alt="evaluation" width="250">
  </a>
  <a>
  <img src="{{ '/assets/img/evaluation/eval3.png' | relative_url }}" alt="evaluation" width="250">
  </a>
  <a>
  <img src="{{ '/assets/img/evaluation/eval4.png' | relative_url }}" alt="evaluation" width="250">
  </a>
</p>


<p class="d-flex justify-content-around align-items-center">
  <a>
  <img src="{{ '/assets/img/evaluation/eval5.png' | relative_url }}" alt="evaluation" width="250">
  </a>
<a>
  <img src="{{ '/assets/img/evaluation/eval6.png' | relative_url }}" alt="evaluation" width="250">
  </a>
<a>
  <img src="{{ '/assets/img/evaluation/eval7.png' | relative_url }}" alt="evaluation" width="250">
  </a>
<a>
  <img src="{{ '/assets/img/evaluation/eval8.png' | relative_url }}" alt="evaluation" width="250">
  </a>
</p>

<p class="d-flex justify-content-around align-items-center">
  <a>
  <img src="{{ '/assets/img/croatia.png' | relative_url }}" alt="evaluation" width="250">
  </a>
  <a>
  <img src="{{ '/assets/img/bbpf.jpg' | relative_url }}" alt="evaluation" width="250" >
  </a>
  <a>
     <img src="{{ '/assets/img/cesp.PNG' | relative_url }}" alt="evaluation" width="250">
  </a>
  <a>
     <img src="{{ '/assets/img/gbif.png' | relative_url }}" alt="evaluation" width="250">
   </a>
   <a>
     <img src="{{ '/assets/img/thf.PNG' | relative_url }}" alt="evaluation" width="250">
   </a>
   <a>
     <img src="{{ '/assets/img/belspo.png' | relative_url }}" alt="evaluation" width="250">
   </a>
   </p>
